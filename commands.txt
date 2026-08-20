django-admin startproject book_manager .
python manage.py startapp books
python manage.py startapp accounts

python manage.py makemigrations
python manage.py migrate

pentru instalat restul de packete, intr-un terminal unde este .venv activat:
pip install -r requirements.txt

Pentru a updata requirements:
pip freeze > requirements.txt

Pentru teste:

pytest

Cand adaugam un APP nou in proiectul de django, trebuie adaugat in settings la INSTALLED_APPS.