# snapgrid

[<img src="logo.png" width="200"/>](https://github.com/VladUsatii/snapgrid/blob/main/logo.png?raw=True)

A tool for lazy programmers to quickly snap an app of their choice and Terminal to the left and right bounds of their screen. Made for fast and efficient workflow.

Designed in Python3, Osascript (AppleScript), Bash/Shell, and C, Snapgrid is customizable and interchangeable.

Contribute if you found this tool helpful. ✏️

## Installation

Firstly, do the following after opening a fresh Terminal screen:

```bash
cd
mkdir Dev
cd Dev
git clone https://github.com/VladUsatii/snapgrid.git
pip install -r requirements.txt # get all required modules
```

Then, ```cmd``` + ```Space``` and find ```Automator.``` Create a new ```Quick Operation```. Make sure that the script handler is titled ```Run Shell Script```. If it is, type the following in the dark grey box:

```bash
cd Dev/snapgrid && sh execute.sh
```

This tells your computer to change directory to Dev/snapgrid and to run the execute shell file.

press ```Play``` in the top-right corner (newest version of MacOS), and make sure it runs a check-mark. This makes sure that Automator won't crash in the middle of its process once assigned.

![How you should look so far](https://github.com/VladUsatii/snapgrid/blob/main/tutorial_image1.png?raw=true)

Lastly, accept permissions for Automator and set the keybind by opening System Preferences in the following order:

```python3
"""
LAST CONFIG STEPS in order (made with a tree):
System Preferences
└ Security
  └ Accessibility
    └ Open Lock
      └ Tap '+' & add Finder and Automator
        └ Close Lock
          └ Make a Keybind in Computer Keybinds
"""
```

How your keybinds window should look when done:

![How your keybinds should look](https://github.com/VladUsatii/snapgrid/blob/main/Keybinds.png?raw=true)

And you are done!

Test keybind and action by pressing keybind.

> **Problems? Errors?** See *Common Issues*.

# Use the App

#### In Terminal, run:

```bash
chmod +x custom.py # must be in snapgrid directory
./custom.py
```

Now, in the top right corner of your Mac, you will be able to click on the Snapgrid logo and select which application you want to snap Terminal with! There are countless options available, currently.

### Update (Stable Release 2):
We now have support for trisnap! If you click on the snapgrid logo, there are snap "Modes" available: Mono, Dual and Trisnap. If you click Trisnap, you will have two Terminal screens and an open screen on the left of your Mac. This was made for max utility and speed reasons. What if a user wants three windows instead of two so that he can go back and forth from Terminal to Terminal and Chrome to Terminal?

We hope you enjoy this change. Next release, we hope to add support for more types of snaps (orientation and screen flips). This is helpful for users who want access to their Desktop and another application (perhaps to drag things into that app?).

### Update (Stable Release 3):
We have added support for inverted windows. The feature isn't currently working, but it will very soon. Also, there is currently a bug where some types of snaps don't work in certain periods of time. For instance, if Terminal is closed (no windows), but it is still open (white dot), the application won't snap (for some reason). There is no hacky fix for this, as we presume. We've done our best to safeguard and open Terminal in every way possible so that we don't slow down your workflow.

## TODO
- **Figure out what is wrong with osascript when counting Unix windows**
- Add orientation and screen change options
- Add tab type options
- Quick Toggle Tabs
- Flip Application and Terminal from Left to Right
- Add Top or Bottom support
- **Decrease Snap Latency**

**Bolded issues are currently the hardest and are being researched.**

## Common Issues

These are common issues when _setting up the app_.

#### Keybinds
One of the most common issues is that your keybinds do not work. The keybinds that I chose are: cmd+-, or the command key synchronously with the negative key. If this key doesn't work for you, there are many resources for other, unused keys online.

#### Access Denied
As stated, go to the System Preferences > Security > Accessibility and add Finder and Automator with the '+' buttons. If this doesn't work, try running ```chmod +x exec.sh``` and running from Terminal.

#### Computer Broken/Frozen
Please run this shortcut when Chrome and Terminal are both open. To quickly quit the operation, ```cmd``` + ```Q``` on the app(s), wait a few seconds, and open both up. Test the command. If this doesn't help, restart your computer and don't open up old windows on restart.

#### Run as Administrator
This doesn't happen, unless you run it from Automator. Please run in Automator.

#### Terminal doesn't snap
There are certain orientations of having Terminal.app open that don't respond to keybinds. We are working on this.

---

Created by Vlad Usatii @ readproduct.com / Maintained by Vlad as of 08/21/2021

