from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from django.conf import settings

from .models import Post


class PostListView(ListView):
    model = Post
    ordering = ['-created_at']
    paginate_by = settings.DEFAULT_PAGE_SIZE


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    paginate_by = settings.DEFAULT_PAGE_SIZE

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Post.objects.filter(author=user).order_by("-created_at")


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        set the author of the created post to the current request user
        :param form: the submitted form
        :return: the validated form
        """
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        """
        set the author of the created post to the current request user
        :param form: the submitted form
        :return: the validated form
        """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """
        validates that the user updating the post is the author
        :return:
        """
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        """
        validates that the user updating the post is the author
        :return:
        """
        post = self.get_object()
        return self.request.user == post.author


def about_page(request):
    context = {
        'title': "About"
    }
    return render(request, "blog/about.html", context)
