from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListAPIView
from articles.serializers import ArticlesSerializer
from articles.models import Article
from users.permissions import UserPermissions
from articles.models import Category
from articles.serializers import CategoriesSerializer


class NewArticleAPI(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [UserPermissions]


class ActionArticleAPI(RetrieveUpdateDestroyAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [UserPermissions]


class GetAllArticlesAPI(ListAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [UserPermissions]


class GetAllArticlesByUserAPI(ListAPIView):
    serializer_class = ArticlesSerializer
    permission_classes = [UserPermissions]

    def get_queryset(self):
        id_user = self.kwargs.get('id_user')
        queryset = Article.objects.filter(id_user=id_user)
        return queryset


class GetAllCategoriesAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [UserPermissions]