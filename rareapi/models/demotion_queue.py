from django.db import models

class DemotionQueue(models.Model):
    """[summary]
    """
    action = models.CharField(max_length=50)
    admin = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='admin_approvals')
    approver_one = models.ForeignKey('Author', on_delete=models.CASCADE)

    # ? RELOAD DATA