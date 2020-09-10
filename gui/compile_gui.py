import subprocess

ui_file = "gui\\mainwindow.ui"
ui_python = "gui\\mainwindow.py"
subprocess.call(['pyside2-uic', ui_file, ">", ui_python], shell=True)

resource_path = "gui\\resources.qrc"
resource_python = "gui\\resources_rc.py"
subprocess.call(["pyside2-rcc", "-o", resource_python, resource_path], shell=True)

with open(ui_python, 'rt') as read_file:
    read = read_file.read()
    new = read.replace("resources_rc", "gui.resources_rc")
    with open(ui_python, 'wt') as write_file:
        write_file.writelines(new)
