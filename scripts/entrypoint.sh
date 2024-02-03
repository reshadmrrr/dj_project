#!/bin/sh -xe

cd core/

python manage.py migrate

python manage.py runserver
