
import json

#local imports
from .Base_test import BaseTest

class TestCreateflag(BaseTest):
    def setUp(self):
        #register a test user
        BaseTest.setUp(self)

    def tearDown(self):
        BaseTest.tearDown(self)


    def test_create_a_flag(self):
        '''Test that a user can create an flag of type red-flag or intervention'''
        response = self.client().post('api/v1/red-flags',  data= (self.test_flags))
        self.assertIn('Successful',str(response.data))
        self.assertEqual(response.status_code, 201)
        

    def test_get_all_flags(self):
        '''Test that a user can get all the flags'''
        response = self.client().get('api/v1/red-flags', data=self.test_flags)
        self.assertTrue(response.status_code == 200)

    # def test_get_a_flag(self):
    #     '''Test user can get a specific flag given its id'''
    #     self.client().post('api/v1/red-flag/',  data=(self.test_flags))
    #     response = self.client().get('api/v1/red-flag/1', data=(self.test_flags))
    #     data = json.loads(response.data)
       
                                                


    
    # def test_update_location(self):
    #     self.client().post('api/v1/red-flags/',  data=(self.edit_flag))
    #     response = self.client().patch('api/v1/red-flags/1',  data=(self.edit_flag))
    #     data = json.loads(response.data) 
    #     self.assertEqual(data['message'], 'Updated successfully')
    #     self.assertTrue(response.status_code == 200)

    # def test_update_comment(self):
    #     self.client().post('api/v1/red-flags/',  data=(self.edit_flag))
    #     response = self.client().patch('api/v1/red-flags/1/',  data=(self.edit_flag))
    #     data = json.loads(response.data)
    #     self.assertEqual(data['message'], 'Updated red-flag record’s comment')
    #     self.assertTrue(response.status_code == 200)

    def test_delete_flag(self):
        response = self.client().post('api/v1/red-flags',  data = (self.test_delete))
        response = self.client().delete('api/v1/red-flag/1', data = (self.test_delete))
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Deleted successfully')
        self.assertTrue(response.status_code == 200)

    def test_create_flag_with_empty_username(self):
        response = self.client().post('api/v1/red-flags',  data = (self.invalid_flag_createdby))
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Username cannot be empty')
        self.assertTrue(response.status_code==400)


    def test_create_flag_with_empty_location(self):
        response = self.client().post('api/v1/red-flags',  data = (self.invalid_flag_location))
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Location cannot be empty')
        self.assertTrue(response.status_code==400)

    def test_create_flag_with_empty_comment(self):
        response = self.client().post('api/v1/red-flags',  data = (self.invalid_flag_comment))
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Comment cannot be empty')
        self.assertTrue(response.status_code==400)  

    def tearDown(self):
        """clean Db"""
        self.client=None