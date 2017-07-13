from django.core.urlresolvers import reverse
from django.test import TestCase

from polls.factories import PollFactory


class TestPollsView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestPollsView, cls).setUpClass()
        cls.polls_url = reverse('list_polls')
        cls.poll1 = PollFactory()
        cls.poll2 = PollFactory()

    def test_list_polls_view_should_open(self):
        response = self.client.get(self.polls_url)
        self.assertEqual(response.status_code, 200)

    def test_if_object_list_in_context(self):
        response = self.client.get(self.polls_url)
        object_list = response.context_data['object_list']
        expected_result = [self.poll1, self.poll2]
        self.assertEqual(set(object_list), set(expected_result))
