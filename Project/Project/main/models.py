import datetime

from django.db import models
#from .models import Post

# Create your models here.
class Task(models.Model):
    task_number = models.IntegerField(null=True)
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Description', max_length=1000)
    create_date = models.DateTimeField(default=datetime.date.today())
    deadtime = models.CharField('DeadTime', max_length=50, null=True)


    def __str__(self):
        return self.title



