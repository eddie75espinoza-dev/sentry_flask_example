import os
from dotenv import load_dotenv
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.loguru import LoguruIntegration
from sentry_sdk.integrations.loguru import LoggingLevels


load_dotenv()


sentry_loguru = LoguruIntegration(
    level=LoggingLevels.INFO.value,        # Capture info and above as breadcrumbs
    event_level=LoggingLevels.ERROR.value  # Send errors as events
)

sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[
        FlaskIntegration(),
        sentry_loguru
    ],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
    environment=os.getenv('SENTRY_ENVIRONMENT'),
    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
)