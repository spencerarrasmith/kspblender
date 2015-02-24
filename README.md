kspblender
==========

KSP in Blender

This is all based around the python file ksparser.py, which operates on a given Kerbal Space Program .craft file
(the file type that ships are stored as)

HOW TO USE DEMO:

1. Download Blender from http://blender.org
2. Download .mu importer Blender addon from https://github.com/taniwha-qf/io_object_mu
3. Extract, put "io\_object\_mu\_master" folder (the whole folder) in Program Files\Blender Foundation\Blender\2.72\scripts\addons. It may be a folder within a folder, so you want the folder that is one level up from the files themselves.
4. Enable the addon in Blender. Press Ctrl+Alt+U or go to User Preferences under File. Go to the Addons tab, search for "mu" and enable the addon by clicking the little checkbox
5. Click "Download Zip" in the lower right on this page.
6. Extract, and open up the kspblenderdemo file inside the demo folder.
7. Place .craft file into the same folder as the Blender file (they can be found under "saves" in the KSP.exe folder)
8. Follow these setup instructions: http://imgur.com/a/oTjPT

Open Blender

Change to Coding view

Change line 9 to be the location of KSP.exe (the game). Be sure to use double backslashes!

Change line 11 to be the name of your craft.craft, and put it in the same folder as the Blender file

Change back to Default view

Press the upper Run Script in the bottom right. This gives you a menu with some extra functions

Press the lower Run Script in the bottom right. This loads the craft.

Wait patiently (it can take up to 10 seconds per unique part, so a maximum of around 20 minutes)

Press Render (or F12)

9. Ask for help on reddit or the ksp forums if these instructions suck
10. Render, then press F3 in the render window and save the image where you want it.
11. You can do tons more, but it will require learning some Blender. I'm happy to help with that.

Project's Trello: https://trello.com/b/ffCPkGyM/kspblender
