#!/bin/bash
./manage.py migrate
gunicorn config.asgi:application
