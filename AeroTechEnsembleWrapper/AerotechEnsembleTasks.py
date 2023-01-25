import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32,Enum,Decimal,Double
from System.ComponentModel import ProgressChangedEventHandler

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

from GlobalLogger import GlobalLogger

import time

from multimethod import multimethod

from collections.abc import Sequence

import AerotechCommonCollections

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    from Aerotech.Ensemble import Tasks
    from Aerotech.Ensemble.Tasks import TaskState,VariableScope,VariableType
except:
    raise RuntimeError

##################

class DedicatedJoystick():

    @multimethod
    def Start(self):
        Tasks.DedicatedJoystick.Start()
    @multimethod
    def Start(self, pairNumber:int):
        Tasks.DedicatedJoystick.Start(pairNumber)

    def Stop(self):
        Tasks.DedicatedJoystick.Stop()
 
class Program():
    def Debug(self):
        pass
    
    def Error(self):
        pass
    
    @property
    def FileName(self):
        return Tasks.Program.FileName
    
    @multimethod
    def Load(self,fileName:str):
        return Tasks.Program.Load(fileName)

    @multimethod
    def Load(self,fileName:str, ProgressChangedEventHandler:ProgressChangedEventHandler):
        return Tasks.Program.Load(fileName,ProgressChangedEventHandler)

    @multimethod
    def Run(self,FileInfo):
        pass

    @multimethod
    def Run(self,fileName:str):
        return Tasks.Program.Run(fileName)

    @multimethod
    def Run(self,fileName:str, ProgressChangedEventHandler:ProgressChangedEventHandler):
        return Tasks.Program.Run(fileName,ProgressChangedEventHandler)

    def Start():
        Tasks.Program.Start()
    
    def Stop():
        Tasks.Program.Stop()
 
class Task():
    def __init__(self):
        pass
 
class TasksCollection():
    def __init__(self):
        pass
    
class TaskState():
    Inactive=TaskState.Inactive
    Idle=TaskState.Idle
    ProgramReady=TaskState.ProgramReady
    ProgramRunning=TaskState.ProgramRunning
    ProgramPaused=TaskState.ProgramPaused
    ProgramComplete=TaskState.ProgramComplete
    Error=TaskState.Error
    RunningPlugin=TaskState.RunningPlugin

class VariableScope():
    Global=VariableScope.Global
    Argument=VariableScope.Argument
    Local=VariableScope.Local

class VariableType():
    Integer=VariableType.Integer
    Long=VariableType.Long
    Double=VariableType.Double
    Float=VariableType.Float
    String=VariableType.String
    Struct=VariableType.Struct
    Array=VariableType.Array


if __name__=='__main__':
    a=1