from track import Track
from racetrack import Racetrack
import os 

car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(3)]
track = Track(Racetrack(), car_image_paths)

track.simulate_generation()