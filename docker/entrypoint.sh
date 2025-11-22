#!/bin/bash

set -e

echo "Starting entrypoint script..."

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to be ready..."
while ! nc -z $POSTGRES_HOST ${POSTGRES_PORT:-5432}; do
    sleep 0.1
done
echo "PostgreSQL is ready!"

# Install npm dependencies if needed
if [ ! -d "node_modules" ]; then
    echo "Installing npm dependencies..."
    npm install
fi

# Run Django migrations
echo "Creating migrations..."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Create superuser
echo "Creating superuser..."
python manage.py shell <<EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"Superuser '{username}' created successfully!")
    else:
        print(f"Superuser '{username}' already exists.")
else:
    print("Superuser creation skipped - no credentials provided.")
EOF

# Start Django development server
echo "Starting Django development server on 0.0.0.0:8000..."
python manage.py runserver 0.0.0.0:8000