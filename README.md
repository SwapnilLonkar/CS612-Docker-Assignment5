# Docker
 Step 1: Installed Docker Toolbox for Mac/Windows.
 
 Step 2: Created Jason database of my fav movies named movies.json
 
 Step 3: Created Home.html and index.html to display data in table
 
 Step 4: Coding of the web services is implemented in python and flask
 
 Step 5: Created a docker file named Dockerfile
 
 Step 6: Open CMD and navigate to the project folder
 
 Step 7: Build image in docker container using **docker build . -t favmovies** (-t is used to tag the docker image with name 'favmovies'.)
 
 Step 8: Run image using docker **run -d -p 5000:5000 favmovies** (5000 is default port for python)
 
 Step 9: To check if the image is assigned with a port we used command docker **ps -a**(This displays the port number)
 
 Step 10: To display welcome page for database open **192.168.99.100:5000**
 
 Step 11: To display entire database we used **192.168.99.100:5000/getmovies/**
 
 Step 12: To get movie by it's id use **192.168.99.100:5000/getmovies/3** (where 3 is the id)
 
 Step 13: To get movie by it's genre use **192.168.99.100:5000/getmovies/type/fiction**
