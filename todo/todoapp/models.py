from django.db import models

# Create your models here.
class todolist(models.Model):
    task = models.CharField(max_length=60)
    desc = models.TextField()
    date = models.CharField(max_length=20)

    def __str__(self):
        return self.task
    
