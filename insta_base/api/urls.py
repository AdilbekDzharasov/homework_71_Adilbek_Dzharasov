from django.urls import path, include
from rest_framework import routers
from api.views import PostApiView, CommentView


router = routers.DefaultRouter()
router.register('posts', PostApiView)
urlpatterns = [
    path('', include(router.urls))
]

