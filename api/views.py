from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.models import Goal
from api.serializers import UserSerializer, GoalSerializer
from api.utils import get_goals_by_user


class UserView(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects
    lookup_field = 'username'


class GoalView(ModelViewSet):
    serializer_class = GoalSerializer
    queryset = Goal.objects

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Goalcheck(APIView):
    http_method_names = ['get']

    def get(self, request):
        get_goals_by_user()
        return Response('done')

