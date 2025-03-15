window.onload = () => 
{
    draw();

    const canvas = document.getElementById("canvas");
    canvas.addEventListener("click", answer);

    const url = 'magic.json';
    var promise = fetch(url);
    let possanswers;

    promise.then((response) =>
        {
            if (!response.ok)
            {
                throw new Error(`HTTP error: ${response.status}`);
            }
            return response.text();
        })
        .then((text) =>
        {
            possanswers = JSON.parse(text);
        })
        .catch((err) =>
        {
            alert(err);
        });
    
    function draw(){

    const canvas = document.getElementById('magicBall');
    const ctx = canvas.getContext('2d');

    // Set canvas size
    const centerX = canvas.width / 2;
    const centerY = canvas.height / 2;
    const outerRadius = 100; // Outer black circle radius
    const innerRadius = 50;  // Inner white circle radius

    // Draw black outer circle
    ctx.beginPath();
    ctx.arc(centerX, centerY, outerRadius, 0, 2 * Math.PI);
    ctx.fillStyle = 'black';
    ctx.fill();
    ctx.closePath();

    // Draw white inner circle
    ctx.beginPath();
    ctx.arc(centerX, centerY, innerRadius, 0, 2 * Math.PI);
    ctx.fillStyle = 'white';
    ctx.fill();
    ctx.closePath();

    // Draw the number 8
    ctx.fillStyle = 'black';
    ctx.font = '48px Arial';
    ctx.font = "bold"
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('8', centerX, centerY);
    }

    function answer()
    {
        let max = possanswers.length;
        let ans = Math.floor(Math.random() * max);
        let color = "green";
        if (possanswers[ans].bool == "no")
        {
            color = "red";
        }
        else if (possanswers[ans].bool == "maybe")
        {
            color = "orange";
        }
        const canvas = document.getElementById("canvas");
        if (canvas.getContext)
        {
            const ctx = canvas.getContext("2d");
            ctx.fillStyle = "black";
            ctx.beginPath();
            ctx.arc(100, 100, 100, 0, 360);
            ctx.fill();

            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(100, 100, 50, 0, 360);
            ctx.fill();
        }

        let infoDiv = document.getElementById("info");
        infoDiv.innerHTML = possanswers[ans].text;
        infoDiv.style.color = color;
    }
}