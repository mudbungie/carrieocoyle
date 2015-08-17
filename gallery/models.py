from django.db import models

class Piece(models.Model):
    title = models.CharField(max_length=255)
    # slug is a short0hand for the name, used in URLs and such
    # it will be set to default to the title with underscore
    # replacement in the admin console
    slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

