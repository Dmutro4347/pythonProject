from django.db import models


class News(models.Model):
    titel = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/t/')
