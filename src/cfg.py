def unpackCfg(cfgFile: str) -> dict[str, str]:  # This is gonna assume that the the headers of the table are vertical
    """Turns a config file into a dictionary

    Args:
        cfgFile (str): Path to the config file

    Returns:
        Dict[str, str]: The config file as a dictionary with the keys being the first column and the other column being the
    """
    with open(cfgFile) as cfgContents:
        return dict([line.split("=", 1) for line in [line.strip("\n") for line in cfgContents if line != ""]])  # The if is needed due to a bug where the process would fail due to an empty line in the config
        # World's ugliest one liner but it gets the job done^
