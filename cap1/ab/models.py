from django.db import models

# Create your models here.
class News(models.Model):
    topic = models.TextField()
    summary = models.TextField()
    article = models.TextField()
