from bluetooth import discover_devices
from pymongo import Connection

class BluePresence():
    ''' Save in a mongo db users registered. Then we can match people who has a bluetooth device and check 
        if they are near our host'''
    def __init__(self):
        self.conn = Connection("localhost")
        self.db = self.conn.blue_users

    def set_user(self, name, mac, fullname):
        self.db.users.save({ "name": name, "mac": mac, "fullname": fullname })
        
    def find_user(self, mac):
        ''' Look for a user in db.'''
        return self.db.users.find_one( { "mac": mac } )

    def get_users_list(self):
        #TODO maybe we can search for services in bluetooth devices
        devices = discover_devices(lookup_names = True)
        user_list = []
        
        for device in devices:
            user = self.db.users.find_one( { "mac": device[0] } )
            if user:
                user_list.append(user['fullname'])

        return user_list
