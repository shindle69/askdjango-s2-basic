from django.db import models
from askcompany.utils import uuid_upload_to


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    gwaesa = models.TextField()    
    danwal = models.TextField()
    sangwal = models.TextField()    
    mununwal = models.TextField()  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()

