#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=config.settings.production

echo 'Applying migrations...'
python manage.py wait_for_db --settings=config.settings.production
python manage.py migrate --settings=config.settings.production

echo 'Run Command...'
python manage.py importar_restaurantes restaurantes.csv

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=melp.settings melp.wsgi:application --bind 0.0.0.0:$PORT