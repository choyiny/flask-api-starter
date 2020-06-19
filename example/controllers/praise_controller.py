from example.controllers.example_base_controller import ExampleBaseController
from example.workers.example import example_task


class PraiseController(ExampleBaseController):
    def get(self):
        example_task.delay("Damn, Jordan Liu. You did a great job.")
        return {"data": "Worker queued."}
