# funicular
Site about funicular railways

git clone https://github.com/mmw111161/funicular.git

cd funicular/

python3 -m venv .venv

source .venv/bin/activate

cd funicular

pip install wagtail

pip install -r requirements.txt 

python3 -m pip install django-debug-toolbar

python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py createsuperuser
user/password: melvyn/admin

python3 manage.py createcachetable

python3 manage.py runserver


