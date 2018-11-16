#!/bin/bash

cd /simulation/goodbackend

## dev serv
#python3 app.py &

## guni prod flask
# python3 wsgi.py &
# gunicorn wsgi

# gunicorn --timeout 7200 --bind 0.0.0.0:5000 --workers=5 wsgi:app &
gunicorn --timeout 7200 --bind 127.0.0.1:5000 --workers=5 app:app &

cd ../
# cd /simulation/frontend/app
#ng build --prod &


nginx -g "daemon off;"
