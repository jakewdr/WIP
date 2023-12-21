def unpackCfg(cfgFile: str) -> dict: # This is gonna assume that the the headers of the table are vertical
    with open(cfgFile, "r") as cfgContents:
        cleanedList = [line.strip("\n") for line in cfgContents]
        separatedLines = dict([line.split("=", 1) for line in cleanedList])
        print(separatedLines)
        return separatedLines