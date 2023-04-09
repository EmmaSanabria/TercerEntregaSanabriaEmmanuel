from django.db import models

# Create your models here.
class User(models.Model):
    user = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    
    def __str__(self):
        return self.user
        
    
class Post(models.Model):
    user_posting = models.CharField(max_length=12)
    post = models.CharField(max_length=92)
    
    def __str__(self):
        return f'{self.user_posting} -- {self.post}'
       
    
class Groups(models.Model):
    name_group = models.CharField(max_length=40)
    description = models.CharField(max_length=92)

    def __str__(self):
        return f'{self.name_group} -- {self.description}'