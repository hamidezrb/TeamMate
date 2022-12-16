CS50 WEB PROGRAMMING FINAL PROJECT: TeamMate
The project video is: https://youtu.be/YtHHEC-bdqA

Main idea
TeamMate is a small web-application with the aim of helping people to find their favourite teams and join them to do volunteer things or their hobbies.
this web-application gives people an opportunity to create their own communities and expand their friends and gain new experiences. 

all users who have accounts after updating their profiles and filling some info they will be able to send requests to join their ideal teams and then 
the creator of team decides who can join by accepting their requests.
 
Distinctiveness and Complexity
The page is not similar to anything we have already created. It's not a social media app nor an e-commerce. It's not similar to other years projects either.

In terms of complexity, I used Django with more than one model (explained below) and several javascript files to the frontend. Moreover, all of the web application is responsive to the different screen sizes (mainly mobile phones and computers).

How to run the application:

Make and apply migrations by running python manage.py makemigrations and python manage.py migrate.
Create superuser with python manage.py createsuperuser. This step is optional.
Go to website address and register an account.


Files and directories:

teamMateApp - main application directory.
static/teamMateApp contains all static content (js,css).

A css file with all of the css used in the web application
js - all JavaScript files used in project.
loadData.js - script that run in teams.html template which is used in profile and index and following page. When page loads completely only 8 teams shown when we 
scroll the next 8 posts shown with this script .
profile.js - this script run in profile.html. it is used for following or unfollowing the user.
request.js - script that run in teams.html template. users can click on plus link on team posts and after confirmation they can sen request to join the team.
dashboard.js - script that run in dashboard.html template.
cookie.js - script that run in layout.html which return cookie for csrftoken.

templates/djangoapp contains all application templates.
Login/Logout/Register
layout.html - base templates. All other tempalates extend it.
teams.html - subtemplate that is used in a couple of other templates(index , profile , following). Contains HTML for teams lists.
following.html - templates for teams lists which their creator has been followed by user.
index.html - main templates that shows new Teams before their finishdate(only for registered users).
participants.html - template that shows all members of a team. for each team if it has more than 3 members , viewmore icon appear and when it is clicked this page will be displayed
profile.html - this template shows user details with  follow button and teams lists created by them or they join it.
dashboard.html - template for creating new teams , editing profile , accepting users' requests for their teams.
dashboard.html - template which has three menus (when click on the username located on the navbar you will be redirected to dashboard page):
1: A page to create new Team
2: A page to edit their own profile
3: A page to accept users' requests for their teams


admin.py - here I added some admin classes and re-registered User model.
models.py contains 5 models I used in the project. User model , Team model ,Request model , Participants model , Follow model .
urls.py - all application URLs.
views.py respectively, contains all application views.
team.py - create a list of teams and return it. it is used in three functions in view.py (teams,profile_teams,following_teams).
media - this directory contains two folders (images and user_images). All users photos will be saved in user_images folder and all teams photo
will be saved in images.


Tech used:
Python(django)
Javascript
HTML, CSS
SQLITE.
