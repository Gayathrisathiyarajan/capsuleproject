from django.core.management.base import BaseCommand
from capsuleapp.models import TimeCapsule
from django.utils.timezone import now
from django.core.mail import send_mail

class Command(BaseCommand):
    help = 'Send emails for capsules scheduled to unlock today'

    def handle(self, *args, **kwargs):
        today = now().date()
        unsent_capsules = TimeCapsule.objects.filter(unlock_date=today, email_sent=False)
        for cap in unsent_capsules:
            send_mail(
                subject=f"Your Time Capsule: {cap.title}",
                message=cap.message,
                from_email='yourcapsulemessage@gmail.com',
                recipient_list=[cap.email],
                fail_silently=False
            )
            cap.email_sent = True
            cap.save()
        self.stdout.write("Emails sent successfully.")
