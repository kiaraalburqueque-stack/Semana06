# Laboratorio 06 — Motor de plantillas con Django

## Integrantes y responsabilidades

| Alumno | Desarrollo realizado |
| --- | --- |
| Completar | Completar con el trabajo real |

Repositorio del equipo: pendiente de crear/conectar en GitHub.

## Desarrollo y evidencias

Por cada evidencia agrega: nombre del alumno, título del desarrollo, captura real,
código relevante, explicación del resultado y casos de prueba. Adjunta también
una captura de la estructura del proyecto en VS Code.

| Evidencia | Archivos o acción que documentar | Captura |
| --- | --- | --- |
| Configuración | news en INSTALLED_APPS, TEMPLATES DIRS, STATIC_URL, MEDIA_URL, MEDIA_ROOT y config/urls.py | Pendiente |
| Modelos y migración | Article, Category, Author; relaciones y campo ImageField | Pendiente |
| Herencia | base.html y extends en las tres páginas; bloques title, content y sidebar | Pendiente |
| Fragmento compartido | _article_card.html incluido en portada y categoría | Pendiente |
| Variables, control y filtros | for, empty, if, date, truncatewords y length | Pendiente |
| Portada | Seis noticias e imágenes visibles | Pendiente |
| Detalle | Imagen, autor, contenido y categorías enlazadas | Pendiente |
| Categoría | Solo noticias del tema seleccionado | Pendiente |
| Estáticos y medios | CSS cargado e imagen servida correctamente | Pendiente |
| Administrador | Columnas, búsqueda y filtros de las tres entidades | Pendiente |
| Gestión de contenido | Crear/editar una noticia desde admin y comprobar el resultado público | Pendiente |
| Escapado automático | Cuerpo con <strong>Noticia de prueba</strong> mostrado literalmente | Pendiente |
| Repositorio | URL, estructura de plantillas, migraciones y observaciones | Pendiente |

Los datos de seed_news facilitan la demostración; registra también el alta manual
de noticias y categorías desde el administrador que solicita la guía.

## Casos de prueba manuales

| Caso | Resultado esperado | Resultado observado / captura |
| --- | --- | --- |
| Abrir portada | Noticias publicadas, resúmenes recortados y fecha formateada | Pendiente |
| Abrir noticia | Imagen, autor, categorías y cuerpo correspondientes | Pendiente |
| Seleccionar categoría | Solo noticias relacionadas | Pendiente |
| Categoría sin noticias | Mensaje de lista vacía | Pendiente |
| Portada sin noticias publicadas | Mensaje de portada vacía | Pendiente |
| Noticia sin imagen | Tarjeta con alternativa visual; detalle sin imagen rota | Pendiente |
| Editar título y cuerpo en admin | Cambios visibles al recargar portada y detalle | Pendiente |
| Cargar una imagen en admin | Se ve en tarjeta y detalle | Pendiente |
| Buscar y filtrar noticias en admin | Registros coincidentes | Pendiente |
| Guardar etiqueta HTML en cuerpo | Etiqueta visible como texto, sin ejecutarse | Pendiente |
| Fecha de publicación futura | Noticia oculta en portada, categoría y detalle público | Pendiente |
| Ruta de noticia inexistente | Respuesta 404 | Pendiente |
| Ejecutar check y test | Sin errores de configuración; pruebas aprobadas | Pendiente |

## Observaciones

El laboratorio 05 proporciona la base del proyecto y la práctica de Django Admin.
El laboratorio 06 incorpora news para cumplir las entidades indicadas en la guía;
movies se conserva en /cine/. No se reinicia ni se modifica la carpeta Semana5.

La base reúne el marcado común; las páginas rellenan sus bloques. La tarjeta
compartida evita duplicar el HTML de las noticias. Las vistas consultan el modelo
y las plantillas presentan el resultado con variables, etiquetas y filtros.

Los cambios en las noticias, autores y categorías se guardan desde el administrador
y aparecen al recargar el portal, sin editar código. Las fechas futuras se filtran
en la vista. El escapado automático convierte los caracteres especiales del HTML
en texto visible; no se usa safe para mostrar el cuerpo.

Las imágenes de ejemplo se generan con Pillow; los archivos multimedia no se
versionan. Al clonar, las migraciones y seed_news reconstruyen la demostración.

## Conclusiones

Completar con conclusiones personales después de ejecutar los casos y adjuntar
capturas. No se incluyen capturas ni resultados manuales inventados.
