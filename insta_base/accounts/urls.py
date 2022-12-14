from django.urls import path

from accounts.views import LoginView, logout_view, RegisterView, ProfileView, UserChangeView, SearchAccountView, SubscriptionsView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('logout/', logout_view, name='logout'),
    path('profile/search', SearchAccountView.as_view(), name='search'),
    path('profile/subscriptions/<int:pk>', SubscriptionsView, name='subscriptions'),
    path('profile/<int:pk>/change', UserChangeView.as_view(), name='change'),
]

