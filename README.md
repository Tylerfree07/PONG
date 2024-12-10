# 🏓 Pong Game

A classic Pong game built with Python and Pygame. This game allows for single-player (against CPU) or two-player modes, customizable settings, and fast-paced gameplay.

---

## 📋 Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Controls](#controls)
- [Game States](#game-states)
- [Customization](#customization)
- [Assets](#assets)
- [License](#license)

---

## 📖 About
This project is a modern twist on the classic Pong game, featuring smooth animations, single and two-player modes, and adjustable difficulty. The game is built using **Pygame**, a Python library for game development. The game includes background images, sound effects, and visual effects for a fun gaming experience.

---

## ✨ Features
- 🎮 **Single-player and two-player modes**
- 🔄 **Game states**: Start menu, game, settings, and game over
- ⚙️ **Adjustable settings**: CPU difficulty, ball speed, and background colors
- 🎵 **Sound effects**: Ball hits and other interactions
- 📏 **Score tracking**: First to 7 points wins
- 📸 **Simple but engaging graphics**: Custom images for backgrounds and menus

---

## 🛠️ Installation
1. **Install Python**: Make sure Python 3.x is installed. You can check this by running:
   ```bash
   python --version
   ```

2. **Install Pygame**: Install the Pygame library using pip:
   ```bash
   pip install pygame
   ```

3. **Download the Code**: Clone the repository or download the source files.

4. **Run the Game**: Open a terminal in the directory where `pong.py` is located and run:
   ```bash
   python pong.py
   ```

---

## 🎮 How to Play
- **Objective**: Be the first player to score 7 points.
- **Game Modes**: 
  - **Single Player**: Play against the CPU.
  - **Two-Player**: Compete against another player.
- **Game Flow**: 
  - Start at the **Start Menu**.
  - Use the keyboard to navigate to **Settings** or **Start the Game**.
  - Control your paddle to prevent the ball from crossing your side.
  - The first player to reach 7 points wins.

---

## 🎮 Controls
**During the Game:**
- **Player 1 (right side)**
  - **Up**: Arrow Up (↑)
  - **Down**: Arrow Down (↓)
- **Player 2 (left side)**
  - **Up**: W
  - **Down**: S

**Game State Controls:**
- **Start Menu**
  - **SPACE**: Start the game
  - **S**: Open settings
  - **Q**: Quit the game
- **Settings Screen**
  - **R**: Change background color to red
  - **G**: Change background color to green
  - **B**: Change background color to blue
  - **K**: Change background color to grey
  - **L**: Change background color to black
  - **E**: Set CPU difficulty to easy
  - **M**: Set CPU difficulty to medium
  - **H**: Set CPU difficulty to hard
  - **S**: Change ball speed to slow
  - **N**: Change ball speed to normal
  - **F**: Change ball speed to fast
  - **C**: Switch to CPU opponent
  - **O**: Switch to 2-player mode
- **Game Over Screen**
  - **R**: Restart the game
  - **S**: Return to settings
  - **Q**: Quit the game

---

## 🕹️ Game States
1. **Start Menu**: Displays options to start the game, open settings, or quit.
2. **Settings**: Customization options for ball speed, background color, and CPU difficulty.
3. **Game**: The main gameplay loop, where you play the Pong match.
4. **Game Over**: The game ends when one player scores 7 points. Options to restart, go to settings, or quit are available.

---

## ⚙️ Customization
You can customize the following in the game:
- **Background Color**: Change with R, G, B, K, L keys in the settings screen.
- **Ball Speed**: Change to slow, normal, or fast with S, N, F keys.
- **CPU Difficulty**: Switch between easy, medium, and hard using E, M, and H keys.

---

## 📦 Assets
The following assets are required for the game to function:
- **Sound Effects**: `assets/hit.mp3`
- **Images**:
  - `assets/main_screen.jpg` (Start menu background)
  - `assets/settings.jpg` (Settings menu background)
  - `assets/game_over.jpg` (Game over screen background)

Make sure to place these files in an `assets/` directory inside the same directory as `pong.py`.

---

## 📜 License
This project is for educational purposes. Feel free to modify and expand it. 
