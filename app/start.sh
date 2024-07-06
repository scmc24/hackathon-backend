#!/bin/sh

if [ "$DATABASE" = "hack" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.5
    done

    echo "PostgreSQL started"
fi
echo "========================makemigrations ========================"
python manage.py makemigrations
#python manage.py makemigrations accounts 


echo "================= migrate ====================================="
echo "==============================================================="
python manage.py migrate
echo "done ."
echo "==============================================================="
echo "================= collect static files ========================"
python manage.py collectstatic --noinput
echo "done ."
echo "=================running app==================================="
#daphne -b 0.0.0.0 -p 8001 app.asgi:application
python manage.py runserver 0.0.0.0:8000
exec "$@"
