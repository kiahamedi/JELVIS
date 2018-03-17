# JELVIS born of J.A.R.V.I.S - Just A Rather Very Intelligent System
<br>

##### This project currently uses Python version 2.7

![Alt text](https://raw.githubusercontent.com/kiahamedi/JELVIS/master/wallpapers/jelviis.png "Optional title")

This project can be an audio assistant on your operating system and perform the tasks that you are considering for it.
You can use different scripts to use in the language interface

Part of the conversations you can do with JELVIS:
- ### Converses, barely.

    **Talk to JELVIS :** hello<br>
    **JELVIS :** Well, hello

    **Talk to JELVIS :** Who is iron man?<br>
    **JELVIS :** Iron man is the one who created me.

    **Talk to JELVIS :** What does JELVIS stand for?<br>
    **JELVIS :** JELVIS stands for Just A Rather Very Intelligent System

JELVIS is not able to learn, and you can increase the sentences with JELVIS (remember JELVIS)
To do this, you can open the file and add your own conversations and send us

- ### Rhythmbox: Play, Stop, Open.

    Uses shell commands to play and pause rhythmbox music.

    **Talk to JELVIS :** play music<br>
    **JELVIS :** On it!<br>
    **Talk to JELVIS :** Stop music<br>
    **JELVIS :** On it!<br>
    **Talk to JELVIS :** Next Track<br>
    **JELVIS :** Right away, sir!
    **Talk to JELVIS :** Previous Track<br>
    **JELVIS :** Right away, sir!

- ### Tells time.
    
    **Talk to JELVIS :** what time is it?<br>
    **JELVIS :** The time is 4 43 am


- ### Suggests Googling for all unrecognized interrogative questions

    **Talk to JELVIS :** What is IIT, Bombay?<br>
    **JELVIS :** Do you want me to google that for you?<br>
    **Talk to JELVIS :** yes<br>
    **JELVIS :** Right away, sir!  Created new window in existing browser session.


    Uses youtube.py script to find the first search result for the last user input in above case, and opens it in chromium browser. (Thanks for the nihal111)

- ### Searches internet.

    **Talk to JELVIS :** Google what is the answer to life?<br>
    **JELVIS :** Right away, sir!  Created new window in existing browser session.<br>
    **Talk to JELVIS :** Search youtube for Call of Duty<br>
    **JELVIS :** On it!  Created new window in existing browser session.<br>
    **Talk to JELVIS :** Search for kia hamedi on google maps<br>
    **JELVIS :** On it!  Created new window in existing browser session.

- ### Changes Wallpaper.

    In the JELVIS folder, a folder is placed for the wallpapers so you can put your own images in the appropriate path and change the image to change the wallpaper.

    **Talk to JELVIS :** change wallpaper<br>
    **JELVIS :** On it!
- ### Volume Controls.
    **Talk to JELVIS :** increase valume to *<br>
    **JELVIS :** Right away, sir!<br>
    **Talk to JELVIS :** decrease valume to *<br>
    **JELVIS :** Right away, sir!<br>
- ### Launches Programs.
    
    **Talk to JELVIS :** open nautilus<br>
    **JELVIS :** Right away, sir!<br>
    **Talk to JELVIS :** take me to /etc<br>
    **JELVIS :** Sure thing! (Opens /etc in nautilus)<br>
    **Talk to JELVIS :** take me home<br>
    **JELVIS:** Sure thing! (Opens ~ in nautilus)<br>
    **Talk to JELVIS:** open chromium / open firefox / open calculator / open vlc<br>
    **JELVIS :** Sure thing!


- ### Other:
    
    Standard replies for unrecognized/unmatched inputs

    **Talk to JELVIS :** go to sleep / exit / quit / bye / goodbye

    closes the python script.

## Requirements:

You can run `pip install -r requirements.txt` to install them all.



## Run:

To run, you can enter the JELVIS path and execute the following commands in text or voice mode

`python script.py text` : for text mode of input

`python script.py voice` : for voice mode of input

Voice mode may give a series of warnings for numerous reasons, but still might fuction properly.

## Exit:

To exit and close the program, you must first close the graphic window and then stop the terminal output with Ctrl + Z control keys.

## DesktopShortcut:

for create icon JELVIS in desktop and your applications, you must copy jelvis.desktop in this path: /home/kia/.local/share/applications

to exit JELVIS in DesjtopShortcut without terminal output , you must first close the graphic windows and next tell jelvis goodbye

And finally I thank Nihal Singh for the original code

