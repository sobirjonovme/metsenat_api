from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# SPONSOR TYPE CHOICES
JISMONIY = 'jismoniy'
YURIDIK = 'yuridik'
SPONSOR_TYPE_CHOICES = [
    (JISMONIY, "jismoniy shaxs"),
    (YURIDIK, "yuridik shaxs"),
]

# SPONSOR STATUS CHOICES
NEW = "yangi"
IN_MODERATION = "moderatsiyada"
CONFIRMED = "tasdiqlangan"
CANCELED = "bekor qilingan"

SPONSOR_STATUS_CHOICES = [
    (NEW, "yangi"),
    (IN_MODERATION, "moderatsiyada"),
    (CONFIRMED, "tasdiqlangan"),
    (CANCELED, "bekor qilingan"),
]

# STUDENT TYPE CHOICES
BAKALAVR = 'bakalavr'
MAGISTR = 'magistr'

STUDENT_TYPE_CHOICES = [
    (BAKALAVR, 'bakalavr'),
    (MAGISTR, 'magistr'),
]

# PAYMENT TYPE CHOICES
TRANSFER = "pul o'tkazma"
CASH = 'naqd'

PAYMENT_TYPE_CHOICES = [
    (TRANSFER, "pul o'tkazma"),
    (CASH, 'naqd'),
]


class CustomUser(AbstractUser):
    pass


class Sponsor(models.Model):
    full_name = models.CharField(max_length=150)
    sponsor_type = models.CharField(
        max_length=20,
        choices=SPONSOR_TYPE_CHOICES,
        default=JISMONIY
    )
    phone_number = models.CharField(max_length=20)
    total_money = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    company_name = models.CharField(max_length=150, null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=50,
        choices=SPONSOR_STATUS_CHOICES,
        default=NEW
    )
    spent_money = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_TYPE_CHOICES,
        default=TRANSFER
    )

    def __str__(self):
        return self.full_name


class University(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Student(models.Model):
    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20)
    university = models.ForeignKey(
        University,
        on_delete=models.CASCADE,
        related_name='students'
    )
    student_type = models.CharField(
        max_length=20,
        choices=STUDENT_TYPE_CHOICES,
        default=BAKALAVR
    )
    tuition_fee = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    create_at = models.DateTimeField(auto_now_add=True)
    received_money = models.DecimalField(max_digits=20, decimal_places=2, default=0)

    def __str__(self):
        return self.full_name
