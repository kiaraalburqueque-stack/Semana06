from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class AuditModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Genre(AuditModel):
    name = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'genero'
        verbose_name_plural = 'generos'

    def __str__(self):
        return self.name


class Person(AuditModel):
    name = models.CharField(max_length=150)
    biography = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'persona'

    def __str__(self):
        return self.name


class Movie(AuditModel):
    title = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField(validators=[MinValueValidator(1888)])
    synopsis = models.TextField(blank=True)
    poster = models.ImageField(upload_to='posters/', blank=True)
    genres = models.ManyToManyField(Genre, related_name='movies')
    people = models.ManyToManyField(Person, related_name='movies', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'pelicula'

    def __str__(self):
        return f'{self.title} ({self.year})'


class Rating(AuditModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    reviewer = models.CharField(max_length=100)
    score = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'valoracion'
        verbose_name_plural = 'valoraciones'
        constraints = [models.CheckConstraint(condition=models.Q(score__gte=1, score__lte=5), name='rating_score_range')]

    def __str__(self):
        return f'{self.movie}: {self.score}/5 - {self.reviewer}'
