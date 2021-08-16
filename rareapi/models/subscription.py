from django.db import models

class Subscription(models.Model):
    """[summary]
    """
    follower = models.ForeignKey('Author', on_delete=models.CASCADE)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    # created_on = models.DateField(default="2021-08-16")
    # ended_on = models.DateField()