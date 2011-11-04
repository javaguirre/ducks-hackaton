import sys, requests, json

class DuckClientApi():
    
    def __init__(self, apikey, endpoint):
        self.apikey = apikey
        self.endpoint = endpoint
    
    def send(self, data):
        requests.settings.verbose = sys.stderr
        req = requests.post("https://push.ducksboard.com/values/%s/" % self.endpoint, 
                            auth = (self.apikey, 'ignored'), 
                            headers = {'Content-Type': 'application/json'},
                            data = json.dumps(data),
                            timeout = 5)
        print req.status_code
        print req.content

