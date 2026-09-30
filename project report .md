# Project Report: Command Line Hangman

Course: Python Essentials
Name: Hitarth Suntha

1. Project Idea
I chose to make a Hangman game for the flipped course project. The problem statement asked for a project from the course domain that is fully executable from the terminal. Since we learned basic concepts like while loops, lists, and conditional statements, a text guessing game was a good way to use all of them together. 

2. Tech Used
Language: Python 3
IDE: Visual Studio Code
Libraries: Only the standard `random` module.

3. Features
- Picks a random word every time you run it.
- Input validation: It checks if the user actually typed a single alphabet. If you type a number or a long string by mistake, it doesn't cut your life, it just asks you to type again.
- Shows the letters you have already guessed so you don't repeat them.

4. How the Code Works
The code is written inside one main function called `play_hangman()`. 
First, it uses `random.choice()` to pick a word from a list. Then I made a list of blanks ("_") to represent the hidden word on the screen. 
The main game runs on a `while` loop. The loop keeps going until the user's lives reach 0 or there are no blanks left. Inside the loop, `input()` takes the guess. 
If the guessed letter is correct, a `for` loop finds its position and replaces the blank. If it is wrong, it just does `lives -= 1`. At the end of the loop, a simple if-else block checks if you won or lost and prints the final message.

5. Conclusion
This was a good project to practice basic Python syntax. The main issue I faced was handling wrong inputs so the game doesn't crash or behave weirdly, but using simple if-conditions fixed it. The project meets all the requirements and runs fully on the CLI.