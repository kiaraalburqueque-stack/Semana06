from django.contrib import admin
from .models import Genre, Movie, Person, Rating


class AuditAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 1
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Movie)
class MovieAdmin(AuditAdmin):
    list_display = ('title', 'year', 'genre_names', 'updated_at')
    list_filter = ('genres', 'year')
    search_fields = ('title', 'people__name')
    filter_horizontal = ('genres', 'people')
    inlines = (RatingInline,)

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('genres')

    @admin.display(description='Generos')
    def genre_names(self, obj):
        return ', '.join(genre.name for genre in obj.genres.all())


@admin.register(Genre)
class GenreAdmin(AuditAdmin):
    list_display = ('name', 'updated_at')
    search_fields = ('name',)


@admin.register(Person)
class PersonAdmin(AuditAdmin):
    list_display = ('name', 'birth_date', 'updated_at')
    search_fields = ('name',)


@admin.register(Rating)
class RatingAdmin(AuditAdmin):
    list_display = ('movie', 'reviewer', 'score', 'created_at')
    list_filter = ('score', 'movie__genres')
    search_fields = ('movie__title', 'reviewer')
    list_select_related = ('movie',)


admin.site.site_header = 'Administracion de peliculas'
admin.site.site_title = 'Movies Admin'
admin.site.index_title = 'Laboratorio 05'
