from timeit import default_timer as timer
import tinyBundle
import shutil
import os

files = ["src/__main__.py", "src/engine.py", "src/game.py", "src/cfg.py", "src/decoder.py"] # Add other files here (can also be a list but a tuple if preferred)

start = timer()
tinyBundle.bundle(files,"out/", 9, False) # out/ is the default output location and 0 is the default compression level
end = timer()

# I'll automate the below later

try:
    shutil.copytree('src/assets', 'out/assets')
except FileExistsError:
    shutil.rmtree("out/assets")
    shutil.copytree('src/assets', 'out/assets')

try:
    shutil.copyfile("src/colours.cfg", "out/colours.cfg")
except FileExistsError:
    os.remove("out/colours.cfg")
    shutil.copyfile("src/colours.cfg", "out/colours.cfg")

print("Bundled files in " + str(end - start) + " seconds") # time in seconds