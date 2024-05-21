
# Test-Intelimetrica

Proyecto para vacante laboral que analiza un csv y expone servicios de restaurantes.

## Tabla de Contenido
- [Instalación](#instalación)
- [Uso](#uso)
- [Servicios Disponibles](#servicios)

## Instalación

Para la instación es necesario realizar el pull del proyecto.

Antes de este punto es necesario ya contar con una base de datos postgres con la extension postgis configurada.

Crear y activar entorno virtual
```bash
  python3 -m venv env

  source env/bin/activate

  pip3 install -r requerimientos.txt
```
Crear archivo para variables de entorno

```bash
cd melp

touch .env

SECRET_KEY=<secret_key_django_app>
DEBUG=True
POSTGRESQL_DB=<nombre_de_la_base_de_datos>
POSTGRESQL_USER=<nombre_del_usuario>
POSTGRESQL_PWD=<contraseña>
POSTGRESQL_HOST=<host>
POSTGRESQL_PORT=<puerto>
```

Ejecutar migraciones e importar CSV


```bash
# Ejecutar migraciones
python manage.py makemigration && python manage.py migrate

# Importar CSV
python manage.py importar_restaurantes restaurantes.csv
```

Correr el proyecto

```bash
python manage.py runserver
```
## Uso

Para utilizar la aplicación, inicia el servidor de desarrollo y accede a http://127.0.0.1:8000 desde tu navegador web. A continuación, podrás interactuar con los servicios de la aplicación mediante las URL definidas.


## Servicios Disponibles

La aplicación ofrece los siguientes servicios:

CRUD de Restaurantes: Permite crear, leer, actualizar y eliminar información de restaurantes.
Servicio de Estadísticas: Permite consultar restaurantes dentro de un área específica y obtener la calificación promedio y la desviación estándar.


### Endpoints
Crear Restaurante: POST /api/restaurantes/

Obtener Restaurantes: GET /api/restaurantes/

Actualizar Restaurante: PUT /api/restaurantes/<id>/

Eliminar Restaurante: DELETE /api/restaurantes/<id>/

Estadísticas de Restaurantes: GET /api/restaurantes/estadisticas/?latitud=<LAT>&longitud=<LNG>&radio=<RADIO>

Parámetros:
- latitud: Latitud del punto central.
- lng: Longitud del punto central.
- radio: Radio en metros.