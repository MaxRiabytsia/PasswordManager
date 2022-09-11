from django.urls import path
from .views import (UserPasswordsListView,
                    PasswordCreateView,
                    PasswordUpdateView,
                    PasswordDetailView,
                    PasswordDeleteView,
                    SearchView)
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user/<str:username>', UserPasswordsListView.as_view(), name='user-passwords'),
    path('user/<str:username>/search', SearchView.as_view(), name='password-search'),
    path('password/<int:pk>/', PasswordDetailView.as_view(), name='password-detail'),
    path('password/new/', PasswordCreateView.as_view(), name='password-create'),
    path('password/<int:pk>/update/', PasswordUpdateView.as_view(), name='password-update'),
    path('password/<int:pk>/delete/', PasswordDeleteView.as_view(), name='password-delete')
]
