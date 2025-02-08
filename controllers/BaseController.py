from res.helpers.config import getSetting ,Settings
import os
class BaseController :
    
    def __init__(self):
         self.app_setting = getSetting()
         self.base_dir = os.path.dirname( os.path.dirname(__file__) )
         self.files_dir = os.path.join(
            self.base_dir,
            "assets/files"
            )

