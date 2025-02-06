from res.helpers.config import getSetting ,Settings
class BaseController :
    
    def __init__(self):
         self.app_setting = getSetting()


