from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class UserRegister(UserCreationForm):
    username = forms.CharField(
        label='Введите имя',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-4'})
    )
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control mb-4'})
    )
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'})
    )
    password2 = forms.CharField(
        label='Подтверждение пароля',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control mb-4'})
    )
    choice = forms.BooleanField(label=' Согласны ли вы с правилами нашего сайта?', required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'choice']


class UserUpdateInfo(forms.ModelForm):
    username = forms.CharField(
        label='Введите новое имя',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control mb-4', 'placeholder': 'Введите имя'})
    )
    email = forms.EmailField(
        label='Введите новый Email',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control mb-4'})
    )

    class Meta:
        model = User
        fields = ['username', 'email']


class UserImageUpdate(forms.ModelForm):
    image = forms.ImageField(label='Изменить фото на сайте', required=False, widget=forms.FileInput)
    choice = forms.BooleanField(label='Просто галочка :3 ', required=False)

    class Meta:
        model = User
        fields = ['image', 'choice']
