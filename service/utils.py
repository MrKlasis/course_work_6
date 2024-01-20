from datetime import datetime

from django.utils.timezone import localtime


def start():
    result = datetime.now()
    return result
