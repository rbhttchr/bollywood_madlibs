#!/bin/sh
rm ./db.sqlite3
rm -rf ./input/migrations
rm -rf ./input/__pycache__
rm -rf ./madlibs/__pycache__
python3 ./manage.py makemigrations input
python3 ./manage.py migrate --run-syncdb
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'ishanp2@illinois.edu', 'admin')" | python3 ./manage.py shell