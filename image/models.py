from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=50, null=True)
    article = models.TextField(null=True)
    image = models.ImageField()
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded at {self.uploaded}"

    def get_absolute_url(self):
        return reverse("article_list")
    
    class Meta:
        ordering = ('-uploaded',)
