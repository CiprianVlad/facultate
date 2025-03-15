window.onload = () =>
{
    localStorage.clear();
    const body = document.body;
    let BubblesCount = parseInt(localStorage.getItem('BubblesCount')) || 0;
    const BubbleCounter = document.createElement('div');
    BubbleCounter.classList.add('Bubble-count');
    updateBubbleCount();
    body.appendChild(BubbleCounter);

    document.addEventListener('keydown', (event) => {
        if (event.key === 's') {
            createBubble();
        }
        else if(event.key === 'p'){ 
            startBubble();
        }
        else if(event.key === 'f'){
            endBubble();
        }
    });

    function createBubble() {
        const bubble = document.createElement('img');
        bubble.src = 'images/bubble-1.png';
        bubble.style.position = "absolute";
        bubble.classList.add('bubble');
        let w = window.innerWidth;
        let h = window.innerHeight;
        bubble.style.left = `${Math.random() * (w - 200)}px`;
        bubble.style.top = `${Math.random() * (h - 200)}px`;

        bubble.addEventListener('click', () => {
            if (bubble.isPopping) {
                clearInterval(bubble.PopInterval);
                bubble.isPopping = false;
            } else {
                StartPopping(bubble);
            }
        });

        body.appendChild(bubble);
    }


    function StartPopping(bubble) {
        const images = [
            'images/bubble-1.png',
            'images/bubble-2.png',
            'images/bubble-3.png',
            'images/bubble-4.png'
        ];

        let currentImageIndex = 0;
        bubble.isPopping = true;

        bubble.PopInterval = setInterval(() => {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            bubble.src = images[currentImageIndex];
            if (currentImageIndex === 0) {
                BubblesCount++;
                updateBubbleCount();
                if (BubblesCount % 1 === 0) {
                    clearInterval(bubble.PopInterval);
                    bubble.remove();
                }
            }
        }, 200);
    }

    function updateBubbleCount() {
        localStorage.setItem('BubblesCount', BubblesCount);
        BubbleCounter.textContent = `Bubbles Popped: ${BubblesCount}`;
    }
    
    function startBubble(){

    }

    function endBubble(){
        
    }
};
