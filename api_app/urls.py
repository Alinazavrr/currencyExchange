from django.urls import path

from . import views


urlpatterns = [
    path('api/currency-rates/', views.CurrencyRatesApiView.as_view()),
]
