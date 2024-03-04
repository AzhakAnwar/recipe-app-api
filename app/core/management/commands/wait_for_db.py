"""
Django command to wait for DB to be available.
"""

from typing import Any
import time
from psycopg2 import OperationalError as Psycopg2OpError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args: Any, **options: Any):  # -> str | None:
        """Encryption for command."""
        # return super().handle(*args, **options)
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write("DB unavailable, waiting 1 second...")
                time.sleep()
        self.stdout.write(self.style.SUCCESS("Database available!"))
