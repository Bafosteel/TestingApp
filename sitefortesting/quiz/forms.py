from django import forms
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list, widget=RadioSelect) #RadioSelect



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')


class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')