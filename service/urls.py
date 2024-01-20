from django.urls import path
from django.views.decorators.cache import cache_page

from service.apps import ServiceConfig
from service.views import MailingListView, MailingCreateView, LogListView, ClientListView, ClientCreateView, \
    MassageCreateView, MailingUpdateView, MailingDeleteView, activate_mailing, start_mailing, \
    ClientDeleteView, ClientUpdateView, MailingDetailView, ClientDetailView, automatic_mailing_start

app_name = ServiceConfig.name


urlpatterns = [
    path('mailing/', MailingListView.as_view(), name='mailing'),
    path('client/', cache_page(60)(ClientListView.as_view()), name='client'),
    path('create_mailing/', MailingCreateView.as_view(), name='create_mailing'),
    path('update_mailing/<int:pk>/', MailingUpdateView.as_view(), name='update_mailing'),
    path('update_client/<int:pk>/', ClientUpdateView.as_view(), name='update_client'),
    path('delete_mailing/<int:pk>/', MailingDeleteView.as_view(), name='delete_mailing'),
    path('delete_client/<int:pk>/', ClientDeleteView.as_view(), name='delete_client'),
    path('create_massage/', MassageCreateView.as_view(), name='create_massage'),
    path('create_client/', ClientCreateView.as_view(), name='create_client'),
    path('add_client/', ClientCreateView.as_view(), name='add_client'),
    path('log/', LogListView.as_view(), name='log'),
    path('activate_mailing/<int:pk>/', activate_mailing, name='activate_mailing'),
    path('automatic_mailing_start/', automatic_mailing_start, name='automatic_mailing_start'),
    path('start_mailing/<int:pk>/', start_mailing, name='start_mailing'),
    path('<int:pk>/mailing_view', MailingDetailView.as_view(), name='mailing_view'),
    path('<int:pk>/client_view', ClientDetailView.as_view(), name='client_view'),
]
