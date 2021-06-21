#!/usr/bin/env python3
# DICT -> Returns wrappers for big NS classes that I hate writing out
import rumps
import subprocess, sys, os
from AppKit import NSWorkspace, NSAttributedString
from PyObjCTools.Conversion import propertyListFromPythonCollection
from Cocoa import (NSFont, NSFontAttributeName, NSColor, NSForegroundColorAttributeName)

# DEFINE

# font
BIG_SYSTEM = NSFont.fontWithName_size_("Helvetica Neue Bold", 16.0)
BIG_MONO = NSFont.fontWithName_size_("Monaco", 16.0)

SMALL_SYSTEM = NSFont.fontWithName_size_("Helvetica Neue Bold", 13.0)
SMALL_MONO = NSFont.fontWithName_size_("Monaco", 13.0)

# color
RED = NSColor.redColor() # r
ORANGE = NSColor.orangeColor() # o
YELLOW = NSColor.yellowColor() # y

GREEN = NSColor.greenColor() # g

BLUE = NSColor.blueColor() # b

# i & v are dumb, so:

BLACK = NSColor.blackColor()
WHITE = NSColor.colorWithCalibratedRed_green_blue_alpha_(1, 1, 1, 1)

class Font(object):
	def __init__(self):
		self.BIG_SYSTEM = BIG_SYSTEM
		self.BIG_MONO = BIG_MONO
		self.SMALL_SYSTEM = SMALL_SYSTEM
		self.SMALL_MONO = SMALL_MONO

class Color(object):
	def __init__(self):
		self.RED = RED
		self.ORANGE = ORANGE
		self.YELLOW = YELLOW
		self.GREEN = GREEN
		self.BLUE = BLUE

		self.BLACK = BLACK
		self.WHITE = WHITE
