from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, FormView
from posts.models import Post
from posts.forms import PostForm
from posts.forms import CommentForm
from posts.models import Comment


class HomePostView(ListView):
    template_name = 'index.html'
    context_object_name = 'posts'
    model = Post

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomePostView, self).get_context_data(object_list=object_list, **kwargs)
        context['favorite_form'] = CommentForm()
        return context


class PostAddView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'add.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse('posts_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostsDetailView(LoginRequiredMixin, DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostsDetailView, self).get_context_data(*args, **kwargs)
        likes_count = get_object_or_404(Post, id=self.kwargs['pk'])
        get_likes = likes_count.get_likes()
        context['get_likes'] = get_likes
        context['comments'] = self.object.comments.order_by('-created_at')
        return context


class CommentAddView(LoginRequiredMixin, FormView):
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            author = request.user
            Comment.objects.create(author=author, post=post, text=text)
        return redirect('index')


def LikeView(request, pk):
    post = get_object_or_404(Post, pk=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('index'))

