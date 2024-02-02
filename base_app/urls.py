from django.urls import path

from . import views


urlpatterns = [
    path('', views.homePage.as_view(), name='home'),
]
