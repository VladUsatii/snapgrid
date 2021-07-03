# snapgrid

[<img src="logo.png" width="150"/>](https://github.com/VladUsatii/snapgrid/blob/main/logo.png?raw=True)

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

Then, ```cmd``` + ```Space``` and find ```Automator.``` Create a new ```Quick Operation```. Make sure that the script handler is titled ```Run Shell Script```. If it is, type the following in:

```bash
cd Dev/snapgrid && sh execute.sh
```

This tells your computer to change directory to Dev/snapgrid and to run the execute.shell file.

press ```Play``` in the top-right corner (newest version of MacOS), and make sure it runs a check-mark.

![How you should look so far](https://github.com/VladUsatii/snapgrid/blob/main/tutorial_image1.png?raw=true)

Lastly, accept permissions for Automator by opening System Preferences, going to Security, pressing Accessibility, opening the lock with password, and dragging in Finder and Automator as accepted tools. Close the lock, make your Automator keybind, and test out the Automator keybind.

# Use the App

#### In Terminal, run:

```bash
chmod +x custom.py
./custom.py
```

#### Now, in the top right corner of your Mac, you will be able to click on the Snapgrid logo and select which application you want to snap Terminal with!

### Update (Stable Release 2):
#### We now have support for trisnap! If you click on the snapgrid logo, there are snap "Modes" available: Dual and Trisnap. If you click Trisnap, you will have two Terminal screens and an open screen on the left of your Mac. This was made for max utility and speed reasons. What if a user wants three windows instead of two so that he can go back and forth from Terminal to Terminal and Chrome to Terminal?

We hope you enjoy this change. Next release, we hope to add support for Mono (snap one application to the side). This is helpful for users who want access to their Desktop and another application (perhaps to drag things into that app?).

#### This is the moment you've been waiting for.

## TODO
- Nothing at the moment

## Common Issues

#### Random Error
Make sure you have an application other than Terminal open when running our osascript.

#### Keybinds
One of the most common issues is that your keybinds do not work. The keybinds that I chose are: cmd+-, or the command key synchronously with the negative key. If this key doesn't work for you, there are many resources for other, unused keys online.

#### Access Denied
As stated, go to the System Preferences > Security > Accessibility and add Finder and Automator with the '+' buttons. If this doesn't work, try running ```chmod +x exec.sh``` and running from Terminal.

#### Computer Broken/Frozen
Please run this shortcut when Chrome and Terminal are both open. To quickly quit the operation, ```cmd``` + ```Q``` on the app(s), wait a few seconds, and open both up. Test the command. If this doesn't help, restart your computer and don't open up old windows on restart.

#### Run as Administrator
This doesn't happen, unless you run it from Automator. Please run in Automator.

