
from rest_framework import serializers

from .models import Profile, CustomUser
from reports.serializers import ReportSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('phone',)


class UserSerializer(serializers.ModelSerializer):
    reports = ReportSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'is_practitioner', 'reports', 'password', 'profile')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
