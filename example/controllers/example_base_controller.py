from flask_apispec import doc

from helpers import BaseResource


@doc(
    tags=['Example']
)
class ExampleBaseController(BaseResource):
    pass
