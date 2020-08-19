"""Extensions module - Set up for additional libraries can go in here."""
import logging

from celery import Celery

import config

# logging
logger = logging.getLogger("flask.general")

# celery
celery = Celery(
    "app", broker=config.CELERY_BROKER_URL, backend=config.CELERY_RESULT_BACKEND
)
