from django.db import models

# Create your models here.

'''
django model field:
- html widget
- validation
- db size
'''


class Job(models.Model):   # table
    title = models.CharField(max_length=10)  # column
