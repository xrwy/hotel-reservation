function navbarShow(){
    var classsNameGet = document.getElementById('navbar');
    if(classsNameGet.className == 'tp_navbar' ){
        classsNameGet.className += " show";
    }
    else{
        classsNameGet.className = "tp_navbar";
    }
}

