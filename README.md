# Laboratorio 06: Motor de plantillas con Django

Este proyecto parte del laboratorio 05 y se mantiene en una carpeta y un
repositorio independientes. Conserva la aplicacion movies como base; la
implementacion especifica del laboratorio 06 esta pendiente.

## Preparar el entorno

```powershell
python -m venv .venv
.\.venv\Scripts\python -m pip install -r requirements.txt
.\.venv\Scripts\python manage.py migrate
.\.venv\Scripts\python manage.py seed_lab
.\.venv\Scripts\python manage.py runserver
```

El comando seed_lab crea datos y cuentas locales de demostracion del laboratorio 05.
Las contrasenas se guardan en .credentials-local.txt, excluido de Git.

La evidencia anterior se conserva en docs/ENTREGABLE.md como referencia del
laboratorio 05. Todavia no corresponde al entregable del laboratorio 06.

Este repositorio local no tiene un remoto de GitHub configurado.
