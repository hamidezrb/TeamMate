from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User
from django import forms
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import User
from django.template import loader
from datetime import datetime

class NewTeamForm(forms.Form):
    title = forms.CharField(
        max_length=500,
        required=True,
         widget=forms.TextInput(
            attrs={"placeholder": "Title", "class": "form-control col-12 mt-3"}
        ))
    participantsNO = forms.IntegerField(
        required=True,
         widget=forms.TextInput(
            attrs={"placeholder": "participantsNO", "class": "form-control col-12 mt-3"}
        ))
    startdate = forms.DateTimeField(
        required=True,
         widget=forms.DateTimeInput(
            attrs={'type':'datetime-local',"placeholder": "startdate", "class": "form-control col-12 mt-3"}
        ))
    finishdate = forms.DateTimeField(
        required=True,
         widget=forms.DateTimeInput(
            attrs={'type':'datetime-local',"placeholder": "finishdate", "class": "form-control col-12 mt-3"}
        ))
    content = forms.CharField(
        required=True,
        max_length=1500,
         widget=forms.Textarea(
            attrs={"placeholder": "content", "class": "form-control col-12"}
        ))
    image = forms.ImageField(label= "photo",required=True)
    
    
class NewProfile(forms.Form):
    first_name = forms.CharField(
        max_length=500,
        required=True,
         widget=forms.TextInput(
            attrs={"placeholder": "firstname", "class": "form-control col-12 mt-3"}
        ))
    last_name = forms.CharField(
        max_length=500,
        required=True,
         widget=forms.TextInput(
            attrs={"placeholder": "lastname", "class": "form-control col-12 mt-3"}
        ))
    info = forms.CharField(
        max_length=1500,
         widget=forms.Textarea(
            attrs={"placeholder": "info", "class": "form-control col-12"}
        ))
    image = forms.ImageField(label= "photo",required=True)
    
    
def index(request):
     return render(request, "teamMateApp/Index.html")

def posts(request):
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    team_count = Team.objects.count()
    if start > team_count:
        return HttpResponse()
    
    teams = Team.objects.filter(finishdate__gte = datetime.now()).order_by("-createdate")[start:end]
    list_team = []
    for team in teams:
        viewMore = False
        if  team.participants_set.count() > 3 :
            viewMore = True
            
        participants = team.participants_set.all()[:3]
        list_team.append({ 'participants':participants ,'team_id' : team.id, 'title' : team.title ,'content' :team.content , 'startdate' : team.startdate,
                          'finishdate' : team.finishdate , 'image' :team.image.url , 'createuser_image' : team.user.image.url, 'user_id' : team.user.id,
                          'createdate' : team.createdate.time(), 'participantsNO' : team.participantsNO , 'viewMore' : viewMore})
        
    context = { "teams" : list_team}
    template = loader.get_template('teamMateApp/posts.html') 
    return HttpResponse(template.render(context))
    
    
    
def participants(request,team_id):
    team = Team.objects.filter(id = team_id).first()
    participants = Participants.objects.filter(team = team)
    return render(request, "teamMateApp/participants.html",{
         "participants" : participants ,
         "team_title" : team.title
    })
    
    
@login_required(login_url='/login')
def profile(request,user_id):
    follow_user = User.objects.get(id = user_id)    
    followers = follow_user.followings.count()
    followings = follow_user.followers.count()
    teams_count = follow_user.teams.count()
    user = User.objects.filter(id = request.user.id).first()
    follower = follow_user.followings.filter(user = user).first()
    
    return render(request, "teamMateApp/profile.html",{
        "followers" : followers,
        "followings" : followings,
        "teams_count" : teams_count,
        "user_info":follow_user,
        "isfollowed": follower is not None
    })

def profile_posts(request,id):
    
    follow_user = User.objects.get(id = id)    
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    team_count = follow_user.teams.count()
    if start > team_count:
        return HttpResponse()
    
    teams = follow_user.teams.all().order_by("-createdate")[start:end]
    list_team = []
    for team in teams:
        viewMore = False
        if  team.participants_set.count() > 3 :
            viewMore = True
            
        participants = team.participants_set.all()[:3]
        list_team.append({ 'participants':participants ,'team_id' : team.id, 'title' : team.title ,'content' :team.content , 'startdate' : team.startdate,
                          'finishdate' : team.finishdate , 'image' :team.image.url , 'createuser_image' : team.user.image.url, 'user_id' : team.user.id,
                          'createdate' : team.createdate.time(), 'participantsNO' : team.participantsNO , 'viewMore' : viewMore})
    
    context = { "teams" : list_team}
    template = loader.get_template('teamMateApp/posts.html') 
    return HttpResponse(template.render(context))
      

@login_required(login_url='/login')
def following(request):
    return render(request, "teamMateApp/following.html")


@login_required(login_url='/login')
def following_posts(request):
   
    user = User.objects.get(id = request.user.id)
    follow = Follow.objects.filter(user = user).first()
    if follow is None:
            return render(request, "teamMateApp/following.html", {
               "posts" : [],
          })
   
    followings = follow.following.all()
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    team_count = Team.objects.filter(user__in = followings , finishdate__gte = datetime.now()).count()
    if start > team_count:
        return HttpResponse()
    
    teams=[]
    list_team = Team.objects.filter(user__in = followings , finishdate__gte = datetime.now()).order_by("-createdate")[start:end]
    for team in list_team:
        viewMore = False
        if  team.participants_set.count() > 3 :
            viewMore = True
            
        participants = team.participants_set.all()[:3]
        teams.append({ 'participants':participants ,'team_id' : team.id, 'title' : team.title ,'content' :team.content , 'startdate' : team.startdate,
                          'finishdate' : team.finishdate , 'image' :team.image.url , 'createuser_image' : team.user.image.url,'user_id' : team.user.id,
                          'createdate' : team.createdate.time(), 'participantsNO' : team.participantsNO , 'viewMore' : viewMore})
   
    context = { "teams" : teams}
    template = loader.get_template('teamMateApp/posts.html') 
    return HttpResponse(template.render(context))



