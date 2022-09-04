from django.db import models
from django.conf import settings


class Ambience(models.Model):
    ENVIRONMENT_CHOICES = (
        ('BOIS', 'Bois'),
        ('TERRE', 'Terre'),

    )
    name = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES, verbose_name="Ambiance")
    date_start = models.CharField(max_length=5)
    date_end = models.CharField(max_length=5)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="utilisateur")

    def __str__(self):
        return f'{self.name} {self.date_start}-{self.date_end}'




