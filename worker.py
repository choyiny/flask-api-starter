import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.redis import RedisIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from extensions import celery
from app import create_app

import config as c

app = create_app(for_celery=True)
app.app_context().push()

# add more external integrations below
if c.CELERY_SENTRY_DSN:
    sentry_sdk.init(
        c.CELERY_SENTRY_DSN,
        integrations=[
            CeleryIntegration(),
            FlaskIntegration(),
            RedisIntegration(),
            SqlalchemyIntegration(),
        ],
    )
