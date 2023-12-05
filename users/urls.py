from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from users.apps import UsersConfig
from users.views import UserCreateView, UserRetrieveAPIView, UserListView
from users.views import UserUpdateAPIView, UserDestroyAPIView, BusyUserView

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
