from django.contrib.auth.models import User
from django.db import models


class Goal(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, related_name='user')
    end_date = models.DateTimeField(null=False)

    class Meta:
        db_table = 'goals'
