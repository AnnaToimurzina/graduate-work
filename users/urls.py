from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from .views import UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='Users')


urlpatterns = [] + router.urls
