"""Settings configuration - Configuration for environment variables can go in here."""


# API
SECRET_KEY = "replace_this"

# SQLAlchemy
SQLALCHEMY_ECHO = False  # do not show SQL statements
SQLALCHEMY_TRACK_MODIFICATIONS = False  # suppress warnings
SQLALCHEMY_DATABASE_URI = "postgresql://choyiny@localhost/wizard"

# CORS
FRONTEND_URL = "http://localhost:4200"

SENTRY_DSN = ""
