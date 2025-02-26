# Turtle Race Game

A fun Python game built using the `turtle` module, where you can bet on a turtle and watch them race to the finish line!

---

## Features

- **Interactive Gameplay**: Place your bet by entering the color of the turtle you think will win.
- **Randomized Races**: Each turtle progresses randomly, making the race unpredictable and exciting.
- **Colorful Turtles**: Six vibrant turtles—red, orange, yellow, green, blue, and purple—compete in the race.

---

## How to Play

1. Run the game. A dialog box will prompt you to **"Make your Bet"**. 
2. Enter the color of the turtle you think will win (e.g., red, green, etc.).
3. Watch the race and see if your turtle wins!

If your bet matches the winning turtle's color, you win; otherwise, you lose.

---

## Prerequisites

- **Python 3.x** installed on your system.
- Basic understanding of how to run Python scripts.

---

## Installation and Setup

1. Clone this repository or copy the script to your local machine.
2. Ensure you have Python installed by running:  
    ```bash
    python --version
    ```
3. Run the program using:  
    ```bash
    python <script_name>.py
    ```
    Replace `<script_name>` with the name of the file containing this code.

---

## Game Rules

1. Six turtles start at different horizontal positions but on the same vertical axis.
2. The turtles randomly progress towards the finish line.
3. The first turtle to cross the finish line wins!
4. The result will be displayed in the terminal.

---

## Code Overview

- **Turtle Setup**: The turtles are assigned different colors and start from their initial positions.
- **Random Movement**: Each turtle moves forward by a random number of steps (between 0 and 10).
- **Winning Logic**: The game checks if any turtle crosses the finish line and announces the winner.

---

## Libraries Used

- `turtle`: Used for graphics and creating the game animation.
- `random`: Used to generate random numbers for turtle movements.

---

## Customization

You can tweak the game to make it even more fun:
- **Add More Turtles**: Add new colors to the `colors` list and update their positions in `y_position`.
- **Change Canvas Size**: Update the `canvas_width` and `canvas_height` variables to resize the game area.

---

## Screenshots

*Screenshots coming soon!*

---

## License

This project is open source. Feel free to use, modify, and share.

---

Enjoy the game and have fun betting on your favorite turtle! 🐢🎉