
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
        
    #toggles power of passed in label and state
    def togglePower(self,token,label,state):
        def getHeaders(self):
            

            headers = {
                "Authorization": "Bearer %s" % token,
            }

            return headers
        payload = {
            "power": state,
        }
        #debug methods
        print("Label togglePower: "+label)
        print("Label state togglePower: "+state)
        self.response= requests.put('https://api.lifx.com/v1/lights/label:'+label+'/state',data=payload, headers=getHeaders(self))
        
    def changeBrightness(self,token,label,brightness):
        def getHeaders(self):
            

            headers = {
                "Authorization": "Bearer %s" % token,
            }

            return headers
        payload = {
            "brightness": brightness,
        }
        #debug methods
        #print("Label Changebrightness: "+label)
        #print("Brightness Level : "+ brightness)
        self.response= requests.put('https://api.lifx.com/v1/lights/label:'+label+'/state',data=payload, headers=getHeaders(self))

    #debug method for printing json from api
    def printAPI(self,r):
        print(r)

#returns raw JSON data from light API
    def getJSON(self):
        data=json.loads(self.response.text)
        print(data)
        return data

    #debug method
    def printPowerState(self):
        data=LIFXController.getJSON(self)
        
            
        for i in range(len(data)):
            print("Label: "+data[i]['label']+" "+ "Power: "+data[i]['power'])
            



    #returns a list of light IDs
    def getLightIDs(self):
        data=LIFXController.getJSON(self)
        ids=[]
        for i in range(len(data)):
            
            ids.append(data[i]['id'])

        return ids
    #returns a list of light labels
    def getLightLabels(self):
        data=LIFXController.getJSON(self)
        info=[]

        for i in range(len(data)):
            info.append(data[i]['label'])
        
        return info
    #returns list of lights and basic info. mainly for debug
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

    #takes in a light label and return t/f if light is on or off.
    def getLightPowerState(self,label):
        data=LIFXController.getJSON(self)
        for i in range(len(data)):
            if(data[i]['label']==label):    
                if(data[i]['power']=='on'):
                    return True
                else:
                    return False
    #gets the current brightness of selected by label light
    def getBrightness(self,label):
            data=LIFXController.getJSON(self)
            for i in range(len(data)):
                if(data[i]['label']==label):    
                    return data[i]['brightness']

    #debug method for printing out basic light info
    def printLightInfoDebug(self):
        data=LIFXController.getJSON(self)
        for i in range(len(data)):
            print("ID: "+data[i]['id'])
            print("Label: "+data[i]['label'])
            print("Power: "+data[i]['power'])

    