from django.db import models

class PostCategory(models.Model):
    """[summary]

    Args:
        models ([type]): [description]
    """
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)