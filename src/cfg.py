from typing import Dict


def unpackCfg(cfgFile: str) -> Dict[str, str]:  # This is gonna assume that the the headers of the table are vertical
	with open(cfgFile, "r") as cfgContents:
		return dict([line.split("=", 1) for line in [line.strip("\n") for line in cfgContents]])
