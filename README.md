# snapgrid

A tool for lazy programmers to quickly snap Google Chrome and Terminal to the left and right bounds of their screen for fast and more efficient workflow. This was designed using Python3, osascript (AppleScript), Bash/Shell, and C. This project was made for public recreation and reuse, but not for sale. Please be kind and contribute if you found this tool helpful <3.

## Installation

Firstly, do the following after opening a fresh Terminal screen:

```bash
cd
mkdir Dev
cd Dev
git clone https://github.com/VladUsatii/snapgrid.git
pip install -r requirements.txt
```

Then, ```cmd``` + ```Space``` and find ```Automator.``` Create a new ```Quick Operation,``` and drag in the ```execute.sh``` file. Make sure that the script handler is titled ```Run Shell Script```. If it is, press ```Play``` in the top-right corner (newest version of MacOS), and make sure it runs a check-mark.

![How you should look so far](https://github.com/VladUsatii/snapgrid/blob/main/tutorial_image1.png?raw=true)

Lastly, accept permissions for Automator by opening System Preferences, going to Security, pressing Accessibility, opening the lock with password, and dragging in Finder and Automator as accepted tools. Close the lock, make your Automator keybind, and test out the Automator keybind.

## TODO

- Figure out how to combat Google Chrome interrupted keybinds (cloned keybinds).
- Find a native solution (with no Python or environment variables).
- Learn the tradeoff between plain osascript and a Bash executable linking to osascript.

## Common Issues

#### Keybinds
One of the most common issues is that your keybinds do not work. The keybinds that I chose are: cmd+-, or the command key synchronously with the negative key. If this key doesn't work for you, there are many resources for other, unused keys online.

#### Access Denied
As stated, go to the System Preferences > Security > Accessibility and add Finder and Automator with the '+' buttons. If this doesn't work, try running ```chmod +x exec.sh``` and running from Terminal.

#### Computer Broken/Frozen
Please run this shortcut when Chrome and Terminal are both open. To quickly quit the operation, ```cmd``` + ```Q``` on the app(s), wait a few seconds, and open both up. Test the command. If this doesn't help, restart your computer and don't open up old windows on restart.

#### Run as Administrator
This doesn't happen, unless you run it from Automator. Please run in Automator.

