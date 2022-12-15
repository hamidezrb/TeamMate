 document.addEventListener('DOMContentLoaded', function() {
   document.querySelector('.add-team').addEventListener('click', () => addTeam());
   document.querySelector('.edit_profile').addEventListener('click', () => editProfile());
   document.querySelector('.team_requests').addEventListener('click', () => teamRequests());
   // document.querySelector('.accept_member').addEventListener('click', () => acceptmember(event));

  //  document.querySelector('#FormNewTeam').onsubmit = submit_team;
  // document.querySelector('#team-form').addEventListener('submit',submit_team);

  // add team
  formTeam.onsubmit =  (event) => {
    event.preventDefault();
    const csrftoken = getCookie('csrftoken');
    fetch('/new_Team', {
      method: 'POST',
      headers:{
       'Accept': 'application/json',
       'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
       'X-CSRFToken': csrftoken,
     },
      body: new FormData(formTeam)
      })
      .then(response => response.json())
      .then(result => {
  
          if(result.status == 200){
             div = document.createElement("div");
             div.setAttribute("class", "alert alert-success");
             div.innerHTML = result.message;
             document.querySelector("#add-team").prepend(div);
          }
          else{
             div = document.createElement("div");
             div.setAttribute("class", "alert alert-danger");
             div.innerHTML = result.message;
             document.querySelector("#add-team").prepend(div);
          }
  
      })
      .catch((error) => 
          alert(error)
      );
      return false;
  }



  // update profile
  formProfile.onsubmit = (event) => {
    event.preventDefault();
    const csrftoken = getCookie('csrftoken');
    fetch('/edit_profile', {
      method: 'POST',
      headers:{
       'Accept': 'application/json',
       'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
       'X-CSRFToken': csrftoken,
     },
      body: new FormData(formProfile)
      })
      .then(response => response.json())
      .then(result => {
  
          if(result.status == 200){
             div = document.createElement("div");
             div.setAttribute("class", "alert alert-success");
             div.innerHTML = result.message;
             document.querySelector("#edit_profile").prepend(div);
          }
          else{
             div = document.createElement("div");
             div.setAttribute("class", "alert alert-danger");
             div.innerHTML = result.message;
             document.querySelector("#edit_profile").prepend(div);
          }
  
      })
      .catch((error) => 
          alert(error)
      );
      return false;
  }




 });

 
 function addTeam(){
   document.querySelector('#add-team').classList.remove( "invisible") 
   document.querySelector('#edit_profile').classList.add( "invisible") 
   document.querySelector('#team_requests').classList.add( "invisible") 
}

function editProfile(){
   document.querySelector('#add-team').classList.add( "invisible") 
   document.querySelector('#edit_profile').classList.remove( "invisible") 
   document.querySelector('#team_requests').classList.add( "invisible") 
}

function teamRequests(){
   document.querySelector('#add-team').classList.add( "invisible") 
   document.querySelector('#edit_profile').classList.add( "invisible") 
   document.querySelector('#team_requests').classList.remove( "invisible") 
}



 
document.addEventListener('DOMContentLoaded', function() {
   document.querySelectorAll('.accept_member').forEach(button => {
           button.onclick = function(event) {
                
            acceptmember(event);
              
           };
       });


     });

 
 
 
function acceptmember(event){
   event.preventDefault();
   let element = event.target;
   let user_id = element.dataset.userid;
   let request_id = element.dataset.requestid;

   const csrftoken = getCookie('csrftoken');
   fetch('/accept_member', {
     method: 'POST',
     headers:{
      'Accept': 'application/json',
      'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
      'X-CSRFToken': csrftoken,
    },
     body: JSON.stringify({'request_id':request_id})
     })
     .then(response => response.json())
     .then(result => {
 
         if(result.status == 200){
            div = document.createElement("div");
            div.setAttribute("class", "alert alert-success");
            div.innerHTML = result.message;
            document.querySelector("#team_requests").prepend(div);
            element.parentElement.remove()
         }
         else{
            div = document.createElement("div");
            div.setAttribute("class", "alert alert-danger");
            div.innerHTML = result.message;
            document.querySelector("#team_requests").prepend(div);
         }
 
     })
     .catch((error) => 
         alert(error)
     );
     return false;
 }
