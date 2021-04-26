from config import *

from messagemicroservice.controller import *

api.add_resource(GetAddMessages, '/api/messages')
api.add_resource(GetGroupMessages,'/api/groupmessages/<int:id>')
api.add_resource(UpdatemessageLikes,'/api/updatelikes/<int:id>')
# api.add_resource(AddGroupMembers,"/api/groupmembers")
# api.add_resource(DeleteGroupMembers,"/api/deletemember")

print(app)
from test3 import *

if __name__=='__main__':
    app.run(host='0.0.0.0')
