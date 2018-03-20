from django.contrib import admin

from articles.models import Article, Category, Favorite, Comment, Underline

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Favorite)
admin.site.register(Comment)
admin.site.register(Underline)