from django.db import models



class Reaction(models.Model):
    """[summary]
    """
    label = models.CharField(max_length=50)
    image_url = models.ImageField(upload_to="image", height_field=None, width_field=None, max_length=None, null=True
)