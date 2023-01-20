import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import pythonnet
import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32,Enum,Decimal

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

from GlobalLogger import GlobalLogger

import time

class AerotechEnsemble():
    defaultPath:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
    controllerDllName:str='Aerotech.Ensemble'
    controllerDllVersion:str=''
    controllerNET=None
    controllerAxes=None
    
    
    logger=GlobalLogger.logger_init()
    
    def __init__(self):
        pass
    
    def enableAxes(self,axes):
        Axis.X.Motion.Enable()
        Axis.Y.Motion.Enable()
        Axis.Z.Motion.Enable()
        
    def enableAxis(self):
        pass
    
    def moveAxisRelative(self):
        pass
    
    def moveAxesRelative(self):
        pass
    
    def moveAxisAbsolute(self):
        pass
    
    def moveAxesAbsolute(self):
        pass
    
    def getAxisPosition(self):
        pass
    
    def getAxesPosition(self):
        pass
    
    def getAxisCurrent(self):
        pass
    
    def getAxesCurrent(self):
        pass
    

    @classmethod
    def connect(cls,index:int=0,libraryPath:str=defaultPath):
        if libraryPath.upper() not in [path.upper() for path in sys.path]:
            sys.path.extend(libraryPath)
            
        try:
            clr.AddReference(cls.controllerDllName)
            from Aerotech.Ensemble import Controller
            Controller.Connect()
            cls.controllerNET=Controller.ConnectedControllers.get_Item(index)
            cls.controllerAxes=cls.controllerNET.Commands.Axes
            cls.driverVersion=cls.getVersionNumber(os.path.join(libraryPath,cls.controllerDllName + '.dll'))
            cls.logger.info(f'|{cls.__name__}| Aerotech Ensemble Driver Successfully Loaded.')
            cls.logger.info(f'|{cls.__name__}| Aerotech Ensemble Driver version: {cls.driverVersion}.')
        except:
            cls.logger.error(f'|{cls.__name__}| Unable to load Aerotech Ensemble Driver.')

        return cls()
            
    @staticmethod
    def getVersionNumber(filename):
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return ".".join([str(HIWORD (ms)), str(LOWORD (ms)), str(HIWORD (ls)), str(LOWORD (ls))])
            
if __name__=='__main__':
    stage=AerotechEnsemble.connect()
    a=1