from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from api.models import Goal
from api.serializers import UserSerializer, GoalSerializer


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects
    lookup_field = 'username'


class GoalView(ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
