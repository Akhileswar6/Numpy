import os
import subprocess

folders=['Numpy1_Tutorial','Numpy2_Random', 'Numpy3_ufuncs']

for folder in folders:
    print(f"\n📁 Folder: {folder}")
    for file in sorted(os.listdir(folder)):
        if file.endswith(".py"):
            path = os.path.join(folder, file)
            print(f"🔄 Running: {path}")
            subprocess.run(["python", path])
            print(f"✅ Finished: {path}")