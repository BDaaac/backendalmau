from django.db import models

from django.db import models

# Create your models here.
class Thread(models.Model):
    name = models.CharField("Название",max_length=20)
    description = models.TextField("Описание")

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField("Название",max_length=20)
    picture = models.FileField(upload_to='uploads/')
    description = models.TextField("Описание")
    author = models.CharField("Автор",max_length=20)
    thread = models.ForeignKey(Thread, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.title