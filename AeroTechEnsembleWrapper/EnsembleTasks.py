import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System.ComponentModel import ProgressChangedEventHandler

from multimethod import multimethod
from enum import Enum

import Ensemble
import EnsembleTasksDebug
import EnsembleStatus
import EnsembleFileSystem
import CommonCollections

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Tasks as AerotechEnsembleTasksNET
except:
    raise RuntimeError

# ! DONE

class TaskState(Enum):
    Inactive=AerotechEnsembleTasksNET.TaskState.Inactive
    Idle=AerotechEnsembleTasksNET.TaskState.Idle
    ProgramReady=AerotechEnsembleTasksNET.TaskState.ProgramReady
    ProgramRunning=AerotechEnsembleTasksNET.TaskState.ProgramRunning
    ProgramPaused=AerotechEnsembleTasksNET.TaskState.ProgramPaused
    ProgramComplete=AerotechEnsembleTasksNET.TaskState.ProgramComplete
    Error=AerotechEnsembleTasksNET.TaskState.Error
    RunningPlugin=AerotechEnsembleTasksNET.TaskState.RunningPlugin

class VariableScope(Enum):
    Global=AerotechEnsembleTasksNET.VariableScope.Global
    Argument=AerotechEnsembleTasksNET.VariableScope.Argument
    Local=AerotechEnsembleTasksNET.VariableScope.Local

class VariableType(Enum):
    Integer=AerotechEnsembleTasksNET.VariableType.Integer
    Long=AerotechEnsembleTasksNET.VariableType.Long
    Double=AerotechEnsembleTasksNET.VariableType.Double
    Float=AerotechEnsembleTasksNET.VariableType.Float
    String=AerotechEnsembleTasksNET.VariableType.String
    Struct=AerotechEnsembleTasksNET.VariableType.Struct
    Array=AerotechEnsembleTasksNET.VariableType.Array

class DedicatedJoystick():
    _DedicatedJoystickNET=None
    def __init__(self,DedicatedJoystickNET=AerotechEnsembleTasksNET.DedicatedJoystick):
        self._DedicatedJoystickNET=DedicatedJoystickNET

    @multimethod
    def Start(self):
        self._DedicatedJoystickNET.Start()
        
    @multimethod
    def Start(self, pairNumber:int):
        self._DedicatedJoystickNET.Start(pairNumber)

    def Stop(self):
        self._DedicatedJoystickNET.Stop()
 
class Program():
    _ProgramNET=None
    def __init__(self,ProgramNET=AerotechEnsembleTasksNET.Program):
        self._ProgramNET=ProgramNET
        
    @property
    def Debug(self):
        EnsembleTasksDebug.ProgramDebug(self._ProgramNET.Debug)
    
    @property
    def Error(self):
        EnsembleStatus.ErrorInformation(self._ProgramNET.Error)

    @property
    def FileName(self):
        return self._ProgramNET.FileName
    
    @multimethod
    def Load(self,fileName:str):
        return self._ProgramNET.Load(fileName)

    @multimethod
    def Load(self,fileName:str, ProgressChangedEventHandler:ProgressChangedEventHandler):
        # TODO Fix the event handler declaration here (Might need a wrapper here)
        return self._ProgramNET.Load(fileName,ProgressChangedEventHandler)

    @multimethod
    def Run(self,fileInfo:EnsembleFileSystem.FileInfo):
        self._ProgramNET.Run(fileInfo._FileInfoNET)

    @multimethod
    def Run(self,fileName:str):
        return self._ProgramNET.Run(fileName)

    @multimethod
    def Run(self,fileName:str, ProgressChangedEventHandler:ProgressChangedEventHandler):
        # TODO Fix the event handler declaration here (Might need a wrapper here)
        return self._ProgramNET.Run(fileName,ProgressChangedEventHandler)

    def Start(self):
        self._ProgramNET.Start()
    
    def Stop(self):
        self._ProgramNET.Stop()
 
class Task():
    _TaskNET=None
    def __init__(self,TaskNET=AerotechEnsembleTasksNET.Task):
        self._TaskNET=TaskNET
        
    @property
    def DedicatedJoystick(self):
        return DedicatedJoystick(self._TaskNET.DedicatedJoystick)
 
    @property
    def Name(self):
        return Ensemble.TaskId[self._TaskNET.Name.ToString()]

    @property
    def Program(self):
        return Program(self._TaskNET.Program)
    
    @property
    def State(self):
        return TaskState[self._TaskNET.State.ToString()]
 
class TasksCollection():
    _TasksCollectionNET=None
    
    def __init__(self,TasksCollectionNET=AerotechEnsembleTasksNET.TasksCollection):
        self._TasksCollectionNET=TasksCollectionNET
        
    @property
    def States(self):
        return CommonCollections.INamedConstantCollection(self._TasksCollectionNET.States,TaskState)
    
    @multimethod
    def StopPrograms(self):
        self._TasksCollectionNET.StopPrograms()
        
    @multimethod
    def StopPrograms(self,taskIds:list[Ensemble.TaskId]):
        for taskId in taskIds:
            self._TasksCollectionNETStopPrograms(taskId.value)
        
if __name__=='__main__':
    a=1