from django.db import models

# Create your models here.

class Articles(models.Model):
  title = models.CharField(max_length=500)
  description = models.TextField()
  content = models.TextField()
