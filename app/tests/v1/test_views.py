
import json

#local imports
from .Base_test import BaseTestCase

class TestCreateflag(BaseTestCase):
    def setUp(self):
        #register a test user
        BaseTestCase.setUp(self)

    def tearDown(self):
        BaseTestCase.tearDown(self)


    def test_create_a_flag(self):
        '''Test that a user can create an flag of type red-flag or intervention'''
        response = self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data)
        )
        data = json.loads(response.data)

        self.assertEqual(data['data'][0]['message'], 'Created flag record')
        self.assertTrue(response.status_code == 200)

    def test_get_all_flags(self):
        '''Test that a user can get all the flags'''
        response = self.client.get(
             'api/v1/red-flags/', headers=self.headers
        )
        self.assertTrue(response.status_code == 200)

    def test_get_a_flag(self):
        '''Test user can get a specific flag given its id'''
        self.client.post(
            'api/v1/red-flag/',  data=json.dumps(self.redflag_data)
        )
        response = self.client.get(
             'api/v1/red-flag/1', headers=self.headers
        )
        data = json.loads(response.data)

        self.assertEqual(data['data'][0]['id'], 1)
        self.assertTrue(response.status_code == 200)

    
    def test_update_location(self):

        self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data)
        )
        response = self.client.patch(
             'api/v1/red-flags/1',  data=json.dumps(self.location_data)
        )

        data = json.loads(response.data)
        
        self.assertEqual(data['message'], 'Updated red-flag record’s location')
        self.assertTrue(response.status_code == 200)

    def test_update_comment(self):

        self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data)
        )

        response = self.client.patch(
             'api/v1/red-flags/1/',  data=json.dumps(self.comment_data)
        )
        data = json.loads(response.data)

        self.assertEqual(data['message'], 'Updated red-flag record’s comment')
        self.assertTrue(response.status_code == 200)

    def test_delete_flag(self):
        self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data)
        )
        response = self.client.delete(
             'api/v1/red-flags/1', headers=self.headers)

        data = json.loads(response.data)

        self.assertEqual(data['data'][0]['id'], 1)
        self.assertTrue(response.status_code == 200)

    def test_create_flag_with_empty_username(self):
        response = self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data_with_empty_created)
            )
        data = json.loads(response.data)

        self.assertEqual(data['message'], {'message': 'fields cannot be empty'})
        self.assertTrue(response.status_code==400)
        
    def test_create_flag_with_empty_type(self):
        response = self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data_with_empty_type)
            )
        data = json.loads(response.data)

        self.assertEqual(data['message'], {'message': 'fields cannot be empty'})
        self.assertTrue(response.status_code==400)

    def test_create_flag_with_empty_location(self):
        response = self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data_empty_location)
            )
        data = json.loads(response.data)

        self.assertEqual(data['message'], {'message': 'fields cannot be empty'})
        self.assertTrue(response.status_code==400)

    def test_create_flag_with_empty_comment(self):
        response = self.client.post(
            'api/v1/red-flags/',  data=json.dumps(self.redflag_data_empty_comment)
            )
        data = json.loads(response.data)

        self.assertEqual(data['message'], {'message': 'fields cannot be empty'})
self.assertTrue(response.status_code==400)