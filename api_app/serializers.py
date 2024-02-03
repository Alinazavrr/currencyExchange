from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import ExchangeRate, Currency
from ..base_app.models import PaidUser


class RatesSerializers(serializers.Serializer):

    class Meta:
        model = ExchangeRate
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidUser
        fields = ('username', 'email')


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user