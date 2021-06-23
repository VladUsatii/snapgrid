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
import fileinput

# STYLES DICTIONARY
from dict import Font, Color
font = Font()
color = Color()

"""
Dictionary of Attributes:

propListFromPyCollec used to make NSDictionary from lambda for converted style class

"""

# <title class>
attributes = propertyListFromPythonCollection({
	NSFontAttributeName: font.BIG_SYSTEM,
	NSForegroundColorAttributeName: color.WHITE},
	conversionHelper=lambda x: x)
## <description class>
attributesDesc = propertyListFromPythonCollection({
	NSFontAttributeName: font.SMALL_SYSTEM,
	NSForegroundColorAttributeName: color.WHITE},
	conversionHelper=lambda x: x)

# Configure Portion
appsOpen = [apps["NSApplicationName"] for apps in NSWorkspace.sharedWorkspace().launchedApplications()]
appsOpen_byPath = [apps["NSApplicationPath"] for apps in NSWorkspace.sharedWorkspace().launchedApplications()]
appsDict = [[app, path] for app, path in zip(appsOpen, appsOpen_byPath)]



# This code has to be here for some reason
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


# search and rewrite the current snappable app
def searchForItem(sender):
	with open("applicationName.txt", "w") as f:
		f.write(sender.title)

# all open apps
for x in appsDict:
	if x[0] == "Finder" or x[0] == "Terminal":
		continue # don't show finder or terminal
	else:
		new_menu_item = rumps.MenuItem(str(x[0]), callback=searchForItem) # 3 spaces
		menu.append(new_menu_item)

# divider
menu.append(None)

# header no. 2
string2 = NSAttributedString.alloc().initWithString_attributes_("Open Keybinds ⌨️", attributes)
menu_item2 = rumps.MenuItem("")
menu_item2._menuitem.setAttributedTitle_(string2)

menu.append(menu_item2)

# description of header no. 2
stringDesc2 = NSAttributedString.alloc().initWithString_attributes_("Click the keybind you want to snap with.", attributesDesc)
menu_itemDesc2 = rumps.MenuItem("")
menu_itemDesc2._menuitem.setAttributedTitle_(stringDesc2)

menu.append(menu_itemDesc2)
menu.append("No options available.")
menu.append(None)


# get a list of a few keybinds
def aboutUs():
	subprocess.Popen(["python3", "about.py"], stdout=subprocess.PIPE)

# about button
# about = rumps.MenuItem("About Snapgrid", callback=lambda: aboutUs(), key="A")
about = rumps.MenuItem("About Snapgrid", callback=None, key="A")
menu.append(about)

# update quit button
def quit():
	rumps.quit_application()
quit = rumps.MenuItem("Quit Snapgrid", callback=lambda: quit(), key="Q")
menu.append(quit)

# init
app = rumps.App("Snapgrid", title=None, icon="snapgridLogo.png", template=None, menu=menu, quit_button=None)
app.run()
