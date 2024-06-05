from track import Track
from racetrack import Racetrack
from network import Network
import os 

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(3)]
track = Track(Racetrack(1), car_image_paths)

network_dimensions = 5, 4, 2
population_count = 40
networks = [Network(network_dimensions) for i in range(population_count)]

simulation_round = 1
track.simulate_generation(networks, simulation_round)