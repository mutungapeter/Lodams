from MRS.settings import SITE_EMAIL
from celery import shared_task
from time import sleep
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from MRS.celery import app

@app.task(name="send_staff_email_notification_task")
def send_staff_email_notification_task(email, name):
    try:
        from_email = settings.SITE_EMAIL
        subject = "Account Created"
        message = f"Hello {name}, your account has been created successfully  , Your Employee Number is emp/ld/2022"
        mail = EmailMessage(
            subject,
            message,
            from_email,
            [email]
        )
        mail.content_subtype = "html"
        mail.send(fail_silently=False)
    except Exception as e:
        raise e

@app.task(name="send_student_email_notification_task")
def send_student_email_notification_task(email, name):
    try:
        from_email = settings.SITE_EMAIL
        subject = "Account Created"
        message = f"Hello {name}, your account has been created successfully  , Your Login password is @Lodamscollegestudent2022"
        mail = EmailMessage(
            subject,
            message,
            from_email,
            [email]
        )
        mail.content_subtype = "html"
        mail.send(fail_silently=False)
    except Exception as e:
        raise e     