from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django_blog.models import TimeStampMixin


class Post(TimeStampMixin):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="author")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
