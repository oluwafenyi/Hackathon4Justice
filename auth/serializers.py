
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        expires = api_settings.ACCESS_TOKEN_LIFETIME
        data['expires'] = expires.seconds
        return data
