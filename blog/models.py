
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Post(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    user_name = models.CharField(max_length=100)
    email = models.EmailField()
    
class PostTags(models.Model):
    name = models.CharField(max_length=100)