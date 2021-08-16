from django.db import models

class PostTag(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)