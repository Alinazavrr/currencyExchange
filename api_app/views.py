from datetime import timedelta, timezone

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from datetime import datetime, timezone

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
from .models import *
from .takeCurrency import takeCurrency
# Create your views here.


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = UserSerializer

class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer



class CurrencyRatesApiView(ListAPIView):
    serializer_class = RatesSerializers

    def get_queryset(self):
        try:
            currency_name = self.request.GET.get('name', 'USD')
            currency_base = Currency.objects.get_or_create(name=currency_name)

            exchange_rate = ExchangeRate.objects.first()

            current_time = datetime.utcnow().replace(tzinfo=timezone.utc)
            if exchange_rate.time_next_update <= current_time:
                takeCurrency(currency_name)

        except DoesNotExist:
            takeCurrency(currency_name)

        return ExchangeRate.objects.filter(currency_base=currency_base).all()