# Script to set flask variables and run the flask file

import os
import platform

plt = platform.system()

# Windows
if plt == "Windows":
    print("Windows OS detected")
    os.system('set FLASK_APP=flaskr')
    os.system('flask run')

# Mac OS
elif plt == "Darwin":
    print("Mac OS detected")
# Linux
elif plt == "Linux":
    print("Linux OS deteted")
else:
    print("Operating System not detected")
