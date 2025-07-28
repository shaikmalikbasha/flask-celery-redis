"""
Deprecated: This code is deprecated and will be removed in a future release.
"""

import logging
from time import sleep

from celery import Celery

logging.basicConfig(level=logging.INFO)
app = Celery("tasks", broker="redis://localhost:6379", backend="redis://localhost:6379")


@app.task
def add(x, y):
    """Add two numbers."""
    i: int = 0
    while i < 5:
        sleep(1)
        i += 1
        logging.info("Processing...")
    logging.info("Done processing.")
    return x + y
