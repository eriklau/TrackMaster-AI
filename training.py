from track import Track
import os 
track_image_path = os.path.join("images", "track1.png")
car_image_paths = [os.path.join("images", f"car{i}.png") for i in range(3)]
track = Track(track_image_path, car_image_paths)

track.simulate_generation()