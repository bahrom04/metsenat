from django.db import models
from accounts.models import Students, Sponsors

# Create your models here.

class Sponsorship(models.Model):
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    sponsor = models.ForeignKey(Sponsors, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.student.full_name} - {self.sponsor.full_name} tominidan {self.amount} so'm sponsorlik qilindi"