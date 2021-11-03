from django.urls import path
from . import views

urlpatterns = [
    path("", views.views_bag, name='views_bag'),
]
