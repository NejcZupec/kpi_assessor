from django.test import TestCase

from polls.models import Field
from polls.models import Poll
from polls.models import Template
from polls.models import Vote


class TestPoll(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestPoll, cls).setUpClass()
        cls.template = Template(title='template')
        cls.poll = Poll(
            title='poll',
            template=cls.template,
        )

    def test_normal_poll_creation(self):
        self.assertEqual(self.poll.title, 'poll')
        self.assertEqual(self.poll.template, self.template)

    def test_string_representation(self):
        self.assertEqual(str(self.poll), self.poll.title)


class TestTemplate(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestTemplate, cls).setUpClass()
        cls.template = Template(title='template')

    def test_normal_template_creation(self):
        self.assertEqual(self.template.title, 'template')

    def test_string_representation(self):
        self.assertEqual(str(self.template), self.template.title)


class TestField(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestField, cls).setUpClass()
        cls.template = Template(title='template')
        cls.field = Field(
            title='field',
            template=cls.template,
        )

    def test_normal_field_creation(self):
        self.assertEqual(self.field.title, 'field')
        self.assertEqual(self.field.template, self.template)

    def test_string_representation(self):
        self.assertEqual(str(self.field), self.field.title)


class TestVote(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestVote, cls).setUpClass()
        template = Template(title='template')

        cls.field = Field(
            title='field',
            template=template,
        )

        cls.poll = Poll(
            title='poll',
            template=template,
        )

        cls.vote = Vote(
            poll=cls.poll,
            field=cls.field,
            value=2,
        )

    def test_normal_vote_creation(self):
        self.assertEqual(self.vote.poll, self.poll)
        self.assertEqual(self.vote.field, self.field)
        self.assertEqual(self.vote.value, 2)

    def test_string_representation(self):
        self.assertEqual(str(self.vote), str(self.vote.value))
