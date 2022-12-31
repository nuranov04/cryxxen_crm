from django.core.management import BaseCommand

from apps.main.roles.models import Role


class Command(BaseCommand):
    help = "Create all roles objects"

    def handle(self, *args, **options):
        Role.objects.all().delete()
        roles_objects = [Role(id=i) for i in range(1, 6)]
        Role.objects.bulk_create(roles_objects)
