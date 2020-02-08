
from rest_framework import serializers

from .models import Profile, CustomUser
from reports.serializers import ReportSerializer


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(view_name='user_detail',
                                               read_only=True)

    class Meta:
        model = Profile
        fields = ('phone', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    reports = ReportSerializer(many=True, required=False)
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
