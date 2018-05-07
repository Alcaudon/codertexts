from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from articles.permisssions import ArticlePermissions
from articles.serializers import ArticlesSerializer
from articles.models import Article
from users.permissions import UserPermissions, IsOwnerOrReadOnly
from articles.models import Category
from articles.serializers import CategoriesSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import datetime


#@method_decorator(csrf_protect, name='dispatch')
class NewArticleAPI(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [ArticlePermissions]


class ActionArticleAPI(RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [ArticlePermissions]


#@method_decorator(csrf_protect, name='dispatch')
class GetAllArticlesAPI(ListAPIView):
    """Artículos que están publicados y cuya fecha es menor o igual a la de hoy"""
    now = datetime.now()
    queryset = Article.objects.filter(pub_date__lte=now).order_by('-pub_date')
    serializer_class = ArticlesSerializer

    def retrieve(self, request, pk=None):
        if request.user.is_superuser or (request.user.is_authenticated and str(request.user.id) == pk):
            posts_list = Article.objects.all().order_by('-publish_date')
        else:
            now = datetime.now()
            posts_list = Article.objects.filter(user=pk, pub_date__lte=now).order_by('-pub_date')
        serializer = ArticlesSerializer(posts_list, many=True)
        return Response(serializer.data)


class ArticlesByUserAPI(ListAPIView):
    """Artículos publicados por un usuario"""
    serializer_class = ArticlesSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        now = datetime.now()
        id_user = self.kwargs.get('id_user')
        queryset = Article.objects.filter(id_user=id_user,  pub_date__lte=now, status='finalizado')
        return queryset


class OwnArticlesAPI(ListAPIView):
    """Artículos propios de un usuario"""
    serializer_class = ArticlesSerializer
    permission_classes = [UserPermissions, IsAuthenticated]

    def get_queryset(self):
        id_user = self.kwargs.get('id_user')
        queryset = Article.objects.filter(id_user=id_user)
        return queryset


class GetAllCategoriesAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
