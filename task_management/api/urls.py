from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TaskViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

router = DefaultRouter()

router.register('users', UserViewSet, basename='users')
router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]

urlpatterns += router.urls
