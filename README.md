make virtualenv \
pip install -r requirements.txt \
python manage.py makemigrations app \
python manage.py migrate \
python manage.py generate_dummy_data \
python manage.py createsuperuser \
python manage.py runserver
