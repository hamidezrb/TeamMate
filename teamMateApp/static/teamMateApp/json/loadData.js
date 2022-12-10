
// Start with first post
let counter = 0;

// Load 8 posts at a time
const quantity = 9;

// When DOM loads, render the first 8 posts
document.addEventListener('DOMContentLoaded', load);

// If scrolled to bottom, load the next 20 posts
window.onscroll = () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight) {
        load();
    }
};

const spinnerBox = document.getElementById('spinner-box')
// Load next set of posts
function load() {
    // Set start and end post numbers, and update counter
    const start = counter;
    const end = start + quantity - 1;
    counter = end;

    fetch(`/posts?start=${start}&end=${end}`)
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
