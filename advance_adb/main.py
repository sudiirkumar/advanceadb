from adb import Adb
from files import files
from app import app
from misc import Misc
from utilities import utils
from analytics import Analytics
from whatsapp import whatsapp

class Main:
    def __init__(self, device_id=None):
        self.adb = Adb(device_id)
        self.files = files(device_id)
        self.app = app(device_id)
        self.misc = Misc(device_id)
        self.utilities = utils(device_id)
        self.analytics = Analytics(device_id)
        self.wh = whatsapp(device_id)

d = Main()
print(d.analytics.analyse_screen_time())