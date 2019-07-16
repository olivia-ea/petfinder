from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home-page'),
    path('registration', views.create_account, name='registration-page'),
]
