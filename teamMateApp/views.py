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

class NewTeamForm(forms.Form):
    title = forms.CharField(
        max_length=500,
         widget=forms.TextInput(
            attrs={"placeholder": "Title", "class": "form-control col-12"}
        ))
    content = forms.CharField(
        max_length=1500,
         widget=forms.Textarea(
            attrs={"placeholder": "content", "class": "form-control col-12"}
        ))
    participantsNO = forms.IntegerField(
         widget=forms.TextInput(
            attrs={"placeholder": "participantsNO", "class": "form-control col-12"}
        ))
    
def index(request):
     return render(request, "teamMateApp/Index.html")
    # teams = Team.objects.all().order_by("-createdate")
    # participants = Participants.objects.all()
    # list_team = []
    # for team in teams:
    #     participants = team.participants_set.all()
    #     list_team.append({'participants':participants, 'title' : team.title ,'content' :team.content , 'startdate' : team.startdate,
    #                       'finishdate' : team.finishdate , 'image' :team.image.url , 'createuser_image' : team.user.image.url,
    #                       'createdate' : team.createdate.time(), 'participantsNO' : team.participantsNO})
    # return render(request, "teamMateApp/Index.html",{
    #      "teams" : list_team 
    # })
    

def posts(request):
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))
    team_count = Team.objects.count()
    if start > team_count:
        return HttpResponse()
    
    teams = list(Team.objects.all().order_by("-createdate"))[start:end]
    participants = Participants.objects.all()
    
    list_team = []
    for team in teams:
        participants = team.participants_set.all()
        list_team.append({'participants':participants, 'title' : team.title ,'content' :team.content , 'startdate' : team.startdate,
                          'finishdate' : team.finishdate , 'image' :team.image.url , 'createuser_image' : team.user.image.url,
                          'createdate' : team.createdate.time(), 'participantsNO' : team.participantsNO})
        
    context = { "teams" : list_team}
    template = loader.get_template('teamMateApp/posts.html') 
    return HttpResponse(template.render(context))
    
@login_required(login_url='/login')    
def dashboard(request):
    return render(request, "teamMateApp/dashboard.html")

@login_required(login_url='/login')
def new_Team(request):
    if request.method == "POST":
        form = NewTeamForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            startdate = form.cleaned_data["startdate"]
            finishdate = form.cleaned_data["finishdate"]
            participantsNO = form.cleaned_data["participantsNO"]
            image = form.cleaned_data["image"]
            # Save a record
            user = User.objects.get(pk = request.user.id)
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
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "teamMateApp/index.html", {
                "form": form
            })
    else:
          return render(request, "teamMateApp/index.html", {
              "form" : NewTeamForm()
          })
          
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