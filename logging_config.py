import logging
import os

PROJECT_LOGGERS = ("__main__", "app", "agent", "retriever", "ingest")


def setup_logging(level: str | None = None) -> None:
    raw_level = (level or os.getenv("LOG_LEVEL", "INFO")).upper()
    app_level = getattr(logging, raw_level, None)
    if not isinstance(app_level, int):
        raise ValueError(
            f"Invalid LOG_LEVEL '{raw_level}'. Use DEBUG, INFO, WARNING, ERROR, or CRITICAL."
        )

    fmt = "%(asctime)s %(levelname)s [%(name)s] %(message)s"

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.setLevel(logging.INFO)

    root_handler = logging.StreamHandler()
    root_handler.setLevel(logging.INFO)
    root_handler.setFormatter(logging.Formatter(fmt))
    root_logger.addHandler(root_handler)

    app_handler = logging.StreamHandler()
    app_handler.setLevel(app_level)
    app_handler.setFormatter(logging.Formatter(fmt))

    for logger_name in PROJECT_LOGGERS:
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger.setLevel(app_level)
        logger.propagate = False
        logger.addHandler(app_handler)
