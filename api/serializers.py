from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Goal
from api.utils import send_mail


class UserSerializer(serializers.ModelSerializer):
    # goals = serializers.PrimaryKeyRelatedField(many=True, queryset=Goal.objects.all())

    class Meta:
        model = User
        fields = '__all__'


class GoalSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Goal
        fields = '__all__'

    def create(self, validated_data):
        data = super(GoalSerializer, self).create(validated_data)
        # TODO: put delay
        send_mail(title=validated_data['title'], action='created')
        return data

    def update(self, instance, validated_data):
        data = super(GoalSerializer, self).update(instance, validated_data)
        # TODO: put delay
        send_mail(title=validated_data['title'], action='updated')
        return data

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
