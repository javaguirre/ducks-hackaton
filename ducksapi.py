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
        
    def update_count(self, count):
        #TODO returns True or False if its working
        self.send({"value": count})

    def update_tl(self, title, content, image = None):
        if image:
            data_image = image
        else:
            data_image = "https://dashboard.ducksboard.com/static/img/timeline/green.gif"

        data = { "value": { "title": title, 
                            "image": data_image,
                            "content": content
                }}
        self.send(data)
    

