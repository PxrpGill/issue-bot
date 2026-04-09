import logging
from aiogram import Dispatcher


def setup_middlewares(dp: Dispatcher) -> None:
    logger = logging.getLogger(__name__)
    logger.info("Middlewares setup complete")