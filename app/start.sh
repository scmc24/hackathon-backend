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
echo "=============== makemigrations accounts ===============\n"
python manage.py makemigrations accounts
echo "=============== makemigrations chat ===============\n"
python manage.py makemigrations chat
echo "=============== makemigrations test ===============\n"
python manage.py makemigrations test
echo "=============== makemigrations course ===============\n"
python manage.py makemigrations course
echo "=============== makemigrations challenge ===============\n"
python manage.py makemigrations challenge



echo "======================== migrations ========================"
echo "=============== migrate ===============\n"
python manage.py migrate accounts
echo "=============== migrate chat ===============\n"
python manage.py migrate chat
echo "=============== migrate test ===============\n"
python manage.py migrate test
echo "=============== migrate course ===============\n"
python manage.py migrate course
echo "=============== migrate challenge ===============\n"
python manage.py migrate challenge

echo "done ."
echo "==============================================================="
echo "================= collect static files ========================"
python manage.py collectstatic --noinput
echo "done ."
echo "=================running app==================================="
#daphne -b 0.0.0.0 -p 8001 app.asgi:application
python manage.py runserver 0.0.0.0:8000
exec "$@"
