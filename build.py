import bundler, os

scriptPath = str(os.path.realpath(__file__).replace(os.sep, "/"))  # Gets the path of the current running python script and makes sure forward-slashes are used
containingFolder = scriptPath.replace("build.py", "")
bundler.bundle(containingFolder + "src/",containingFolder + "out/", 9) # out/ is the default output location and 0 is the default compression level