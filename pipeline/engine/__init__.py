import sys


def get_engine():
    if 'maya' in sys.executable:
        from pipeline.engine import maya_engine as me
        return me.MayaEngine()

    elif 'houdini' in sys.executable:
        from pipeline.engine import houdini_engine as he
        return he.HoudiniEngine()
    else:
        from pipeline.engine import base_engine as be
        print("NO ENGINE! OMG THE WORLD IS DESTROYED")
        return be.BaseEngine()


if __name__ == '__main__':
    result = get_engine()
    print(result)
