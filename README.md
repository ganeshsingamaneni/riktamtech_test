# riktamtech_test
* clone the repository and create a python3 environvent 
* And chnage directory to riktamtech_test/riktamtech_test and then install all requirements in requirements.txt(pip install -r requirements.txt)
* Run the flask server(python app.py)
* To run functional test script open a new terminal with environment and run functional_test.py (python functional_test.py)
## Api's 
1 user get and post api -> '/api/users'
1a get method to get all users
1b post method to add data into users
1c sample data {"userName":"user 1","email":"user1@gamil.com","password":"123456"}

2 users get call by userid -> '/api/users/<int:id>'

3 users login call -> "/api/login"
3a post method and sampledata is {"email":"user1@gamil.com","password":"123456"}

4 groups get and post call-> '/api/groups'
4a get method to get all groups
4b post method to add data into groups
4c sample data {"name":"first Group","createdBy":2} createdBy is userid

5 groups get call by is -> '/api/groups/<int:id>' id is group id

6 groupmembers post call "/api/groupmembers"
6a sample data {"userId":2,"groupId":1,"isAdmin":0}

7 get call to get groupmembers by group id '/api/groupmembers/<int:id>'


8 Messages get all and post api-> '/api/messages'
8a get method to get all messages
8b post method to add data into messages
8c sample data {"userId":2,"groupId":2,"message":"sample1"}

9 get api to get message by group id -> '/api/groupmessages/<int:id>'

10 put to updates likes for a message by message id ->'/api/updatelikes/<int:id>' id is message id
10a sample data is {"userLikes":1} here 1 is userID



## Docker
* install docker in your system 
* after cloning the repository go to first riktamtech_test directory
* Now run command sudo docker-compose build
* After that sudo docker-compose up
* now the server is running 
* To run functional test script open a new terminal with environment and run functional_test.py (python functional_test.py)
