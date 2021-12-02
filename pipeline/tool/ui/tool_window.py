import sys


# packagesPath = "C:/Users/avish/PycharmProjects/FirstProject/First_Tool_Python/venv/Lib/site-packages"
projectPath = "C:/Users/avish/PycharmProjects/FirstProject"
# sys.path.append(packagesPath)
sys.path.append(projectPath)

from Qt import QtWidgets
from pipeline.tool.ui import datas
import os
import  pipeline.engine as e

class ToolWindow(QtWidgets.QMainWindow):
    listOfAllItems = None

    def __init__(self):
        super(ToolWindow, self).__init__()
        # QtCompat.loadUi(str(ui_path), self)

        self.currentEngine = e.get_engine()
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('Tool Window')
        self.layout = QtWidgets.QVBoxLayout()

        self.listItems = QtWidgets.QListWidget()
        self.layout.addWidget(self.listItems)

        self.cb = QtWidgets.QComboBox()
        self.cb.addItem("Please select which files to see in list")
        self.cb.addItems(self.currentEngine.file_endings)
        self.cb.currentIndexChanged.connect(self.selection_change)

        self.layout.addWidget(self.cb)

        self.listItems.show()

        self.widget = QtWidgets.QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

        self.refresh_list_widget("")

        self.generate_button()

    def generate_button(self):
        for f in self.currentEngine.EngineImplementations:
            method = getattr(self.currentEngine, f)

            button = QtWidgets.QPushButton(str(f))

            button.clicked.connect(lambda b=button, m=method: self.click_it(b, m))

            self.layout.addWidget(button)

            button.setCheckable(True)

            button.show()

    def selection_change(self, i):
        del list(self.listOfAllItems)[:]  # [:] SELECTS ALL ELEMENTS - CAN PUT SPECIFIC INDEX INSIDE
        self.listItems.clear()

        for count in range(self.cb.count()):
            print(self.cb.itemText(count))
        print("Current index", i, "selection changed ", self.cb.currentText())

        if self.cb.currentText() == "All":
            file_ending_local = ""
        else:
            file_ending_local = self.cb.currentText()

        self.refresh_list_widget(file_ending_local)

    def click_it(self, button, method):
        button.toggle()

        method()

    def refresh_list_widget(self, endingText):
        self.listOfAllItems = datas.get_files(endingText)
        self.populate_list()

    def populate_list(self):
        for i in self.listOfAllItems:
            self.listItems.addItem(os.path.basename(str(i)))

    def get_selected_item_path(self):
        index = self.listItems.currentRow()
        return list(self.listOfAllItems)[index]


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    t = ToolWindow()
    t.show()
    app.exec_()
