#!/usr/bin/env python3
# error.py
# Handles all user errors, such as broken binaries
import subprocess

CMD =	'''
		on run argv
			display notification (item 2 of argv) with title (item 1 of argv)
		end run
		'''

# notify user of errors
def notify(title: str, text: str):
	subprocess.call(['osascript', '-e', CMD, title, text])
	print("Error thrown; restart Chrome for Snapgrid to function correctly.")

if sys.argv[1] == 'chromebinaryerror':
	notify("Chrome Broke!", "Please relaunch Chrome for Snapgrid to function correctly.")
