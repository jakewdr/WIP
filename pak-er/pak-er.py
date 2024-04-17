import shutil
import base64
import os

containingFolder = str(os.path.realpath(__file__).replace(os.sep, '/')).replace("/pak-er.py", "")

def paker(folderToBePacked:str, outputLocation:str, manifestName:str):
    with open(folderToBePacked + manifestName, "r") as cfgContents:
        separatedLines = [line.split("=") for line in [line.strip("\n") for line in cfgContents]] # Reads config

    shutil.make_archive(separatedLines[0][1], "zip", folderToBePacked)
    if os.path.isfile(separatedLines[0][1] + ".pak"): os.remove(separatedLines[0][1] + ".pak")
    with open(separatedLines[0][1] + ".zip", "rb") as fileIn, open(separatedLines[0][1] + ".pak", "wb") as fileOut:
        base64.encode(fileIn, fileOut)
    if os.path.isfile(separatedLines[0][1] + ".zip") == True: os.remove(separatedLines[0][1] + ".zip")

if __name__ == "__main__":
    PAKNAME = "template"
    paker(containingFolder + f"/src/{PAKNAME}/", containingFolder +"/out/", "manifest.cfg")