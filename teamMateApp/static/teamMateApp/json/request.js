
      document.addEventListener('click', event => {
        const element = event.target;
        if (element.className === 'team_request') {

            Swal.fire({
                title: 'are you sure you want to send request to join this team ?',
                icon: 'warning',
                confirmButtonText: 'Yes',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
              }).then((result) => {

                if (result.isConfirmed) {
                    let team_id = element.parentElement.dataset.teamid;
                    const csrftoken = getCookie('csrftoken');
        
                    fetch(`/team_request/${team_id}`, {
                        method: 'POST',
                        headers:{
                            'Accept': 'application/json',
                            'X-Requested-With': 'XMLHttpRequest', 
                            'X-CSRFToken': csrftoken,
                          }
                    }).then(response => response.json())
                    .then(data => {
                        
                        if(data.status === 200)
                        {
                            Swal.fire({
                                icon: 'success',
                                title: 'success',
                                text: data.message
                              })   
                        }
                        else
                        {
                           Swal.fire({
                            icon: 'error',
                            title: 'Oops...',
                            text: data.message
                          })   
                        }
                        
                    })
                }
              })

        }
    });

     