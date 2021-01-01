from django.db import models

# Create your models here.

class ProjectModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=50)
    image = models.FilePathField(path='/img')
    githubLink = models.URLField(max_length=200, blank=True)
    demonstrationLink = models.URLField(max_length=200, blank=True)