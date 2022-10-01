from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete

from .models import SponsorStudent


@receiver(post_save, sender=SponsorStudent)
def sponsorstudent_create(sender, instance, created, **kwargs):
    if created:
        sponsor = instance.sponsor
        sponsor.spent_money += instance.amount
        sponsor.save()

        student = instance.student
        student.received_money += instance.amount
        student.save()


@receiver(pre_save, sender=SponsorStudent)
def sponsorstudent_update(sender, instance, **kwargs):
    if instance.id is not None:
        previous = SponsorStudent.objects.get(id=instance.id)
        curr_sponsor = instance.sponsor
        curr_student = instance.student

        if previous.sponsor == curr_sponsor:
            curr_sponsor.spent_money += instance.amount - previous.amount
        else:
            previous.sponsor.spent_money -= previous.amount
            curr_sponsor.spent_money += instance.amount
            previous.sponsor.save()

        if previous.student == curr_student:
            curr_student.received_money += instance.amount - previous.amount
        else:
            previous.student.received_money -= previous.amount
            curr_student.received_money += instance.amount
            previous.student.save()

        curr_sponsor.save()
        curr_student.save()


@receiver(pre_delete, sender=SponsorStudent)
def delete_profile(sender, instance, *args, **kwargs):
    sponsor = instance.sponsor
    sponsor.spent_money -= instance.amount
    sponsor.save()

    student = instance.student
    student.received_money -= instance.amount
    student.save()
