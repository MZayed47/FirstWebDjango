import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    subject = models.CharField(max_length=20)
    date = models.DateTimeField('Date published')

    def __str__(self):
        return self.subject + " question."

    def was_published_recently(self):
        return self.date >= timezone.now() - datetime.timedelta(days=3)
    was_published_recently.admin_order_field = 'date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.option + "!"
