from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

# some = forms.ModelChoiceField(queryset=User.objects.all())


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label='Введите имя',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )
    email = forms.EmailField(
        label='Введите почту',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите почту'})
    )
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdaterForm(forms.ModelForm):
    username = forms.CharField(
        label='Введите имя',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите имя'})
    )
    email = forms.EmailField(
        label='Введите почту',
        required=True,
        help_text='текст ограничения для поля',
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите почту'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileImageForm(forms.ModelForm):
    img = forms.ImageField(
        label='Загрузить фото',
        required=False,
        widget=forms.FileInput
    )

    class Meta:
        model = Profile
        fields = ['img']


class ChooseGenderForm(forms.ModelForm):
    # gender = forms.ModelChoiceField(queryset=Profile.objects.all())
    # gender = forms.ChoiceField()

    class Meta:
        model = Profile
        fields = ['gender']


class EmailSenderForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['sender']
