import sys


class BaseEngineClass(object):
    EngineImplementations = ["open_file", "save_file"]


def GetEngine():
    if 'maya' in sys.executable:
        from engine.enginePackagesRelaod import maya_engine as me
        return me.MayaEngine()

    elif 'houdini' in sys.executable:
        from engine.enginePackagesRelaod import houdini_engine as he
        return he.houdini_engine()
    else:
        from engine.enginePackagesRelaod import maya_engine as me
        print("NO ENGINE! OMG THE WORLD IS DESTROYED")
        return me.MayaEngine()


if __name__ == '__main__':
    GetEngine()
