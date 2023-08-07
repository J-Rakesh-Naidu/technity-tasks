function Strike(path){
    var Play = new Audio(path);
    Play.currentTime = 0;
    Play.play();
}

document.addEventListener('keydown',(e)=>{
    var code = e.key;
    if(code == "w"){
        Strike('sounds/tom-1.mp3');
    }else if(code == "a"){
        Strike('sounds/crash.mp3');
    }else if(code == "s"){
        Strike('sounds/tom-2.mp3');
    }else if(code == "d"){
        Strike('sounds/kick-bass.mp3');
    }else if(code == "j"){
        Strike('sounds/tom-3.mp3')
    }else if(code == "k"){
        Strike('sounds/snare.mp3')
    }else if(code == "l"){
        Strike('sounds/tom-4.mp3')
    }
})