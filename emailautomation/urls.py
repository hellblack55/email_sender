from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('send_email/', views.send_email, name='send_email'),
    path('email_sent/', views.email_sent, name='email_sent'),
]
