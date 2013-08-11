import requests 




class Clavin:

    def __init__(self, server):
        self.server = server  

    def resolve(self, document):
        headers = {'content-type': 'text/plain'}
        r = requests.post(self.server, data=document, headers=headers)
        return r.json() 


 
