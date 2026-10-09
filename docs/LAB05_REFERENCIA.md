# Laboratorio 05 - Administrador con Django

## Integrantes y responsabilidades

Completar con los integrantes reales y el trabajo realizado.

| Alumno | Desarrollo realizado |
| --- | --- |
| Pendiente | Pendiente |

## Desarrollo y evidencias

Para cada desarrollo registra: nombre del alumno, titulo, captura real del
resultado, codigo relevante, explicacion y casos de prueba.

1. Modelos relacionados: adjuntar estructura del editor y migraciones.
2. Registro inicial: capturar el panel con registro simple antes de personalizar.
   Para reproducir esa etapa en una copia del proyecto, registrar los cuatro
   modelos con `admin.site.register([Movie, Genre, Person, Rating])` sin las
   clases ModelAdmin, capturar y volver a la version personalizada.
3. Panel personalizado: capturar columnas, filtro por genero y anio, y busqueda.
4. Formulario: capturar valoraciones en linea y campos de auditoria no editables.
5. Datos: registrar carga manual desde el panel de diez peliculas, cuatro generos
   y valoraciones para al menos cinco peliculas. El comando de ejemplo no
   sustituye la evidencia de esta carga manual.
6. Roles: capturar grupo editores, permisos y comparacion de ambas sesiones.
7. Recomendaciones: capturar una pelicula y el resultado ordenado por promedio.

## Casos de prueba manuales

| Caso | Resultado esperado | Resultado observado / captura |
| --- | --- | --- |
| Buscar Interstellar | Solo titulos coincidentes | Pendiente |
| Filtrar por genero y anio | Solo peliculas coincidentes | Pendiente |
| Agregar valoracion como admin | Se guarda dentro de la pelicula | Pendiente |
| Intentar puntuacion 6 | Error de validacion | Pendiente |
| Cambiar auditoria | No existen entradas editables | Pendiente |
| Entrar como editor | Puede agregar y cambiar peliculas | Pendiente |
| Borrar como editor por URL | Acceso denegado (403) | Pendiente |
| Abrir valoraciones como editor | Acceso denegado (403) | Pendiente |
| Ver recomendaciones | Mismo genero, sin pelicula original, promedio descendente | Pendiente |

## Observaciones

El panel resuelve CRUD, filtros y permisos mediante configuracion de ModelAdmin.
La recomendacion requiere una vista propia porque aplica una consulta especifica
del negocio para visitantes. El rol editor limita operaciones por responsabilidad
y evita conceder acceso total para tareas de mantenimiento del catalogo.

## Conclusiones

Redactar conclusiones personales despues de ejecutar las pruebas y adjuntar
las evidencias. Incluir enlace del repositorio del equipo.
