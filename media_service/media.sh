#!/bin/bash
apt-get update
apt-get upgrade
apt-get install python3-venv python3-dev gcc nginx

mkdir -p /home/hailemichael_atrsaw/Projects/Django
mkdir -p /home/hailemichael_atrsaw/Server_Logs
mkdir -p /home/hailemichael_atrsaw/Virtual_Environments

python3 -m venv /home/hailemichael_atrsaw/Virtual_Environments/media_service_env
mkdir /home/hailemichael_atrsaw/Virtual_Environments/media_service_env/vassals
source /home/hailemichael_atrsaw/Virtual_Environments/media_service_env/bin/activate

cd /home/hailemichael_atrsaw/Projects/Django
git clone https://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@github.com/hailatGH/KinIdeas_dev.git
cd KinIdeas_dev/media_service/

pip install -r requirements.txt
pip install uwsgi

cp ../Server_Conf/media.conf /etc/nginx/sites-available/
cp ../Server_Conf/uwsgi_params /src/
cp ../Server_Conf/media_service_uwsgi.ini /src/
cp ../Server_Conf/emperor.uwsgi.service /etc/systemd/system/emperor.uwsgi.service

cd src
python manage.py makemigrations audio_book
python manage.py migrate audio_book
python manage.py makemigrations music
python manage.py migrate music
python manage.py makemigrations podcast
python manage.py migrate podcast
python manage.py makemigrations radio
python manage.py migrate radio
python manage.py makemigrations company_profile
python manage.py migrate company_profile
python manage.py migrate --run-syncdb
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@kinideas.com', 'playground')" | python manage.py shell
python manage.py collectstatic --no-input

sudo ln -s /etc/nginx/sites-available/media.conf /etc/nginx/sites-enabled/
uwsgi --socket media.sock --module core.wsgi --chmod-socket=666
uwsgi --ini media_service_uwsgi.ini
sudo ln -s /home/hailemichael_atrsaw/Projects/Django/KinIdeas_dev/media_service/src/media_service_uwsgi.ini /home/hailemichael_atrsaw/Virtual_Environments/media_service_env/vassals/

systemctl enable emperor.uwsgi.service
systemctl start emperor.uwsgi.service
systemctl stop emperor.uwsgi.service
systemctl restart emperor.uwsgi.service