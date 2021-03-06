from django.db import models

class student(models.Model):
    
    rollNo=models.TextField()
    firstName=models.TextField()
    lastName=models.TextField()
    email=models.EmailField
    class Meta:
        db_table="tstudent"

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    class Meta:
        db_table="tpost"

