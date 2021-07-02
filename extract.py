#!/usr/bin/env python3
# extract.py
# Extract user screen dimensions and title of Chrome & Terminal apps.
import subprocess, sys, os
import platform

# check platform
if platform.system() == 'Darwin':
	from AppKit import NSScreen # get native resolution

	# grab width and height for user
	width = int(NSScreen.mainScreen().frame().size.width)
	height = int(NSScreen.mainScreen().frame().size.height)

	with open('applicationName.txt', 'r') as file:
		applicationName = file.read().replace('\n', '')

		print(sys.argv)

		# dual option selected through argument change
		if str(sys.argv[1]) == "dual":
			# TODO: Figure out a better way to organize prerequisites
			applescript = '''\
			tell application "{application}"
				set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
			end tell
			tell application "Terminal"
				set bounds of front window to {{{leftPos_terminal}, 0, {W_terminal}, {H_terminal}}}
			end tell\
			'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height))

			# parse and stdout
			args = [item for x in [("-e",l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
			proc = subprocess.Popen(["osascript"] + args ,stdout=subprocess.PIPE )
			progname = proc.stdout.read().strip()
			sys.stdout.write(str(progname))

		# tripend option selected through argument change
		elif str(sys.argv[1]) == "trisnap":
			# TODO: Figure out a better way to organize prerequisites
			applescript = '''\
			tell application "{application}"
				set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
			end tell
			tell application "Terminal"
				set bounds of front window to {{{leftPos_terminal}, 0, {W_terminal}, {H_terminal}}}
			end tell\
			'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height//2))

			# parse and stdout
			args = [item for x in [("-e",l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
			proc = subprocess.Popen(["osascript"] + args ,stdout=subprocess.PIPE )
			progname = proc.stdout.read().strip()
			sys.stdout.write(str(progname))

elif platform.system() == 'Windows':
	import ctypes
	ctypes.windll.user32.MessageBoxW(0, "Error", "Please use Mac for snapgrid. Do not attempt to run on Windows or Linux.", 0)

elif platform.system() == 'Linux':
	from tkinter import messagebox as tkMessageBox
	tkMessageBox.showerror('Error', 'Please use Mac for snapgrid. We are not cross-platform.. even for Linux.')

else:
	from tkinter import messagebox as tkMessageBox
	tkMessageBox.showerror('Error', 'Please use Mac for snapgrid. We are not cross-platform.')
