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
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.ImageField(upload_to="image", height_field=None, width_field=None, max_length=None, null=True)
    content = models.CharField(max_length=5000)
    approved = models.BooleanField()
    tags = models.ManyToManyField("Tag", through="PostTag", related_name="tags")
    # comments = models.ForeignKey("Comment", on_delete=models.CASCADE)
    
    @property
    def is_post_author(self):
        return self.__is_post_author
    @is_post_author.setter
    def is_post_author(self, value):
        self.__is_post_author = value