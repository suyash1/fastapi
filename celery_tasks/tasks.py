from celery import shared_task

@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='something:get_something_done')
def get_something_done_task(self):
    data = "Getting something done here..."
    return data
