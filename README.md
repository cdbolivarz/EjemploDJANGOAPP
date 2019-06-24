# EjemploDJANGOAPP
Ejemplo aplicación en Django

### Instalación

Instalar django

```shell
pip install django
```

Instalar ORM

```shell
pip install mysqlclient
```

Configurar la base de datos en el archivo, obviamente deben tener instalado MySQL y corriendo en algún puerto.

Se debe de crear una base de datos llamada **asesoratebd**.

```
AsesorateSAS/settings.py
```

Ubicarse en el directorio del repositorio y desde la consola realizar los siguientes pasos:

Crear migraciones

```shell
pyhton manage.py makemigrations
```

Migrar base de datos

```shell
pyhton manage.py migrate
```

Run server

```shell
pyhton manage.py runserver
```

Ir al navegador a la ruta:
<localhost:8000/registroForm>

Los archivos importantes son:

```
models.py
AsesorateSAS/urls
views.py
serializables.py
vista/registro.html
```

aunque en este ejemplo no se utilizó serializables.