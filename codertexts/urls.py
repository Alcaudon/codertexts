from django.contrib import admin
from django.urls import path

from users.api import UserCreateAPI, UserUpdateAPI, UserDeleteAPI
from articles.api import NewArticleAPI, GetAllArticlesAPI, GetAllArticlesByUserAPI, ActionArticleAPI,GetAllCategoriesAPI
from articles.views import home
from users.views import LoginUserView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home_page"),
    # API URLs
    path('api/1.0/createUser/', UserCreateAPI.as_view(), name="api_create_users"),
    path('api/1.0/login/', LoginUserView.as_view(), name="api_login_users" ),
    path('api/1.0/updateUser/<int:pk>', UserUpdateAPI.as_view(), name="api_update_users"),
    path('api/1.0/deleteUser/<int:pk>', UserDeleteAPI.as_view(), name="api_delete_users"),

    path('api/1.0/article/<int:pk>', ActionArticleAPI.as_view(), name="api_article_detail"),
    path('api/1.0/article/new/', NewArticleAPI.as_view(), name="api_new_article"),
    path('api/1.0/articles/all/', GetAllArticlesAPI.as_view(), name="api_articles_all"),
    path('api/1.0/articles/user/<int:id_user>', GetAllArticlesByUserAPI.as_view(), name="api_new_article"),

    path('api/1.0/categories/all/', GetAllCategoriesAPI.as_view(), name="api_categories_all")
]
