
// Start with first team
let counter = 0;

// Load 8 teams at a time
const quantity = 9;

// When DOM loads, render the first 8 teams
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 8 teams
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

const spinnerBox = document.getElementById('spinner-box')
// Load next set of teams
function load() {
    // Set start and end team numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end;
    url = document.querySelector('#posts').dataset.url
    fetch(`${url}?start=${start}&end=${end}`)
    .then(response => response.text())
    .then(data => {
        if(data){
            spinnerBox.classList.remove('invisible')
            setTimeout(()=>{
    
                spinnerBox.classList.add('invisible')
                const post = document.createElement('div');
                post.className = 'container card-group';
                post.innerHTML = data;
                document.querySelector('#posts').append(post)
                
            },500)
        }
    })
};
