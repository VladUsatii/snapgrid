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

# ACCESSORIES DICT
from dict import Font, Color
font = Font()
color = Color()

#TODO: learn why Cocoa's wrappers require a dictionary
"""
Dictionary of Attributes:

propListFromPyCollec used to make NSDictionary from lambda for converted style class

"""

# "Open Apps" title class
attributes = propertyListFromPythonCollection({
	NSFontAttributeName: font.BIG_SYSTEM,
	NSForegroundColorAttributeName: color.WHITE},
	conversionHelper=lambda x: x)
## "Open Apps" description class
attributesDesc = propertyListFromPythonCollection({
	NSFontAttributeName: font.SMALL_SYSTEM,
	NSForegroundColorAttributeName: color.WHITE},
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

@rumps.clicked("Quit Snapgrid")
def quit(_):
	rumps.quit_application()


# header
string = NSAttributedString.alloc().initWithString_attributes_("Open Apps 🚦", attributes)
menu_item = rumps.MenuItem("")
menu_item._menuitem.setAttributedTitle_(string)
menu = [menu_item]

# description of header
stringDesc = NSAttributedString.alloc().initWithString_attributes_("Click the app you want to snap Terminal with.", attributesDesc)
menu_itemDesc = rumps.MenuItem("")
menu_itemDesc._menuitem.setAttributedTitle_(stringDesc)

menu.append(menu_itemDesc)


def searchForItem(x):
	pass

# all open apps
for x in appsDict:
	if x[0] == "Finder" or x[0] == "Terminal":
		continue # don't show finder or terminal
	else:
		new_menu_item = rumps.MenuItem(str("" + x[0]), callback=searchForItem(x[1])) # 3 spaces
		menu.append(new_menu_item)

menu.append(None)

# update quit button
def quit():
	rumps.quit_application()
quit = rumps.MenuItem("Quit Snapgrid", callback=lambda: quit(), key="Q")
menu.append(quit)

# init
app = rumps.App("Snapgrid", title=None, icon="snapgridLogo.png", template=None, menu=menu, quit_button=None)
app.run()
