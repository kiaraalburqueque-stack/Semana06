from datetime import timedelta
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Article, Author, Category


class PortalTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = Author.objects.create(name='Test author')
        cls.category = Category.objects.create(name='Tecnología', slug='tecnologia')
        cls.empty_category = Category.objects.create(name='Vacía', slug='vacia')
        cls.article = Article.objects.create(
            title='Published article', slug='published', summary='A useful summary',
            body='<strong>Noticia de prueba</strong>', author=cls.author,
        )
        cls.article.categories.add(cls.category)
        cls.future = Article.objects.create(
            title='Future article', slug='future', summary='Pending', body='Pending',
            author=cls.author, published_at=timezone.now() + timedelta(days=2),
        )

    def test_home_uses_base_and_shared_card(self):
        response = self.client.get(reverse('news:home'))
        self.assertContains(response, self.article.title)
        self.assertNotContains(response, self.future.title)
        for template in ['base.html', 'news/home.html', 'news/_article_card.html']:
            self.assertTemplateUsed(response, template)

    def test_detail_escapes_html_and_handles_missing_image(self):
        response = self.client.get(reverse('news:detail', args=[self.article.slug]))
        self.assertContains(response, '&lt;strong&gt;Noticia de prueba&lt;/strong&gt;')
        self.assertNotContains(response, '<strong>Noticia de prueba</strong>')
        self.assertContains(response, self.author.name)
        self.assertContains(response, reverse('news:category', args=[self.category.slug]))

    def test_category_filters_and_empty_state(self):
        other = Article.objects.create(title='Other topic', slug='other', author=self.author, summary='Other', body='Other')
        response = self.client.get(reverse('news:category', args=[self.category.slug]))
        self.assertContains(response, self.article.title)
        self.assertNotContains(response, other.title)
        self.assertTemplateUsed(response, 'news/_article_card.html')
        response = self.client.get(reverse('news:category', args=[self.empty_category.slug]))
        self.assertContains(response, 'No hay noticias publicadas')

    def test_empty_home_and_unknown_urls(self):
        Article.objects.all().delete()
        self.assertContains(self.client.get(reverse('news:home')), 'Todavía no hay noticias')
        self.assertEqual(self.client.get(reverse('news:detail', args=['missing'])).status_code, 404)
        self.assertEqual(self.client.get(reverse('news:category', args=['missing'])).status_code, 404)

    def test_future_article_is_not_public(self):
        self.assertEqual(self.client.get(reverse('news:detail', args=[self.future.slug])).status_code, 404)

    def test_admin_edit_appears_in_portal(self):
        user = get_user_model().objects.create_superuser('portal_admin', 'test@example.com', 'test-password')
        self.client.force_login(user)
        response = self.client.post(reverse('admin:news_article_change', args=[self.article.pk]), {
            'title': 'Updated through admin', 'slug': self.article.slug,
            'summary': 'Changed summary', 'body': 'Changed body',
            'author': self.author.pk, 'categories': [self.category.pk],
            'published_at_0': '2026-01-01', 'published_at_1': '12:00:00', '_save': 'Save',
        })
        self.assertEqual(response.status_code, 302)
        self.client.logout()
        self.assertContains(self.client.get(reverse('news:home')), 'Updated through admin')
        self.assertContains(self.client.get(reverse('news:detail', args=[self.article.slug])), 'Changed body')
