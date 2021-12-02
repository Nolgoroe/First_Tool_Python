from pipeline.tool.ui import FileExplorerCode as fec


class BaseEngine(object):
    file_endings = [".py", ".txt"]
    EngineImplementations = ["save_file"]
    file_sort_config = "All Files (*);;Python Files (*.py);;Text files (*.txt)"

    def test(self, path):
        print(path)

    def save_file(self):
        nameOfFile = fec.FileExplore().save_file_dialog(self)  # Creates an instacne using the ()

        open(nameOfFile, 'w')
        print(nameOfFile)


if __name__ == '__main__':
    be = BaseEngine()
    FE = fec.FileExplore()

    be.save_file()
