from django.test import TestCase

from polls.models import Field
from polls.models import Poll
from polls.models import Template
from polls.models import Vote


class TestPoll(TestCase):

    def test_normal_poll_creation(self):
        template = Template(title='template')
        poll = Poll(
            title='poll',
            template=template,
        )
        self.assertEqual(poll.title, 'poll')
        self.assertEqual(poll.template, template)


class TestTemplate(TestCase):

    def test_normal_template_creation(self):
        template = Template(
            title='template',
        )
        self.assertEqual(template.title, 'template')


class TestField(TestCase):

    def test_normal_field_creation(self):
        template = Template(title='template')
        field = Field(
            title='field',
            template=template,
        )
        self.assertEqual(field.title, 'field')
        self.assertEqual(field.template, template)


class TestVote(TestCase):

    def test_normal_vote_creation(self):
        template = Template(title='template')

        field = Field(
            title='field',
            template=template,
        )

        poll = Poll(
            title='poll',
            template=template,
        )

        vote = Vote(
            poll=poll,
            field=field,
            value=2,
        )

        self.assertEqual(vote.poll, poll)
        self.assertEqual(vote.field, field)
        self.assertEqual(vote.value, 2)
