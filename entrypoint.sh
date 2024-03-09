#!/bin/sh

# Wait for PostgreSQL to be ready
while ! nc -z db 5432; do
  sleep 1
done

# Perform migrations
flask db init
flask db migrate
flask db upgrade

# Start Flask app
exec flask run --host=0.0.0.0
