#!/usr/bin/env python3
#
# custom.py
# > 1
# GUI implementation to change code for different applications. TL;DR: Snap two screens horizontally of YOUR CHOICE, chosen from a GUI like rumps Objc-Status-Bar-App.
# > 2
# Duplicate/play around with windows and keep the same events.
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

# divider
menu.append(None)

# header no. 3
string3 = NSAttributedString.alloc().initWithString_attributes_("Snap Layout 🧰", attributes)
menu_item3 = rumps.MenuItem("")
menu_item3._menuitem.setAttributedTitle_(string3)

menu.append(menu_item3)

# description of header no. 3
stringDesc3 = NSAttributedString.alloc().initWithString_attributes_("Select the layout you want to snap to.", attributesDesc)
menu_itemDesc3 = rumps.MenuItem("")
menu_itemDesc3._menuitem.setAttributedTitle_(stringDesc3)

menu.append(menu_itemDesc3)


# alter the execute.sh file to dual on click
def mono(sender):
	lines = open("execute.sh").read().splitlines()
	lines[-1] = "python3 extract.py mono"
	open("execute.sh", 'w').write('\n'.join(lines))
	open("execute.sh").close()
	rumps.notification("Mono enabled", "Your keybinds have remained the same", "To change your snap orientation, click another option", data=None, sound=True)

monosnap = rumps.MenuItem("Mono", callback=mono, key='1')

menu.append(monosnap)

# alter the execute.sh file to dual on click
def dual(sender):
	lines = open("execute.sh").read().splitlines()
	lines[-1] = "python3 extract.py dual"
	open("execute.sh", 'w').write('\n'.join(lines))
	open("execute.sh").close()
	rumps.notification("Dual enabled", "Your keybinds have remained the same", "To change your snap orientation, click another option", data=None, sound=True)

dualsnap = rumps.MenuItem("Dual", callback=dual, key='2')

menu.append(dualsnap)

# alter the execute.sh file to tripend on click
def trisnap(sender):
	lines = open("execute.sh").read().splitlines()
	lines[-1] = "python3 extract.py trisnap"
	open("execute.sh", 'w').write('\n'.join(lines))
	open("execute.sh").close()
	rumps.notification("Trisnap enabled", "Your keybinds have remained the same", "To change your snap orientation, click another option", data=None, sound=True)

tripend = rumps.MenuItem("Trisnap", callback=trisnap, key='3')

menu.append(tripend)

# divider
menu.append(None)


# header no. 4
string4 = NSAttributedString.alloc().initWithString_attributes_("Accessibility ⚙️", attributes)
menu_item4 = rumps.MenuItem("")
menu_item4._menuitem.setAttributedTitle_(string4)

menu.append(menu_item4)

# description of header no. 4
stringDesc4 = NSAttributedString.alloc().initWithString_attributes_("Make any changes to events.", attributesDesc)
menu_itemDesc4 = rumps.MenuItem("")
menu_itemDesc4._menuitem.setAttributedTitle_(stringDesc4)

menu.append(menu_itemDesc4)

# alter the execute.sh file to tripend on click
def flipwindows(sender):
	rumps.notification("Flipped your windows", "Your keybinds have remained the same", "To change your snap orientation, click another option", data=None, sound=True)

flipwindows = rumps.MenuItem("Invert windows", callback=flipwindows, key='3')

menu.append(flipwindows)



# divider
menu.append(None)


#TODO:
# get a list of a few keybinds
def aboutUs(sender):
	subprocess.Popen(["chmod", "+x", "about.sh"], stdout=subprocess.PIPE)
	# subprocess.Popen(["python3", "about.py"], stdout=subprocess.PIPE) # not working

# about button
# about = rumps.MenuItem("About Snapgrid", callback=lambda: aboutUs(), key="A")
about = rumps.MenuItem("About Snapgrid", callback=aboutUs, key="A")
menu.append(about)

# update quit button
def quit():
	rumps.quit_application()

quit = rumps.MenuItem("Quit Snapgrid", callback=lambda: quit(), key="Q")
menu.append(quit)

# init
app = rumps.App("Snapgrid", title=None, icon="snapgridLogo.png", template=None, menu=menu, quit_button=None)
app.run()
