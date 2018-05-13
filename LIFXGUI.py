import LFXControl as LFX
from appJar import gui

#disabled appjar icon to show custom icon
app = gui("LFX Controller", "800x600",showIcon=False)
app.setTransparency(90)
#ICON CREDIT: Light by Numero Uno from the Noun Project
app.setIcon("LIFXGUI.gif")

app.addLabelEntry("Token:")
# handles posting of changed parameters for lights

#known bug: if you click on the x instead of the Exit button
#and then edit another light, it will throw a duplicate widget
#exception. destroying the subwindow allow it to re-create the
#widget each time you click the edit_light button. This might 
#impact performance? 
def editLight(button):
    token = app.getEntry("Token:")
    light = LFX.LIFXController(token)
    #calls method to toggle power
    light.togglePower(token, app.getListBox("labels")[
                      0], app.getRadioButton("power"))
    #calls method to change brightness from controller class
    light.changeBrightness(token, app.getListBox(
        "labels")[0], app.getScale("brightness"))
    #calls method to change color based on option box in subwindow
    light.changeColor(token,app.getListBox("labels")[0],app.getOptionBox("Colors"))
                      
    

    # this was added to make sure a duplicate widget exception won't be thrown
    if(button == "Exit"):
        app.destroySubWindow("light_edit")


def launchWin(win):
    app.showSubWindow(win)


def debug(button):
    token = app.getEntry("Token:")
    light = LFX.LIFXController(token)

    if(button == "light_edit"):
        app.startSubWindow("light_edit", modal=True)
        app.addRadioButton("power", "on")
        app.addRadioButton("power", "off")
        # if the light is on set the only available option to off
        if(light.getLightPowerState(app.getListBox("labels")[0]) == True):
            app.setRadioButton("power", "off", callFunction=False)
        # adds brightness select slider
        app.addScale("brightness")
        app.setScaleRange("brightness", 0.0, 1.0,
                          light.getBrightness(app.getListBox("labels")[0]))

        app.addLabelOptionBox("Colors",["white","red","orange","yellow","cyan","green","blue","purple","pink"])
        
        #buttons for edit window
        app.addButtons(["Submit Changes", "Exit"], editLight)
        app.stopSubWindow()
        app.showSubWindow("light_edit")

    else:
        app.addListBox("labels", light.getLightLabels())
        print(light.printLightInfoDebug())


app.addButton("Connect", debug)
app.addButton("light_edit", debug)


app.go()
