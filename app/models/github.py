from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    login: str
    id: int
    avatar_url: Optional[str] = None


class Issue(BaseModel):
    number: int
    title: str
    html_url: str
    user: Optional[User] = None
    pull_request: Optional[dict] = None

    @property
    def is_pull_request(self) -> bool:
        return self.pull_request is not None


class Label(BaseModel):
    name: str
    color: str


class Milestone(BaseModel):
    number: int
    title: str


class Event(BaseModel):
    id: int
    event: str
    actor: Optional[User] = None
    issue: Optional[Issue] = None
    pull_request: Optional[dict] = None
    label: Optional[Label] = None
    milestone: Optional[Milestone] = None
    assignee: Optional[User] = None
    commit_sha: Optional[str] = None
    created_at: str