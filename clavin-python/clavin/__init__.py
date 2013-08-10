import requests 




class Clavin:

    def __init__(self, server):
        self.server = server  

    #def connect(self, server):
    #    self.server = server 
    #    # connect to web server, should return basic metadata to verify it is working 


    def resolve(self, document):
	headers = {'content-type': 'text/plain'}
        r = requests.post(self.server, data=document, headers=headers)
        return r.json() 


 
