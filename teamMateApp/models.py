from django.contrib.auth.models import AbstractUser
from django.db import models
from teamMate import settings

# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to="user_images/")
    Info = models.CharField(null = True,max_length=2000)


class Team(models.Model):
    title = models.CharField(null = False,max_length=500)
    content = models.CharField(null = False,max_length=1500)
    image = models.ImageField(upload_to="images/")
    startdate = models.DateTimeField(auto_now_add = False)
    finishdate = models.DateTimeField(auto_now_add = False)
    participantsNO = models.IntegerField(null = False)
    createdate = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "teams")
    
    class Meta:
        ordering = ["createdate"]
        
    def __str__(self):
        return f"title : {self.title} "
    
    
class Participants(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    team = models.ManyToManyField(Team,blank=True)
    
    def __str__(self):
        return f"user : {self.user.username} , team : {self.team.count()}"
    
class Follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    follower = models.ManyToManyField(User,blank=True,related_name = "followers")
    following= models.ManyToManyField(User,blank=True,related_name = "followings")
    
    
    def __str__(self):
        return f"user : {self.user.username}"
    
    
class Request(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    user = models.ManyToManyField(User)

    def __str__(self):
        return f"team : {self.team.title}"