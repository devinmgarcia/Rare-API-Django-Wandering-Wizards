from django.db import models

class Category(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    
    label = models.CharField(max_length=50)
