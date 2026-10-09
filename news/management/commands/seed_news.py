import io
from datetime import timedelta

from PIL import Image, ImageDraw
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from news.models import Article, Author, Category


class Command(BaseCommand):
    help = 'Create six example articles in three categories without overwriting edits.'

    @transaction.atomic
    def handle(self, *args, **options):
        author, _ = Author.objects.get_or_create(
            name='Redacción Campus',
            defaults={'biography': 'Equipo editorial dedicado a compartir novedades de la comunidad.'},
        )
        entries = [
            ('Tecnología', 'tecnologia', 'Un espacio para aprender programación', 'aprender-programacion',
             'Los talleres de programación acercan nuevas herramientas a estudiantes de distintas especialidades.',
             'El campus abre un espacio de aprendizaje colaborativo. Los participantes construyen pequeños proyectos y comparten sus avances.\n\nLa iniciativa combina ejercicios prácticos con sesiones de revisión para resolver dudas y mejorar el código.', '#215b53'),
            ('Tecnología', 'tecnologia', 'Ideas que se convierten en aplicaciones', 'ideas-aplicaciones',
             'Equipos estudiantiles presentan propuestas digitales para resolver necesidades de su comunidad.',
             'Los proyectos parten de una necesidad concreta y avanzan mediante prototipos. Cada equipo presenta su propuesta y recibe comentarios para mejorarla.\n\nEl objetivo es conectar la creatividad con soluciones que puedan ponerse a prueba.', '#356b79'),
            ('Cultura', 'cultura', 'El cine abre nuevas conversaciones', 'cine-conversaciones',
             'Una selección de películas invita a reflexionar y compartir distintas miradas sobre el mundo.',
             'El cineforo propone un encuentro entre historias y espectadores. Después de cada función se abre un diálogo sobre personajes, decisiones y contextos.\n\nEl catálogo de películas de la semana anterior sigue disponible en la sección Cine.', '#9b694b'),
            ('Cultura', 'cultura', 'Lecturas para descubrir otras voces', 'lecturas-voces',
             'El club de lectura reúne a estudiantes para conversar sobre cuentos y experiencias de distintos autores.',
             'Cada encuentro parte de un texto breve. Los asistentes comparten interpretaciones y recomendaciones para la siguiente sesión.\n\nNo se requiere experiencia previa: basta la curiosidad y las ganas de escuchar.', '#77618b'),
            ('Campus', 'campus', 'Una comunidad que aprende en equipo', 'comunidad-equipo',
             'Las jornadas de trabajo colaborativo promueven el intercambio de conocimientos entre estudiantes.',
             'Estudiantes de diferentes ciclos se reúnen para revisar proyectos y compartir recursos. El trabajo en equipo permite reconocer fortalezas y aprender nuevas formas de resolver problemas.\n\nCada grupo documenta sus avances y distribuye responsabilidades.', '#4a7250'),
            ('Campus', 'campus', 'Cómo se muestra una etiqueta HTML', 'prueba-escapado-html',
             'Una demostración del escapado automático explica cómo las plantillas muestran texto de forma segura.',
             'Este es el texto guardado desde el administrador:\n<strong>Noticia de prueba</strong>\n\nLa etiqueta se muestra literalmente y no convierte el texto en negrita. Django escapa los caracteres HTML al mostrar la variable en la plantilla.', '#526a8c'),
        ]
        for index, (name, category_slug, title, slug, summary, body, color) in enumerate(entries):
            category, _ = Category.objects.get_or_create(slug=category_slug, defaults={'name': name})
            article, created = Article.objects.get_or_create(slug=slug, defaults={
                'title': title, 'summary': summary, 'body': body, 'author': author,
                'published_at': timezone.now() - timedelta(hours=index),
            })
            if created:
                article.categories.add(category)
                picture = Image.new('RGB', (1000, 560), color)
                draw = ImageDraw.Draw(picture)
                draw.ellipse((600, -160, 1150, 390), fill='#c8ed72')
                draw.rectangle((70, 90, 85, 460), fill='#c8ed72')
                draw.text((120, 250), name.upper() + ' / CAMPUS NOTICIAS', fill='white', font_size=32)
                output = io.BytesIO()
                picture.save(output, format='JPEG', quality=90)
                article.featured_image.save(slug + '.jpg', ContentFile(output.getvalue()), save=True)
        self.stdout.write(self.style.SUCCESS('Six example articles and three categories are ready.'))
