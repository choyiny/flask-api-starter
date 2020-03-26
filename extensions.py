"""Extensions module - Set up for additional libraries can go in here."""
import logging

from flask_sqlalchemy import SQLAlchemy

# logging
logger = logging.getLogger('flask.general')


# database
db = SQLAlchemy()
