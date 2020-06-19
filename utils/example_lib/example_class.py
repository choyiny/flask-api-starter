from logging import getLogger
from flask.logging import default_handler

logger = getLogger()


class ExampleClass:
    """
  Example Class
  """

    @staticmethod
    def praise_jordan_liu():
        """
    Praises Jordan Liu
    """
        logger.info("Damn, Jordan Liu. You did a great job.")
