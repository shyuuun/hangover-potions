from django.db import models


class Comment(models.Model):
    user = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user

