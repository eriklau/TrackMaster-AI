from track import Track
from racetrack import Racetrack
from network import FirstNetwork
import os 

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(3)]
track = Track(Racetrack(), car_image_paths)


population_count = 3
networks = [FirstNetwork() for i in range(population_count)]

simulation_round = 1
track.simulate_generation(networks, simulation_round)