from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title
    
    def snippet(self):
        if (len(self.title) > 50):
            return self.title[0:50] + '...'
        else:
            return self.title
    