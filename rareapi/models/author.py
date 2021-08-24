from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import activate  # pylint:disable=imported-auth-user

class Author(models.Model):
    """[summary]
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_image_url = models.ImageField(upload_to="image", height_field=None, width_field=None, max_length=None, null=True)
    created_on = models.DateField()
    active = models.BooleanField( default=True )

