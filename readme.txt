Made a folder named React-Django-Project in desktop
installed 3 extensions
Javascript ES6 , React ,Django , Python

need some pre install packages
pip install django djangorestframework

Open the terminal write the command to make a django project :
django-admin startproject music_controller
result: I got music_controller folder inside that same name folder and a manage.py file

Inside the first folder cd.\music_controller i will write command for my django app.
command: django-admin startapp api

Now we need this api app connected with music_controller other folder or second folder
soo we will go inside settings.py and inside installed apps we will write app name that is api and continue with other so the end result will be 
api.apps.ApiConfig soo after saving u can see automatic ApiConfig class in apps.py

Now we will add another app that is rest_framework that we will need for our project.
Inside apps we can see views we will see the api folder which is our first app we can see views file.
Views are use to render the page whatever we want to display ,we write the endpoints in urls that are navigated to views. 
Endpoints are  the location in the web server (after the slash /) where we want to land.
We can write functions in views for example we are going to write a function name request
with param name request and that will return a response.
wherever we have web server , their an incoming request denoted with the name request varaible.
Request will return a response it can be in any formt like json or http response.


so we  need to import http response in views: from django.http import HttpResponse
now we will write return HttpResponse("Hello), we can write anything we will go to this endpoint it will display Hello.

Creating new file name urls.py in api folder.
Go to urls.py file from music_controller folder.
This is the main urls if we write  path as ""  any url should go to this file . so this should go to include we neeed to import include .
So include api.urls.
now we will go to urls.py from api and copy the same code just remove admin and write "" this path
we wont write include instead we will import function main from views.py soo wherever this "" path it will go to main function which responses with hello text.
now we need to go to the terminal and write python manage.py makemigrations which is used to update databse.
Now we dont have database but we are going to run our code soo we need to define it .
After running u can see django automatically creates sqlite database.

then run python manage.py migrate in the terminal then finally to start the server write python manage.py runserver
you can see a link ctrl click that will display hello
but if u change the view.py and write h1 tg so u see whenever we save server automatically restarts .

now if we change the urls.py in api app and write home instead of ""
we save and check their is an error but if write /home we noticed it displays hello.

now change in main urls.py file instead of"" write api/ we see an error then in location we write api/ we get error then we write
api/home we get hello.

lets get strated with models which is in api folder.
Models helps to create database using python code and also helps in perform database operations.

First model we are going to create is Room model
were are going to create room to group all users in one room and have the controll over the host music.
Each room will have only one host for one room
guest_can_pause send the permission whether the guest is allowed to pause the music
votes_to_skip integer field to get the number of guest who vote to skip the music
created_at  its a time field give date and time on creation of room.

while creating a room a 8 digit code should be generated of random numbers
Making a function to generate that code
length = 6 
while true generate bunch of code until i find one thats unique
code variable to generate string upercase
then filter or query to check whther the room object code has same code as we generated
if the generated list count is o then break and return the code


now we will run code because if made changes in the database  that is model.
i got an error while makemigrations saying that auto_now_add need to have default value sooo 
i altered the code and removed auto_now_add and wrote default = current dat and time
run the make migrations and then edited ctrl z that is remove the default and added auto_now_add
then made migrate

user tried to join the room and backend says that this room exist soo we 
need endpoint that shows info and return to frontend in json format
{'key':'key value'}

soo we need serializers class we need to make a file name
serilizers.py
which takes all the data from model and converts it into json format 
so that we can send it to frontend
inside this serializer file we need to import from rest framework import serializers
and from.model import room so we can access the room class,
i have added 'id' also, which is automatically created called as primary key
for identifying the model and it is created in each model.

Now going to views file removing the def function which we had created it earlier 
and removing the httpresponse imports
and adding from restframeworks import generics

Generic provided byrest framework helps to quickly build api views that map closely to your models
Creating view with class name RoomView inclusing generics.CreateAPIView
then defining variables qeury_set containing all objects from room models 
and other is serializer_class having room serailizer 
but before that dont forget to import models and serializer in view before defining

Going to api urls.py and replacing the views import of main function to RoomView class
and later changing in path with room and class roomView and adding .as_view()
as_view()  just takes the class and gives view to it

After runing the code i went to that page and i can see the some nice page
that contains the fields like out models
and i can fill the data and click on post i can see it 

now updating the generic.ListAPIView and run the code it doesnt gives me post just gives me get
that gives the list of data i have field in that model class

Go to the terminals and type npm if it works the we are going create new app
frontend app.
command - django-admin startapp frontend
now go to cd ./frontend
soo this folder is going to have all the frontend of the project
that is react component and the api folder is strictly for te backend
Now we are going to create 2 new folders in frontend
name templates and static
soo the static folder is going to contain all the static files
and creating 3 folders inside the static folder name frontend
it would contain all the javascript bundles.
and other one name css in lowercase and the last one name images.
Another folder in main frontend folder name src
inside src (source) folder we are going to create another
folder name components. In react we have components that we will keep in that folder.

In terminals inside frontend main folder write the command
npm init -y which will create packages, node modules and other things that will be need in frontend project.

Soo we can see a package.json file in frontend folder
so we cant see node modules soo we need to install bunch of stuff from npm
command npm i webpack webpack-cli --save-dev 
so this is webpack we need it as it takes javascript stufff and transpilot it to a single javascript file.

Next  we need babble and the command is
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev

this will take our code and transpile it so that it can be run in old browsers


we need to install react command 
npm i react react-dom --save-dev

Next we are going to install is material UI
prebuilt component we will need while styling
npm install @material-ui/core

Next is babel again
npm install @babel/plugin-proposal-class-properties

next we need is react router to route the pages
npm install react-router-dom

last one we need is materail-ui icons
npm install @material-ui/icons

next inside out main frontend folder create one file name babel.config.json
pasted a code 
{
  "presets": [
    [
      "@babel/preset-env",
      {
        "targets": {
          "node": "10"
        }
      }
    ],
    "@babel/preset-react"
  ],
  "plugins": ["@babel/plugin-proposal-class-properties"]
}


it sets a babel loader and plugins

Inside main frontend folder make another file for
webpack named webpack.config.js it bundles all the javascript into one file and gives to the browser.
and pasted code 
const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
  ],
};
   
