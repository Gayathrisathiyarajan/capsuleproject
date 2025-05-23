# from django.core.management.base import BaseCommand
# from .models import *
# from django.core.mail import send_mail
# from django.utils.timezone import now

# class Command(BaseCommand):
#     help = 'Send time capsule emails on unlock date'

#     def handle(self, *args, **kwargs):
#         today = now().date()
#         capsules = TimeCapsule.objects.filter(unlock_date=today)
#         for capsule in capsules:
#             send_mail(
#                 subject='Your Time Capsule is unlocked!',
#                 message=capsule.message,
#                 from_email='411gayathiri@gmail.com',
#                 recipient_list=[capsule.email],  # make sure `email` field exists
#             )
#         self.stdout.write(self.style.SUCCESS('Successfully sent emails'))
