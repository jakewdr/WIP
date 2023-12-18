def unpackCfg(cfgFile: str): # This is gonna assume that the the headers of the table are vertical
    with open(cfgFile, "r") as cfgContents:
        cleanedList = [line.strip("\n") for line in cfgContents]
        separatedLines = [line.split("=") for line in cleanedList]
        return separatedLines