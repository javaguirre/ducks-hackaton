import json, requests
from StringIO import StringIO

class Github():
    '''  With this widget we can watch our favourites projects/developers from github '''
    
    def __init__(self, user, repo, branch):
        self.url = "http://github.com/api/v2/json/"
        self.user = user
        self.repo = repo
        self.branch = branch
    
    def get_commits(self):
        data = requests.get("%scommits/list/%s/%s/%s" % (self.url, self.user, self.repo, self.branch))
        io = StringIO(data.content)
        
        return json.load(io)
        
    def get_issues(self, state, search_term):
        data = requests.get("%sissues/search/%s/%s/%s/%s" % (self.url, self.user, self.repo, state, search_term))
        io = StringIO(data.content)
        
        return json.load(io)
