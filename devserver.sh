#!/bin/sh
source .venv/bin/activate
PORT=${PORT:-5000}
FLASK_ENV=development
python -u -m flask --app main run -p $PORT --debug