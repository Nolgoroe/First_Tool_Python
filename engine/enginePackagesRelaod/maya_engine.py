from tool.ui import FileExplorerCode as fec

try:
    import pymel.core as pm
except:
    pm = None
    print("PM IN NONE")

from engine.enginePackagesRelaod import base_engine


class MayaEngine(base_engine.BaseEngineClass):
    EngineImplementations = ["open_file", "open_file_reference", "save_file"]
    FileEndings = ["All", ".mb", ".ma"]

    def __init__(self):
        super(MayaEngine, self).__init__()

    def open_file(self, path):
        pm.openFile(path, force=True, loadReferenceDepth="all")

    def open_file_reference(self, path):
        pm.createReference(path, loadReferenceDepth="all")

    def save_file(self, path):
        nameOfFile = fec.File_Explore().saveFileDialog("Maya Engine")  # Creates an instacne using the ()
        print(nameOfFile)
        if nameOfFile != 'Error':
            pm.saveAs(nameOfFile)
        else:
            print("ERROR in the naming of save file")
