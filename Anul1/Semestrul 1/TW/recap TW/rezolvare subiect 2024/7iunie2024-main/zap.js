document.addEventListener('DOMContentLoaded', () => {
    const tv = document.querySelector('.tv');
    const timeElement = document.querySelector('.time');
    const titleElement = document.querySelector('.title');
    const posterElement = document.querySelector('.poster');
    const additionalInfoElement = document.querySelector('.additional-info');

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

    tv.addEventListener('click', fetchMovieData);

    posterElement.addEventListener('mouseover', () => {
        additionalInfoElement.style.display = 'block';
    });x``

    posterElement.addEventListener('mouseout', () => {
        additionalInfoElement.style.display = 'none';
    });
});
