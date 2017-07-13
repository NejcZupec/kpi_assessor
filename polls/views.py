from django.views.generic import ListView

from polls.models import Poll


class PollsView(ListView):
    models = Poll
    queryset = Poll.objects.all()
    template_name = 'polls.html'
