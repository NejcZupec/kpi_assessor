from django import forms


class PollForm(forms.Form):

    def __init__(self, questions, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)
        choices = [(str(i), str(i)) for i in range(1, 11)]
        for question in questions:
            self.fields[question] = forms.ChoiceField(
                widget=forms.RadioSelect(),
                choices=choices,
            )
