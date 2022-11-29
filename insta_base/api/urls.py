from django.urls import path, include
from rest_framework import routers
from api.views import PostApiView, CommentApiView


router = routers.DefaultRouter()
router.register('posts', PostApiView)
router.register('comments', CommentApiView)
urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', PostApiView.as_view({'get': 'like'})),
    path('posts/<int:pk>/dislike/', PostApiView.as_view({'get': 'dislike'}))
]

