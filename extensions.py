"""Extensions module - Set up for additional libraries can go in here."""
import logging


from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base


# logging
logger = logging.getLogger('flask.general')


# database
db = SQLAlchemy()
BaseModel = declarative_base()
try:
    from example.models import User
    METADATA = BaseModel.metadata
except ImportError:
    pass
