from django import forms
from django.contrib.auth.models import User
from .models import Feedback
# from django.contrib.auth.forms import UserCreationForm

# some = forms.ModelChoiceField(queryset=User.objects.all())


class FeedbackForm(forms.ModelForm):
    theme = forms.CharField(
        label='Тема письма',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Тема письма'})
    )
    email = forms.EmailField(
        label='Введите почту',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите почту'})
    )
    textMess = forms.CharField(
        label='Текст сообщения',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.Textarea(
            attrs={'class': 'form-control', 'placeholder': 'Текст сообщения'})
    )

    class Meta:
        model = Feedback
        fields = ['theme', 'email', 'textMess']
