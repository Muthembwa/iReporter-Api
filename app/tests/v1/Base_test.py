import os, sys
import unittest
from app import create_app

#local imports
from app.api.v1.models import RedFlagModel
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
redFlag = RedFlagModel()

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        self.client = self.app.test_client
       
       
        self.test_flags ={  
            "CreatedBy": "Jacob",
            "CeatedOn": "12/02/2018",
            "Location": "Nairobi",
            "Status": "draft",
            "Comment": "Corruption at county offices"
                    }
        self.edit_flag = {
            "CreatedBy": "Jacob",
            "CeatedOn": "12/02/2018",
            "Location": "Kitui",
            "Status": "pending",
            "Comment": "Corruption at county offices"
                        }
        self.invalid_flag = {
            "CreatedBy": "Jacob",
            "CeatedOn": "draft",
            "Location": "Kitui",
            "Status": "12/02/2018",
            "Comment": ""
                        }
    

    def tearDown(self):
        """clean Db"""
        redFlag.db.clear()
        self.client=None


if __name__ == '__main__':
    unittest.main(verbosity=2)
        