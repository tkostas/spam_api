#!/bin/sh
exec gunicorn -b :5000 --workers=2 --access-logfile - --error-logfile - api:app