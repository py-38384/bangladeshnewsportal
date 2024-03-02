from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from django.utils import timesince

class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,blank=True,null=True)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=150)
    content = HTMLField(null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/',null=True,blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0,null=True,blank=True)
    yt_video_id = models.CharField(max_length=150,null=True,blank=True)
    brief = models.CharField(max_length=300)
    Highlighted = models.BooleanField(help_text='Note that. only latest 5 content will show. and need atleast 5 content.',default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    
    @property
    def timesince(self):
        return timesince.timesince(self.time)