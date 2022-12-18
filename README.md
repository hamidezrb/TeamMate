<h1>CS50 WEB PROGRAMMING FINAL PROJECT: TeamMate</h1>

The project video is: -

<h1>Main idea</h1>

<p>TeamMate is a small web-application with the aim of helping people to find their favorite teams and join them to do volunteer things or their hobbies.
this web-application gives people more opportunities to expand their social circle and make new friends and get new experiences. </p>
<p>All users who have accounts after updating their profiles they will be able to send requests to join their ideal teams and then 
the creator of team decides who can join their team.<p>
 
<h1>Distinctiveness and Complexity</h1>

<p>This project helps people find awesome people with similar interests and help them to be more sociable, therefore it is completely different than the other projects in this course, but i try to implement all methods learned through the lectures and problem sets. </p>
<p>In terms of complexity, I used Django with more than one model and several javascript files to the frontend. Moreover, all of the web application is responsive to the different screen sizes (mainly mobile phones and computers).<p>

<h1>How to run the application</h1>

Make and apply migrations by running 
<code>python manage.py makemigrations teamMateApp</code>
<code>python manage.py migrate</code>
and run the server by running 
<code>python manage.py runserver</code>
<p>Go to website address and register an account.</p>


<h4>Setup Django's deafult admin interface (optional)</h4>

In order to access the administrative interface via /admin, it is necessary to creat an administrative user.
To do that, Create superuser with <code>python manage.py createsuperuser</code>.

<h1>Files and directories</h1>

<h4>teamMateApp - main application directory.</h4>
<h4>static/teamMateApp contains all static content (js,css).</h4>

<h4>A css file with all of the css used in the web application</h4>
<h4>js - all JavaScript files used in project.</h4>
<ul>
<li>loadData.js - script that run in teams.html subtemplate which is used in profile.html and index.html and following.html. When these pages load completely only 8 teams will be displayed and when we scroll down the next 8 teams will be displayed.</li>
<li>profile.js - this script run in profile.html. it is used for following or unfollowing the user and showing teams user created or joined.</li>
<li>request.js - script that run in teams.html template. users can click on plus link on teams lists and after confirmation they can sen request to join the team.</li>
<li>dashboard.js - script that run in dashboard.html template. it is used for adding new team and editing profile and showing requests in order to be accepted.</li>
<li>cookie.js - script that run in layout.html which return cookie for csrftoken.</li>
</ul>
<h4>templates/djangoapp contains all application templates.</h4>
<ul>
<li>Login/Logout/Register</li>
<li>layout.html - base templates. All other tempalates extend it.</li>
<li>teams.html - subtemplate that is used in a couple of other templates(index , profile , following). Contains HTML for teams lists.</li>
<li>following.html - templates for teams lists which their creator has been followed by user(only for registered users).</li>
<li>index.html - main templates that shows new Teams before their finish date.</li>
<li>participants.html - template that shows all members of a team. If each team has more than 3 members , viewmore icon appears and when it is clicked this page will be displayed</li>
<li>profile.html - this template shows user details with follow button and teams lists which user created or joined.</li>
<li>dashboard.html - template which has three menus (only for registered users when click on the username located on the navbar they will be redirected to dashboard page):</li>
<ol>
<li> A page to create new Team</li>
<li> A page to edit their profile</li>
<li> A page to accept requests sent to their teams</li>
</ol>
</ul>


<ul>
<li>admin.py - here I added some admin classes.</li>
<li>models.py contains 5 models I used in the project. User model , Team model ,Request model , Participants model , Follow model .</li>
<li>urls.py - all application URLs.</li>
<li>views.py - contains all application views.</li>
<li>team.py - creates a list of teams and return it. it is used in three functions in view.py (teams,profile_teams,following_teams).</li>
<li>media - this directory contains two folders (images and user_images). All users photos will be saved in user_images folder and all teams photo
will be saved in images.</li>
</ul>

<h1>Tech used</h1>
<ul>
<li>Python(django)</li>
<li>Javascript</li>
<li>HTML, CSS</li>
<li>SQLITE</li>
</ul>
