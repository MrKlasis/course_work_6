import logging

from django.core.management import BaseCommand

from service.jobs import job_rady_check

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        job_rady_check()
