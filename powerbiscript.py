import sys
import os

# add location to path so that modules can be imported
location = r'C:\...'
sys.path.append(location)

# change working directory so that json files can be opened
os.chdir(location)
    
from main import *