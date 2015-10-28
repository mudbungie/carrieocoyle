from django.db import models

class Universals(models.Model):
    copyright_text = models.CharField(max_length=1024)
    background_image = models.ImageField()

class TextPage(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
