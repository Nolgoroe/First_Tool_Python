import sys

# packagesPath = "C:/Users/avish/PycharmProjects/FirstProject/venv/Lib/site-packages"

projectPath = "C:/Users/avish/PycharmProjects/FirstProject"
# sys.path.append(packagesPath)
sys.path.append(projectPath)

from Qt import QtWidgets
from engine.enginePackagesRelaod import base_engine
from tool.ui import datas
import os


class ToolWindow(QtWidgets.QMainWindow):
    listOfAllItems = None

    def __init__(self):
        super(ToolWindow, self).__init__()
        # QtCompat.loadUi(str(ui_path), self)

        self.currentEngine = base_engine.GetEngine()

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Tool Window')
        self.layout = QtWidgets.QVBoxLayout()

        self.listItems = QtWidgets.QListWidget()
        self.layout.addWidget(self.listItems)

        self.cb = QtWidgets.QComboBox()
        self.cb.addItem("Please select which files to see in list")
        self.cb.addItems(self.currentEngine.FileEndings)
        self.cb.currentIndexChanged.connect(self.selectionchange)

        self.layout.addWidget(self.cb)

        self.listItems.show()

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.RefreshListWidget("")

        self.GenerateButton()

    def GenerateButton(self):
        for f in self.currentEngine.EngineImplementations:
            method = getattr(self.currentEngine, f)

            button = QtWidgets.QPushButton(str(f))

            button.clicked.connect(lambda b=button, m=method: self.clickit(b, m))

            self.layout.addWidget(button)

            button.setCheckable(True)

            button.show()

    def selectionchange(self, i):
        del list(self.listOfAllItems)[:]  # [:] SELECTS ALL ELEMENTS - CAN PUT SPECIFIC INDEX INSIDE
        self.listItems.clear()

        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index", i, "selection changed ", self.cb.currentText())

        if self.cb.currentText() == "All":
            file_ending_local = ""
        else:
            file_ending_local = self.cb.currentText()

        self.RefreshListWidget(file_ending_local)

    def clickit(self, button, method):
        button.toggle()
        index = self.listItems.currentRow()
        method(list(self.listOfAllItems)[index])

    def RefreshListWidget(self, endingText):
        self.listOfAllItems = datas.get_files(endingText)
        self.PopulateList()

    def PopulateList(self):
        for i in self.listOfAllItems:
            self.listItems.addItem(os.path.basename(str(i)))


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()
