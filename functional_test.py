import requests
from config import *
from app import *
from models.users import Users
from models.groups import Groups
from models.group_members import GroupMembers
from models.messages import Messages
from schemas.userschema import *
from schemas.groupschema import *
from schemas.messageschema import *
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import datetime

def test_server():
    res = requests.get('0.0.0.0:5000/')
    if res.status_code == 200:
        return True
    else:
        return False  

def delete_data():
    try:
        delmessages = db.session.query(Messages).delete()
        delgrpmembers = db.session.query(GroupMembers).delete()
        delgroups = db.session.query(Groups).delete()
        deluser = db.session.query(Users).delete()
        db.session.commit()
        return True
    except Exception as e:
        print(str(e))
        return False    

def add_users():
    try:
        print("Adding Users ....")
        userdata = [{"userName":"user 1","email":"user1@gmail.com","password":"123456"},{"userName":"user 2","email":"user2@gmail.com","password":"123456"},{"userName":"user 3","email":"user3@caratred.com","password":"123456"},{"userName":"user 4","email":"user4@gmail.com","password":"123456"},{"userName":"user 5","email":"user5@gmail.com","password":"123456"},{"userName":"user 6","email":"user6@caratred.com","password":"123456"},{"userName":"user 7","email":"user7@caratred.com","password":"123456"},{"userName":"user 8","email":"user8@caratred.com","password":"123456"}]
        for each in userdata:
            
            each['password'] = generate_password_hash(
                        each['password'])
            print("user  : ",each)
            schema = AddUserSchema()
            new_user_obj = schema.load(
                each, session=db.session).data
            db.session.add(new_user_obj)
            db.session.commit()
        obj = Users.query.order_by(Users.id).all()
        if obj:
            schema = UsersSchema(many=True)
            data = schema.dump(obj).data    
        return {"success":True,"data":data}
    except Exception as e:
        print(str(e)) 
        return {"success":False}   

def add_groups(inputdata):
    try:
        print("Adding Groups ....")
        userdata = [{"name":"First Group","createdBy":1},{"name":"Second Group","createdBy":2}]
        for each in userdata:
            schema = AddGroupschema()
            new_Group_obj = schema.load(
                each, session=db.session).data
            db.session.add(new_Group_obj)
            db.session.commit()
        obj = Groups.query.order_by(Groups.id).all()
        if obj:
            schema = GroupsSchema(many=True)
            data = schema.dump(obj).data    
        return {"success":True,"data":data}
    except Exception as e:
        print(str(e)) 
        return {"success":False}   

def add_group_members(inputdata):
    try:
        print("Adding Group Members...")
        userdata = [{"userId":2,"groupId":1,"isAdmin":0},{"userId":3,"groupId":1,"isAdmin":0},{"userId":5,"groupId":1,"isAdmin":0},{"userId":7,"groupId":1,"isAdmin":0},{"userId":1,"groupId":2,"isAdmin":0},{"userId":4,"groupId":2,"isAdmin":0}]
        for each in userdata:
            memschema = AddGroupMemberschema()
            new_GroupMem_obj = memschema.load(
                each, session=db.session).data
            db.session.add(new_GroupMem_obj)
            db.session.commit()
        obj = GroupMembers.query.order_by(GroupMembers.id).all()
        if obj:
            schema = AddGroupMemberschema(many=True)
            data = schema.dump(obj).data    
        return {"success":True,"data":data}
    except Exception as e:
        print(str(e)) 
        return {"success":False}  

# def userlogin():
# socketio.emit('CallWaiterResponse', {"tableName":tableName,"uniqueId":get['uniqueId']}, get['data'])
# socketio.emit('CallWaiterReqBlock', json['tableId'])

def add_messages():
    try:
        print("Adding messages in groups...")
        userdata = [{"userId":1,"groupId":1,"message":"Hi Buddies...","type":"message"},{"userId":7,"groupId":1,"message":"Hi Bro..","type":"message"},{"userId":1,"groupId":1,"message":"what plans for today?","type":"message"},{"userId":3,"groupId":1,"message":"Stay home & stay safe","type":"message"},{"userLikes":5,"type":"like","message":4},{"userLikes":7,"type":"like","message":4},{"userId":5,"groupId":1,"message":"That's cool!!","type":"message"}]
        for each in userdata:
            if each["type"] == "message":
                del each['type']
                memschema = AddMessageschema()
                new_GroupMem_obj = memschema.load(
                    each, session=db.session).data
                db.session.add(new_GroupMem_obj)
                db.session.commit()
            else:
                obj = Messages.query.filter(Messages.id == each['message']).one_or_none()
                if obj is not None:
                    schema = MessagesSchema()
                    data = schema.dump(obj).data
                    if data['userLikes'] is None:
                    
                        userlikes = [each['userLikes']]
                    elif each['userLikes'] in data['userLikes']:
                        return {"success": True, "message": "Already Liked Message"}
                    else:
                        userlikes = data['userLikes']
                        userlikes.append(each['userLikes']) 
                    Messages.query.filter(Messages.id == each['message']).update({"userLikes":userlikes})
                    db.session.commit()

        # obj = GroupMembers.query.order_by(GroupMembers.id).all()
        # if obj:
        #     schema = AddMessageschema(many=True)
        #     data = schema.dump(obj).data    
        return {"success":True,"data":'data'}
    except Exception as e:
        print(str(e)) 
        return {"success":False}  


def functional_test():
    try:
        print(datetime.datetime.now())
        #test server is working or not working
        res = requests.get('http://0.0.0.0:5000/')
        if res.status_code == 200:
            # delete previous data
            deldata = delete_data()
            if deldata == True:
                # add users
                addUsers = add_users()
                if addUsers['success'] == True:
                    addgroups = add_groups(addUsers['data'])
                    if addgroups['success'] == True:
                        addgroupmembers = add_group_members(addgroups['data'])
                        if addgroupmembers['success'] == True:
                            addmessages = add_messages()
                            if addmessages['success'] == True:
                                print("Successfully completed functional testing")
                                return "Successfully completed functional testing"
                            else:
                                print("Failed to complete functional testing in message")
                        else:
                            print("Failed to complete functional testing in group members") 
                    else:
                        print("Failed to complete functional testing in groups")
                else:
                    print("Failed to complete functional testing in users")
            else:
                print("Failed to complete functional testing in delete previous data")
        else:
            print("server down please run the server again")
    except Exception as e:
        print(str(e))                                                   
                    
functional_test()
print(datetime.datetime.now())



