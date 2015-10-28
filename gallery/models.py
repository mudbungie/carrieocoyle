from django.db import models
from django.utils.text import slugify

class Medium(models.Model):
    medium_name = models.CharField(max_length=255)

class Piece(models.Model):
    title = models.CharField(max_length=255)
    # jargon for short title; derived from title
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='/static/signature.jpg')    
#    medium = models.ForeignKey(Medium)
    
    def save(self, *args, **kwargs):
        # add identifying slug field on save
        self.slug = slugify(self.title)
        super(Piece, self).save(*args, **kwargs)
