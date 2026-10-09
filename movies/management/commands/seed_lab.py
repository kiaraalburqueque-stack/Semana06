import secrets
from pathlib import Path

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from django.db import transaction

from movies.models import Genre, Movie, Person, Rating


class Command(BaseCommand):
    help = 'Create repeatable lab data, roles and local demonstration accounts.'

    @transaction.atomic
    def handle(self, *args, **options):
        genres = {name: Genre.objects.get_or_create(name=name)[0] for name in (
            'Ciencia ficcion', 'Drama', 'Animacion', 'Aventura'
        )}
        person, _ = Person.objects.get_or_create(name='Christopher Nolan')
        entries = [
            ('Interstellar', 2014, ['Ciencia ficcion', 'Drama'], 5),
            ('Inception', 2010, ['Ciencia ficcion', 'Aventura'], 5),
            ('The Martian', 2015, ['Ciencia ficcion', 'Aventura'], 4),
            ('Arrival', 2016, ['Ciencia ficcion', 'Drama'], 4),
            ('The Shawshank Redemption', 1994, ['Drama'], 5),
            ('Forrest Gump', 1994, ['Drama'], 4),
            ('Toy Story', 1995, ['Animacion', 'Aventura'], 5),
            ('Finding Nemo', 2003, ['Animacion', 'Aventura'], 4),
            ('Up', 2009, ['Animacion', 'Aventura'], 4),
            ('Jurassic Park', 1993, ['Aventura', 'Ciencia ficcion'], 4),
        ]
        for title, year, names, score in entries:
            movie, created = Movie.objects.get_or_create(
                title=title, year=year, defaults={'synopsis': f'Pelicula de {year} para el catalogo del laboratorio.'}
            )
            if created:
                movie.genres.set([genres[name] for name in names])
                if title in ('Interstellar', 'Inception'):
                    movie.people.add(person)
            Rating.objects.get_or_create(movie=movie, reviewer='Demo', defaults={'score': score})

        group, _ = Group.objects.get_or_create(name='editores')
        group.permissions.set(Permission.objects.filter(
            content_type__app_label='movies',
            content_type__model='movie',
            codename__in=['add_movie', 'change_movie', 'view_movie'],
        ))
        credentials = []
        for username, is_superuser in [('admin', True), ('editor', False)]:
            user, created = get_user_model().objects.get_or_create(
                username=username, defaults={'is_staff': True, 'is_superuser': is_superuser}
            )
            if created:
                password = secrets.token_urlsafe(14)
                user.set_password(password)
                user.save()
                credentials.append(f'{username}: {password}')
            if username == 'editor':
                user.groups.add(group)
        if credentials:
            path = Path(settings.BASE_DIR) / '.credentials-local.txt'
            with path.open('a', encoding='utf-8') as output:
                output.write('\n'.join(credentials) + '\n')
            self.stdout.write('New account passwords: .credentials-local.txt (excluded from Git).')
        self.stdout.write(self.style.SUCCESS('Lab data and editor group are ready.'))
