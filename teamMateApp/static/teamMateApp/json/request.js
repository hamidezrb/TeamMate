
      document.addEventListener('click', event => {
        const element = event.target;
        if (element.className === 'team_request') {

            var result = confirm("are you sure you want to send request to join this team ? ");
            if (result == true) {
                let team_id = element.parentElement.dataset.teamid;
                const csrftoken = getCookie('csrftoken');
    
                fetch(`/team_request/${team_id}`, {
                    method: 'POST',
                    headers:{
                        'Accept': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
                        'X-CSRFToken': csrftoken,
                      }
                }).then(response => response.json())
                .then(data => {
                    
                    if(data.status === 200)
                    {
                        alert(data.message);    
                    }
                    else
                    {
                       alert(data.message);    
                    }
                    
                })
            } 
        }
    });

     