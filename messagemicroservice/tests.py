from config import app
from unittest import TestCase

testdata = {"success": true,"message": "data fetched successfully","data": [{"message": "sample","groupId": 7,"id": 2,"userLikes": null,"userId": 1}]}        
class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_thing(self):
        response = self.app.get('api/groupmessages/7')
        self.assertEqual(response.json(), testdata)

if __name__ == "__main__":
    unittest.main()