@login_required(login_url='/login')
def follow_user(request):
        data = json.load(request)
        follow_status = data['follow_status']
        user_id = data['user_id']
       
        follow_user = User.objects.filter(id = user_id).first()
        if follow_user is None:
            message = "user is not found"
            return JsonResponse({
                 "message" : message,
                 "status": 404
            })
        if  follow_user.id == request.user.id:
            message = "you are not allowed to follow yourself"
            return JsonResponse({
                 "message" : message,
                 "status": 401
            })
            
        user = User.objects.filter(id = request.user.id).first()
        follow1= Follow.objects.filter(user = user).first()
        follow2= Follow.objects.filter(user = follow_user).first()
       
        follow_status = int(follow_status)
        
        if follow_status == 1 :
            if  follow1 is None:
                follow = Follow(user = user)
                follow.save()
                follow.following.add(follow_user)
            
            else:
                follow1.following.add(follow_user)
                
            
            if  follow2 is None:
                follow = Follow(user = follow_user)
                follow.save()
                follow.follower.add(user)
            
            else:
                follow2.follower.add(user)
            
        else:
            follow1.following.remove(follow_user)
            follow2.follower.remove(user)
       
            
        return JsonResponse({
                 "status": 200,
                 "followers": follow_user.followings.count(),
                 "followings":  follow_user.followers.count(),
            })
   
     
   
 
 
@login_required(login_url='/login')
def team_request(request,team_id):
    
    team = Team.objects.filter(id = team_id).first()
    if  team.user.id == request.user.id:
        message = "you are not allowed to request to your own team"
        return JsonResponse({
        "message" : message,
        "status": 401
        })
        
    requested_user = User.objects.filter(id = request.user.id).first()
    if  requested_user.image is None:
          message = f"you have to first edit your profile to be able to request"
          return JsonResponse({
          "message" : message,
          "status": 401
          })
        
    count_team_requests = team.request_set.count()
    if count_team_requests != 0 :
        users_id = team.request_set.values_list('user')
        for elem in users_id :
            if request.user.id == elem[0] :
               message = f"you have already requested to {team.user.username}"
               return JsonResponse({
               "message" : message,
               "status": 401
               })
               
        add_request = Request.objects.filter(team = team).first()
        add_request.user.add(requested_user)
            
    else:
        add_request = Request(team = team)
        add_request.save()   
        add_request.user.add(requested_user)
               
    
    message = f"your request sent successfully to {team.user.username}"
    return JsonResponse({
                "message" : message,
                 "status": 200,
            })
 
  
@login_required(login_url='/login')
def Accept(request,request_id):
    
    user = User.objects.filter(id = request.user.id).first()
    team_request= Request.objects.filter( id = request_id).first()
    
    if  team_request.team.user.id != request.user.id:
        message = "you are not allowed to accept"
        return JsonResponse({
        "message" : message,
        "status": 401
        })
       
    participant = Participants(user = team_request.user , team = team_request.team)
    participant.save()
    
    message = f"request of {team_request.user.username} has been accepted successfully"
    return JsonResponse({
                "message" : message,
                 "status": 200
            })
    
      

@login_required(login_url='/login')    
def dashboard(request):
    user = User.objects.get(pk = request.user.id)
    return render(request, "teamMateApp/dashboard.html",
                  {
                      "teamForm" : NewTeamForm(),
                      "profileForm" : NewProfile(),
                      "user" : user
                   })

@login_required(login_url='/login')
def new_Team(request):
    if request.method == "POST":
        form = NewTeamForm(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(pk = request.user.id)
            if  user.image is None:
                message = f"you have to first edit your profile to be able to add a team"
                return JsonResponse({
                "message" : message,
                "status": 401
                })
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            startdate = form.cleaned_data["startdate"]
            finishdate = form.cleaned_data["finishdate"]
            participantsNO = form.cleaned_data["participantsNO"]
            image = form.cleaned_data["image"]
            
            team = Team(
                user = user,
                title = title,
                content = content,
                startdate = startdate,
                finishdate = finishdate,
                participantsNO = participantsNO,
                image = image
            )
            team.save()
            return JsonResponse({
                "message": "team added successfully.",
                "status": 200})
        else:
            return JsonResponse({
                "message": "all fields are required",
                "status": 401})
            
    else:
            return JsonResponse({
                "message": "check your request",
                "status": 401})
            
            
@login_required(login_url='/login')
def edit_profile(request):
    if request.method == "POST":
        form = NewProfile(request.POST, request.FILES)
        if form.is_valid():
            user = User.objects.get(pk = request.user.id)
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            info = form.cleaned_data["info"]
            image = form.cleaned_data["image"]
            
            user.first_name = first_name
            user.last_name = last_name
            user.info = info
            user.image = image
            user.save()
          
            return JsonResponse({
                "message": "profile updated successfully.",
                "status": 200})
        else:
            return JsonResponse({
                "message": "all fields are required",
                "status": 401})
            
    else:
            return JsonResponse({
                "message": "check your request",
                "status": 401})
          
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "teamMateApp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "teamMateApp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "teamMateApp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "teamMateApp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "teamMateApp/register.html")