#!/bin/sh
sleep 8s

if [ ! -f .initialized ]; then
    echo "Initializing container"

    python manage.py makemigrations qxorkut
    python manage.py migrate

    touch .initialized
fi

python manage.py runserver 0.0.0.0:8000