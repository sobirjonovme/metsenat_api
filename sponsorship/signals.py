from django.dispatch import receiver
from django.db.models.signals import post_save, pre_delete

from .models import SponsorStudent


@receiver(post_save, sender=SponsorStudent)
def sponsorstudent(sender, instance, created, **kwargs):
    if created:
        sponsor = instance.sponsor
        sponsor.spent_money += instance.amount
        sponsor.save()

        student = instance.student
        student.received_money += instance.amount
        student.save()

    else:
        sponsor = instance.sponsor
        sponsorships = SponsorStudent.objects.filter(sponsor=sponsor)
        money = 0
        for i in range(len(sponsorships)):
            money += sponsorships[i].amount
        sponsor.spent_money = money
        sponsor.save()

        student = instance.student
        sponsorships = SponsorStudent.objects.filter(student=student)
        money = 0
        for i in range(len(sponsorships)):
            money += sponsorships[i].amount
        student.received_money = money
        student.save()


@receiver(pre_delete, sender=SponsorStudent)
def delete_profile(sender, instance, *args, **kwargs):
    sponsor = instance.sponsor
    sponsor.spent_money -= instance.amount
    sponsor.save()

    student = instance.student
    student.received_money -= instance.amount
    student.save()
