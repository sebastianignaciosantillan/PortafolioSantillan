let menuVisible = false;
//Función que oculta o muestra el menu
function mostrarOcultarMenu(){
    if(menuVisible){
        document.getElementById("nav").classList ="";
        menuVisible = false;
    }else{
        document.getElementById("nav").classList ="responsive";
        menuVisible = true;
    }
}

function seleccionar(){
    //oculto el menu una vez que selecciono una opcion
    document.getElementById("nav").classList = "";
    menuVisible = false;
}
//Funcion que aplica las animaciones de las habilidades
function efectoHabilidades(){
    var skills = document.getElementById("skills");
    var distancia_skills = window.innerHeight - skills.getBoundingClientRect().top;
    if(distancia_skills >= 300){
        let habilidades = document.getElementsByClassName("progreso");
        habilidades[0].classList.add("javascript");
        habilidades[1].classList.add("htmlcss");
        habilidades[2].classList.add("photoshop");
        habilidades[3].classList.add("wordpress");
        habilidades[4].classList.add("drupal");
        habilidades[5].classList.add("comunicacion");
        habilidades[6].classList.add("trabajo");
        habilidades[7].classList.add("creatividad");
        habilidades[8].classList.add("dedicacion");
        habilidades[9].classList.add("proyect");
    }
}


//detecto el scrolling para aplicar la animacion de la barra de habilidades
window.onscroll = function(){
    efectoHabilidades();
} 


const text = document.querySelector(".sec-text");
        
        const textLoad = () => {
            setTimeout(() =>{
            text.textContent = "FrontEnd"
    }, 0 );
            setTimeout(() =>{
            text.textContent = "BackEnd."
    }, 4000 );
            setTimeout(() =>{
            text.textContent = "Develop."
    }, 8000 );
    
    }
    textLoad();
    setInterval(textLoad, 12000);

//contact form
const scriptURL = 'https://script.google.com/macros/s/AKfycbyFj3Tv_XJDj0B7GK9yQOz1AqOrMAFLeIjnOF9PjXjEg0Gd860BBFgCEzJJnUJkebAWJA/exe';

const form = document.forms['contact-form'];

form.addEventListener('submit', e => {
    e.preventDefault();
    fetch(scriptURL, { method: 'POST', body: new FormData(form) })
        .then(response => alert("¡Gracias por enviar su consulta"))
        .then(() => { window.location.reload(); })
        .catch(error => console.error('¡Error!', error.message));
});

