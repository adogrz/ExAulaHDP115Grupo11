#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
python manage.py import_prices_CB_from_csv canasta/data/anios.csv canasta/data/precios.csv
python manage.py create_custom_superuser admin admin@admin.com --password admin