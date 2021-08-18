from django.db import models

class Tag(models.Model):
    """[summary]
    """
    
    label = models.CharField(max_length=50)

    @property
    def isAuthor(self):
        return self.__isAuthor
        
    @isAuthor.setter
    def isAuthor(self, value):
        self.__isAuthor = value