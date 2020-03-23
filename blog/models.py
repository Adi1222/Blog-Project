from django.db import models
from django.contrib.auth.models import User
from task2.media.blog_image import *


class UserPosts(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='Title')
    description = models.TextField(max_length=500, blank=True)
    img = models.ImageField(upload_to='blog_image', blank=True, null=True)

    PUBLIC = 'Public'
    PRIVATE = 'Private'

    POST_CHOICES = [
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    ]

    post_choice = models.CharField(max_length=8, choices=POST_CHOICES, default='Public')

    class Meta:
        verbose_name_plural = "UserPosts"

    def __str__(self):
        return self.title
