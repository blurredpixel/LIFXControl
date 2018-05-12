import LFXControl as LFX
from appJar import gui







app=gui("LFX Controller","800x600")

app.addLabelEntry("Token:")

def launchWin(win):
    app.showSubWindow(win)

def debug(button):
    token=app.getEntry("Token:")
    light = LFX.LIFXController(token)
    
    if(button=="listbox"):
        print(light.getLightPowerState(app.getListBox("labels")[0]))
    if(button=="light_edit"):
        app.startSubWindow("light_edit",modal=True)
        app.addRadioButton("power","on")
        app.addRadioButton("power","off")
        if(light.getLightPowerState(app.getListBox("labels")[0])==True):
            app.setRadioButton("power","off",callFunction=False)
        
        app.stopSubWindow()
        app.showSubWindow("light_edit")

    else:
        app.addListBox("labels",light.getLightLabels())
        print(light.printLightInfoDebug())
    
        
    


app.addButtons(["Connect","listbox"],debug)
app.addButton("light_edit",debug)




app.go()



