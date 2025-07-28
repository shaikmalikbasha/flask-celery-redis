import time
from app.celery_worker import celery


@celery.task
def process_match(data):
    # Simulate ML processing
    time.sleep(5)  # Replace with real ML match logic
    return {"status": "match processed", "input": data}
