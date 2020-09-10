import os, subprocess

appdata = os.getenv('LOCALAPPDATA')
pyinstaller = (f"{appdata}\\Programs\\Python\\Python38-32\\Scripts\\pyinstaller.exe")

icon = os.path.abspath('gui\\icons\\BlackTraxIcon.ico')

subprocess.call(
[pyinstaller, 
"--distpath", "builds\\dist", 
"--workpath", "builds\\build", 
"--specpath", "builds\\build", 
"-F", 
"-w",
"--icon", icon,
"-n", "BlackTrax AP", 
"main.py"]
)
