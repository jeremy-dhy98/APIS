# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 07:44:33 2024

@author: mulwa
"""

import pandas as pd
from cat_dogVidsData import cats_info, dogs_info
from pathlib import Path
import os

path = Path(Path.home().joinpath("Desktop", "CSV", "catsVidInfo.xlsx"))
path2 = Path(Path.home().joinpath("Desktop", "CSV", "dogsVidInfo.xlsx"))


def export_catsvidinfo():
    if Path.exists(path):
        pd.DataFrame(data=cats_info).to_excel(path, index=False)
        print("Path exists and file is saved: ")
        
    elif not (Path.exists(path)):
        os.makedirs(path)
        print("Path was created: ")
        
    else:
        print("Error in your code")
        
export_catsvidinfo()

     
def export_dogsvidinfo():
    if Path.exists(path2):
        pd.DataFrame(data=dogs_info).to_excel(path2, index=False)
        print("Path exists and file is saved: ")
        
    elif not (Path.exists(path2)):
        os.makedirs(path2)
        print("Path was created: ")
        
    else:
        print("Error in your code")

export_dogsvidinfo()

    


