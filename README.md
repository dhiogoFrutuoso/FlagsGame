#!/bin/bash

cat << 'EOF'
# 🗺️ FlagsGame

An educational quiz game where players guess the country based on its flag. Developed using **Python** and **Kivy**, it supports multiple difficulty levels, hints, and a simple, cross-platform UI.

---

## 🧭 Table of Contents

* [🌟 Overview](#-overview)
* [✨ Features](#-features)
* [💻 Technologies](#-technologies)
* [⬇️ Installation](#-installation)
* [🕹️ How to Play](#-how-to-play)
* [🏗️ Code Structure](#-code-structure)
* [⚙️ Customization and Configuration](#-customization-and-configuration)
* [📦 Packaging for Mobile or Desktop](#-packaging-for-mobile-or-desktop)
* [⚖️ License](#-license)
* [🤝 Contributing](#-contributing)

---

## 🌟 Overview

**FlagsGame** is an interactive quiz game where the player sees a country flag and must choose the correct answer from multiple options. It includes three difficulty levels, scoring, hints, and a final results screen.

### Project Goals:

* Make geography learning fun and dynamic.
* Be lightweight and compatible with both **desktop and mobile** devices (using Kivy).
* Be easily customizable (new flags, languages, question counts, etc.).

## ✨ Features

### 🎯 Difficulty Selection

The game offers three sets of countries for varying challenge levels:

* **Easy:** A set of more commonly known countries.
* **Medium:** Moderately popular countries.
* **Hard:** Less commonly known countries.

### 🎮 Gameplay

* A flag is shown, and four country options are presented.
* Players must choose the correct country that matches the flag.

### 💡 Hint System

* A hint button shows a piece of information (capital, language, population, or continent) about the country.
* Hints can be used only **once per game**.

### 🏆 Scoring and Final Screen

* **+1 point** for each correct answer.
* The final screen displays how many questions the player got right out of the total questions answered.

### 🖥️ User Interface (UI)

* Developed using **Kivy**, a Python framework for building cross-platform applications.

## 💻 Technologies

The game is primarily built around the Python ecosystem:

* **Python 3.x**
* **Kivy** (for UI and cross-platform)
* Standard Python libraries (`random`, `clock`, `animation`, etc.).
* Modular design using screen management (`ScreenManager`) for easier navigation.

## ⬇️ Installation

### Prerequisites

Ensure you have the following installed on your system:

* **Python 3.x**
* **Kivy:** Install via pip: `pip install kivy`
* Any additional dependencies specified in a `requirements.txt` file.

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/dhiogoFrutuoso/FlagsGame.git](https://github.com/dhiogoFrutuoso/FlagsGame.git)
    cd FlagsGame
    ```

2.  **Install dependencies** (if a `requirements.txt` file exists):
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the game:**
    ```bash
    python main.py
    ```
    (Or the main entry file that initializes the Kivy App).

## 🕹️ How to Play

1.  On the **Start Screen**, click "**Play**" to begin the game.
2.  Choose a difficulty level (**Easy**, **Medium**, or **Hard**).
3.  In each round:
    * A flag is displayed.
    * Four buttons with country names appear.
    * Select the country that matches the flag.
4.  After answering a question, the next round starts automatically after **0.7 seconds**.
5.  Use the **Hint** button (lightbulb icon) to get a hint about the country.
6.  Once the maximum number of questions is reached, the **Final Screen** appears showing your score.

## 🏗️ Code Structure

The project is divided into modules and classes to manage different aspects of the game:

* `main.py` (or equivalent): Main entry point for the app.
* `COUNTRIES_FLAGS`: Dictionary mapping country names to their data (image, capital, continent, language, population).
* `DIFFICULTY_LEVELS`: Defines which countries belong to which difficulty level.

### Screen Classes

* `StartScreen`: Displays the game’s start screen.
* `DifficultyScreen`: Allows the user to select a difficulty.
* `GameScreen`: The main game screen where flags and options are shown.
* `FinalScreen`: Shows the final score after the game ends.

### Key Functions

* `start_game()`: Initializes the game state.
* `new_round()`: Configures the next round.
* `select_answer()`: Handles the selection of an answer.
* `show_clue()`: Displays a clue for the current country.

## ⚙️ Customization and Configuration

The game is designed to be easily modifiable:

| Configuration | How to Modify |
| :--- | :--- |
| **Max Number of Questions** | Adjust the `MAX_QUESTIONS` variable. |
| **Country Selection** | Modify the `DIFFICULTY_LEVELS` dictionary. |
| **Add/Remove Countries** | Edit the `COUNTRIES_FLAGS` dictionary and associated data. |
| **Graphics** | Replace assets (icons, button designs, flag images) in the resources directory. |
| **Translations** | Adjust text elements (e.g., "Play", "You got X out of Y") within the screen classes. |

## 📦 Packaging for Mobile or Desktop

### Desktop (Windows/Linux/macOS)

Use **PyInstaller** to package the game into an executable.

```bash
pyinstaller --onefile --add-data "bandeiras;./bandeiras" main.py
Note: Ensure paths are relative and use sys._MEIPASS to access resources when packaged.

Android
Use Buildozer (or the Kivy toolchain) to package the game for Android.

Configure the buildozer.spec file.

Package with: buildozer android debug (adjust for your system).

⚖️ License
This project is licensed under the MIT License.

Feel free to modify, distribute, or contribute!

🤝 Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository.

Create a new branch: git checkout -b feature/my-new-feature.

Make changes and commit with clear messages.

Open a Pull Request for review.
