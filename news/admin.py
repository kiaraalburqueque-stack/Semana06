from django.contrib import admin
from .models import Article, Author, Category


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_at']
    list_filter = ['categories', 'author', 'published_at']
    search_fields = ['title', 'summary', 'body', 'author__name']
    prepopulated_fields = {'slug': ['title']}
    filter_horizontal = ['categories']
    date_hierarchy = 'published_at'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    search_fields = ['name']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'biography']
    list_filter = ['name']
    search_fields = ['name', 'biography']
