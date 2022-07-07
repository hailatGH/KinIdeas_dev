#!/bin/bash
python manage.py makemigrations audio_book
python manage.py migrate audio_book
python manage.py makemigrations company_profile
python manage.py migrate company_profile
python manage.py makemigrations music
python manage.py migrate music
python manage.py makemigrations podcast
python manage.py migrate podcast
python manage.py makemigrations radio
python manage.py migrate radio
python manage.py migrate --run-syncdb
python manage.py collectstatic --no-input