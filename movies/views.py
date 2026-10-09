from django.db.models import Avg
from django.shortcuts import get_object_or_404, render
from .models import Movie


def catalog(request):
    movies = Movie.objects.annotate(average_score=Avg('ratings__score')).prefetch_related('genres')
    query = request.GET.get('q', '').strip()
    if query:
        movies = movies.filter(title__icontains=query)
    return render(request, 'movies/catalog.html', {'movies': movies, 'query': query})


def recommendations(request, pk):
    movie = get_object_or_404(Movie.objects.prefetch_related('genres'), pk=pk)
    # A subquery avoids multiplying ratings when movies share several genres.
    related_ids = Movie.objects.filter(genres__in=movie.genres.all()).values('pk')
    movies = (
        Movie.objects.filter(pk__in=related_ids).exclude(pk=movie.pk)
        .annotate(average_score=Avg('ratings__score'))
        .filter(average_score__isnull=False)
        .prefetch_related('genres').order_by('-average_score', 'title')[:10]
    )
    return render(request, 'movies/catalog.html', {'movies': movies, 'selected': movie})
