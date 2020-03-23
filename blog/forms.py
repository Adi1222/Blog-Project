from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import UserPosts


class SignUpForm(UserCreationForm):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    Ans = forms.IntegerField(label='What is 22 + 12 ?')

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")
        return password2

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'Ans', )


class PostForm(forms.ModelForm):
    class Meta:
        model = UserPosts
        fields = ('title', 'description', 'img', 'post_choice')

