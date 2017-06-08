#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

    from django.core.management import execute_from_command_line


    # This allows easy placement of apps within the interior
    # pydanny_cookiecutter directory.
    current_path = os.path.dirname(os.path.abspath(__file__))
    sys.path.append(os.path.join(current_path, 'apps'))

    execute_from_command_line(sys.argv)
