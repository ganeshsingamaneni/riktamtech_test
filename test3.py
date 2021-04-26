from config import app
import unittest
import flask_unittest
import flask.globals

testdata = {"success": True,"message": "data fetched successfully","data": [{"message": "sample","groupId": 7,"id": 2,"userLikes": None,"userId": 1}]}        
class TestIntegrations(flask_unittest.ClientTestCase):
    def setUp(self):
        print(app)
        self.app = app.test_client()
        self.assertInResponse(app.debug, False)
        # self.app = app.test_client()

    def test_thing(self,client):
        print(app,"/a/a/")
        # self.app = app.test_client(self)
        # response = self.app.get('http://0.0.0.0:5000/api/groupmessages/7')
        # print(response)
        # print(response)
        rv = client.get('/api/groupmessages/7')
        self.assertInResponse(rv,testdata)
if __name__ == "__main__":
    unittest.main()