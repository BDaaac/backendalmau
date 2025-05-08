from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title       = models.CharField(max_length=200)
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post        = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    text        = models.TextField()
    created_at  = models.DateTimeField(auto_now_add=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author}'
