from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=255)
    template = models.ForeignKey('polls.Template')


class Template(models.Model):
    title = models.CharField(max_length=255)


class Field(models.Model):
    title = models.CharField(max_length=255)
    template = models.ForeignKey('polls.Template')


class Vote(models.Model):
    poll = models.ForeignKey('polls.Poll')
    field = models.ForeignKey('polls.Field')
    value = models.IntegerField()
