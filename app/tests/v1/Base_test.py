import os, sys
import unittest
from app import create_app

#local imports
from app.api.v1.views import RedFlag, RedFlagModel 
from app.api.v1.models import RedFlagModel
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client
       
       
        self.test_flags ={  

            "Id":1,
            "CreatedBy": "Jacob",
            "Location": "Nairobi",
            "Status": "draft",
            "Comment": "Corruption at county offices"
                    }
        self.edit_flag = {
            "Id":2,
            "CreatedBy": "Jacob", 
            "Location": "Kitui",
            "Status": "pending",
            "Comment": "Corruption at county offices"
                        }
        self.invalid_flag_createdby = {
            "Id":3,
            "CreatedBy": "",
            "Location": "Nairobi",
            "Status": "Draft",
            "Comment": "The Comment exists here"
                        }
        self.invalid_flag_comment = {
            "Id":4,
            "CreatedBy": "Jacob",
            "Location": "Kitui",
            "Status": "Draft",
            "Comment": ""
                        }
        self.invalid_flag_location = {
            "Id":5,
            "CreatedBy": "Jacob",
            "Location": "",
            "Status": "Draft",
            "Comment": "The Comment exists here"
                        }
        self.test_delete = {
            "Id":6,
            "CreatedBy": "",
            "Location": "Nairobi",
            "Status": "Draft",
            "Comment": "The Comment exists here"
                        }

    def tearDown(self):
        """clean Db"""
        self.client=None


if __name__ == '__main__':
    unittest.main(verbosity=2)
        