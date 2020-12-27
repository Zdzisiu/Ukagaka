function GetColor(){
            var colors = ["#ff89ef","#ff999c","#89ffff", "#92ff89", "#faff89", "#ff8989", "#9591ff","#ffb778","#ff88c7","#f9f871"];

            var random_color = colors[Math.floor( 
                                Math.random() * colors.length)]; 
            var a = document.getElementsByClassName("color");
            var b = a.length
            
            for(var i=0;i<b;i++)
            {
                a[i].style.color = random_color;
            }
            
        }