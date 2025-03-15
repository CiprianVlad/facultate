document.addEventListener('DOMContentLoaded', function () {

    const morningInfo = document.getElementById("morning-info");
    const middayInfo = document.getElementById("midday-info");
    const afternoonInfo = document.getElementById("afternoon-info");
    const eveningInfo = document.getElementById("evening-info");

    if (morningInfo) {
        morningInfo.addEventListener("mouseover", function () {
            alert("I start my day by brushing my teeth and taking a cold shower...");
        });
    }

    if (middayInfo) {
        middayInfo.addEventListener("mouseover", function () {
            alert("I can't wait to finish my TODO list...");
        });
    }

    if (afternoonInfo) {
        afternoonInfo.addEventListener("mouseover", function () {
            alert("Afternoon workout – a 30-minute grind...");
        });
    }

    if (eveningInfo) {
        eveningInfo.addEventListener("mouseover", function () {
            alert("Evening is for board games like Backgammon...");
        });
    }

    const chessModal = document.getElementById("chessModal");
    const chessBtn = document.getElementById("chess");
    const chessClose = document.querySelector(".close-chess");

    if (chessModal && chessBtn && chessClose) {
        chessBtn.addEventListener("click", function () {
            chessModal.style.display = "block";
        });

        chessClose.addEventListener("click", function () {
            chessModal.style.display = "none";
        });

        window.addEventListener("click", function (event) {
            if (event.target == chessModal) {
                chessModal.style.display = "none";
            }
        });
    }

    const webpageSpan = document.getElementById("webpage");

    const rainbowColors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"];

    if (webpageSpan) {
        setInterval(function () {
            const randomColor = rainbowColors[Math.floor(Math.random() * rainbowColors.length)];
            webpageSpan.style.color = randomColor;
        }, 500);
    }

    const catImage = document.getElementById("catImage");

    if (catImage) {
        catImage.addEventListener("click", function () {
            catImage.src = "images/happycat.jpg";
        });
    }

    const moreHobbiesBtn = document.getElementById("more-hobbies");
    const hobbyParagraph = document.getElementById("hobby-paragraph");

    if (moreHobbiesBtn && hobbyParagraph) {
        moreHobbiesBtn.addEventListener("click", function () {
            hobbyParagraph.style.display = "block";
            hobbyParagraph.innerHTML = "I've always loved chess and played it professionally for a while. I'm also into a bunch of different games, especially strategy ones like 'Kingdom Come: Deliverance' and the Souls series. Lately, I've been reading books that get me thinking about things like capitalism and society, which I find pretty interesting. When I'm hanging out with friends, you'll usually find us playing board games like Catan or Backgammon.";
        });
    }


    function loadSavedData() {

        if (localStorage.getItem('hobbyFormData')) {
            const savedData = JSON.parse(localStorage.getItem('hobbyFormData'));

            // Populate the form with saved data
            document.getElementById('name').value = savedData.name || '';
            document.getElementById('favorite-game').value = savedData.favoriteGame || '';
            document.getElementById('game-type').value = savedData.gameType || '';
            document.getElementById('experience-level').value = savedData.experienceLevel || 1;

            if (savedData.hobbies) {
                savedData.hobbies.forEach(hobby => {
                    document.getElementById(hobby).checked = true;
                });
            }
        }
    }

    function saveSurveyData(event) {
        event.preventDefault(); // Prevent the form from submitting

        const name = document.getElementById('name').value;
        const favoriteGame = document.getElementById('favorite-game').value;
        const gameType = document.getElementById('game-type').value;
        const experienceLevel = document.getElementById('experience-level').value;
        const hobbies = [];

        document.querySelectorAll('input[name="hobbies"]:checked').forEach(checkbox => {
            hobbies.push(checkbox.value);
        });


        const formData = {
            name: name,
            favoriteGame: favoriteGame,
            gameType: gameType,
            experienceLevel: experienceLevel,
            hobbies: hobbies
        };

        localStorage.setItem('hobbyFormData', JSON.stringify(formData));

        alert("Your data has been saved!");
    }

    document.getElementById('hobby-form').addEventListener('submit', saveSurveyData);


    loadSavedData();

    const canvas = document.getElementById("canvChessboard");
    const ctx = canvas.getContext("2d");

    let boardColors = ["#f0d9b5", "#b58863"]; // light and dark square colors
    let tileSize = 50;

    // chessboard
    function drawBoard() {
        for (let row = 0; row < 8; row++) {
            for (let col = 0; col < 8; col++) {
                let x = col * tileSize;
                let y = row * tileSize;
                ctx.fillStyle = (row + col) % 2 === 0 ? boardColors[0] : boardColors[1];
                ctx.fillRect(x, y, tileSize, tileSize);
            }
        }
    }

    drawBoard(); 

    canvas.addEventListener("click", function(event) {
        let rect = canvas.getBoundingClientRect();
        let x = event.clientX - rect.left;
        let y = event.clientY - rect.top;
        let col = Math.floor(x / tileSize);
        let row = Math.floor(y / tileSize);

        let clickedColor = (row + col) % 2 === 0 ? boardColors[0] : boardColors[1];

        ctx.fillStyle = clickedColor === boardColors[0] ? boardColors[1] : boardColors[0];
        ctx.fillRect(col * tileSize, row * tileSize, tileSize, tileSize);
    });
});
