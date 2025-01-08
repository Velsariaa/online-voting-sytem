#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cpetovs.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment? If you haven't installed Django, you can do so by running 'pip install django'."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

# To run the Django application, use the following command:
# python manage.py runserver
# pip instal mysqlclient
# pip installl django
# pip install Pillow