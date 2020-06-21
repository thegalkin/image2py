"""import os
from pathlib import Path
def scanner():
    obj = os.scandir("Import")
    for item in obj:
        print(item.name)
"""
from shutil import rmtree

rmtree("Import")