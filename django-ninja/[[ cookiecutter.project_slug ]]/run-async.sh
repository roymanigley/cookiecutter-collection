#!/bin/bash
./manage.py migrate
uvicorn config.asgi:application
