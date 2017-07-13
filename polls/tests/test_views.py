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


class TestPollVoteView(TestCase):

    @classmethod
    def setUpClass(cls):
        super(TestPollVoteView, cls).setUpClass()
        cls.poll = PollFactory()
        cls.poll_vote_url = reverse(
            'poll_vote',
            kwargs={'poll_id': cls.poll.id},
        )

    def test_poll_vote_should_not_be_opened(self):
        url = reverse('poll_vote', kwargs={'poll_id': '99999'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_check_if_page_is_opened_for_existing_poll(self):
        response = self.client.get(self.poll_vote_url)
        self.assertEqual(response.status_code, 200)

    def test_check_if_poll_is_in_the_context(self):
        response = self.client.get(self.poll_vote_url)
        self.assertEqual(response.context_data['poll'], self.poll)
