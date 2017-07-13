from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=255)
    template = models.ForeignKey('polls.Template')

    def __str__(self):
        return self.title


class Template(models.Model):
    title = models.CharField(max_length=255)

    @property
    def fields(self):
        return self.field_set.all()

    def __str__(self):
        return self.title


class Field(models.Model):
    title = models.CharField(max_length=255)
    template = models.ForeignKey('polls.Template')

    def __str__(self):
        return self.title


class Vote(models.Model):
    poll = models.ForeignKey('polls.Poll')
    field = models.ForeignKey('polls.Field')
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)
