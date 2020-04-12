from extensions import celery


@celery.task
def example_task(example_msg):
    print(example_msg)
