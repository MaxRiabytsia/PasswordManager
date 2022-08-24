from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Password


def home(request):
    return render(request, 'passwords/home.html')


class UserPasswordsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Password
    template_name = 'passwords/passwords.html'
    context_object_name = 'passwords'
    ordering = ['service']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Password.objects.filter(author=user).order_by('service')

    def test_func(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return self.request.user == user


class PasswordDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Password

    def test_func(self):
        password = self.get_object()
        return self.request.user == password.author


class PasswordCreateView(LoginRequiredMixin, CreateView):
    model = Password
    fields = ['service', 'password', 'username', 'email', 'additional_info']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PasswordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Password
    fields = ['service', 'password', 'username', 'email', 'additional_info']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        password = self.get_object()
        return self.request.user == password.author


class PasswordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Password
    success_url = '/'

    def test_func(self):
        password = self.get_object()
        return self.request.user == password.author
