from django.db import models

# Create your models here.


class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class notesdata(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    myfile=models.FileField(upload_to='User_Notes')
    desc=models.TextField()


class feedback(models.Model):
    fullname=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    msg=models.TextField()