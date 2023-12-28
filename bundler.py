import os
import shutil
import zipfile
import pathlib
import py_compile
import python_minifier

pythonFiles = []
compiledFiles = []

def path_leaf(path):
    import ntpath
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def bundle(srcDirectory: str, outputDirectory: str, compressionLevel: int):
    
    shutil.rmtree(outputDirectory)
    shutil.copytree(srcDirectory, outputDirectory)

    [pythonFiles.append(str(entry).replace(os.sep, '/')) for entry in pathlib.Path(outputDirectory).iterdir() if entry.is_file() and pathlib.Path(entry).suffix == ".py" or pathlib.Path(entry).suffix == ".pyw"]

    for file in pythonFiles:
        with open(file, "r") as fileContents:
            contents = fileContents.read()
            minifiedCode = python_minifier.minify(contents, rename_locals=False, rename_globals=False )
            
        with open(file, "w") as fileWrite:
            fileWrite.writelines(minifiedCode)
        
    for file in pythonFiles:
        if "__main__" not in file:  
            py_compile.compile(file, cfile=outputDirectory + path_leaf(file) + "c" , optimize=2)
            os.remove(file)
            compiledFiles.append(outputDirectory + path_leaf(file) + "c")
        else:
            compiledFiles.append(file)

    with zipfile.ZipFile(str(outputDirectory + "bundle.py"), 'w',compression= zipfile.ZIP_DEFLATED,
            compresslevel= int(compressionLevel)) as bundler:
        [bundler.write(file, arcname=str(path_leaf(file))) for file in compiledFiles] # List comprehension
        [os.remove(file) for file in compiledFiles]
        
if __name__ == "__main__":
    scriptPath = str(os.path.realpath(__file__).replace(os.sep, "/"))  # Gets the path of the current running python script and makes sure forward-slashes are used
    containingFolder = scriptPath.replace("bundler.py", "")
    bundle("src/", "out/", 0)