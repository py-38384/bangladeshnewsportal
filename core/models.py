from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from tinymce.models import HTMLField
from django.utils import timesince
from django.db.models.signals import post_save
from django.dispatch import receiver

class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        if not self.full_name:
            self.full_name = self.user.username
        return self.full_name
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)

class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)
    highlighted = models.BooleanField(help_text='Note that. only latest 5 content will show.',default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-id']

class Content(models.Model):
    title = models.CharField(max_length=150)
    content = HTMLField(null=True,blank=True)
    thumbnail = models.ImageField(upload_to='thumbnail/',null=True,blank=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    time = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title',unique=True,null=True,default=None)
    views = models.IntegerField(default=0,null=True,blank=True)
    yt_video_id = models.CharField(max_length=150,null=True,blank=True)
    brief = models.CharField(max_length=300)
    highlighted = models.BooleanField(help_text='Note that. only latest 5 content will show. and need atleast 5 content.',default=False)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
    
    @property
    def timesince(self):
        return timesince.timesince(self.time)