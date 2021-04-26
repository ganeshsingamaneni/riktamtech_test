from config import *
# from controller import distanceCaluclation

from usersmicroservice.controller import GetAddUsers, GetUpdateUser, Signin

api.add_resource(GetAddUsers, '/api/users')
api.add_resource(GetUpdateUser,'/api/users/<int:id>')
api.add_resource(Signin,"/api/login")
# end point

# api.add_resource(distanceCaluclation,'/api/faces')


@app.before_first_request
def create_tables():
    
    db.init_app(app)
    db.create_all()
    db.session.commit()



if __name__=='__main__':
    app.run(host='0.0.0.0')