Now isnide package.json we are going to remove the scripts  the thing inside the double qoutes and write
"dev":"webpack --mode development --watch"
it means we want webpack to run in development mode and want watch mode

separated with comma and write built script
"build":"webpack --mode production"

Now make a new file in src name index.js

now make one folder in templates named frontend and make file in it name index.html

and write the boiler plate instide index.html
After the title tag i have written {% load static %} which means it will allows us to load static files to look at javascript code

then add script for jQuery CDN  and link of css file
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:300,400,500,700&display=swap">
    <link rel="stylesheet" type="text/css" href="{% static 'css/index.css' %}"/>

Inside body we are going to add the div with id = 'main' and inside that another div with id='app'
react will go inside div with id app
and outside div tags we are, going to add script tag for javascript file static folder /frontend

Going to views file in our frontend and defining a index function  for request and render 
in return i will render the request with location frontend/index.html
soo the react will take care of this it will the request and render the index.html file

Create a new file urls.py in main frontend folder 
Going to music_controller folder's urls file and adding a path 
empty path and include the urls from frontend folder

again copying the main urls.py and pasting it in main
frontend's urls file removing admin import and include 
removing first 2 paths of admin and api 
and third empty path removing include and first importing 
from .views import index  this function we just defined in views
and in the empty path after comma write this function name index.

Now we are going to create first component in react
creating a new file name app.js in components folder


Then import react and component from react 
and import render from react-dom

Making a class name App extends Component
inside that write constructor and take props inside that inside that
call the super and inside that again props
then come outside of constructor and write render and return h1 tag Testing React Code

Now we need this component to render in main index.html through a id
we have already made and id name app soo we need to access it from app.js file
so after the class app  we need to define variable 
const appDiv = document.getElementById("app")
and then write render(<App/>,appDiv)

soo now we are ready we just need to put this file i mean
connect with index.js file
import App from whatever location

then we will run the frontend soo for we need to go terminals
and be in frontend directory by cd ./frontend and write npm run dev
soo i got an error so i changed the webpack file
i mean i updated NODE_ENV: JSON.stringify("production"), this
production to development and it was succesfully running.

soo now in static we had frontend folder inside that you can see main.js
that bundle up all the javascript code .

and also run the django music controller in terminal
i got an error that templatedoesnotexist at /
its a silly mistake soo
lets go to settings.py and add frontend app in installed apps
'frontend.apps.FrontendConfig',
and i got one more error in app.js file
i imported component and used Component 
so i need to import capital C, Component

Yee so its running alright


Now in index.html file we had mention index.css in head script tag 
soo we have a css folder and inside that lets create a index.css file.
lets add some basic styles in it.
im going to make height 100% for html and body tag in css then margin =0; padding=0; 
next lets make style for id main and id app using #
main is wrapping the app and app is containing our actual react component
main style includes firstly position is going to be fixed then height and width 100%
we are going to position  this with left 0 and top 0 which means it going to take this div to
top left cornor of the screen and make height and width fill the entire screen 
and since the position is fixed it means their would'nt be any scroll bars 
our page will be fixed
now going to id app  and make height and width 100 %
display=flex this is beacuse some of the components we are going to use requires flex grid

im going to update my app.js file simplifying it 
removing constructor  because no need and instead of class and component im going to use
export const function name App and i wont render but i will return in it
After running the code it works well .

We can pass props inside the component tag, props is just an argument or an attribute we give to component
it will use that to modify the behaviour of the component
for example in app function i have return a h1 tag the isnide data i will change
i will put it in {name} and also in function argument i will write {name}
and when i render the app function <app name="nandita"/> name is the prop i have passed it in component
export const App =({name})=>{
    return(
        <h1>{name}</h1>
    )
}
const appDiv = document.getElementById("app");
render(<App name="Nandita"/>,appDiv);

Let me tell a little bit about state if u write state in a component it will automatically render the component\
so u dont need to render the whole page completely

Now we will go back to our return h1 tag and write it like previous and remove the prop name
lets make another component and make it render from this main app
In components folder im going to make new file name HomePage.js its going to be the home page of our project
lets import react and first write the export const function name HomePage
and returning a p tag inside a div tag wrting hey its my home page

Lets go to app.js and import home page component so instead of the h1 tag we are going to return <HomePgae/> tag component
now add one more file in components folder name RommJoinPage write the similiar thing as Homepage function and return h1 writing RoomJoinPage
Making another file in components folder for CreateRoomPage component write similiar as the previous just change the h1 tag text to CreateRoomPage

Now go to

















