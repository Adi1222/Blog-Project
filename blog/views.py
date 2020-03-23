from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import SignUpForm, PostForm
from .models import UserPosts
from django.contrib.auth import logout, login
from django.core.exceptions import ValidationError
from django.urls import *


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            _username = form.cleaned_data.get('username')
            _password = form.cleaned_data.get('password1')

            ans = form.cleaned_data.get('Ans')

            if ans == 34:
                user = User.objects.create_user(username=_username, password=_password)
                user_posts = UserPosts(author=user)
                user_posts.save()
                user.save()

            else:
                error = 'Wrong answer!'
                return render(request, 'blog/register.html', {'form': form, 'error': error})

            user = authenticate(username=_username, password=_password)
            login(request, user)
            return render(request, 'blog/base.html')
            # return redirect('post_list')
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})


def log(request):
    if request.method == 'POST':
        _username = request.POST.get('username')
        _password = request.POST.get('password')
        user = authenticate(username=_username, password=_password)
        login(request, user)
        if user is not None:
            return redirect('/home/')
        else:
            return render(request, 'blog/login.html')
    else:
        return render(request, 'blog/login.html')


def post_list(request):
    aut = User.objects.get(username=request.user)
    posts = UserPosts.objects.filter(author=aut, post_choice='Public')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(UserPosts, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post_choice = 'Public'
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form, 'edit_or_new': 'New Post'})


def post_edit(request, pk):
    post = get_object_or_404(UserPosts, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post_choice = 'Public'
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'edit_or_new': 'Edit Post'})


def other_post_list(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        try:
            other_user = User.objects.get(username=uname)
        except User.DoesNotExist:
            return HttpResponse('User Does Not Exist!')
            # return render(request, 'blog/other_post_list.html', {'nouser': 'No such user exist!'})

        other_user_posts = UserPosts.objects.filter(author=other_user, post_choice='Public')
        return render(request, 'blog/other_post_list.html', {'other_user_posts': other_user_posts, 'uname': uname})
    else:
        return HttpResponse('NO POSTS!')


def logout1(request):
    logout(request)
    form = SignUpForm()
    return render(request, 'blog/register.html', {'form': form})

