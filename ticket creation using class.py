import requests
import json

class Incident:
    api_url="https://dev64700.service-now.com/api/now/table/incident"
    
    headers={"Accept":"application/json","content-type":"application/json"}
    
    descrip={"description":"money detected","short_description":"ticket creation testing from service now api"}
    
    def __init__(self,user,pswd):
        self.user=user
        self.pswd=pswd
        
    def note(self):
        response=requests.post(self.api_url,auth=(self.user,self.pswd),headers=self.headers,data=json.dumps(self.descrip))
        
        print(response.json())
    
x=Incident("admin","1YWcL!%1Vjkv")
x.note()
    
    