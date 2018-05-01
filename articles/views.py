from django.utils.datetime_safe import datetime
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from articles.models import Article, Comment, Category
from codertexts.settings import ARTICLES_LIMIT
from users.models import User


def ordenarArticulos(peticion):
    orden = peticion.GET.get('order_by')
    if orden == 'antiguos':
        orden_list = 'pub_date'
    elif orden == 'modernos':
        orden_list = '-pub_date'
    else:
        orden_list = '-pub_date'
    return orden_list


def contarComentarios(comentarios, articulos):
    numberofcomments = dict()
    for articulo in articulos:
        numberofcomments[articulo.id] = 0
        for comentario in comentarios:
            if comentario.id_article.id == articulo.id:
                numberofcomments[articulo.id] = numberofcomments[articulo.id] + 1
    return numberofcomments


class HomeView(ListView):
    model = Article
    template_name = "home.html"
    paginate_by = ARTICLES_LIMIT # variable global en settings.py

    def get_queryset(self):
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).order_by(ordenarArticulos(self.request)) # limitamos el número de artículos en esta vista en la variable ARTICLES_LIMIT de settings.py
        return queryset
        # artículos publicados, con fecha de publicación en el pasado y ordenadas de más reciente a más antigua

    def get_context_data(self, *args, **kwargs):  # función para meter el número de comentarios en función de la lista
        context = super().get_context_data(*args, **kwargs)
        categorias = Category.objects.order_by('name')
        comentarios = Comment.objects.order_by('-pub_date')
        articulos = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).order_by(ordenarArticulos(self.request))
        context['numofcomments'] = contarComentarios(comentarios, articulos)
        context['categories'] = categorias
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "article_detail_page.html"

    def get_object(self):
        user_name = self.kwargs.get('username')
        return get_object_or_404(Article, id_user=User.objects.get(username=user_name).id, slug=self.kwargs.get('title'))

    def get_context_data(self, *args, **kwargs):  # función para meter info de los comentarios
        context = super().get_context_data(*args, **kwargs)
        title = self.kwargs.get('title')
        query = Comment.objects.filter(id_article__slug=title).order_by('-pub_date')
        context['comment'] = query
        return context


class CategoryView(ListView):
    model = Article
    context_object_name = 'category'
    template_name = "category_list.html"
    paginate_by = ARTICLES_LIMIT # variable global en settings.py

    def get_queryset(self):
        category_selected = self.kwargs.get('category')
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(categories__name=category_selected).order_by(ordenarArticulos (self.request))
        return queryset

    def get_context_data(self, *args, **kwargs):  # función para meter info de la categoría de la URL /category/<categoria>
        context = super().get_context_data(*args, **kwargs)
        category_selected = self.kwargs.get('category')
        context['categoria'] = category_selected
        return context

    def get_context_data(self, *args, **kwargs):  # función para meter el número de comentarios en función de la lista
        context = super().get_context_data(*args, **kwargs)
        category_selected = self.kwargs.get('category')
        comentarios = Comment.objects.order_by('-pub_date')
        articulos = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(categories__name=category_selected).order_by(ordenarArticulos (self.request))
        context['numofcomments'] = contarComentarios(comentarios, articulos)
        return context


class UserArticlesView(ListView):
    model = Article
    context_object_name = 'username'
    template_name = "user_articles_list.html"
    paginate_by = ARTICLES_LIMIT # variable global en settings.py

    def get_queryset(self):
        username_selected = self.kwargs.get('username')
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(id_user__username=username_selected).order_by(ordenarArticulos (self.request))
        return queryset

    def get_context_data(self, *args, **kwargs):  # función para meter info del usuario de la URL /username
        context = super().get_context_data(*args, **kwargs)
        username_selected = self.kwargs.get('username')
        context['usuario'] = username_selected
        return context

    def get_context_data(self, *args, **kwargs):  # función para meter el número de comentarios en función de la lista
        context = super().get_context_data(*args, **kwargs)
        username_selected = self.kwargs.get('username')
        comentarios = Comment.objects.order_by('-pub_date')
        articulos = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(id_user__username=username_selected).order_by(ordenarArticulos (self.request))
        context['numofcomments'] = contarComentarios(comentarios, articulos)
        return context


