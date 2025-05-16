
# 🐦 floppy-bird-ai

A fully custom AI agent that learns to play a Flappy Bird-style game using **neural evolution** — built entirely from scratch with **Python** and **Pygame**. No machine learning libraries or frameworks involved — just math and code.

## 🚀 Overview

This project is a fun and educational demonstration of **Neuroevolution**, where a population of simple neural networks is evolved over generations to play the game better and better. The bird starts out clueless, but over time, it learns how to survive longer and flap smarter.

## 🧠 Key Features

- 🧬 **Neural Evolution**: Evolutionary algorithms breed better-performing birds.
- 🧮 **Handcrafted Neural Networks**: No TensorFlow, PyTorch, or ML libraries — just pure Python.
- 🎮 **Flappy Bird Game**: Game mechanics recreated from scratch using Pygame.
- 📈 **Real-Time Visualization**: Watch birds learn in real time — from chaos to competence.

## 📸 Screenshots

![Demo of AI playing Flappy Bird](https://github.com/ahmednabiled/ai-plays-flappy-bird/blob/main/assets/demo.gif)


## 🛠️ Built With

- [Python](https://www.python.org/)
- [Pygame](https://www.pygame.org/)

## 📂 Project Structure

```
floppy-bird-ai/
├── categories.py # Likely contains types/categories of nodes or components
├── components.py # Game components like pipes, ground, etc.
├── config.py # Configuration and hyperparameters
├── connection.py # Handles neural network connections
├── main.py # Main entry point to run the game and AI
├── node.py # Defines nodes used in the neural network
├── perceptron.py # Custom neural network (from scratch)
├── player.py # The bird/player agent logic
└── population.py # Handles evolution and population of birds
```

## 🧪 How It Works

Each bird is controlled by a tiny neural network that takes in inputs like:
- Bird’s vertical position
- Distance to the next pipe
- Gap height

And outputs whether to flap or not.

The population evolves using:
- **Fitness-based selection**
- **Crossover**
- **Mutation**

Over generations, the birds get better at surviving longer and passing pipes.

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/ahmednabiled/floppy-bird-ai.git
   cd floppy-bird-ai
    ```

2. Install dependencies:
    
    ```bash
    pip install pygame
    ```
    
3. Run the game:
    
    ```bash
    python main.py
    ```
    

## 💡 Inspiration

This project was inspired by classic Flappy Bird AI projects and the desire to build an intelligent agent without relying on black-box ML frameworks.

---
_Made with ❤️ and a lot of flapping neurons._
---
