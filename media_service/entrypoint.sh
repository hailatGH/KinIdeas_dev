#!/bin/bash
APP_PORT=${PORT:-8000}
cd /app/src/
/opt/venv/bin/python manage.py makemigrations audio_book
/opt/venv/bin/python manage.py migrate audio_book
/opt/venv/bin/python manage.py makemigrations company_profile
/opt/venv/bin/python manage.py migrate company_profile
/opt/venv/bin/python manage.py makemigrations music
/opt/venv/bin/python manage.py migrate music
/opt/venv/bin/python manage.py makemigrations podcast
/opt/venv/bin/python manage.py migrate podcast
/opt/venv/bin/python manage.py makemigrations radio
/opt/venv/bin/python manage.py migrate radio
/opt/venv/bin/python manage.py migrate --run-syncdb
/opt/venv/bin/python manage.py collectstatic --no-input
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@kinideas.com', 'playground')" | /opt/venv/bin/python manage.py shell
/opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm core.wsgi:application --bind "0.0.0.0:${APP_PORT}"