import base64
import zipfile
from io import BytesIO

"""
This is hellish code for speed purposes,
the less hellish version is on my github under the un-paker repo
"""


def decodeTextFile(pakFilePath: str, filePath: str) -> str:
    """Decodes a text file from within a pakFile

    Args:
        pakFilePath (str): The path to the pakFile
        filePath (str): The local file path of the textfile within the pakFile

    Returns:
        str: Decoded text file as a string
    """
    with open(pakFilePath, "rb") as pakFile:
        return str(zipfile.ZipFile(BytesIO(base64.b64decode(pakFile.read())), "r").read(filePath).decode("UTF-8")).replace("\r", "")  # Backslash Rs are added for some reason, hopefully we don't add them by accident in the future


def decodeImageFile(pakFilePath: str, filePath: str) -> BytesIO:
    """Decodes an image file from within a pakFile

    Args:
        pakFilePath (str): The path to the pakFile
        filePath (str): The local file path of the image within the pakFile

    Returns:
        BytesIO: The image data in bytes
    """
    with open(pakFilePath, "rb") as pakFile:
        return BytesIO(zipfile.ZipFile(BytesIO(base64.b64decode(pakFile.read())), "r").read(filePath))


# I think I could simplify this with three subroutines where it does the common stuff
# between them and then offloads it to the specialized function

# zipfile.ZipFile(BytesIO(base64.b64decode(pakFile.read())), "r"
# Then conv to string or bytesIO depending on use case whilst doing the extra formatting for
# the string version
