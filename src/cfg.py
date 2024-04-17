from typing import Dict


def unpackCfg(cfgFile: str) -> Dict[str, str]:  # This is gonna assume that the the headers of the table are vertical
    """Turns a config file into a dictionary

    Args:
        cfgFile (str): Path to the config file

    Returns:
        Dict[str, str]: The config file as a dictionary with the keys being the first column and the other column being the
    """
    with open(cfgFile, "r") as cfgContents:
        return dict([line.split("=", 1) for line in [line.strip("\n") for line in cfgContents if line != ""]])
        # World's ugliest one liner but it gets the job done^
