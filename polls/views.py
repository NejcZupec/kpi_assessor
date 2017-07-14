from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import TemplateView

from polls.forms import PollForm
from polls.models import Poll


class PollsView(ListView):
    models = Poll
    queryset = Poll.objects.all()
    template_name = 'polls.html'


class PollVoteView(TemplateView):
    template_name = 'poll_vote.html'

    def get(self, request, *args, **kwargs):
        context = super(PollVoteView, self).get_context_data(**kwargs)

        # get a Poll instance from the db and add it to the context
        poll_id = kwargs.get('poll_id')
        poll = get_object_or_404(Poll, pk=poll_id)
        context['poll'] = poll

        # add poll form to the context
        questions = [field.title for field in poll.template.fields]
        context['form'] = PollForm(questions=questions)

        return self.render_to_response(context)
