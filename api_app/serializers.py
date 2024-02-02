from rest_framework import serializers

from .models import ExchangeRate, Currency

class RatesSerializers(serializers.Serializer):

    class Meta:
        model = ExchangeRate
        fields = '__all__'