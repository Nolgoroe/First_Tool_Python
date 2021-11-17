from tool.ui import FileExplorerCode as fec

try:
    import hou as h
except:
    h = None
    print("NO HOUDINI!")

from engine.enginePackagesRelaod import base_engine

class houdini_engine(base_engine.BaseEngineClass):
    EngineImplementations = ["open_file", "open_file_merge", "save_file"]
    FileEndings = ["All", ".hip"]

    def __init__(self):
        super(houdini_engine, self).__init__()

    def open_file(self, path):
        h.hipFile.load(str(path), suppress_save_prompt=True)

    def open_file_merge(self, path):
        print("MERGE")
        h.hipFile.merge(str(path))

    def save_file(self, path):
        nameOfFile = fec.File_Explore().saveFileDialog("Houdini Engine")  # Creates an instacne using the ()

        if nameOfFile != 'Error':
            print("Saved!")
            h.hipFile.save(file_name=nameOfFile, save_to_recent_files=True)
        else:
            print("ERROR in the naming of save file")
