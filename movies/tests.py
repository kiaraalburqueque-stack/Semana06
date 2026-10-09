from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from .models import Genre, Movie, Rating


class LabTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Existing users prevent the seed command from writing password files.
        get_user_model().objects.create_superuser('admin', password='Test-only-password!')
        get_user_model().objects.create_user('editor', is_staff=True)
        call_command('seed_lab', verbosity=0)

    def test_seed_is_repeatable(self):
        call_command('seed_lab', verbosity=0)
        self.assertEqual(Movie.objects.count(), 10)
        self.assertEqual(Genre.objects.count(), 4)
        self.assertEqual(Rating.objects.count(), 10)

    def test_editor_permissions_and_admin_routes(self):
        user = get_user_model().objects.get(username='editor')
        self.client.force_login(user)
        movie = Movie.objects.first()
        self.assertTrue(user.has_perm('movies.add_movie'))
        self.assertTrue(user.has_perm('movies.change_movie'))
        self.assertFalse(user.has_perm('movies.delete_movie'))
        self.assertFalse(user.has_perm('movies.change_rating'))
        self.assertEqual(self.client.get(reverse('admin:movies_movie_add')).status_code, 200)
        self.assertEqual(self.client.get(reverse('admin:movies_movie_change', args=[movie.pk])).status_code, 200)
        self.assertEqual(self.client.post(reverse('admin:movies_movie_delete', args=[movie.pk]), {'post': 'yes'}).status_code, 403)
        self.assertEqual(self.client.get(reverse('admin:movies_rating_changelist')).status_code, 403)

    def test_recommendations_are_ranked_and_exclude_unrelated(self):
        movie = Movie.objects.get(title='Interstellar')
        response = self.client.get(reverse('movies:recommendations', args=[movie.pk]))
        results = list(response.context['movies'])
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(movie, results)
        self.assertNotIn(Movie.objects.get(title='Toy Story'), results)
        scores = [item.average_score for item in results]
        self.assertEqual(scores, sorted(scores, reverse=True))

    def test_audit_fields_are_readonly_and_search_works(self):
        self.client.force_login(get_user_model().objects.get(username='admin'))
        movie = Movie.objects.first()
        response = self.client.get(reverse('admin:movies_movie_change', args=[movie.pk]))
        form = response.context['adminform'].form
        self.assertNotIn('created_at', form.fields)
        self.assertNotIn('updated_at', form.fields)
        response = self.client.get(reverse('admin:movies_movie_changelist'), {'q': 'Interstellar'})
        self.assertEqual(list(response.context['cl'].queryset), [Movie.objects.get(title='Interstellar')])

    def test_public_catalog_and_missing_movie(self):
        self.assertContains(self.client.get(reverse('movies:catalog')), 'Interstellar')
        self.assertEqual(self.client.get(reverse('movies:recommendations', args=[99999])).status_code, 404)
