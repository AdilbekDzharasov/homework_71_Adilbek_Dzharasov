from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView
from accounts.models import Account
from posts.models import Post
from posts.forms import PostForm


class HomePostView(ListView):
    template_name = 'index.html'
    context_object_name = 'accounts'
    model = Account


class PostAddView(CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('posts_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostsDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'


