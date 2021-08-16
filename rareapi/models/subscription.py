from django.db import models

class Subscription(models.Model):
    """[summary]
    """
    follower = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='followers')
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    created_on = models.DateField()
    ended_on = models.DateField()