import os

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help_text = "Creates Default Admin User. DOES NOT USE THAT FOR PRODUCTION."

    def handle(self, *args, **options):
        User = get_user_model()
        try:
            User.objects.create_superuser(
                username=os.getenv("SUPERUSER_USERNAME"),
                password=os.getenv("SUPERUSER_PASSWORD")
            )
            self.stdout.write(
                self.style.SUCCESS(
                    'Successfully created superuser with '
                    'username=admin password=rootpassword'
                )
            )

        except:
            pass
