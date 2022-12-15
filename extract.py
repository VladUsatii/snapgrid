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
		# parse and stdout
		def parse(applescript):
			try:
				args = [item for x in [("-e",l.strip()) for l in applescript.split('\n') if l.strip() != ''] for item in x]
				proc = subprocess.Popen(["osascript"] + args , stdout=subprocess.PIPE)
				progname = proc.stdout.read().strip()
				sys.stdout.write(str(progname))
			except Error as error:
				print(f'error: {err}'.format(err=error))

		# read open application name
		applicationName = file.read().replace('\n', '')

		# dual option selected through argument change
		if str(sys.argv[1]) == "mono":
			num_of_terminals = int(subprocess.check_output("bash openterminals.sh", shell=True))
			if num_of_terminals == 1:
				mono_applescript = '''\
				tell application "Terminal" to activate
					tell application "System Events" to keystroke "t" using command down
						repeat while contents of selected tab of window 1 starts with linefeed
						delay 0.01
					end repeat
					do script "" in front window
					activate
					set bounds of front window to {{0, 0, {W_terminal}, {H_terminal}}}
				end tell\
				'''.format(W_terminal=str(width), H_terminal=str(height))

				#		tell application "Terminal"
				#					activate
				#					tell window 1 of application
				#					do script " "
				#					activate
				#					set bounds of front window to {{0, 0, {W_terminal}, {H_terminal}}}
				#					windows where name contains "bash"
				#					if result is not {{}} then set index of item 1 of result to 1
				#				end tell\

			else:
				mono_applescript = '''\
				tell application "Terminal"
					activate
					set bounds of front window to {{0, 0, {W_terminal}, {H_terminal}}}
				end tell\
				'''.format(W_terminal=str(width), H_terminal=str(height))

			parse(mono_applescript)

		elif str(sys.argv[1]) == "dual":
			try:
				num_of_terminals = int(subprocess.check_output("bash openterminals.sh", shell=True))
			except ValueError:
				num_of_terminals = 2
			if num_of_terminals == 2:
				dual_applescript = '''\
				tell application "{application}"
					set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
				end tell
				tell application "Terminal"
					set bounds of front window to {{{leftPos_terminal}, 0, {W_terminal}, {H_terminal}}}
				end tell\
				'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height))
			elif num_of_terminals == 1:
				dual_applescript = '''\
				tell application "{application}"
					set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
				end tell
				tell application "Terminal"
					activate
					do script " "
					activate
					set bounds of front window to {{{leftPos_terminal}, 0, {W_terminal}, {H_terminal}}}
				end tell\
				'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height))
			else:
				dual_applescript = '''\
				tell application "{application}"
					set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
				end tell
				tell application "Terminal"
					set bounds of front window to {{{leftPos_terminal}, 0, {W_terminal}, {H_terminal}}}
				end tell\
				'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height))

			parse(dual_applescript)

		# tripend option selected through argument change
		elif str(sys.argv[1]) == "trisnap":
			try:
				num_of_terminals = int(subprocess.check_output("bash openterminals.sh", shell=True))
			except ValueError:
				num_of_terminals = 2
			num_of_terminals = 2
			if num_of_terminals == 2:
				trisnap_applescript = '''\
				tell application "{application}"
					set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
				end tell
				tell application "Terminal"
					set bounds of front window to {{{leftPos_terminal}, 0, {W_terminal}, {H_terminal}}}
					do script " "
					activate
					set bounds of front window to {{{leftPos_terminal}, {H_terminal}, {W_terminal}, {H_terminal2}}}
				end tell\
				'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height//2), H_terminal2=str(height))
			elif num_of_terminals == 1:
				trisnap_applescript = '''\
				tell application "{application}"
					set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
				end tell
				tell application "Terminal"
					activate
					do script " "
					activate
					set bounds of front window to {{{leftPos_terminal}, 0, {W_terminal}, {H_terminal}}}
				end tell
				tell application "Terminal"
					activate
					do script " "
					activate
					set bounds of front window to {{{leftPos_terminal}, {H_terminal}, {W_terminal}, {H_terminal2}}}
				end tell\
				'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height//2), H_terminal2=str(height))
			else:
				trisnap_applescript = '''\
				tell application "{application}"
					set bounds of front window to {{0, 0, {W_chrome}, {H_chrome}}}
				end tell
				tell application "System Events" to tell process "Terminal"
					tell window 1
						set position to {{{leftPos_terminal}, 0}}
						set size to {{{W_terminal}, {H_terminal}}}
					end tell
					tell window 2
						set position to {{{leftPos_terminal}, {H_terminal}}}
						set size to {{{leftPos_terminal}, {H_terminal}}}
					end tell
				end tell\
				'''.format(application=str(applicationName), W_chrome=str((width//2) - 1), H_chrome=str(height), leftPos_terminal=str(width//2), W_terminal=str(((width//2) - 1) + (width//2)), H_terminal=str(height//2))

			parse(trisnap_applescript)

elif platform.system() == 'Windows':
	import ctypes
	ctypes.windll.user32.MessageBoxW(0, "Error", "Please use Mac for snapgrid. Do not attempt to run on Windows or Linux.", 0)

elif platform.system() == 'Linux':
	from tkinter import messagebox as tkMessageBox
	tkMessageBox.showerror('Error', 'Please use Mac for snapgrid. We are not cross-platform.. even for Linux.')

else:
	from tkinter import messagebox as tkMessageBox
	tkMessageBox.showerror('Error', 'Please use Mac for snapgrid. We are not cross-platform.')
