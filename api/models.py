from django.contrib.auth.models import User
from django.db import models


class Goal(models.Model):
    title = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, related_name='goals')
    end_date = models.DateTimeField(null=False)
    achieved = models.BooleanField(default=False)

    class Meta:
        db_table = 'goals'

    def __unicode__(self):
        return "title: {0} \nend_date: {1} \nachieved: {2}\n".format(self.title, self.end_date, self.achieved)
