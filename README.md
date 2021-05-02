# riktamtech_test
* clone the repository and create a python3 environvent 
* And chnage directory to riktamtech_test/riktamtech_test and then install all requirements in requirements.txt(pip install -r requirements.txt)
* Run the flask server(python app.py)
* To run functional test script open a new terminal with environment and run functional_test.py (python functional_test.py)
## Api's 
1 user get and post api -> '/api/users'
    1a get method to get all users
    1b post method to add data into users
    1c sample data
api.add_resource(GetUpdateUser,'/api/users/<int:id>')
api.add_resource(Signin,"/api/login")
api.add_resource(ServerTest,"/")

api.add_resource(GetAddGroups, '/api/groups')
api.add_resource(GetGroup,'/api/groups/<int:id>')
api.add_resource(GetGroupMembers,'/api/groupmembers/<int:id>')
api.add_resource(AddGroupMembers,"/api/groupmembers")
api.add_resource(DeleteGroupMembers,"/api/deletemember")

api.add_resource(GetAddMessages, '/api/messages')
api.add_resource(GetGroupMessages,'/api/groupmessages/<int:id>')
api.add_resource(UpdatemessageLikes,'/api/updatelikes/<int:id>')
