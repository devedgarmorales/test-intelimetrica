#!/bin/sh

echo 'Applying migrations...'
python manage.py makemigration && python manage.py migrate

echo 'Run Command...'
python manage.py importar_restaurantes restaurantes.csv

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=melp.settings melp.wsgi:application --bind 0.0.0.0:$PORT