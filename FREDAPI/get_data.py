from fredapi import Fred
import os
import matplotlib.pyplot as plt
import pandas as plt
#%matplotlib inline


API_KEY = os.environ.get("FRED_API_KEY")

# Create fred obj
fred = Fred(api_key=API_KEY)

# Querry some data
data = fred.search("S&P")
print(data)
