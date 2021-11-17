import sys
from Qt.QtWidgets import QApplication, QWidget, QFileDialog
from Qt import QtWidgets


class File_Explore(QWidget):

    def __init__(self):
        #super().__init__(self)
        super(File_Explore, self).__init__()
        self.fileEnding = ".error"
        # self.title = 'File Explorer'
        # self.left = 10
        # self.top = 10
        # self.width = 640
        # self.height = 480
        # self.initUI()

    # def closeEvent(self, event):
    # event.accept()
    # print("X is clicked")

    # def initUI(self):
    # self.setWindowTitle(self.title)
    # self.setGeometry(self.left, self.top, self.width, self.height)

    # def openFileNameDialog(self):
    # self.show()
    # options = QFileDialog.Options()
    # options |= QFileDialog.DontUseNativeDialog
    # fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
    # "All Files (*);;Python Files (*.py)", options=options)
    # if fileName:
    #   print(fileName)

    # def openFileNamesDialog(self):
    # self.show()
    # options = QFileDialog.Options()
    # options |= QFileDialog.DontUseNativeDialog
    # files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
    # "All Files (*);;Python Files (*.py)", options=options)
    # if files:
    # print(files)

    def saveFileDialog(self, engine):
        # self.show()
        print("this " + engine)
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        if 'Maya Engine' in engine:
            self.fileName = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                        "All Files (*);;Maya Binary (*.mb);; Maya ASCII "
                                                        "(*.ma)", options=options)
            return self.saveFilesMaya()
        elif 'Houdini Engine' in engine:
            self.fileName = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                        "All Files (*);; Houdini Scenes (*.hip)", options=options)
            return self.saveFilesHoudini()

    def saveFilesMaya(self):
        if '.mb' in self.fileName[0] or '.ma' in self.fileName[0]:
            self.fileEnding = ""
        else:
            if 'mb' in self.fileName[1]:
                self.fileEnding = ".mb"
            elif 'ma' in self.fileName[1]:
                self.fileEnding = ".ma"
            else:
                print("Either you exited the window or its not a maya file! Make sure you save in the correct Format")

        completeFileName = self.fileName[0] + self.fileEnding

        if completeFileName is not None and self.fileEnding != ".error":
            return completeFileName
        else:
            return "Error"

    def saveFilesHoudini(self):
        if '.hip' in self.fileName[0]:
            self.fileEnding = ""
        else:
            if '.hip' in self.fileName[1]:
                self.fileEnding = ".hip"
            else:
                print("Either you exited the window or its not a maya file! Make sure you save in the correct Format")

        completeFileName = self.fileName[0] + self.fileEnding

        if completeFileName is not None and self.fileEnding != ".error":
            return completeFileName
        else:
            return "Error"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    FE = File_Explore()
    sys.exit(app.exec_())
