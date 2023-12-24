from typing import Dict, List
from functools import cache

def unpackCfg(cfgFile: str) -> Dict[str, str]: # This is gonna assume that the the headers of the table are vertical
    cleanedList = parseCfg(cfgFile)
    return cleanCfg(cleanedList)
    
def parseCfg(cfgFile: str) -> List[str]:
    with open(cfgFile, "r") as cfgContents:
        return [line.strip("\n") for line in cfgContents] # Removes new line characters

@cache # Using the cached operation if the list config is the same as before
def cleanCfg(cleanedList: List[str]) -> Dict[str, str]:
    return dict([line.split("=",1) for line in cleanedList])