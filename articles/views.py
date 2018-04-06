from django.utils.datetime_safe import datetime

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from articles.models import Article
from users.models import User

def orderList(request):
    answer = request.POST["order_list"]
    if answer == 0:
        return "-pub_date"
    if answer == 1:
        return "pub_date"


class HomeView(ListView):
    model = Article
    template_name = "home.html"
    ordering = orderList

    def get_queryset(self):
        queryset = Article.objects.filter(status='finalizado').filter(pub_date__lte=datetime.now())[:10] # limitamos a 10 el número de artículos en esta vista
        return queryset
        # artículos publicados, con fecha de publicación en el pasado y ordenadas de más reciernte a más antigua

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = "article_detail_page.html"

    def get_object(self):
        user_name = self.kwargs.get('username')
        return get_object_or_404(Article, id_user=User.objects.get(username=user_name).id, slug=self.kwargs.get('title'))
