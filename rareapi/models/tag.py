from django.db import models

class Tag(models.Model):
    """[summary]
    """
    
    label = models.CharField(max_length=50)
