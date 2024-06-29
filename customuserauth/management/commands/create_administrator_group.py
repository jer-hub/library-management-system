from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

def create_admin_group(self):
    if not Group.objects.filter(name="Administrators").exists():
        admin_group = Group.objects.create(name="Administrators")
        print(f'Administrator group "{admin_group.name}" created successfully!')

class Command(BaseCommand):
    help = 'Creates the "Administrators" group if it does not exist.'

    def handle(self, *args, **options):
        create_admin_group(self)
