from django.urls import path, include
from rest_framework import routers
from api.views import PostApiView


router = routers.DefaultRouter()
router.register('posts', PostApiView)
urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:pk>/like/', PostApiView.as_view({'get': 'like'})),
    path('posts/<int:pk>/dislike/', PostApiView.as_view({'get': 'dislike'}))
]

