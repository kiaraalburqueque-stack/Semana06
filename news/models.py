from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField('nombre', max_length=80, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'categoría'
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField('nombre', max_length=150)
    biography = models.TextField('biografía', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'autor'
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField('título', max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.TextField('resumen')
    body = models.TextField('contenido')
    featured_image = models.ImageField('imagen destacada', upload_to='articles/', blank=True)
    published_at = models.DateTimeField('fecha de publicación', default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='articles', verbose_name='autor')
    categories = models.ManyToManyField(Category, related_name='articles', verbose_name='categorías')

    class Meta:
        ordering = ['-published_at', '-pk']
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'

    def __str__(self):
        return self.title
