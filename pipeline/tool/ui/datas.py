import glob
import six

if six.PY2:
    from pathlib2 import Path
else:
    from pathlib import Path


hardCodedPath = "C:/Users/avish/Desktop/testingPython"


def get_files(file_end_text):
    if six.PY3:
        text_files = glob.glob(hardCodedPath + "/**/*{}".format(file_end_text), recursive=True)
        print(hardCodedPath + "/**/*{}".format(file_end_text))
        return text_files
    elif six.PY2:
        text_files = Path(hardCodedPath).rglob("**/*{}".format(file_end_text))
        #print(Path(hardCodedPath).rglob("**/*{}".format(file_end_text)))
        return list(text_files)

