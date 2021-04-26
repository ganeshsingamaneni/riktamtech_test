# Technologies used

* Python3 - A programming language that lets you work more quickly (The universe loves speed!).

* Flask - A microframework for Python based on Werkzeug, Jinja 2 and good intentions.

* SQLite – SQLite database offers many advantages over others ,it comes along with python.

* Minor dependencies can be found in the requirements.txt file on the root folder.

# how to test this?
 
 1. [Install Docker Compose](https://docs.docker.com/compose/install/ "Install Docker Compose")
 
 2. Run all containers with 
       # docker-compose up --build 
 
 3. test api using Postman
 
     http://0.0.0.0:4000/api/distance
     
     ## data must be send using form-data
     
     # parameters
     * field: image1  
     * type: file
     * field : image2
     * type: file
  4. please upload valid face images make sure face images may not be turned sideways or upside-down.
     
 
  
