from django.db import models

# Create your models here.

class Contact(models.Model):
    user=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        return self.user


class Todo(models.Model):
    todo_name=models.CharField(max_length=100)
    is_complete=models.BooleanField(default=False)

    
    
    
    