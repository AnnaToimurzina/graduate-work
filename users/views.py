from django.db.models import Count, Q
from rest_framework import generics, viewsets


from users.models import User
from users.serializers import UserSerializer, BusyUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserListView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()


class BusyUserView(generics.ListAPIView):
    serializer_class = BusyUserSerializer

    def get_queryset(self):
        return User.objects.annotate(count_active_tasks=Count('task_executor', filter=Q(task_executor__status__in=['pending', 'processing']))).order_by('-count_active_tasks')
