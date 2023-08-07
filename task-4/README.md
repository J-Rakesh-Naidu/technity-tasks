![Image](https://github.com/J-Rakesh-Naidu/technity-tasks/blob/main/task-4/Screenshot%20(630).png)

<h2>My Approach,</h2>

I made a function which takes the path as argument and plays the audio file named Strike(path),
and used onClick event attribute to call the function when the button is clicked.

Then, added Keyboard event listener to call the function when the respective button is pressed on keyboard.

I added a pressed effect to the buttons when clicked by changing the box shadows, text shadow and opacity.

<h3>For the design</h3>
 I went with a Kid's School theme,
 
 I used bright and playful colors for buttons which go well and complement each other to make it look like a kid's toy.
 
 I changed the background to charcoal and the heading to white with Chalkduster font, so the background looks like a BlackBoard in School.
 
 The font I used for the buttons is KG HAPPY which is uneven on line like a kid's handwriting.

My HTML
```
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
  <meta charset="utf-8">
  <title>Drum Kit</title>
  <link rel="stylesheet" href="styles.css">
</head>

<body>

  <h1 id="title">DRUM KIT</h1>
  <div class="set">
    <button class="w drum" onclick="Strike('sounds/tom-1.mp3')">W</button>
    <button class="a drum" onclick="Strike('sounds/crash.mp3')">A</button>
    <button class="s drum" onclick="Strike('sounds/tom-2.mp3')">S</button>
    <button class="d drum" onclick="Strike('sounds/kick-bass.mp3')">D</button>
    <button class="j drum" onclick="Strike('sounds/tom-3.mp3')">J</button>
    <button class="k drum" onclick="Strike('sounds/snare.mp3')">K</button>
    <button class="l drum" onclick="Strike('sounds/tom-4.mp3')">L</button>
  </div>
  <script src="index.js"></script>
</body>

</html>
```
MY CSS
```
@import url(https://db.onlinewebfonts.com/c/bd9805cba4fdbd10e6f9d097dab9225f?family=Chalkduster);
@import url(https://db.onlinewebfonts.com/c/fb39a9928c0b77d063ad5613bc1443a8?family=Marker);

body {
  text-align: center;
  background-color: #333333;
}

h1 {
  font-size: 5rem;
  color:  #F5F5F5;
  font-family: 'Chalkduster';
}

.drum {
  border: 2px solid #000000;
  box-shadow: 5px 5px 5px 5px black;
  font-size: 5rem;
  font-weight: 200;
  border-radius: 40px;
  display: inline-block;
  width: 150px;
  height: 150px;
  text-align: center;
  margin: 10px;
  font-family: "Marker";
}

.w {
  background-color: #007BFF ;
  color: #FFFFFF;
  text-shadow: 2px 2px 2px #004BA0;
}

.a {
  background-color: #17A2B8;
  color: #FF6B6B;
  text-shadow: 2px 2px 2px #156C7E ;
}

.s {
  background-color: #B19CD9;
  color:  #66DE93;
  text-shadow: 2px 2px 2px #6B5D94 ;
}

.d {
  background-color: #FFD700;
  color: #333333;
  text-shadow: 2px 2px 2px #B4A5A5;
}

.j {
  background-color: #E63946;
  color: #F1FAEE;
  text-shadow: 2px 2px 2px #A12631;
}

.k {
  background-color: #2ECC71;
  color: #D5DBDB ;
  text-shadow: 2px 2px 2px #186A3B;
}

.l {
  background-color: #800080;
  color: #FFD700;
  text-shadow: 2px 2px 2px #36013F;
}

.set {
  margin: 10% auto;
}

.drum:active{
  box-shadow: 2px 2px 2px 2px black;
  opacity: 0.9;
  transform: translateX(3px);
  text-shadow: 0px 0px 0px;
}
```
MY JS
```
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
```
