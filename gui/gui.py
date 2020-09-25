from PySide2.QtCore import QFileInfo, QThreadPool, Slot
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox

import engine
import gui.mainwindow

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.threadpool = QThreadPool.globalInstance()
        self.ui = gui.mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

        self.default_folder = ""
        self.selected_file = ""
        
        self.signals()

    def signals(self):
        """Watches for button pushes."""

        self.ui.oldWYGBrowseButton.clicked.connect(lambda : self.browse_file("oldWYGFile", "CSV File (*.csv)"))
        self.ui.newWYGBrowseButton.clicked.connect(lambda : self.browse_file("newWYGFile", "CSV File (*.csv)"))
        self.ui.btCalBrowseButton.clicked.connect(lambda : self.browse_file("btCalFile", "BlackTrax Calibration File (*.btcal)"))

        self.ui.generateButton.clicked.connect(self.generate_patch)

    @Slot()
    def browse_file(self, label, file_filter):
        """Opens a browse menu to select a file."""
              
        # Opens browse menu with the last used file path selected (if it exsits)
        file_name = QFileDialog.getOpenFileName(
            self, 
            "Browse", 
            self.default_folder,
            file_filter
        )

        # Store last used path for next open
        if file_name[0] != "":
            self.default_folder = QFileInfo(file_name[0]).path()
            self.selected_file = file_name[0]
            getattr(self.ui, label).setText(file_name[0])

    def pop_up(self, title, message):
        """Displays a message with the title and message."""

        # Generate pop up with title, message, an info icon, and an OK button
        pop_up = QMessageBox(self)
        pop_up.setWindowTitle(title)
        pop_up.setText(message)
        pop_up.setStandardButtons(QMessageBox.Ok)
        pop_up.setIcon(QMessageBox.Information)

        pop_up.exec()
    
    def generate_patch(self):
        """Prompts the user to browse for an output and starts process."""

        validation = [
            self.ui.oldWYGFile.text(),
            self.ui.newWYGFile.text(),
            self.ui.btCalFile.text()
        ]

        # Don't continue if not all files are selected
        if "No File Loaded" in validation:
            self.pop_up("Files Aren't Selected", "Not all input files were selected. Please browse for all three input files above and try again.")
            return

        # Browse for output
        output_file = QFileDialog.getSaveFileName(
            self, 
            "Save File", 
            self.default_folder,
            "BlackTrax Calibration File (*.btcal)"
        )

        engine.generate_patch(
            self.ui.oldWYGFile.text(),
            self.ui.newWYGFile.text(),
            self.ui.btCalFile.text(),
            output_file[0]
        )

        # Great success!
        self.pop_up("Output Successful", """The file was updated successfully. 
        
You may now import this into BlackTrax by going to File - Import - Fixture Calibration.""")
