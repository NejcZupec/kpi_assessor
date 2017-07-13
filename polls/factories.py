import factory

from polls.models import Field
from polls.models import Poll
from polls.models import Template
from polls.models import Vote


class TemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Template

    title = 'template_title'


class PollFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Poll

    title = 'poll_title'
    template = factory.SubFactory(TemplateFactory)


class FieldFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Field

    title = 'field_title'
    template = factory.SubFactory(TemplateFactory)


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vote

    poll = factory.SubFactory(PollFactory)
    template = factory.SubFactory(TemplateFactory)
