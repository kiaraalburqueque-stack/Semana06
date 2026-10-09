# Laboratorio 06: Motor de plantillas con Django

Proyecto acumulativo basado en el laboratorio 05, con carpeta y repositorio
independientes. La aplicación movies conserva el trabajo anterior. La aplicación
news implementa el portal de noticias solicitado por la guía del laboratorio 06.

## Ejecutar en Windows

Requiere Python 3.12 o superior. Desde D:\Semana6:

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py seed_lab
.\.venv\Scripts\python manage.py seed_news
.\.venv\Scripts\python manage.py runserver 8006
```

- Portada: http://127.0.0.1:8006/
- Administrador: http://127.0.0.1:8006/admin/
- Catálogo del laboratorio 05: http://127.0.0.1:8006/cine/

seed_lab crea las cuentas admin y editor. Las contraseñas locales aleatorias
se guardan en .credentials-local.txt, excluido de Git. No se publican en el
repositorio. El editor conserva los permisos del laboratorio 05; para gestionar
noticias usa admin. También puedes crear una cuenta con createsuperuser.

seed_news carga seis noticias en tres categorías y genera imágenes de ejemplo
con Pillow. Repetirlo no sobrescribe cambios del administrador. Estos datos son
demostrativos. Practica y documenta también la carga manual desde el panel.
Las noticias con fecha futura no aparecen hasta su publicación.

## Estructura de las plantillas

- templates/base.html: estructura común, navegación y bloques title, content y sidebar.
- news/templates/news/home.html: portada con for, empty, include y length.
- news/templates/news/_article_card.html: tarjeta compartida con if, date y truncatewords.
- news/templates/news/detail.html: cuerpo, imagen, autor y categorías; hereda de base.
- news/templates/news/category_list.html: listado filtrado; reutiliza la tarjeta.
- news/static/news/styles.css: estilos cargados con load static.

Las rutas se enlazan con url. Las consultas y la selección de noticias publicadas
se resuelven en views.py; las plantillas presentan los datos. El contenido se
gestiona con ArticleAdmin, CategoryAdmin y AuthorAdmin, incluyendo columnas,
filtros y búsqueda. Las imágenes cargadas se sirven localmente desde MEDIA_ROOT.

## Escapado automático

La noticia “Cómo se muestra una etiqueta HTML” contiene
<strong>Noticia de prueba</strong>. El detalle muestra esos caracteres como texto,
sin convertirlos en negrita. Django escapa el HTML al renderizar article.body.
Se conserva el escapado automático y no se utiliza safe. white-space: pre-wrap
mantiene los saltos de línea sin interpretar HTML.

## Verificar

```powershell
python manage.py check
python manage.py test
```

Las pruebas de news comprueban herencia, fragmentos, categorías, estados vacíos,
escapado, fechas futuras y una edición real a través del administrador que se
refleja en el portal. También se conservan las pruebas de movies.

## Entrega

Completa docs/ENTREGABLE.md con integrantes, capturas reales y resultados
observados. docs/LAB05_REFERENCIA.md conserva el documento anterior.
La base SQLite, medios, contraseñas y entorno virtual están excluidos de Git.
El repositorio local aún no tiene remoto: crea un repositorio vacío Semana06
en GitHub y conecta su URL antes de subirlo. Esta configuración es para uso local.
