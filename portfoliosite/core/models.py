from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    project_content = models.TextField(default="")
    published = models.BooleanField()
    thumbnail = models.ImageField()

    def __str__(self):
        return f"{self.title} - {self.pk}"