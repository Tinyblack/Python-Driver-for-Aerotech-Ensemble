import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32,Enum,Decimal,Double

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

from GlobalLogger import GlobalLogger

import time

from multimethod import multimethod

import Common
import CommonCollections
import EnsembleCommands 
import EnsembleCommunication 
import EnsembleConfiguration  
import EnsembleDataCollection
import EnsembleExceptions
import EnsembleFileSystem
import EnsembleFirmware
import EnsembleInformation
import EnsembleParameters
import EnsembleStatus
import EnsembleTasks
import EnsembleTasksDebug

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble as AerotechEnsembleNET

except:
    raise RuntimeError
        

class AxisMask():
    _AxisMaskNET=None
    
    NONE= getattr(AerotechEnsembleNET.AxisMask,'None')
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
    
    def __init__(self,AxisMask):
        self._AxisMaskNET=AxisMask
    

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
        return None

    @classmethod  
    @property
    def ConnectedControllers(cls):
        return CommonCollections.INamedConstantCollection(Controller.ConnectedControllers,cls)

    @classmethod
    def Connect(cls):
        Controller.Connect()

    @property
    def ControlCenter(self):
        pass # To collections
    
    @property
    def DataCollection(self):
        pass # To collections
    
    @classmethod
    def Disconnect(cls):
        Controller.Connect()
    
    def EnumerateAxes(self):
        self._ControllerNET.EnumerateAxes()

    @property
    def FileManager(self):
        pass # To collections
    
    @classmethod
    def Identify(cls):
        pass

    @property
    def Information(self):
        pass # To collections
    
    @property
    def IsConnected(self):
        return self._ControllerNET.IsConnected()

    #def IsConnectedChanged  Raised when IsConnected changes 

    #def INamed<(Of <<'(String>)>>)..::..Name
    
    @property
    def Parameters(self):
        pass # To collections

    @multimethod
    def Reset(self):
        self._ControllerNET.Reset()
    
    @multimethod
    def Reset(self,restartPrograms:bool):
        self._ControllerNET.Reset(restartPrograms)
        
    @property
    def Tasks(self):
        pass # To collections
    
class ServoRateParameter():
    OnekHz=ServoRateParameter.OnekHz
    TwokHz=ServoRateParameter.TwokHz
    FourkHz=ServoRateParameter.FourkHz
    FivekHz=ServoRateParameter.FivekHz
    TenkHz=ServoRateParameter.TenkHz
    TwentykHz=ServoRateParameter.TwentykHz
    
class TaskId():
    TLibrary=TaskId.TLibrary
    T01=TaskId.T01
    T02=TaskId.T02
    T03=TaskId.T03
    T04=TaskId.T04
    TAuxiliary=TaskId.TAuxiliary
    
class SoftwareEnvironment():
        # @classmethod
        # @property
        # This is equivalent to [static public property] in a certain namespace

        @classmethod
        @property
        def BinDir(cls):
            return SoftwareEnvironment.BinDir 
        
        @classmethod
        @property
        def InstallDir(cls):
            return SoftwareEnvironment.InstallDir 
        
        @classmethod
        @property
        def IsLoaderRunning(cls):
            return SoftwareEnvironment.IsLoaderRunning 
        
        @classmethod
        @property
        def NumberOfProcesses(cls):
            return SoftwareEnvironment.NumberOfProcesses 
        
        @classmethod
        @property
        def ProductKey(cls):
            return SoftwareEnvironment.ProductKey 
        
        @classmethod
        @property
        def Version(cls):
            return SoftwareEnvironment.Version 
    
if __name__=='__main__':

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