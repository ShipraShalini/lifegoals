from pprint import pprint

import datetime

import pytz
from django.contrib.auth.models import User

from api.mail_utils import send_mail
from api.serializers import UserSerializer
from lifegoals.celery import task_queue

ist = pytz.timezone('Asia/Kolkata')

@task_queue.task
def send_daily_mail(user):
    data = prepare_mail_body(user)
    curr_date = str(datetime.date.today())
    send_mail(subject="Notification for {}".format(curr_date), body=data)


def prepare_mail_body(user):
    return "Hi {0}, \nYour goals are:\n".format(user['first_name']) + '\n'.join(user['goals'])


@task_queue.task
def get_goals_by_user():
    serializer = UserSerializer(User.objects.all(), many=True)
    print serializer.data
    for user in serializer.data:
        send_daily_mail.delay(user)

