from django.shortcuts import render, redirect
from .forms import UserRegister, UserUpdateInfo, UserImageUpdate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def registration(request):
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Пользователь {username} был создан!'
            )
            return redirect('home')
    else:
        form = UserRegister
    data = {
        'form': form
    }
    return render(request, 'users/registration.html', data)


@login_required
def profile(request):
    if request.method == 'POST':
        userUpdate = UserUpdateInfo(request.POST, instance=request.user)
        imageUpdate = UserImageUpdate(request.POST, request.FILES, instance=request.user.profile)

        if userUpdate.is_valid() and imageUpdate.is_valid():
            userUpdate.save()
            imageUpdate.save()
    else:
        userUpdate = UserUpdateInfo(instance=request.user)
        imageUpdate = UserImageUpdate(request.POST, instance=request.user.profile)

    data = {
        'userUpdate': userUpdate,
        'imageUpdate': imageUpdate
    }
    return render(request, 'users/profile.html', data)
