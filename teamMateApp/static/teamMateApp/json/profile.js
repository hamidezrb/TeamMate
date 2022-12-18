
document.addEventListener('DOMContentLoaded', function() {

        document.querySelector('#owner-tab').addEventListener('click', () => teamOwner(event));
        document.querySelector('#member-tab').addEventListener('click', () => teamMember(event));


        document.querySelector('#follow').onclick = (event) => {
                        
            let element = event.target;
            let user_id = element.dataset.userid;
            let follow_status = element.dataset.follow;
            const csrftoken = getCookie('csrftoken');
            fetch(`/follow_user`, {
                        method: 'POST',
                        headers:{
                          'Accept': 'application/json',
                          'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
                          'X-CSRFToken': csrftoken,
                        },
                        body: JSON.stringify({'follow_status':follow_status,'user_id':user_id})
                    }).then(response => response.json())
                    .then(data => {
                        if(data.status === 200)
                        {
                          document.querySelector('#followers').innerHTML = data.followers;
                          document.querySelector('#followings').innerHTML = data.followings;
                          if (follow_status === "1")
                          {
                            document.querySelector('#follow').innerHTML = "UnFollow";
                            document.querySelector('#follow').dataset.follow = 0
                          }
                          else{
                            document.querySelector('#follow').innerHTML = "Follow";
                            document.querySelector('#follow').dataset.follow = 1
                          }

                        }
                        else
                        {
                           alert(data.message);    
                        }
                    })
            };

      });

     function teamOwner(event){
      let element = event.target;
      let url = element.dataset.url;
      document.querySelector('#posts').dataset.url = url;
      document.querySelector('#posts').innerHTML = "";
      counter = 0;
      load();
     } 
     function teamMember(event){
      let element = event.target;
      let url = element.dataset.url;
      document.querySelector('#posts').dataset.url = url ;
      document.querySelector('#posts').innerHTML = "";
      counter = 0;
      load();
     }

