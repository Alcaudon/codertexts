from django.contrib import admin
from django.urls import path

from users.api import UserCreateAPI, UserUpdateAPI, UserDeleteAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    # API URLs
    path('api/1.0/createUser/', UserCreateAPI.as_view(), name="api_create_users"),
    path('api/1.0/updateUser/<int:pk>', UserUpdateAPI.as_view(), name="api_update_users"),
    path('api/1.0/deleteUser/<int:pk>', UserDeleteAPI.as_view(), name="api_delete_users")
]
