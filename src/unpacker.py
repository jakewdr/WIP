def unpackCsv(csvFile: str): # This is gonna assume that the the headers of the table are vertical
    with open(csvFile, "r") as csvContents:
        cleanedList = [line.strip("\n") for line in csvContents]
        separatedLines = [line.split(",") for line in cleanedList]
        
        return separatedLines