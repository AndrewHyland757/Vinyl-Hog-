from django.db import models
from django.contrib.auth.models import User
from products.models import Album, Artist

# Create your models here.


class Author(models.Model):
    """
    An Author profile model from the Allauth User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.author_name




class RecommendationPost(models.Model):
    """
    Stores a single recommendation post entry.
    """
    title = models.CharField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=200, unique=True)
    
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE)
    product = models.ForeignKey(Album, null=False, blank=False, on_delete=models.CASCADE)
    
    article_image = models.ImageField(
        null=True, blank=True)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | written by {self.author}"