from django.db.models.deletion import SET_NULL
from rareapi.models.tag import Tag
from django.db import models
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey("Category", null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    image_url = models.ImageField(upload_to="image", height_field=None, width_field=None, max_length=255, null=True)
    content = models.TextField()
    approved = models.BooleanField()
    tags = models.ManyToManyField("Tag", through="PostTag", related_name="tags")
    
    @property
    def is_post_author(self):
        return self.__is_post_author
    @is_post_author.setter
    def is_post_author(self, value):
        self.__is_post_author = value
