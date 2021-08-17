from django.db import models
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user

long = 5000

class Comment(models.Model):

    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=long)
    created_on = models.DateField()