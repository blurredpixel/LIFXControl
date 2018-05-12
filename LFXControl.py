import appJar as app
import requests 
import json


token = "c04590e531bd82fa3d56633a1dd4a82b86f58890fa4f367c5d1200e2d232cf4a"

headers = {
    "Authorization": "Bearer %s" % token,
}

response = requests.get('https://api.lifx.com/v1/lights/all', headers=headers)

def printAPI(r):
    print(r)


def getJSON(r):
    data=json.loads(r.text)
    print(data)
    return data

def printPowerState(r):
    data=getJSON(r)
    
        
    for i in range(len(data)):
        print("Label: "+data[i]['label']+" "+ "Power: "+data[i]['power'])
        



    
def getLightIDs(r):
    data=getJSON(r)
    ids=[]
    for i in range(len(data)):
        
        ids.append(data[i]['id'])

    return ids

def getLightsInfo(r):
    data=getJSON(r)

    for i in range(len(data)):
        print("ID: "+data[i]['id'])
        print("Label: "+data[i]['label'])
        print("Power: "+data[i]['power'])



printAPI(response)
getJSON(response)
printPowerState(response)
getLightsInfo(response)