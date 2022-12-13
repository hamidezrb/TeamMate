document.addEventListener('click', event => {
    const element = event.target;
    if (element.className === 'add-team') {

       addTeam()
    }
    else if(element.className === 'edit_profile'){
        editProfile()
    }
    else if(element.className === 'team_requests'){
        teamRequests()
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