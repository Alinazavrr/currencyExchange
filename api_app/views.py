from datetime import timedelta, timezone

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView

from datetime import datetime, timezone

from .serializers import *
from .models import *
from .takeCurrency import takeCurrency
# Create your views here.

class CurrencyRatesApiView(ListAPIView):
    serializer_class = RatesSerializers


    def get_queryset(self):
        currency_name = self.request.GET.get('name', 'USD')
        currency_base = Currency.objects.get(name=currency_name)
        exchange_rate = ExchangeRate.objects.first()

        current_time = datetime.utcnow().replace(tzinfo=timezone.utc)
        if exchange_rate.time_next_update <= current_time:
            takeCurrency(currency_name)

        return ExchangeRate.objects.filter(currency_base=currency_base).first()
