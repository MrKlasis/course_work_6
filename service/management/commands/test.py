from django.core.management import BaseCommand

from service.utils import get_test


class Command(BaseCommand):
    def handle(self, *args, **options):
        print(get_test())
