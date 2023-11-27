from rest_framework.routers import DefaultRouter

from tasks.apps import TasksConfig
from .views import TaskViewSet

app_name = TasksConfig.name

router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='Task')


urlpatterns = [] + router.urls