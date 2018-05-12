import LFXControl as LFX
from appJar import gui







app=gui("LFX Controller","800x600")

app.addLabelEntry("Token:")


def debug(button):
    token=app.getEntry("Token:")
    light = LFX.LIFXController(token)
    print(light.printLightInfoDebug())
    app.addListBox("labels",light.getLightLabels())



app.addButton("Test",debug)





app.go()



