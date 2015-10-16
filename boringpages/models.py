from django.db import models

class Universals(models.Model):
    copyright_text = models.CharField(max_length=1024)
    background_image = models.ImageField()
