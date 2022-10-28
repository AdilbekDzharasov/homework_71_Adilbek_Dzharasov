from django.views.generic import ListView, DetailView, CreateView
from accounts.models import Account


class HomePostView(ListView):
    template_name = 'index.html'
    context_object_name = 'accounts'
    model = Account

