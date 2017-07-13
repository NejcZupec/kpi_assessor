from django.test import TestCase

from polls.forms import PollForm


class TestPollForm(TestCase):

    def test_no_questions(self):
        form = PollForm(questions=[])
        self.assertEqual(set(form.fields), set([]))

    def test_insert_questions(self):
        questions = ['q1', 'q2']
        form = PollForm(questions)
        self.assertEqual(set(form.fields), set(questions))
