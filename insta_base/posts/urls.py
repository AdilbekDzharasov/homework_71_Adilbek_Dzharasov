from django.urls import path
from posts.views import HomePostView
from posts.views import PostAddView
from posts.views import PostsDetailView


urlpatterns = [
    path('posts', HomePostView.as_view(), name='index'),
    path('add', PostAddView.as_view(), name='posts_add'),
    path('detail/<int:pk>', PostsDetailView.as_view(), name='posts_detail')
    ]

