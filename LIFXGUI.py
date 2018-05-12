import LFXControl as LFX
from appJar import gui

#token="c04590e531bd82fa3d56633a1dd4a82b86f58890fa4f367c5d1200e2d232cf4a"





app=gui("LFX Controller","800x600")

app.addLabelEntry("Token:")


def debug(button):
    token=app.getEntry("Token:")
    light = LFX.LIFXController(token)
    print(light.printLightInfoDebug())
    app.addListBox("labels",light.getLightLabels())



app.addButton("Test",debug)





app.go()



