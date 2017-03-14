import logging

from lifegoals.celery import task_queue

logger = logging.getLogger('mail')

subject_dict = {
    "created": "Alert: New LifeGoal created",
    "updated": "Alert: LifeGoal updated"
}

@task_queue.task
def notify_user(title, action):
    subject = subject_dict[action]
    body = "Your lifegoal titled {0} has been {1}".format(title, action)
    send_mail(subject, body)


def send_mail(subject, body):
    logger.info({"subject": subject, "body": body})


