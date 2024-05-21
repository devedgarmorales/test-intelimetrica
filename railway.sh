#!/bin/bash
python manage.py makemigrations && python manage.py migrate && python manage.py importar_restaurantes restaurantes.csv

gunicorn --bind 0.0.0.0:8000 melp.wsgi
