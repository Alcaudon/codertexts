from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils.datetime_safe import datetime
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.views.generic.list import MultipleObjectMixin

from articles.forms import NewCommentForm
from articles.models import Article, Comment, Category
from codertexts.settings import ARTICLES_LIMIT
from users.models import User

def ordenarArticulos (peticion):
    orden = peticion.GET.get('order_by')
    if orden == 'antiguos':
        orden_list = 'pub_date'
    elif orden == 'modernos':
        orden_list = '-pub_date'
    else:
        orden_list = '-pub_date'
    return orden_list

def contarComentarios (comentarios, articulos):
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
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).order_by(ordenarArticulos (self.request)) # limitamos el número de artículos en esta vista en la variable ARTICLES_LIMIT de settings.py
        return queryset
        # artículos publicados, con fecha de publicación en el pasado y ordenadas de más reciente a más antigua

    def get_context_data(self, *args, **kwargs):  # función para meter el número de comentarios en función de la lista
        context = super().get_context_data(*args, **kwargs)
        comentarios = Comment.objects.order_by('-pub_date')
        articulos = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).order_by(ordenarArticulos(self.request))
        context['numofcomments'] = contarComentarios(comentarios, articulos)
        return context


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    context_object_name = 'article'
    form_class = NewCommentForm
    template_name = "article_detail_page.html"

    def get_object(self):
        user_name = self.kwargs.get('username')
        return get_object_or_404(Article, id_user=User.objects.get(username=user_name).id, slug=self.kwargs.get('title'))

    def get_context_data(self, *args, **kwargs):  # función para meter info de los comentarios
        context = super().get_context_data(*args, **kwargs)
        title = self.kwargs.get('title')
        query = Comment.objects.filter(id_article__slug=title).order_by('-created_at')
        context['comment'] = query
        return context

    def post(self, request, username, title):
        form = NewCommentForm(request.POST)
        if form.is_valid():
            form.instance.id_article = get_object_or_404(Article, slug = title)
            form.instance.id_user_comment = get_object_or_404(User, username = request.user)
            form.instance.pub_date = datetime.now()
            form.save()
            return HttpResponseRedirect(reverse('article_detail_page', kwargs={'username': username, 'title': title}))
        else:
            messages.error(request, "Vuelva a intentarlo")
        return HttpResponseRedirect(reverse('article_detail_page', kwargs={'username': username, 'title': title}))

class CategoryView(ListView, MultipleObjectMixin):
    model = Article
    context_object_name = 'category'
    template_name = "category_list.html"
    paginate_by = ARTICLES_LIMIT # variable global en settings.py

    def get_queryset(self):
        category_selected = self.kwargs.get('category')
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(categories__name=category_selected).order_by(ordenarArticulos(self.request))
        return queryset

    def get_context_data(self, *args, **kwargs):  # función para meter el número de comentarios en función de la lista e info de la categoría de la URL /category/<categoria>
        context = super().get_context_data(*args, **kwargs)
        categoria = get_object_or_404(Category, name=self.kwargs.get('category'))
        comentarios = Comment.objects.order_by('-pub_date')
        articulos = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(categories__name=categoria.name).order_by(ordenarArticulos(self.request))
        context['numofcomments'] = contarComentarios(comentarios, articulos)
        context['categoria']=categoria
        return context

class UserArticlesView(ListView):
    model = Article
    context_object_name = 'username'
    template_name = "user_articles_list.html"
    paginate_by = ARTICLES_LIMIT # variable global en settings.py

    def get_queryset(self):
        username_selected = self.kwargs.get('username')
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(id_user__username=username_selected).order_by(ordenarArticulos(self.request))
        return queryset

    def get_context_data(self, *args, **kwargs):  # función para meter el número de comentarios en función de la lista e info de la categoría de la URL /<username>
        context = super().get_context_data(*args, **kwargs)
        usuario = get_object_or_404(User, username=self.kwargs.get('username'))
        comentarios = Comment.objects.order_by('-pub_date')
        articulos = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(id_user__username=usuario.username).order_by(ordenarArticulos(self.request))
        context['numofcomments'] = contarComentarios(comentarios, articulos)
        context['usuario'] = usuario
        return context

class LookUpView(ListView): #sin acabar, en desarrollo
    model = Article
    context_object_name = 'lookup'
    template_name = "lookup_list.html"
    paginate_by = ARTICLES_LIMIT  # variable global en settings.py

    def get_queryset(self, request):
        busqueda = request.GET.get('lookup')
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now()).filter(title=busqueda).order_by(ordenarArticulos(self.request))
        return queryset

def angular(request):
    return render(request, "angular/index.html")

