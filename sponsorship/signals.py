from django.dispatch import receiver
from django.db.models.signals import post_save

from .models import SponsorStudent


@receiver(post_save, sender=SponsorStudent)
def sponsorstudent(sender, instance, created, **kwargs):
    if created:
        print("\n\n Create signal\n\n")
        sponsor = instance.sponsor
        sponsor.spent_money += instance.amount
        sponsor.save()

        student = instance.student
        student.received_money += instance.amount
        student.save()
