from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, ProfileImageForm, UserUpdaterForm, ChooseGenderForm, EmailSenderForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} добавлен')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(
        request,
        'users/registration.html',
        {
            'title': 'Страница регистрации',
            'form': form
        }
    )


@login_required
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileImageForm(
            request.POST, request.FILES, instance=request.user.profile)
        updateUserForm = UserUpdaterForm(request.POST, instance=request.user)
        chooseGenderForm = ChooseGenderForm(
            request.POST, instance=request.user.profile)
        emailSenderForm = EmailSenderForm(
            request.POST, instance=request.user.profile)

        if profileForm.is_valid() and updateUserForm.is_valid() and chooseGenderForm.is_valid() and emailSenderForm.is_valid():
            profileForm.save()
            updateUserForm.save()
            chooseGenderForm.save()
            emailSenderForm.save()
            messages.success(request, f'Данные успешно обновлены')
            return redirect('profile')
    else:
        profileForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UserUpdaterForm(instance=request.user)
        chooseGenderForm = ChooseGenderForm(instance=request.user.profile)
        emailSenderForm = EmailSenderForm(instance=request.user.profile)

    data = {
        'profileForm': profileForm,
        'updateUserForm': updateUserForm,
        'chooseGenderForm': chooseGenderForm,
        'emailSenderForm': emailSenderForm
    }

    return render(request, 'users/profile.html', data)
