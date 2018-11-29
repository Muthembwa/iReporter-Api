import unittest
import os
import json
from .app import create_app

class RedFlagTestCases (unittest.TestCase):
    #This represent the Red-flag test case
    def setUp(self):
        #test varriables to initialize app
        app.testing = True
        self.app = app.test_client
        
    def test_CreateFlag(self):
        #Test API can create a Red-Flag (POST request)
        response=self.app.POST("/flags")
        result=json.loads(response, data)
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,200)
        

    
    def test_GetAllRedFlags(self):
        #Test API can get all existing Red-Flag (GET request)
        response =self.app.GET("/flags")
        result=json.loads(response, data)
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,200)

    def test_GetRedFlagsById(self):
        #Test get an existing Red-Flag by Id (GET request)
        response =self.app.GET("/flags/flag_id")
        result=json.loads(response, data)
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,200)
        

    def test_EditRedFlagsById(self):
        #Test API can edit an existing Red-Flag by Id (PUT request)
        response =self.app.PATCH("/flags/flag_id")
        result=json.loads(response, data)
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,200)

    def test_DeleteRedFlagById(self):
        #Test API can delete an existing Red-Flag by Id (DELETE request)
        response =self.app.DELETE("/flags/flag_id")
        result=json.loads(response, data)
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,200)

    def tearDown():
        #teardown all initialized variables.
        pass

if __name__ =="__main__":
    unittest.main()