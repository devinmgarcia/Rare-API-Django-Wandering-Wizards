from django.db import models
from django.contrib.auth.models import User  # pylint:disable=imported-auth-user

long = 5000

class Comment(models.Model):

    post = models.ForeignKey("Post", null=True, on_delete=models.SET_NULL, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=long)
    created_on = models.DateField()
    @property
    def isAuthor(self):
        return self.__isAuthor
        
    @isAuthor.setter
    def isAuthor(self, value):
        self.__isAuthor = value
        