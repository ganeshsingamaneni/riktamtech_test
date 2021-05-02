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
import time



def delete_data():
    try:
        print("Deleting Previous Data...")
        delmessages = db.session.query(Messages).delete()
        delgrpmembers = db.session.query(GroupMembers).delete()
        delgroups = db.session.query(Groups).delete()
        deluser = db.session.query(Users).delete()
        db.session.commit()
        time.sleep(2)
        print("Successfully Deleted Previous Data")
        return True
    except Exception as e:
        print(str(e))
        return False    

def add_users():
    try:
        print("                        ")
        print("***************************")
        print("Adding Users ....")
        print("***************************")
        userdata = [{"userName":"user 1","email":"user1@gmail.com","password":"123456"},{"userName":"user 2","email":"user2@gmail.com","password":"123456"},{"userName":"user 3","email":"user3@caratred.com","password":"123456"},{"userName":"user 4","email":"user4@gmail.com","password":"123456"},{"userName":"user 5","email":"user5@gmail.com","password":"123456"},{"userName":"user 6","email":"user6@caratred.com","password":"123456"},{"userName":"user 7","email":"user7@caratred.com","password":"123456"},{"userName":"user 8","email":"user8@caratred.com","password":"123456"}]
        for each in userdata:
            print("         ")
            each['password'] = generate_password_hash(
                        each['password'])
            # print("user  : ",each)
            schema = AddUserSchema()
            new_user_obj = schema.load(
                each, session=db.session).data
            db.session.add(new_user_obj)
            db.session.commit()
            print(each['userName'],"        Added")
            time.sleep(1)
        obj = Users.query.order_by(Users.id).all()
        if obj:
            schema = UsersSchema(many=True)
            data = schema.dump(obj).data  
        print("     ")
        print("Successfully Added Users")      
        return {"success":True,"data":data}
    except Exception as e:
        print(str(e)) 
        return {"success":False}   

def add_groups(inputdata):
    try:
        print("     ")
        print("***************************")
        print("Adding Groups ....")
        print("***************************")
        userdata = [{"name":"First Group","createdBy":1},{"name":"Second Group","createdBy":2}]
        for each in userdata:
            print("     ")
            schema = AddGroupschema()
            new_Group_obj = schema.load(
                each, session=db.session).data
            db.session.add(new_Group_obj)
            db.session.commit()
            data = schema.dump(new_Group_obj).data
            memschema = AddGroupMemberschema()
            membdata = {"groupId":data['id'],"userId":each['createdBy'],"isAdmin":1}
            new_GroupMem_obj = memschema.load(
                membdata, session=db.session).data
            db.session.add(new_GroupMem_obj)
            db.session.commit()
            print(each['name'],"       Added")
            time.sleep(1)
        obj = Groups.query.order_by(Groups.id).all()
        if obj:
            schema = GroupsSchema(many=True)
            data = schema.dump(obj).data   
        print("     ")
        print("Successfully Created Groups")      
        return {"success":True,"data":data}
    except Exception as e:
        print(str(e)) 
        return {"success":False}   

def add_group_members(inputdata):
    try:
        print("     ")
        print("***************************")
        print("Adding Group Members...")
        print("***************************")
        userdata = [{"userId":2,"groupId":1,"isAdmin":0},{"userId":3,"groupId":1,"isAdmin":0},{"userId":5,"groupId":1,"isAdmin":0},{"userId":7,"groupId":1,"isAdmin":0},{"userId":1,"groupId":2,"isAdmin":0},{"userId":4,"groupId":2,"isAdmin":0}]
        for each in userdata:
            memschema = AddGroupMemberschema()
            new_GroupMem_obj = memschema.load(
                each, session=db.session).data
            db.session.add(new_GroupMem_obj)
            db.session.commit()
            print("     ")
            if each['groupId'] == 1:
                group = "First Group" 
            else:
                group = "Second Group"    
            print("User "+str(each['userId'])+" Added to "+group)
            time.sleep(1)
        obj = GroupMembers.query.order_by(GroupMembers.id).all()
        if obj:
            schema = AddGroupMemberschema(many=True)
            data = schema.dump(obj).data
        print("     ")
        print("Successfully Added  Users in Groups")        
        return {"success":True,"data":data}
    except Exception as e:
        print(str(e)) 
        return {"success":False}  

# def userlogin():
# socketio.emit('CallWaiterResponse', {"tableName":tableName,"uniqueId":get['uniqueId']}, get['data'])
# socketio.emit('CallWaiterReqBlock', json['tableId'])

def add_messages():
    try:
        print("     ")
        print("***************************")
        print("Messages in First group...")
        print("***************************")
        userdata = [{"userId":1,"groupId":1,"message":"Hi Buddies...","type":"message"},{"userId":7,"groupId":1,"message":"Hi Bro..","type":"message"},{"userId":1,"groupId":1,"message":"what plans for today?","type":"message"},{"userId":3,"groupId":1,"message":"Stay home & stay safe","type":"message"},{"userLikes":5,"type":"like","message":4},{"userLikes":7,"type":"like","message":4},{"userId":5,"groupId":1,"message":"That's cool!!","type":"message"}]
        for each in userdata:
            print("     ")
            if each["type"] == "message":
                del each['type']
                memschema = AddMessageschema()
                new_GroupMem_obj = memschema.load(
                    each, session=db.session).data
                db.session.add(new_GroupMem_obj)
                db.session.commit()
                print("Message from user "+str(each['userId'])+"  : "+each['message'])
                time.sleep(2)
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
                    print("user "+str(each['userLikes'])+" Likes "+"user "+str(obj.userId)+" message "+obj.message)
                    time.sleep(2)
        # obj = GroupMembers.query.order_by(GroupMembers.id).all()
        # if obj:
        #     schema = AddMessageschema(many=True)
        #     data = schema.dump(obj).data    
        return {"success":True,"data":'data'}
    except Exception as e:
        print(str(e)) 
        return {"success":False}

def add_messages2():
    try:
        print("     ")
        print("***************************")
        print("Messages in Second group...")
        print("***************************")
        userdata = [{"userId":2,"groupId":2,"message":"Hello everyone","type":"message"},{"userId":4,"groupId":2,"message":"Hi ","type":"message"},{"userId":2,"groupId":2,"message":"Any Web series Suggestions..?","type":"message"},{"userId":1,"groupId":2,"message":"Person of Interest In Prime Video","type":"message"},{"userLikes":2,"type":"like","message":9},{"userLikes":4,"type":"like","message":9},{"userId":2,"groupId":2,"message":"That's good and Bye.","type":"message"}]
        for each in userdata:
            print("     ")
            if each["type"] == "message":
                del each['type']
                memschema = AddMessageschema()
                new_GroupMem_obj = memschema.load(
                    each, session=db.session).data
                db.session.add(new_GroupMem_obj)
                db.session.commit()
                print("Message from user "+str(each['userId'])+"  : "+each['message'])
                time.sleep(2)
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
                    print("user "+str(each['userLikes'])+" Likes "+"user "+str(obj.userId)+" message "+obj.message)
                    time.sleep(2)
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
        res = requests.get('http://'+host+':'+str(port)+'/')
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
                                addmessages2 = add_messages2()
                                if addmessages2['success'] == True:
                                    print("       ")
                                    print("Successfully completed functional testing")
                                    return "Successfully completed functional testing"
                                else:
                                    print("Failed to complete functional testing in message2")   
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



