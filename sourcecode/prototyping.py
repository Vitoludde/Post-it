#%%

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize, Qt

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(320, 320))    
        self.setWindowTitle(" ") 

        self.line = QLineEdit(self)
        self.line.resize(320, 320)
        self.line.setAlignment(Qt.AlignLeft)
        self.line.setAlignment(Qt.AlignTop)

        f = self.line.font()
        f.setPointSize(16) # sets the size to 27
        self.line.setFont(f)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )


# %%
