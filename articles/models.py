from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
import datetime

from django.template.defaultfilters import slugify
from django.urls import reverse

STATUS_CHOICES = (
    ('finalizado','FINALIZADO'),
    ('borrador', 'BORRADOR'),
)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Article(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles")
    pub_date = models.DateField(default=datetime.date.today)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrador')
    image = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=250)
    text = models.TextField()
    id_reply = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name="articles")
    slug = models.SlugField(max_length=250) #nuevo campo en el modelo para las URLs

    def save(self, *args, **kwargs): # convertimos el 'title' en slug y lo guardamos en 'slug'
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    #def get_absolute_url(self):
        #    kwargs = {'username': self.User.objects.get(id=id_user).username,
        #          'title': self.slug
        #          }
    #return reverse('article_detail_page', kwargs=kwargs)

    def __str__(self):
        return self.pub_date.strftime('%m/%d/%Y') + " - " + self.title

    class Meta:
        indexes = [models.Index(fields=['-pub_date', 'id_user']), ]
        ordering = ['-pub_date', ]
        verbose_name_plural = "articles"

    def clean(self):
        if (self.image == '' or self.image == None) and (self.video == '' or self.video == None):
            raise ValidationError('Debes incluir una imagen o un video.')


class Favorite(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favorites")
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="favorites")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "favorites"

    def __str__(self):
        return str(self.id_user) + " - " + str(self.id_article)


class Comment(models.Model):
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comment")
    id_user_comment = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comment")
    pub_date = models.DateField(default=datetime.date.today)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "comments"

    def __str__(self):
        return str(self.id_article) + " - " + str(self.id_user_comment)


class Underline(models.Model):
    id_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="underline")
    id_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="underline")
    marked_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "underlines"

    def __str__(self):
        return str(self.id_user) + " - " + str(self.id_article)