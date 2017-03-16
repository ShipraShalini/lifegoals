from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from api.mail_utils import notify_user
from api.models import Goal


class GoalSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Goal
        fields = '__all__'

    def create(self, validated_data):
        data = super(GoalSerializer, self).create(validated_data)
        notify_user.delay(title=validated_data['title'], action='created')
        return data

    def update(self, instance, validated_data):
        data = super(GoalSerializer, self).update(instance, validated_data)
        notify_user.delay(title=validated_data['title'], action='updated')
        return data


class UserSerializer(serializers.ModelSerializer):
    goals = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'goals', 'password')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
