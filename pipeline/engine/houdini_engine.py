from pipeline.tool.ui import FileExplorerCode as fec
from pipeline.tool.ui import tool_window as tw

try:
    import hou as h
except:
    h = None
    print("NO HOUDINI!")

from pipeline.engine import base_engine


class HoudiniEngine(base_engine.BaseEngine):
    EngineImplementations = ["open_file", "open_file_merge", "save_file"]
    FileEndings = [".hip"]
    file_sort_config = "All Files (*);; Houdini Scenes (*.hip)"

    def open_file(self):
        path = tw.ToolWindow.get_selected_item_path()
        h.hipFile.load(str(path), suppress_save_prompt=True)

    def open_file_merge(self):
        print("MERGE")
        path = tw.ToolWindow.get_selected_item_path()
        h.hipFile.merge(str(path))

    def save_file(self):
        nameOfFile = fec.File_Explore().save_file_dialog("Houdini Engine")  # Creates an instacne using the ()

        if nameOfFile != 'Error':
            print("Saved!")
            h.hipFile.save(file_name=nameOfFile, save_to_recent_files=True)
        else:
            print("ERROR in the naming of save file")