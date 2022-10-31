from django.urls import path
from posts.views import HomePostView, PostAddView, PostsDetailView, CommentAddView


urlpatterns = [
    path('', HomePostView.as_view(), name='index'),
    path('add', PostAddView.as_view(), name='posts_add'),
    path('detail/<int:pk>', PostsDetailView.as_view(), name='posts_detail'),
    path('add/comment/<int:pk>', CommentAddView.as_view() ,name='to_comment')
    ]

