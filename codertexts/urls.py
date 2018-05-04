from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete
from django.urls import path, include
from codertexts import settings
from articles.views import HomeView, ArticleDetailView, CategoryView, UserArticlesView, angular, LookUpView
from users.api import UserCreateAPI, UserUpdateAPI, UserDeleteAPI, UserListAPI, Logout, RecuperarUsuarioAPI
from articles.api import NewArticleAPI, GetAllArticlesAPI, GetAllArticlesByUserAPI, \
    ActionArticleAPI, GetAllCategoriesAPI
from users.views import SignupView, LoginView, logout, VerificarToken, ActualizarToken, ObtenerToken, password_reset, \
    UploadAvatarAPI, GetAvatarAPI, DeleteAvatarAPI

urlpatterns = [
    path('admin/', admin.site.urls),

    # Auth URLs
    path('api/1.0/token-obtain/', ObtenerToken.as_view()),
    path('api/1.0/token-refresh/', ActualizarToken.as_view()),
    path('api/1.0/token-verify/', VerificarToken.as_view()),


    path('articles/category/<str:category>', CategoryView.as_view(), name="category_page"),
    path('articles/<str:username>/<slug:title>', ArticleDetailView.as_view(), name="article_detail_page"),
    path('articles/<str:username>/', UserArticlesView.as_view(), name="user_articles_page"),
    path('articles/lookup/', LookUpView.as_view(), name="look_up_page"),
    path('login/', LoginView.as_view(), name="login_page"),
    path('logout/', logout, name="logout_page"),
    path('signup/', SignupView.as_view(), name="signup_page"),
    path('', HomeView.as_view(), name="home_page"),
    path('i18n/', include('django.conf.urls.i18n')),

    # Ajax URLs
    #path('ajax/addfavorite', AddFavorite, name = "add_favorite"),

    # API URLs
    path('api/1.0/createUser/', UserCreateAPI.as_view(), name="api_create_users"),
    path('api/1.0/logout/', Logout.as_view(), name="api_logout_users"),
    path('api/1.0/updateUser/<int:pk>', UserUpdateAPI.as_view(), name="api_update_users"),
    path('api/1.0/deleteUser/<int:pk>', UserDeleteAPI.as_view(), name="api_delete_users"),
    path('api/1.0/user/', UserListAPI.as_view(), name="api_user_list"),
    path('api/1.0/recuperarPassword/', RecuperarUsuarioAPI.as_view(), name="api_user_list"),


    path('api/1.0/article/new/', NewArticleAPI.as_view(), name="api_new_article"),
    path('api/1.0/article/<int:pk>', ActionArticleAPI.as_view(), name="api_article_detail"),
    path('api/1.0/articles/all/', GetAllArticlesAPI.as_view(), name="api_articles_all"),
    path('api/1.0/articles/user/<int:id_user>', GetAllArticlesByUserAPI.as_view(), name="api_user_article"),
    path('api/1.0/article/delete/<int:pk>', ActionArticleAPI.as_view(), name="api_article_delete"),
    path('api/1.0/categories/all/', GetAllCategoriesAPI.as_view(), name="api_categories_all"),

    #  Rutas para la recuperación de password
    path('api/1.0/sendEmailPassword/', password_reset, name='password_reset'),
    url(r'^password_reset/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', password_reset_complete, name='password_reset_complete'),

    #  Rutas para la gestión de imágenes
    path('api/1.0/subirAvatar/<str:id_user>', UploadAvatarAPI.as_view(), name="upload_avatar_api"),
    path('api/1.0/getAvatar/<str:id_user>', GetAvatarAPI.as_view(), name="get_avatar_api"),
    path('api/1.0/deleteAvatar/<str:dir>/<str:name>', DeleteAvatarAPI.as_view(), name="delete_avatar_api"),

]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
