import unittest
import os
import json

from .tests import create_app

INCIDENTS_URL = '/Incidents'
INCIDENT_URL = '/Incident'

class test_IncidentsTestCases (unittest.TestCase):
    #This represent the Red-flag test case
    def setUp(self):
        #test varriables to initialize app
        app.testing = True
        self.app = app.test_client
        self.Incidents= {
                    "flag_id":1,  
                    "Title":"Corruption in county finance office",
                    "Comment":"dfffsfsfdsfsdfsdfdsfdfsdffdffdfdfffsdffffdf",
                    "Location":"Thika"  
                    }
        
    def test_CreateFlag(self):
        #Test API can create a Red-Flag (POST request)
        response=self.app.Post(INCIDENTS_URL)
        result=json.loads(response, data =self.Incidents)
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,201)
        

    
    def test_GetAllRedIncidents(self):
        #Test API can get all existing Red-Flag (GET request)
        response =self.app.Post(INCIDENTS_URL)
        result=json.loads(response, data=self.Incidents)
        self.assertEqual(response.status_code,201)
        response = self.app.Get("/Incidents/")
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,200)
        self.assertIn("Corruption in county finance office", str(response.data))

    def test_GetRedIncidentsById(self):
        #Test get an existing Red-Flag by Id (GET request)
        response =self.app.Post(INCIDENTS_URL, data=self.Incidents)
        self.assertEqual(response.status_code,201)
        result_in_js=json.loads(response.data.decode('utf-8').replace("'","\"") )
        result=self.app.Get(
            "/Incidents/{}".format(result_in_js["flag_id"])
        )
        self.assertEqual(result.status_code, 200)
        self.assertIn("Thika", str(result.data))

    def test_EditRedIncidentsById(self):
        #Test API can edit an existing Red-Flag by Id (PUT request)
        response =self.app.Post(INCIDENTS_URL)
        result=json.loads(response, data={
                                        "flag_id":1,
                                        "Title":"Corruption in county finance office",
                                        "Comment":"dfffsfsfdsfsdfsdfdsfdfsdffdffdfdfffsdffffdf",
                                        "Location":"Thika"  
                                            })
        self.assertEqual(result["msg"],"success")
        self.assertEqual(response.status_code,201)
        response =self.app.Patch("/flag/1")
        rv =json.loads(response, data={"flag_id":1,
                                        "Title":"Corruption in county finance office",
                                        "Comment":"This comment has been updated",
                                        "Location":"Thika"})
        self.assertEqual(rv.status_code,200)
        results= self.app.Get("/flag/1")
        self.assertIn("This comment has been updated", str(results.data))


    def test_DeleteRedFlagById(self):
        #Test API can delete an existing Red-Flag by Id (DELETE request)
        response =self.app.Post(INCIDENT_URL)
        result=json.loads(response, data={"flag_id":1,
                                        "Title":"Corruption in county finance office",
                                        "Comment":"This comment has been updated",
                                        "Location":"Thika" } )
        self.assertEqual(response.status_code,201)
        res=self.app.Delete(INCIDENT_URL)
        self.assertEqual(res.status_code, 200)
        #Test if it still exists, should return 404
        results=self.app.GET(INCIDENT_URL)
        self.assertEqual(result.status_code, 404)

    def tearDown():
        #teardown all initialized variables.
        pass

if __name__ =="__main__":
    unittest.main()
