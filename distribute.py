"""
After multiple hours of programming I realized this approach did not work

I need significant amounts of reparations for all the python articles I had to read through

Considering just making python a required dependent
"""






#files = ["src/__main__.py", "src/engine.py", "src/game.py", "src/cfg.py", "src/decoder.py"]
#exec(open("out/bundle.py").read())

import tinyBundle
import shutil
import os

VERSION = "0.0.1"
EXENAME = "torsion " + VERSION

SOURCEDIRECTORY = "src/"
EXELOCATION = "dist/" + VERSION + "/"
BUNDLELOCATION = "dist/" + VERSION + "/" + "gameFiles/"
ENTRYPOINTNAME = "entrypoint.py"

sourceFiles = [SOURCEDIRECTORY + "__main__.py", SOURCEDIRECTORY + "engine.py", SOURCEDIRECTORY + "game.py",SOURCEDIRECTORY + "cfg.py", SOURCEDIRECTORY + "decoder.py"]

if os.path.exists("dist/") == False:
    os.mkdir("dist/")
    
if os.path.exists(EXELOCATION) == False:
    os.mkdir(EXELOCATION)
    
if os.path.exists(BUNDLELOCATION) == False:
    os.mkdir(BUNDLELOCATION)

[shutil.copy(file,"dist/" + VERSION + "/" + "gameFiles") for file in sourceFiles]


os.rename(BUNDLELOCATION + "__main__.py", BUNDLELOCATION + "entrypoint.py")
newFiles = [BUNDLELOCATION + "entrypoint.py", BUNDLELOCATION + "engine.py", BUNDLELOCATION + "game.py", BUNDLELOCATION + "cfg.py", BUNDLELOCATION + "decoder.py"]
tinyBundle.bundle(newFiles, BUNDLELOCATION, 9, False)
[os.remove(file) for file in newFiles]

#os.system(f"pyinstaller --onefile --windowed --noconfirm --hidden-import=pygame --name={EXENAME} loader.py")