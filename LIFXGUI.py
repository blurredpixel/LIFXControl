import LFXControl as LFX
from appJar import gui







app=gui("LFX Controller","800x600")

app.addLabelEntry("Token:")
#handles posting of changed parameters for lights
def editLight(button):
    token=app.getEntry("Token:")
    light = LFX.LIFXController(token)

    light.togglePower(token,app.getListBox("labels")[0],app.getRadioButton("power"))
    light.changeBrightness(token,app.getListBox("labels")[0],app.getScale("brightness"))
    #this was added to make sure a duplicate widget exception won't be thrown
    if(button=="Exit"):
        app.destroySubWindow("light_edit")

def launchWin(win):
    app.showSubWindow(win)

def debug(button):
    token=app.getEntry("Token:")
    light = LFX.LIFXController(token)
    
    
    
    if(button=="light_edit"):
        app.startSubWindow("light_edit",modal=True)
        app.addRadioButton("power","on")
        app.addRadioButton("power","off")
        #if the light is on set the only available option to off
        if(light.getLightPowerState(app.getListBox("labels")[0])==True):
            app.setRadioButton("power","off",callFunction=False)
        #adds brightness select slider
        app.addScale("brightness")
        app.setScaleRange("brightness",0.0,1.0,light.getBrightness(app.getListBox("labels")[0]))
        app.addButtons(["Submit Changes","Exit"],editLight)
        app.stopSubWindow()
        app.showSubWindow("light_edit")

    else:
        app.addListBox("labels",light.getLightLabels())
        print(light.printLightInfoDebug())
    
        
    


app.addButton("Connect",debug)
app.addButton("light_edit",debug)




app.go()



