#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "biblioteca_ceb.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        if not any(
            p in str(exc)
            for p in ("django", "django-admin", "django-admin.py")
        ):
            raise
        sys.stderr.write(
            "Error: Django is not installed or not in your PYTHONPATH.\n"
        )
        sys.exit(1)
    execute_from_command_line(sys.argv)
