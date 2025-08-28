#!/usr/bin/env bash
# Exit on any command failure
set -o errexit

# Run database migrations
python manage.py migrate

# Optional: uncomment to collect static files if you have them
# python manage.py collectstatic --no-input