import sys
from Qt.QtWidgets import QApplication, QWidget, QFileDialog


class FileExplore(QWidget):

    def __init__(self):
        super(FileExplore, self).__init__()
        self.fileEnding = ".error"

    def save_file_dialog(self, engine):
        print("this " + str(engine))
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        self.fileName = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                    engine.file_sort_config, options=options)

        if self.is_file_name_valid(engine):
            completeFileName = self.fileName[0] + self.fileEnding

            if completeFileName is not None and self.fileEnding != ".error":
                return completeFileName
            else:
                return "Error"

    def is_file_name_valid(self, engine):
        success = False

        for file_ending in engine.file_endings:
            if file_ending in self.fileName[0]:
                self.fileEnding = ""
                success = True
                break

            if file_ending in self.fileName[1]:
                self.fileEnding = file_ending
                success = True
                break

        if success:
            print("NICE")
            return True
        else:
            print("Either you exited the window or its not a maya file! Make sure you save in the correct Format")
            return False


if __name__ == '__main__':
    from pipeline.engine import get_engine

    app = QApplication(sys.argv)
    FE = FileExplore()
    name_of_file = FE.save_file_dialog(get_engine())
    sys.exit(app.exec_())
