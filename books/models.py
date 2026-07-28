from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


# Create your models here.
# django's ORM (object-relational mapping)


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="books", default=1)
    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return f"{self.title} by {self.author} | "
