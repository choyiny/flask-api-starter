from flask import request

from extensions import logger


def before_request():
    """
    Run before every request to API.
    """
    logger.info(
        "Request from [%s]: %s %s %s %s",
        request.environ.get("HTTP_X_REAL_IP", request.remote_addr),
        request.method,
        request.scheme,
        request.full_path,
        request.data.decode("utf-8"),
    )
