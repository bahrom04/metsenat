from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = 'Universities'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Degree(models.TextChoices):
    BACHELOR = "BACHELOR", "Bakalavr"
    MAGISTER = "MAGISTER", "Magister"
    

class Students(models.Model):

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

    university = models.ForeignKey(University, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100, choices=Degree.choices)

    contract = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name


class StatusSponsor(models.TextChoices):
    MODERATION = "MODERATION", "Moderatsiya"
    NEW = "NEW", "Yangi"
    APPROVED = "APPROVED", "Tasdiqlangan"
    CANCELED = "CANCELED", "Bekor qilingan"


class TypeSponsor(models.TextChoices):
    JISMONIY = "Jismoniy shaxs"
    YURIDIK = "Yuridik shaxs"


class Sponsors(models.Model):

    class Meta:
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'
        
    full_name = models.CharField(max_length=100)
    phone_number = models.PositiveIntegerField()
    balance = models.PositiveIntegerField()
    sponsored = models.PositiveIntegerField()
    company = models.CharField(max_length=100, null=True)

    sponsor_type = models.CharField(max_length=100, choices=TypeSponsor.choices)

    status = models.CharField(max_length=100, choices=StatusSponsor.choices, default=StatusSponsor.MODERATION)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name