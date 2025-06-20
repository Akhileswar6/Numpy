import os
import subprocess

folder='Numpy1_Tutorial'

for file in os.listdir(folder):
    if file.endswith(".py"):
        path = os.path.join(folder, file)
        print(f"Running {path}...")
        subprocess.run(["python", path])