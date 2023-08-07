![image](https://github.com/J-Rakesh-Naidu/technity-tasks/blob/main/task-1/Screenshot%20(632).png)

HTML Code:
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <title>Document</title>
    <link rel="stylesheet" href="styles.css">
    </head>
<body>
    <header>
        <p>Create.co</p>
        <div>
            <ul>
                <li>Home</li>
                <li>Service</li>
                <li>Team</li>
                <li>Blog</li>
                <li>Contact Us</li>
            </ul>
            <ul>
                <li>Log in</li>
                <button class="navbut">Getting Started</button>
            </ul>
        </div>
    </header>

    <div class="torso">
        <div class="content">
            <div>
                <p class="blue">Grow Your Business<br>With</p><p class="red"> Social Media<br>Marketing</p>
                <span>Lorem ipsum dolor sit amet consectetur<br>adipisicing elit. Dolorum vel nihil dolor cupiditate minima?<br>Similique ullam sapiente impedit itaque esse!</span>
                <input type="email" placeholder="Email Address" name="email"><input type="button" value="Learn More">
            </div>
            <footer>
                <i class="fab fa-instagram"></i>
                <i class="fab fa-facebook"></i>
                <i class="fab fa-twitter"></i>
                <i class="fab fa-youtube"></i>
                <i class="fab fa-whatsapp"></i>
            </footer>
        </div>
        <div><img src="BASE.png" alt="base img"></div>
    </div>
</body>
</html>
```

CSS Code:
```
@import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');

:root{
    --lightlavender : #5654b3;
    --lightred : #fa676d ;
    --darklavender: #2d2c62 ;
    --creamlike : #e3f0ff;
}

*{
    font-family: 'Montserrat', sans-serif;
    font-weight: 400;
}

body{
    background-color: var(--creamlike);
}

header{
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin: 1rem 5rem 0;
}

header p{
    font-weight: 1000;
    font-size: xx-large;
    color: var(--darklavender);
}

header div{
    display: flex;
}

ul{
    display: flex;
    list-style-type: none;
    justify-content: center;
    align-items: center;
}

li{
    text-decoration: none;
    display: block;
    height: 20px;
    margin: 30px;
}

.navbut{
    background-color: var(--lightlavender);
    color: var(--creamlike);
    border: none;
    outline: none;
    border-radius: 5px;
    height: 50px;
    width: 150px;
}

.torso{
    display: flex;
    justify-content: space-between;
    width: 95%;
    margin: 1rem 5rem 0;
}

img{
    height: 600px;
    width: 900px;
    margin: 0;
    display: inline-flex;
}

.content{
    align-items: center;
}

.content div{
    position: relative;
    top: 20%;
}

.content div p{
    display: inline;
    font-weight: bold;
    font-size: 50px;
    line-height: 1.2;
}

.blue{
    color: var(--darklavender);
}

.red{
    color: var(--lightred);
}

span{
    display: block;
    font-weight: 500;
    opacity: 0.5;
    margin: 10px 0;
    line-height: 1.5;
}

input[type=email]{
    margin: 10px 0;
    height: 50px;
    width: 200px;
    display: inline-block;
    border-radius: 10px 0 0 10px;
    border: 0;
    padding-left: 20px;
}

input[type=button]{
    width: 150px;
    margin: 0;
    height: 52px;
    border-radius: 0px 10px 10px 0px;
    border: none;
    background-color: var(--lightlavender);
    color: var(--creamlike);
}

footer{
    position: relative;
    top: 35%;
}

i{
    background-color: var(--darklavender);
    padding: 8px;
    border-radius: 5px;
    color: var(--creamlike);
}
```
