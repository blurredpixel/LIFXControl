import LFXControl as LFX
from appJar import gui







app=gui("LFX Controller","800x600")

app.addLabelEntry("Token:")

def launchWin(win):
    app.showSubWindow(win)

def debug(button):
    token=app.getEntry("Token:")
    light = LFX.LIFXController(token)
    print(light.printLightInfoDebug())
    app.addListBox("labels",light.getLightLabels())



app.addButton("Test",debug)
app.addButton("light_edit",launchWin)
app.startSubWindow("light_edit",modal=True)
app.addRadioButton("power","on")
app.addRadioButton("power","off")
app.stopSubWindow()



app.go()



