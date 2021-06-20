#!/usr/bin/env python3
#
# custom.py
# GUI implementation to change code for different applications. TL;DR: Snap two screens horizontally of YOUR CHOICE, chosen from a GUI like rumps Objc-Status-Bar-App.
import rumps
import subprocess, sys, os
from AppKit import NSWorkspace, NSAttributedString
from PyObjCTools.Conversion import propertyListFromPythonCollection
from Cocoa import (NSFont, NSFontAttributeName, NSColor, NSForegroundColorAttributeName)
from itertools import chain
from appscript import *

# DEFINE
# font
system = NSFont.fontWithName_size_("Helvetica Neue", 16.0)
# color
black = NSColor.blackColor()
red = NSColor.redColor()
green = NSColor.greenColor()
white = NSColor.colorWithCalibratedRed_green_blue_alpha_(1, 1, 1, 1)

#TODO: learn why Cocoa's wrappers require a dictionary
"""
Dictionary of Attributes:

propListFromPyCollec used to make NSDictionary from lambda for converted style class

"""

# "Open Apps" title class
attributes = propertyListFromPythonCollection({
	NSFontAttributeName: system,
	NSForegroundColorAttributeName: white},
	conversionHelper=lambda x: x)

# "Set Keybinds" title class (TODO)


#
# Configure Portion
#

appsOpen = [apps["NSApplicationName"] for apps in NSWorkspace.sharedWorkspace().launchedApplications()]
appsOpen_byPath = [apps["NSApplicationPath"] for apps in NSWorkspace.sharedWorkspace().launchedApplications()]

appsDict = [[app, path] for app, path in zip(appsOpen, appsOpen_byPath)]

# Open Automator Here


# View Tutorial


# Settings Portion

@rumps.clicked("About Snapgrid")
def about(sender):
	rumps.alert("Snapgrid is an app created to configure the windows and keybinds used in your shortcut code. The shortcut code snaps your first application to the left and the second application to the right.")

@rumps.clicked("Preferences")
def preferences(sender):
	rumps.alert("Nothing here yet.")

@rumps.clicked("Quit Snapgrid")
def quit(_):
	rumps.quit_application()

# header
string = NSAttributedString.alloc().initWithString_attributes_("Open Apps", attributes)
menu_item = rumps.MenuItem("")
menu_item._menuitem.setAttributedTitle_(string)
menu = [menu_item]

def searchForItem(file_to_find):

# all open apps
for x in appsDict:
	new_menu_item = rumps.MenuItem(str(x[0]), callback=searchForItem(x[1]))
	menu.append(new_menu_item)

menu.append(None)


# init
app = rumps.App("Snapgrid", title=None, icon="snapgridLogo.png", template=None, menu=menu, quit_button=None)
app.run()
