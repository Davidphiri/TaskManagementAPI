from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, TaskSerializer
from tasks.models import Task

User = get_user_model()

class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
     