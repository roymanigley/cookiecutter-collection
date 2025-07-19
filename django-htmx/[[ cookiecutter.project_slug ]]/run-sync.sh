#!/bin/bash
./manage.py compilemessages
./manage.py migrate
gunicorn config.asgi:application
