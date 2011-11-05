from bluetooth import discover_devices
from pymongo import Connection

class BluePresence():
    
    def __init__(self):
        self.conn = Connection("localhost")
        self.db = self.conn.blue_users

    def set_user(self, name, mac, fullname):
        self.db.users.save({ "name": name, "mac": mac, "fullname": fullname })
        
    def find_user(self, mac):
        ''' Look for a user in db.'''
        self.db.users.find_one( { "mac": mac } )

#discover_devices(lookup_names = True)
