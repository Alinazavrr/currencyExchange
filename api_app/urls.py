from django.urls import path

from . import views


urlpatterns = [
    path('currency-rates/', views.CurrencyRatesApiView.as_view()),
]
