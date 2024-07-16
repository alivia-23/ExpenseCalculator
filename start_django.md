# start a python3 virtual environment, install django and django rest framework
mkdir expense_calculator
cd expense_calculator
python3 -m venv venv
source venv/bin/activate
pip install django djangorestframework
django-admin startproject expense_calculator .
django-admin startapp expenses
python manage.py runserver