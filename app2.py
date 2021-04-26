from config import *
# from controller import distanceCaluclation

from groupsmicroservice.controller import *

api.add_resource(GetAddGroups, '/api/groups')
api.add_resource(GetUpdateGroup,'/api/groups/<int:id>')
api.add_resource(GetGroupMembers,'/api/groupsmembers/<int:id>')
api.add_resource(AddGroupMembers,"/api/groupmembers")
api.add_resource(DeleteGroupMembers,"/api/deletemember")




if __name__=='__main__':
    app.run(host='0.0.0.0')
