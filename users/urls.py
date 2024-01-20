from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from django.views.generic import TemplateView

from users.apps import UsersConfig
from users.views import RegisterView, activate, main, UserListView, users_active

app_name = UsersConfig.name


urlpatterns = [
    path('', main, name='main'),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('users_list/', UserListView.as_view(), name='users_list'),
    path('users_active/<int:pk>', users_active, name='users_active'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email_verify/', TemplateView.as_view(template_name='users/verify.html'), name='email_verify'),
    path('activate/<token>', activate, name='activate'),
]