window.onload = function() { 
    draw();
      
    const canvas = document.getElementById("canvas");
    canvas.addEventListener("click", answer);
  
    const url = 'fibacup.json';    
    var promiseFetch = fetch(url);
    let answers;
    
     promiseFetch.then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error: ${response.status}`);
        }
        return response.text();
          })
          
          .then(function(text) {    
            answers = JSON.parse(text); 
        })
          .catch(function(err){
        alert(err);});   
/*
      function draw() {
        const canvas = document.getElementById("canvas");
        if (canvas.getContext) {
          const ctx = canvas.getContext("2d");
          
          
          TBC 
 
        }
     }
*/ 
  function fetchMovieData() {
    fetch('zap.json')
        .then(response => response.json())
        .then(data => {
            const movie = data[Math.floor(Math.random() * data.length)];
            displayMovie(movie);
        })
        .catch(error => console.error('Eroare plangacioasa:', error));
  }   
  function displayMovie(movie) {
    timeElement.textContent = `${movie.date} at ${movie.time}`;
    titleElement.textContent = movie.title;
    posterElement.src = movie.poster;
    posterElement.src = `./resources/${movie.poster}`;
    posterElement.alt = movie.title;
    posterElement.title = movie.title;
    posterElement.style.display = 'block';
    additionalInfoElement.innerHTML = `<p>Cast: ${movie.starring}</p><p>Rating: ${movie.rate}</p>`;
  }
}