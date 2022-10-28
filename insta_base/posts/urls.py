from django.urls import path
from posts.views import HomePostView

urlpatterns = [
    path('posts', HomePostView.as_view(), name='index')
    ]

