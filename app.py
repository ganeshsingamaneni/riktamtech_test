from config import *
# from controller import distanceCaluclation

from controllers.user_controller import *
from controllers.message_controller import *
from controllers.group_controller import *

api.add_resource(GetAddUsers, '/api/users')
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


# end point

# api.add_resource(distanceCaluclation,'/api/faces')

@app.before_first_request
def create_tables():
    
    db.init_app(app)
    db.create_all()
    db.session.commit()

# socket = socketio   
host = '127.0.0.1'
port = 5000


if __name__=='__main__':
    app.run(host=host,port=port,debug=True)
