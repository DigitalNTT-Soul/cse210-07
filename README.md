# Greed

"There are old skydivers and bold skydivers, but there are no old, bold skydivers." - Jeff Wuorio

---

Greed is a game in which the player seeks to gather as many falling gems as possible. The game continues as long as the player wants more!

## Getting Started

---

Make sure you have Python 3.10.4 or newer installed and running on your machine. Open terminal or PowerShell and
browse to the project's root folder. Start the program by running the following command.

```
python3 greed
```

You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the
project folder. Select the main module inside the hilo folder and click the "run" button.

There are some rules to this game and are listed as follows:

- Gems (\*) and rocks (o) randomly appear and fall from the top of the screen.
- The player (#) can move left or right along the bottom of the screen.
- If the player touches a gem they earn a point.
- If the player touches a rock they lose a point.
- Gems and rocks are removed when the player touches them.
- The game continues until the player closes the window.

The goal of the game is to collect as many falling gems as possible.

## Project Structure

---

```
root                    (project root folder)
+-- Greed              (source code for game)
  +-- game              (specific classes)
    +-- director.py     (director class script)
    +-- rules.py        (rules class script)
    +-- ui.py           (ui class script)
    +-- word_list.py    (word_list class script)
    +-- word_list.txt   (raw text file of words, for easy editing)
  +-- __main__.py       (program entry point)
+-- README.md           (general info)
```

## Required Technologies

---

Python 3.10.4

## Authors

---

- Dylan Ruppell (ruppelld@byui.edu) (github: DigitalNTT-Soul): Program design
- Austin Donovan (iskarr9g@gmail.com) (github: Iskarr): ASCII Parachute Design, Parachute Class, Parachute guy function
- Matt Pellét (mattpellet@byui.edu) (github: m4j0rCSE): Word list, README, word_list class
- Larry Brys (bry21010@byui.edu) (github: ljbrys) collaborated with design
