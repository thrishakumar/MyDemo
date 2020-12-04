from django.db import models
import datetime

# Create your models here.

# POST Table
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    blog_image = models.ImageField(upload_to='blog_images',null=True,default='placeholder.jpg')
    date_posted = models.DateTimeField(default=datetime.datetime.now())
    author = models.CharField(max_length=40)

# Author

    def __str__(self):
        return self.title
