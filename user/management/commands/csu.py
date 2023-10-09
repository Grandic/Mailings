from django.core.management import BaseCommand

from user.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        user = User.objects.create(
            email='d.bitkov@gmail.com',
            is_staff=True,
            is_active=True,
            is_superuser=True,
            verify_code='1234'
        )
        user.set_password('151087')
        user.save()