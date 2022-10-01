from django.db import models

from users.models import Sponsor, Student


# Create your models here.
class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(
        Sponsor,
        on_delete=models.CASCADE,
        related_name='sponsorships_given'
    )
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='sponsorships_recieved'
    )
    amount = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.amount} is given to {self.student} by {self.sponsor}"
