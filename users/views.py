import random

from django.conf import settings
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.decorators.cache import cache_page
from django.views.generic import CreateView, ListView

from blog.models import Blog
from service.jobs import start
from service.models import Mailing, Client
from users.forms import UserRegisterForm
from users.models import User
from users.utils import create_token


@login_required
@cache_page(60)
def main(request):
    start()
    mailing_count = Mailing.objects.count()
    mailing_active_count = Mailing.objects.filter(is_active=True).count()
    client_count = Client.objects.count()
    blog_all = Blog.objects.all()
    blog_random_post = []
    end = True
    while end:
        if blog_all:
            post = random.choice(blog_all)
            if post not in blog_random_post:
                blog_random_post.append(post)
                blog_all = blog_all.exclude(pk=post.pk)
        else:
            end = False

    blog_random_post = blog_random_post[:3]
    context = {
        'mailing_count': mailing_count,
        'mailing_active_count': mailing_active_count,
        'client_count': client_count,
        'blog_random_post': blog_random_post
    }
    return render(request, 'users/main.html', context)


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'users.view_user'


@login_required
@permission_required('users.set_is_active')
def users_active(request, pk):
    user = get_object_or_404(User, pk=pk)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect(reverse('users:users_list'))


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:email_verify')

    def form_valid(self, form):
        new_user = form.save()
        new_user.token = create_token()
        send_mail(
            subject='Подтвердите почту',
            message=f'Пройдите по ссылке http://127.0.0.1:8000/activate/{new_user.token}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def activate(request, token):
    user = User.objects.get(token=token)
    user.email_verify = True
    user.save()
    return render(request, 'users/activate.html')



