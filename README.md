# Translations w/ OpenGL

## Description

This project is focused on learning and demonstrating the concept of translations using OpenGL. As part of the learning process, we developed a simple Snake Game using the pygame and OpenGL libraries. The game involves moving a snake on a grid, and the movement is managed using translations in OpenGL, helping visualize how objects can be moved efficiently in 2D and 3D space.

## Getting Started

1. Clone the repository

```bash
git clone https://github.com/Nunofonsecaflorencio/translations-pyopengl
cd translations-pyopengl
```

2. Create an environment and install requirements

```bash
python -m venv env
venv\Scripts\activate.ps1

pip install -r requirements.txt
```

3. Run the main file (main.py)

```bash
cd snake-game
python main.py
```

## How It Works

- The game grid and snake movement are managed using **Pygame**, while rendering and translations of objects are done using the OpenGL library.

- The **glTranslatef()** function from OpenGL is used to move the snake across the game grid, providing a simple way to demonstrate how translations work in a 2D space.

---

Feel free to send any pull request.

Happy Coding ! 😁