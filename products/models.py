from django.db import models
import uuid


# Create your models here.

class Album(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title
