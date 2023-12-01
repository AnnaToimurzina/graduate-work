
'''from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = []
from django.urls import path

from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserCreateView, UserListView, UserRetrieveAPIView, UserUpdateAPIView, UserDestroyAPIView, \
    UserViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='Users')

urlpatterns = [path('user/create/', UserCreateView.as_view(), name='user_create'),
               path('user/list/', UserListView.as_view(), name='user_list'),
    path('user/<int:pk>/', UserRetrieveAPIView.as_view(), name='user_get'),
    path('user/update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('user/delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),

] + router.urls'''

from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateView, UserRetrieveAPIView, UserListView, UserUpdateAPIView, UserDestroyAPIView, \
    BusyUserView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/', UserRetrieveAPIView.as_view(), name='user_detail'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDestroyAPIView.as_view(), name='user_delete'),
    path('busy_users/', BusyUserView.as_view(), name='busy_users'),

]








