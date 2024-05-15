import os
import pathlib
import py_compile
import shutil
import zipfile
from time import perf_counter

import python_minifier

compiledFiles = []


def pathLeaf(path) -> str:
    return str(os.path.split(path)[1])


def bundle(srcDirectory: str, outputDirectory: str, compressionLevel: int) -> None:
    """Creates a bundle from all python files in a directory

    Args:
        srcDirectory (str): The original python file directory
        outputDirectory (str): The output directory for the bundle
        compressionLevel (int): The level of compression from 0 to 9
    """

    shutil.rmtree(outputDirectory)  # Deletes current contents of output directory
    shutil.copytree(srcDirectory, outputDirectory)  # Copies source to output directory

    start = perf_counter()  # Two perf counters to better represent the actual bundle time

    pythonFiles = [
        str(entry).replace(os.sep, "/")  # Appends a string of the file path with forward slashes
        for entry in pathlib.Path(outputDirectory).iterdir()  # For all the file entries in the directory
        if ".py" in str(pathlib.Path(entry))
    ]  # If it is a verified file and is a python file
    # Below is where the compiling and optimizations happen
    for file in pythonFiles:
        with open(file, "r+") as fileRW:
            minifiedCode = python_minifier.minify(fileRW.read(), rename_locals=False, rename_globals=False)  # I don't rename vars as that could cause problems when importing between files
            fileRW.seek(0)
            fileRW.writelines(minifiedCode)
            fileRW.truncate()  # This line and the seek one somehow fix some corruption issues

        if "__main__" not in file:  # If the __main__.py file is found in the list ignore compilation (this is to avoid the interpreter finding no entrypoint)
            compiledFile = f"{outputDirectory}{pathLeaf(file)}c"
            py_compile.compile(file, cfile=compiledFile, optimize=2)
            os.remove(file)
            compiledFiles.append(compiledFile)  # Outputs compiled python file
        else:
            compiledFiles.append(file)  # This is only for the __main__.py file
    with zipfile.ZipFile(f"{outputDirectory}bundle.py", "w", compression=zipfile.ZIP_DEFLATED, compresslevel=compressionLevel) as bundler:
        for file in compiledFiles:
            bundler.write(file, arcname=pathLeaf(file))  # pathleaf is needed to not maintain folder structure
            os.remove(file)  # Clean up

    end = perf_counter()
    print(f"Bundled in {end - start} seconds")


if "__main__" in __name__:
    start = perf_counter()
    bundle("src/", "out/", 9)
    end = perf_counter()
    print(f"Process completed in {end - start} seconds")

# If more maths loops were added/we started to use numpy then perhaps we could ahead
# of time numba compile some of the functions increasing performance further
