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
from aenum import extend_enum
from typing import Union

import Ensemble

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Firmware as AerotechEnsembleFirmwareNET
except:
    raise RuntimeError

# * Checked
class PluginType(Enum):  # Represents a type of plugin  
    E= AerotechEnsembleFirmwareNET.PluginType.E # Type E plugins 
    All= AerotechEnsembleFirmwareNET.PluginType.All # All types of plugins  
extend_enum(PluginType,'None',getattr(AerotechEnsembleFirmwareNET.PluginType,'None'))

# * Checked
class Debug():  # Provides the ability to debug the firmware 
    _DebugNET=None
    @multimethod
    def __init__(self,DebugNET:AerotechEnsembleFirmwareNET.Debug=AerotechEnsembleFirmwareNET.Debug):
        self._DebugNET=DebugNET
        
    @multimethod
    def __init__(self,Controller:object):
        self._DebugNET=AerotechEnsembleFirmwareNET.Debug(Controller._ControllerNET)
 
    def CommitFlash(self):  # Commits the flash memory to permanent storage on the master 
        self._DebugNET.CommitFlash()
    
    def CommitFlash(self,axisNumber:int):  # Commits the flash memory to permanent storage 
        self._DebugNET.CommitFlash(axisNumber)

    @property
    def Controller(self):  # Provides access to the Controller being debugged 
        return Ensemble.Controller(self._DebugNET.Controller)
    
    @multimethod
    def ReadFlash(self,address:int):  # Read flash of the master
        # TODO Need to deal with the TType 
        return self._DebugNET.ReadFlash(address)
        
    @multimethod
    def ReadFlash(self,axisNumber:int,address:int):  # Read flash
        # TODO Need to deal with the TType 
        return self._DebugNET.ReadFlash(axisNumber,address)
    
    def ReadMem(self,address:int):  # Read from memory 
        # TODO Need to deal with the TType
        return self._DebugNET.ReadMem(address)
        
    @multimethod
    def WriteFlash(self,address:int,value):  # Write flash on the master 
        # TODO Need to deal with the TType
        return 
    
    @multimethod
    def WriteFlash(self,axisNumber:int,address:int,value):  # Write flash 
        # TODO Need to deal with the TType
        return 
    
    def WriteMem(self,address:int,value):  # Write to memory 
        # TODO Need to deal with the TType
        return 
       
class Loader():  # Provides ability to update the firmware on the Controllers 
    _LoaderNET=None
    def __init__(self,LoaderNET=AerotechEnsembleFirmwareNET.Loader):
        self._LoaderNET=LoaderNET
        
    @multimethod
    def Commit(self): # Commits the loaded firmware on the controllers 
        return self._LoaderNET.Commit()
    
    @multimethod
    def Commit(self,progressChangedEventHandler:ProgressChangedEventHandler): # Commits the loaded firmware on the controllers 
        # TODO Fix the event handler declaration here (Might need a wrapper here)
        return self._LoaderNET.Commit(progressChangedEventHandler)
    
    @multimethod
    def Load(self,mlodFileName:str): # Loads the firmware on all connected Controllers 
        return self._LoaderNET.Load(mlodFileName)
    
    @multimethod
    def Load(self,mlodFileName:str, progressChangedEventHandler:ProgressChangedEventHandler): # Loads the firmware on all connected Controllers 
        # TODO Fix the event handler declaration here (Might need a wrapper here) 
        return self._LoaderNET.Load(mlodFileName,progressChangedEventHandler)
        
class PluginHandler():  # Helps with managing the plugins 
    _PluginHandlerNET=None
    @multimethod
    def __init__(self,PluginHandlerNET:AerotechEnsembleFirmwareNET.PluginHandler=AerotechEnsembleFirmwareNET.PluginHandler):
        self._PluginHandlerNET=PluginHandlerNET
        
    @multimethod
    def __init__(self,Controller):
        self._PluginHandlerNET=AerotechEnsembleFirmwareNET.PluginHandler(Controller._ControllerNET)
 
    def IsRunning(self,pluginType:PluginType): # The plugin type to check if it is running  
        return AerotechEnsembleFirmwareNET.IsRunning(pluginType.value)