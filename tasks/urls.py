from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tasks.apps import TasksConfig

from .views import TaskViewSet, ImportantTasksView, UserListView

app_name = TasksConfig.name

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='Task')


urlpatterns = [path('', include(router.urls)),
               path('important_tasks/', ImportantTasksView.as_view(), name='important-tasks'),
               path('users_list_all/', UserListView.as_view(), name='user-list'),
               path('users_vip/', ImportantTasksView.as_view(), name='user-2')]

