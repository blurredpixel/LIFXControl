
import requests 
import json

class LIFXController():
    

     

    def __init__(self,token):
        def getHeaders(self):
            

            headers = {
                "Authorization": "Bearer %s" % token,
            }

            return headers
        self.response= requests.get('https://api.lifx.com/v1/lights/all', headers=getHeaders(self))
        
    
        


    def printAPI(self,r):
        print(r)


    def getJSON(self):
        data=json.loads(self.response.text)
        #print(data)
        return data

    #debug method
    def printPowerState(self):
        data=LIFXController.getJSON(self)
        
            
        for i in range(len(data)):
            print("Label: "+data[i]['label']+" "+ "Power: "+data[i]['power'])
            



        
    def getLightIDs(self):
        data=LIFXController.getJSON(self)
        ids=[]
        for i in range(len(data)):
            
            ids.append(data[i]['id'])

        return ids

    def getLightLabels(self):
        data=LIFXController.getJSON(self)
        info=[]

        for i in range(len(data)):
            info.append(data[i]['label'])
        
        return info

    def getLightsInfo(self):
        data=LIFXController.getJSON(self)

        info=[]

        for i in range(len(data)):
            print("ID: "+data[i]['id'])
            print("Label: "+data[i]['label'])
            print("Power: "+data[i]['power'])
            info.append(data[i]['id'])
            info.append(data[i]['label'])
            info.append(data[i]['power'])
        return info

    def printLightInfoDebug(self):
        data=LIFXController.getJSON(self)
        for i in range(len(data)):
            print("ID: "+data[i]['id'])
            print("Label: "+data[i]['label'])
            print("Power: "+data[i]['power'])

    