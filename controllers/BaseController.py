from res.helpers.config import getSetting ,Settings
import os
import random
import string

class BaseController :
    
    def __init__(self):
         self.app_setting = getSetting()
               #    parent of current file           current file
         self.base_dir = os.path.dirname( os.path.dirname(__file__) )
         self.files_dir = os.path.join(
            self.base_dir,
            "assets/Files"
            )

    def generate_random_string(self, length: int=12):
            return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))