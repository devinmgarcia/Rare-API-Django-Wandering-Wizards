from django.db import models

class DemotionQueue(models.Model):
    """[summary]
    """
    action = models.CharField(max_length=50)
    admin = models.ForeignKey('Author', on_delete=models.CASCADE)
    approver_one = models.ForeignKey('Author', on_delete=models.CASCADE)