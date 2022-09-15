from django.db import models
from django.conf import settings


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Ambience(BaseModel):
    ENVIRONMENT_CHOICES = (
        ('BOIS', 'Bois'),
        ('TERRE', 'Terre'),

    )
    name = models.CharField(max_length=20, choices=ENVIRONMENT_CHOICES, verbose_name="Ambiance")
    date_start = models.DateField()
    date_end = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="utilisateur")

    def get_year(self):
        pass

    def __str__(self):
        return f'{self.name} {str(self.date_start)[:4]}-{str(self.date_end)[:4]}'
