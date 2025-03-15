window.onload = () => 
{   
    localStorage.clear();
    let print = document.createElement('div');
    print.setAttribute("id", "print");
    document.body.appendChild(print);
    let range = document.createElement('input');
    range.type = "range";
    range.id = "range";
    range.min = "20";
    range.max = "150";
    range.value = "20";
    document.body.appendChild(range);

    document.addEventListener('keydown', (event) => {
        createBulina(event);
    });

    function createBulina(event){
        let div = document.createElement("div");
        let size = document.getElementById("range").value;

        div.style.height = size + "px";
        div.style.width = size + "px";
        div.style.borderRadius = "50%";
        div.style.background = "red";
        div.style.position = "absolute"; /* ChatGPT addition */
        div.classList.add('div');

        let w = window.innerWidth;
        let h = window.innerHeight;
        let posx = Math.floor(Math.random() * (w - size));
        let posy = Math.floor(Math.random() * (h - size));
        div.style.left = posx + "px";
        div.style.top = posy + "px";

        switch (event.key) 
        {
            case "r":
                div.style.backgroundColor = "red";
                break;
            case "g":
                div.style.backgroundColor = "green";
                break;
            case "b":
                div.style.backgroundColor = "blue";
                break;
            case "y":
                div.style.backgroundColor = "yellow";
                break;
            default:
                return;
        }
        
        document.body.appendChild(div);

        let x = Number(localStorage.getItem("nodots"));

        if (x)
        {
            localStorage.setItem("nodots", x + 1);
        }
        else
        { 
            localStorage.setItem("nodots", "1");
        }
        document.getElementById("print").innerHTML = localStorage.getItem("nodots");
        
        /* Nu uita de addEventListener pentru click */
        div.addEventListener("click", () => {
            createBulina(event, div.style.backgroundColor);
        });
    } 
};