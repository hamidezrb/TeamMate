## CS50 WEB PROGRAMMING FINAL PROJECT: TeamMate ##



### [TeamMate](https://youtu.be/mOPNEz_3I-E)

![TeamMate Application](https://repository-images.githubusercontent.com/576754788/9cfbc41f-b881-4793-9e1b-ae7a03f3c9db)

## Main idea ##

TeamMate is a small web-application with the aim of helping people to find their favorite teams and join them to do volunteer things or their hobbies.
this web-application gives people more opportunities to expand their social circle and make new friends and get new experiences.

All users who have accounts after updating their profiles they will be able to send requests to join their ideal teams and then 
the creator of team decides who can join their team.
 
## Distinctiveness and Complexity ##

This project helps people find awesome people with similar interests and help them to be more sociable, therefore it is completely different than the other projects in this course, but i try to implement all methods learned through the lectures and problem sets.

In terms of complexity, I used Django with more than one model and several javascript files to the frontend. Moreover, all of the web application is responsive to the different screen sizes (mainly mobile phones and computers).

## How to run the application ##

Make and apply migrations by running 
```python manage.py makemigrations teamMateApp```
```python manage.py migrate```
and run the server by running 
```python manage.py runserver```

Go to website address and register an account.


#### Setup Django's deafult admin interface (optional) ####

In order to access the administrative interface via /admin, it is necessary to creat an administrative user.
To do that, Create superuser with ```python manage.py createsuperuser```.

## Files and directories ##

#### application teamMateApp ####
#### static/teamMateApp contains all static content (js,css). ####

#### A css file with all of the css used in the web application ####
#### js - all JavaScript files used in project. ####
 
* loadData.js - script that run in teams.html subtemplate which is used in profile.html and index.html and following.html. When these pages load completely only 8 teams will be displayed and when we scroll down the next 8 teams will be displayed.
* profile.js - this script run in profile.html. it is used for following or unfollowing the user and showing teams user created or joined.
* request.js - script that run in teams.html template. users can click on plus link on teams lists and after confirmation they can send request to join the team.
* dashboard.js - script that run in dashboard.html template. it is used for adding new team and editing profile and showing requests in order to be accepted.
* cookie.js - script that run in layout.html which returns cookie for csrftoken.
 
#### templates/teamMateApp contains all application templates. ####
 
* Login/Logout/Register 
* layout.html - base templates. All other tempalates extend it. 
* teams.html - subtemplate that is used in a couple of other templates(index , profile , following). Contains HTML for teams lists. 
* following.html - templates for teams lists which their creator has been followed by user(only for registered users). 
* index.html - main templates that shows new Teams before their finish date. 
* participants.html - template that shows all members of a team. If each team has more than 3 members , viewmore icon appears and when it is clicked this page will be displayed 
* profile.html - this template shows user details with follow button and teams lists which user created or joined. 
* dashboard.html - template which has three menus (only for registered users when click on the username located on the navbar they will be redirected to dashboard page): 

1. A page to create new Team
2. A page to edit their profile
3. A page to accept requests sent to their teams

 


 
* admin.py - here I added some admin classes. 
* models.py contains 5 models I used in the project. User model , Team model ,Request model , Participants model , Follow model . 
* urls.py - all application URLs. 
* views.py - contains all application views. 
* team.py - creates a list of teams and return it. it is used in three functions in view.py (teams,profile_teams,following_teams). 
* media - this directory contains two folders (images and user_images). All users photos will be saved in user_images folder and all teams photo
will be saved in images. 
 

## Tech used ##
 
* Python(django) 
* Javascript 
* HTML, CSS 
* SQLITE 
 
