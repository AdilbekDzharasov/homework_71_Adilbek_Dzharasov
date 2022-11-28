from django.urls import path, include
from rest_framework import routers
from api.views import PostApiView


router = routers.DefaultRouter()
router.register('posts', PostApiView)
urlpatterns = [
    path('', include(router.urls))
]

