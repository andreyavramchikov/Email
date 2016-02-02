# -*- coding: utf-8 -*-
import time
from random import randint

from django.conf import settings
from django.core.mail.message import EmailMessage
from django.core.management.base import BaseCommand
from sendmail.emails_not_for_common_sending import EMAILS_NOT_FOR_COMMON_SENDING

from sendmail.messages import COMMON_MESSAGE_1, COMMON_MESSAGE_2
from tripadvisor.models import Restaurant


SUBJECTS = ('Seasonal recruiting: Fast & Easy.',
            'Cooperation Opportunity. Filling job openings.',
            'Hiring great summer employees.')

TIME_TO_SLEEP = 180


#python manage.py send_mail
class Command(BaseCommand):
    def handle(self, *args, **options):
        restaurants = Restaurant.objects.filter(sent=False, email__contains='@')[0:3000]
        print 'count of not sent emails are {0}'.format(restaurants.count())
        random_count = len(SUBJECTS) - 1
        for restaurant in restaurants:
            email = restaurant.email
            if email not in EMAILS_NOT_FOR_COMMON_SENDING:
                rand = randint(0, random_count)
                subject = SUBJECTS[randint(0, random_count)]
                message = COMMON_MESSAGE_1 if rand < random_count else COMMON_MESSAGE_2
                mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email,])
                mail.send()
                restaurant.sent = True
                restaurant.save()
                print 'email has been sent to {0}'.format(email)
                time.sleep(TIME_TO_SLEEP)
