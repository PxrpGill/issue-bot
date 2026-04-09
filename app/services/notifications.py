import logging
from aiogram import Bot

from app.config import config

logger = logging.getLogger(__name__)


EVENT_DESCRIPTIONS = {
    "issues": "открыт",
    "closed": "закрыт",
    "reopened": "переоткрыт",
    "labeled": "добавлена метка",
    "unlabeled": "удалена метка",
    "assigned": "назначен исполнитель",
    "unassigned": "удалён исполнитель",
    "milestoned": "добавлен в milestone",
    "demilestoned": "удалён из milestone",
    "head_ref_force_pushed": "force-pushed",
    "merged": "слит",
    "referenced": "упомянут",
    "moved_columns_in_project": "перемещён в колонку проекта",
}


def format_notification(event_type: str, event: dict) -> str:
    actor = event.get("actor", {})
    actor_login = actor.get("login", "unknown")

    issue = event.get("issue", {})
    issue_number = issue.get("number", "?")
    issue_title = issue.get("title", "")
    issue_url = issue.get("html_url", "")
    is_pr = "pull_request" in issue and issue.get("pull_request") is not None

    object_type = "PR" if is_pr else "issue"
    event_desc = EVENT_DESCRIPTIONS.get(event_type, event_type)

    parts = [f"<b>{actor_login}</b> {event_desc} {object_type} <b>#{issue_number}</b>"]

    if issue_title:
        parts.append(f"<i>{issue_title}</i>")

    if event_type in ("labeled", "unlabeled"):
        label = event.get("label", {})
        label_name = label.get("name", "?")
        parts.append(f"Метка: {label_name}")

    if event_type in ("assigned", "unassigned"):
        assignee = event.get("assignee", {})
        assignee_login = assignee.get("login", "?")
        parts.append(f"Исполнитель: {assignee_login}")

    if event_type in ("milestoned", "demilestoned"):
        milestone = event.get("milestone", {})
        milestone_title = milestone.get("title", "?")
        parts.append(f"Milestone: {milestone_title}")

    if event_type == "moved_columns_in_project":
        project_card = event.get("project_card", {})
        column_name = project_card.get("column_name", "?")
        parts.append(f"Колонка: {column_name}")

    parts.append(f"<a href=\"{issue_url}\">Открыть</a>")

    return "\n".join(parts)


async def send_notification(bot: Bot, event_type: str, event: dict) -> None:
    if not config.telegram_chat_id:
        logger.warning("Telegram chat_id not configured")
        return

    try:
        text = format_notification(event_type, event)
        await bot.send_message(chat_id=config.telegram_chat_id, text=text)
    except Exception as e:
        logger.error(f"Failed to send notification: {e}")