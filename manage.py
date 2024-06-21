#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if 'collectstatic' in sys.argv and os.environ.get('DISABLE_COLLECTSTATIC') == '1':
        sys.argv = [arg for arg in sys.argv if arg != 'collectstatic']
        sys.argv.append('check')  # Replace 'collectstatic' with 'check' to avoid errors
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()