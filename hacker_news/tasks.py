from hackernews.celery import app
from .updateapi import updateNewStories


@app.task
def update():
    updateNewStories()
    return 'data fetch complete'
    