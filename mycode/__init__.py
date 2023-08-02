import logging

_LOGGER = logging.getLogger(__name__)


def log_something():
    _LOGGER.error("something")
