import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr

from multimethod import multimethod

from enum import Enum
from aenum import extend_enum

import CommonCollections
import EnsembleCommands 
import EnsembleCommunication 
import EnsembleDataCollection
import EnsembleFileSystem
import EnsembleInformation
import EnsembleParameters
import EnsembleStatus
import EnsembleTasks


DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble as AerotechEnsembleNET
except:
    raise RuntimeError
        
# * Checked
class AxisMask(Enum):    
    A0=AerotechEnsembleNET.AxisMask.A0
    A1=AerotechEnsembleNET.AxisMask.A1
    A2=AerotechEnsembleNET.AxisMask.A2
    A3=AerotechEnsembleNET.AxisMask.A3
    A4=AerotechEnsembleNET.AxisMask.A4
    A5=AerotechEnsembleNET.AxisMask.A5
    A6=AerotechEnsembleNET.AxisMask.A6
    A7=AerotechEnsembleNET.AxisMask.A7
    A8=AerotechEnsembleNET.AxisMask.A8
    A9=AerotechEnsembleNET.AxisMask.A9
    ALL=AerotechEnsembleNET.AxisMask.All
extend_enum(AxisMask,'None',getattr(AerotechEnsembleNET.AxisMask,'None'))

# * Checked
class Controller():
    _ControllerNET:AerotechEnsembleNET.Controller=None
    def __init__(self,controller):
        self._ControllerNET=controller

    def ChangePassword(self,oldPassword:str,newPassword:str):
        self._ControllerNET.ChangePassword(oldPassword,newPassword)

    @property
    def Commands(self):
        return EnsembleCommands.RootCommands(self._ControllerNET)

    @classmethod
    @property
    def Configuration(cls):
        return EnsembleCommunication.NetworkSetup(AerotechEnsembleNET.Controller.Configuration)
    
    @classmethod
    def Connect(cls):
        return CommonCollections.NamedConstantCollection(AerotechEnsembleNET.Controller.Connect(),cls)

    @classmethod  
    @property
    def ConnectedControllers(cls):
        return CommonCollections.NamedConstantCollection(AerotechEnsembleNET.Controller.ConnectedControllers,cls)

    @property
    def ControlCenter(self):
        return EnsembleStatus.ControlCenter(self._ControllerNET.DataCollection)
    
    @property
    def DataCollection(self):
        return EnsembleDataCollection.Data(self._ControllerNET.DataCollection)
    
    @classmethod
    def Disconnect(cls):
        cls._ControllerNET.Disconnect()
    
    def EnumerateAxes(self):
        self._ControllerNET.EnumerateAxes()

    @property
    def FileManager(self):
        return EnsembleFileSystem.FileManager(self._ControllerNET.FileManager)
    
    @classmethod
    def Identify(cls):
        return CommonCollections.NamedConstantCollection(AerotechEnsembleNET.Controller.Identify(),EnsembleCommunication.NetworkNode)

    @property
    def Information(self):
        EnsembleInformation.ControllerInformation(self._ControllerNET.Information)
    
    @property
    def IsConnected(self):
        return self._ControllerNET.IsConnected()

    #def IsConnectedChanged  Raised when IsConnected changes 

    #def INamed<(Of <<'(String>)>>)..::..Name
    
    @property
    def Parameters(self):
        EnsembleParameters.ControllerParameters(self._ControllerNET.Parameters)

    @multimethod
    def Reset(self):
        self._ControllerNET.Reset()
    
    @multimethod
    def Reset(self,restartPrograms:bool):
        self._ControllerNET.Reset(restartPrograms)
        
    @property
    def Tasks(self):
        return EnsembleTasks.TasksCollection(self._ControllerNET.Tasks)
    
# * Checked
class ServoRateParameter(Enum):
    OnekHz=AerotechEnsembleNET.ServoRateParameter.OnekHz
    TwokHz=AerotechEnsembleNET.ServoRateParameter.TwokHz
    FourkHz=AerotechEnsembleNET.ServoRateParameter.FourkHz
    FivekHz=AerotechEnsembleNET.ServoRateParameter.FivekHz
    TenkHz=AerotechEnsembleNET.ServoRateParameter.TenkHz
    TwentykHz=AerotechEnsembleNET.ServoRateParameter.TwentykHz

# * Checked
class TaskId(Enum):
    TLibrary=AerotechEnsembleNET.TaskId.TLibrary
    T01=AerotechEnsembleNET.TaskId.T01
    T02=AerotechEnsembleNET.TaskId.T02
    T03=AerotechEnsembleNET.TaskId.T03
    T04=AerotechEnsembleNET.TaskId.T04
    TAuxiliary=AerotechEnsembleNET.TaskId.TAuxiliary
    
# * Checked 
class SoftwareEnvironment():
    _SoftwareEnvironmentNET=None
    def __init__(self,SoftwareEnvironmentNET=AerotechEnsembleNET.SoftwareEnvironment):
        self._SoftwareEnvironmentNET=SoftwareEnvironmentNET
        
    @property
    def BinDir(self):
        return self._SoftwareEnvironmentNET.BinDir 
    
    @property
    def InstallDir(self):
        return self._SoftwareEnvironmentNET.InstallDir 
    
    @property
    def IsLoaderRunning(self):
        return self._SoftwareEnvironmentNET.IsLoaderRunning 
    
    @property
    def NumberOfProcesses(self):
        return self._SoftwareEnvironmentNET.NumberOfProcesses 
    
    @property
    def ProductKey(self):
        return self._SoftwareEnvironmentNET.ProductKey 
    
    @property
    def Version(self):
        return self._SoftwareEnvironmentNET.Version 
    
if __name__=='__main__':
    
    print(SoftwareEnvironment.BinDir)
    print(SoftwareEnvironment.InstallDir)
    print(SoftwareEnvironment.IsLoaderRunning)
    print(SoftwareEnvironment.NumberOfProcesses)
    print(SoftwareEnvironment.ProductKey)
    print(SoftwareEnvironment.Version)

    Controller.Connect()
    controller=Controller.ConnectedControllers[0]
    controller.Commands.Motion.Enable(0)
    controller.Commands.Motion.Enable("Y")
    controller.Commands.Motion.Enable(AxisMask.A2)

    controller.Commands.Motion.Home(0)
    controller.Commands.Motion.Home("Y")
    controller.Commands.Motion.Home(AxisMask.A2)

    controller.Commands.Motion.Disable(0)
    controller.Commands.Motion.Disable("Y")
    controller.Commands.Motion.Disable(AxisMask.A2)
    
    a=1