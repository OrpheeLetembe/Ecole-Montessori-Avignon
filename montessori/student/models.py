from django.db import models

from PIL import Image

from ambience.models import Ambience


class Students(models.Model):

    photo = models.ImageField(null=True, blank=True, upload_to='photos')
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    profil = models.TextField()
    ambience = models.ForeignKey(Ambience, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    IMAGE_MAX_SIZE = (100, 100)

    def resize_image(self):
        image = Image.open(self.photo)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.photo.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'



