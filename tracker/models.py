from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Medicine(models.Model):
    class Dosagechoice(models.TextChoices):
        MG = 'MG', _('mg')
        ML = 'ML', _('ml')

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    medicine_name = models.CharField(max_length=100)
    dosage = models.PositiveIntegerField()
    dosage_unit = models.CharField(max_length=2, choices=Dosagechoice, default=Dosagechoice.MG)
    frequency = models.PositiveIntegerField()
    start_date = models.DateField(verbose_name=None, name=None, auto_now=None, auto_now_add=None, auto_created=None)
    end_date = models.DateField(verbose_name=None, name=None, auto_now=None, auto_now_add=None, auto_created=None)
    time = models.TimeField(verbose_name=None, name=None, auto_now=None, auto_now_add=None, auto_created=None)

    def __str__(self):
        return self.medicine_name
