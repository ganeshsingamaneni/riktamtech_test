from config import app
from app import *
import unittest

# testdata = {"success": True,"message": "data fetched successfully","data": [{"message": "sample","groupId": 7,"id": 2,"userLikes": None,"userId": 1}]}        
class TestIntegrations(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/api/messages")
        status = response.status_code
        self.assertEqual(status,200)
    def test_index_post(self):
        tester = app.test_client(self)
        response = tester.post("/api/users",json={"userName":"Kiran","email":"kiran@caratred.com","password":"Ganesh55@"})
        status = response.status_code
        self.assertEqual(status,200)    
   
if __name__ == "__main__":
    unittest.main()