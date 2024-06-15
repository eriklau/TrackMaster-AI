# TrackMaster AI

This project simulates self-driving cars navigating a custom racetrack layout using genetic algorithms to optimize their neural networks. The cars are trained to drive on the track without going off-road by adjusting their control mechanisms based on sensor feedback.

![trackmaster_ai](https://github.com/eriklau/TrackMaster-AI/assets/51893550/134152c0-6e78-4292-b57f-3a2405b385b1)

## Usage

Requires Python 3.12+

Clone the repo:
   ```bash
   git clone https://github.com/eriklau/TrackMaster-AI.git
  ```

Install Pyglet:
   ```bash
   pip install pyglet
  ```

Run the program:
   ```bash
   python training.py
  ```
## How It Works
Neural Networks: Each car has a neural network initialized with random weights
Fitness: The performance of each car is evaluated based on how close it gets to the goal without going off-road
Genetic Algorithm: The best-performing cars are selected to reproduce, creating offspring with combined and mutated weights
Iteration: The process is repeated over multiple generations, gradually improving the cars' driving abilities
