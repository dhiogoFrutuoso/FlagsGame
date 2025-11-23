FlagsGame

An educational quiz game where players guess the country based on its flag. Developed using Python and Kivy, it supports multiple difficulty levels, hints, and a simple UI.

Table of Contents

Overview

Features

Technologies

Installation

How to Play

Code Structure

Customization and Configuration

Packaging for Mobile or Desktop

License

Contributing

Overview

FlagsGame is an interactive quiz game where the player sees a country flag and must choose the correct answer from multiple options. It includes three difficulty levels, scoring, hints, and a final results screen.

This project aims to:

Make geography learning fun and dynamic.

Be lightweight and compatible with both desktop and mobile devices (using Kivy).

Be easily customizable (new flags, languages, question counts, etc.).

Features

Difficulty Selection:

Easy: Set of more commonly known countries.

Medium: Moderately popular countries.

Hard: Less commonly known countries.

Gameplay:

A flag is shown, and four country options are presented.

Players must choose the correct country that matches the flag.

Hint:

A hint button shows a piece of information (capital, language, population, or continent) about the country.

Hints can only be used once per game.

Scoring:

+1 point for each correct answer.

Final Screen:

Displays how many questions the player got right out of the total questions answered.

UI:

Developed using Kivy, a Python framework for building cross-platform applications.

Technologies

Python 3.x

Kivy (for UI)

Standard Python libraries: random, clock, animation, etc.

Modular design using screen management (ScreenManager) for easier navigation between game stages.

Installation
Prerequisites

Python 3.x installed.

Kivy installed: pip install kivy.

Any additional dependencies specified in a requirements.txt file.

Steps

Clone the repository:

git clone https://github.com/dhiogoFrutuoso/FlagsGame.git
cd FlagsGame


Install dependencies (if there's a requirements.txt file):

pip install -r requirements.txt


Run the game:

python main.py


(or the main entry file that initializes the Kivy App)

How to Play

On the Start Screen, click "Play" to start the game.

Choose a difficulty level (Easy, Medium, or Hard).

In each round:

A flag is displayed.

Four buttons with country names appear.

Select the country that matches the flag.

After answering a question, you have 0.7 seconds before the next round starts automatically.

Use the Hint button (lightbulb icon) to get a hint about the country (capital, language, continent, or population).

Once the maximum number of questions is reached, the Final Screen appears showing the score.

Code Structure

main.py (or equivalent): Main entry point for the app.

COUNTRIES_FLAGS: Dictionary mapping country names to data (image, capital, continent, language, population).

DIFFICULTY_LEVELS: Defines which countries belong to which difficulty level.

Screen Classes:

StartScreen: Displays the game’s start screen.

DifficultyScreen: Allows the user to select a difficulty.

GameScreen: The main game screen where flags and options are shown.

FinalScreen: Shows the final score after the game ends.

Key functions:

start_game(): Initializes the game state.

new_round(): Configures the next round.

select_answer(): Handles the selection of an answer.

show_clue(): Displays a clue for the current country.

Customization and Configuration

Max Number of Questions: Set using MAX_QUESTIONS.

Country Selection per Difficulty: Modify the DIFFICULTY_LEVELS dictionary to change which countries appear at each level.

Add/Remove Countries: Modify the COUNTRIES_FLAGS dictionary to add or remove countries and their associated data.

Graphics: Replace assets like the hint icon, button designs, or flag images.

Translations: Translate the game to other languages by adjusting text elements like "Play", "You got X out of Y", etc.

Layout Adjustments: Modify the layout for different screen sizes or devices.

Packaging for Mobile: Instructions below for packaging for Android, iOS, etc.

Packaging for Mobile or Desktop
Desktop (Windows/Linux/macOS)

Use PyInstaller to package the game into an executable. For example:

pyinstaller --onefile --add-data "bandeiras;./bandeiras" main.py


Ensure paths are relative and use sys._MEIPASS to access resources when packaged.

Android

Use Buildozer (or toolchain for Kivy) to package the game for Android. Example:

Configure the buildozer.spec file.

Package with buildozer android debug (adjust for your system).

License

This project is licensed under the MIT License
.
Feel free to modify, distribute, or contribute!

Contributing

Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch (git checkout -b feature/my-new-feature).

Make changes and commit with clear messages.

Open a pull request for review.
