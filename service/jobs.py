import smtplib
from datetime import datetime, timedelta

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone


from service.const import CREATED, READY, COMPLETED, LAUNCHED, NO_ACTIVE
from service.models import Mailing, Log


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job_rady_check, 'interval', minutes=1)
    scheduler.start()
    return True


def job_rady_check():
    mailing = Mailing.objects.all()
    print('началась проверка')
    now = datetime.now()
    now = timezone.make_aware(now, timezone.get_current_timezone())
    print(now)
    for mail in mailing:
        if not mail.is_active:
            mail.status = NO_ACTIVE
        else:
            mail.status = CREATED
            if not mail.stop > datetime.now():
                mail.status = COMPLETED
            else:
                mailing_clients = mail.clients.all()
                if mail.massage not in [None, ''] and mailing_clients.exists():

                    if not mail.start < datetime.now():
                        mail.status = READY
                    else:
                        mail.status = LAUNCHED
                        mail.start = datetime.now() + timedelta(minutes=mail.periodic)
                        log = Log()
                        for client in mailing_clients:
                            try:
                                send_mail(
                                    subject=mail.massage.title,
                                    message=mail.massage.text,
                                    from_email=settings.EMAIL_HOST_USER,
                                    recipient_list=[client.email]
                                )
                            except smtplib.SMTPAuthenticationError:
                                print('Ошибка smtplib.SMTPAuthenticationError:')
                                log.mail_server_response = 'Ошибка smtplib.SMTPAuthenticationError:'

                            log.name = mail.name
                            log.time_attempt = datetime.now()
                            if log.mail_server_response:
                                log.status = 'Не отправлено'
                            else:
                                log.status = 'Отправлено'
                                log.mail_server_response = ''
                            log.mode = 'Автоматический'
                        log.save()
        mail.save()

