from pipeline.tool.ui import FileExplorerCode as fec
from pipeline.tool.ui import tool_window as tw

try:
    import pymel.core as pm
except:
    pm = None
    print("PM IN NONE")

from pipeline.engine import base_engine


class MayaEngine(base_engine.BaseEngine):
    EngineImplementations = ["open_file", "open_file_reference", "save_file"]
    file_endings = [".mb", ".ma"]
    file_sort_config = "All Files (*);;Maya Binary (*.mb);; Maya ASCII (*.ma)"

    #def __init__(self):
    #    super(MayaEngine, self).__init__()

    def open_file(self):
        path = tw.ToolWindow.get_selected_item_path()
        pm.openFile(path, force=True, loadReferenceDepth="all")

    def open_file_reference(self):
        path = tw.ToolWindow.get_selected_item_path()
        pm.createReference(path, loadReferenceDepth="all")

    def save_file(self):
        nameOfFile = fec.File_Explore().save_file_dialog("Maya Engine")  # Creates an instacne using the ()

        print(nameOfFile)
        if nameOfFile != 'Error':
            pm.saveAs(nameOfFile)
        else:
            print("ERROR in the naming of save file")

