from typing import Dict

def unpackCfg(cfgFile: str) -> Dict[str, str]: # This is gonna assume that the the headers of the table are vertical
    with open(cfgFile, "r") as cfgContents:
        cleanedList = [line.strip("\n") for line in cfgContents] # Removes new line characters
        separatedLines = dict([line.split("=",1) for line in cleanedList]) # Splits the strings into lists and then converts to a dictionary
        return separatedLines