document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    let genuflexiuniCount = parseInt(localStorage.getItem('genuflexiuniCount')) || 0;
    const genuflexiuneCounter = document.createElement('div');
    genuflexiuneCounter.classList.add('genuflexiune-count');
    updateGenuflexiuniCount();
    body.appendChild(genuflexiuneCounter);

    document.addEventListener('keydown', (event) => {
        if (event.key === 'b') {
            createBadger();
        } else if (event.key === 'p') {
            playSound();
        }
    });

    function createBadger() {
        const badger = document.createElement('img');
        badger.src = 'resources/images/badger-1.png';
        badger.classList.add('badger');
        badger.style.left = `${Math.random() * (window.innerWidth - 100)}px`;
        badger.style.top = `${Math.random() * (window.innerHeight - 100)}px`;

        badger.addEventListener('click', () => {
            if (badger.isDancing) {
                clearInterval(badger.danceInterval);
                badger.isDancing = false;
                badger.remove();
            } else {
                startDancing(badger);
            }
        });

        body.appendChild(badger);
    }

    function startDancing(badger) {
        const images = [
            'resources/images/badger-1.png',
            'resources/images/badger-2.png',
            'resources/images/badger-3.png',
            'resources/images/badger-4.png'
        ];

        let currentImageIndex = 0;
        badger.isDancing = true;

        badger.danceInterval = setInterval(() => {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            badger.src = images[currentImageIndex];

            if (currentImageIndex === 0) {
                genuflexiuniCount++;
                updateGenuflexiuniCount();
                if (genuflexiuniCount % 5 === 0) {
                    createMushroom();
                    clearInterval(badger.danceInterval);
                    setTimeout(() => {
                        badger.danceInterval = setInterval(danceStep, 200);
                    }, 1000);
                }
            }
        }, 200);

        function danceStep() {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            badger.src = images[currentImageIndex];

            if (currentImageIndex === 0) {
                genuflexiuniCount++;
                updateGenuflexiuniCount();
                if (genuflexiuniCount % 5 === 0) {
                    createMushroom();
                    clearInterval(badger.danceInterval);
                    setTimeout(() => {
                        badger.danceInterval = setInterval(danceStep, 200);
                    }, 1000);
                    //l am pus sa stea la 5 genuflexiuni facute ca sa faca sport, imi asum depunctarea daca nu va place si vreti sa se odihneasca, dar in lumea asta e bine sa faca sport :**
                }
            }
        }
    }

    function updateGenuflexiuniCount() {
        localStorage.setItem('genuflexiuniCount', genuflexiuniCount);
        genuflexiuneCounter.textContent = `Genuflexiuni: ${genuflexiuniCount}`;
    }

    function createMushroom() {
        const mushroom = document.createElement('img');
        mushroom.src = 'resources/images/mush.png';
        mushroom.classList.add('mushroom');
        mushroom.style.left = `${Math.random() * (window.innerWidth - 50)}px`;
        mushroom.style.top = `${Math.random() * (window.innerHeight - 50)}px`;
        body.appendChild(mushroom);
    }

    function playSound() {
        const audio = new Audio('resources/badger.mp3');
        audio.play();
        audio.volume = 0.5;
        audio.onended = () => {
            audio.pause();
            audio.currentTime = 0;
        };
    }
});
