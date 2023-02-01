import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr

from enum import Enum

import Common
import Ensemble
import EnsembleCommunication 


DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Exceptions as AerotechEnsembleExceptionsNET
except:
    raise RuntimeError

# * Checked
class Criticality(Enum):  # The criticality of an exception 
    FatalError=AerotechEnsembleExceptionsNET.Criticality.FatalError  # Error grave enough that the system cannot carry on operations 
    Error=AerotechEnsembleExceptionsNET.Criticality.Error  # The exception was caused by an error, the process failed 
    Message=AerotechEnsembleExceptionsNET.Criticality.Error  # The exception was caused by a message, the process succeeded but not fully  

# * Checked
class EnsembleException(Common.AerotechException):  # Represents software library errors 
    _EnsembleExceptionNET=None
    def __init__(self,EnsembleExceptionNET=AerotechEnsembleExceptionsNET.EnsembleException):
        self._EnsembleExceptionNET=EnsembleExceptionNET
        Common.AerotechException.__init__(self,EnsembleExceptionNET)
        
    @property    
    def Criticality(self):  # Specifies how severe the exception is  
        return Criticality[self._EnsembleExceptionNET.Criticality.ToString()]
    
    @property  
    def HelpKey(self):  # Specifies the key to look for in the help file for more detailed description 
        return self._EnsembleExceptionNET.HelpKey

# * Checked
class AeroBasicException(EnsembleException):  # Represents errors that occur due to operations with AeroBasic 
    _AeroBasicExceptionNET=None
    def __init__(self,AeroBasicExceptionNET=AerotechEnsembleExceptionsNET.AeroBasicException):
        self._AeroBasicExceptionNET=AeroBasicExceptionNET
        EnsembleException.__init__(self,AeroBasicExceptionNET)

# * Checked
class ControllerException(EnsembleException):  # Represents errors that occur when operating on a specific controller 
    _ControllerExceptionNET=None
    def __init__(self,ControllerExceptionNET=AerotechEnsembleExceptionsNET.ControllerException):
        self._ControllerExceptionNET=ControllerExceptionNET
        EnsembleException.__init__(self,ControllerExceptionNET)
        
    @property    
    def Controller(self):  # The controller that generated the exception  
        return Ensemble.Controller(self._ControllerExceptionNET.Controller)

# * Checked
class IOException(EnsembleException):  # Represents errors that occur during I/O operations 
    _IOExceptionNET=None
    def __init__(self,IOExceptionNET=AerotechEnsembleExceptionsNET.IOException):
        self._IOExceptionNET=IOExceptionNET
        EnsembleException.__init__(self,IOExceptionNET)

# * Checked
class NetworkException(EnsembleException):  # Represents errors that occur during use of network 
    _NetworkExceptionNET=None
    def __init__(self,NetworkExceptionNET=AerotechEnsembleExceptionsNET.NetworkException):
        self._NetworkExceptionNET=NetworkExceptionNET
        EnsembleException.__init__(self,NetworkExceptionNET)

# * Checked
class SoftwareEnvironmentException(EnsembleException):  # Represents errors that occur due to an invalid Software environment 
    _SoftwareEnvironmentExceptionNET=None
    def __init__(self,SoftwareEnvironmentExceptionNET=AerotechEnsembleExceptionsNET.SoftwareEnvironmentException):
        self._SoftwareEnvironmentExceptionNET=SoftwareEnvironmentExceptionNET
        EnsembleException.__init__(self,SoftwareEnvironmentExceptionNET)
   
# * Checked          
class CallbacksException(ControllerException):  # Represents errors that occur due to callbacks on a controller 
    _CallbacksExceptionNET=None
    def __init__(self,CallbacksExceptionNET=AerotechEnsembleExceptionsNET.CallbacksException):
        self._CallbacksExceptionNET=CallbacksExceptionNET
        ControllerException.__init__(self,CallbacksExceptionNET)

# * Checked
class CommunicationException(ControllerException):  # Represents errors that occur due to communication errors 
    _CommunicationExceptionNET=None
    def __init__(self,CommunicationExceptionNET=AerotechEnsembleExceptionsNET.CommunicationException):
        self._CommunicationExceptionNET=CommunicationExceptionNET
        ControllerException.__init__(self,CommunicationExceptionNET)

# * Checked       
class DataCollectionException(ControllerException):  # Represents errors that occur during operations of data collection 
    _DataCollectionExceptionNET=None
    def __init__(self,DataCollectionExceptionNET=AerotechEnsembleExceptionsNET.DataCollectionException):
        self._DataCollectionExceptionNET=DataCollectionExceptionNET
        ControllerException.__init__(self,DataCollectionExceptionNET)

# * Checked
class FileManagerException(ControllerException):  # Represents errors that occur during file operations on a controller 
    _FileManagerExceptionNET=None
    def __init__(self,FileManagerExceptionNET=AerotechEnsembleExceptionsNET.FileManagerException):
        self._FileManagerExceptionNET=FileManagerExceptionNET
        ControllerException.__init__(self,FileManagerExceptionNET)

# * Checked      
class ParameterException(ControllerException):  # Represents errors that occur due to operations on parameters 
    _ParameterExceptionNET=None
    def __init__(self,ParameterExceptionNET=AerotechEnsembleExceptionsNET.ParameterException):
        self._ParameterExceptionNET=ParameterExceptionNET
        ControllerException.__init__(self,ParameterExceptionNET)

# * Checked
class TaskException(ControllerException):  # Represents errors that occur due to operations on a task 
    _TaskExceptionNET=None
    def __init__(self,TaskExceptionNET=AerotechEnsembleExceptionsNET.TaskException):
        self._TaskExceptionNET=TaskExceptionNET
        ControllerException.__init__(self,TaskExceptionNET)
   
# * Checked 
class FileIOException(IOException):  # Represents errors that occur during file I/O operations 
    _FileIOExceptionNET=None
    def __init__(self,FileIOExceptionNET=AerotechEnsembleExceptionsNET.FileIOException):
        self._FileIOExceptionNET=FileIOExceptionNET
        IOException.__init__(self,FileIOExceptionNET)

# * Checked
class FileAccessFailureException(FileIOException):  # Represents errors that occur due to file access failure errors 
    _FileAccessFailureExceptionNET=None
    def __init__(self,FileAccessFailureExceptionNET=AerotechEnsembleExceptionsNET.FileAccessFailureException):
        self._FileAccessFailureExceptionNET=FileAccessFailureExceptionNET
        FileIOException.__init__(self,FileAccessFailureExceptionNET)
 
# * Checked       
class InvalidFileFormatException(FileIOException):  # Represents errors that occur due to invalid file format 
    _InvalidFileFormatExceptionNET=None
    def __init__(self,InvalidFileFormatExceptionNET=AerotechEnsembleExceptionsNET.InvalidFileFormatException):
        self._InvalidFileFormatExceptionNET=InvalidFileFormatExceptionNET
        FileIOException.__init__(self,InvalidFileFormatExceptionNET)

# * Checked       
class NetworkConnectionException(NetworkException):  # Represents errors that occur while establishing the connection over the network 
    _NetworkConnectionExceptionNET=None
    def __init__(self,NetworkConnectionExceptionNET=AerotechEnsembleExceptionsNET.NetworkConnectionException):
        self._NetworkConnectionExceptionNET=NetworkConnectionExceptionNET
        NetworkException.__init__(self,NetworkConnectionExceptionNET)

# * Checked
class NetworkSetupException(NetworkException):  # Represents errors that occur when the configuration of the network is invalid 
    _NetworkSetupExceptionNET=None
    def __init__(self,NetworkSetupExceptionNET=AerotechEnsembleExceptionsNET.NetworkSetupException):
        self._NetworkSetupExceptionNET=NetworkSetupExceptionNET
        NetworkException.__init__(self,NetworkSetupExceptionNET)

# * Checked       
class UnknownCommunicationTypeException(NetworkException):  # Represents errors that occur when the communication type specified is not supported by the library  
    _UnknownCommunicationTypeExceptionNET=None
    def __init__(self,UnknownCommunicationTypeExceptionNET=AerotechEnsembleExceptionsNET.UnknownCommunicationTypeException):
        self._UnknownCommunicationTypeExceptionNET=UnknownCommunicationTypeExceptionNET
        NetworkException.__init__(self,UnknownCommunicationTypeExceptionNET)
        
    @property    
    def CommunicationType(self):  # The communication type that is being used 
        return EnsembleCommunication.CommunicationType[self._UnknownCommunicationTypeExceptionNET.CommunicationType.ToString()]

# * Checked 
class DisconnectedException(CommunicationException):  # Represents errors that occur when trying to perform operations on a disconnected controller 
    _DisconnectedExceptionNET=None
    def __init__(self,DisconnectedExceptionNET=AerotechEnsembleExceptionsNET.DisconnectedException):
        self._DisconnectedExceptionNET=DisconnectedExceptionNET
        CommunicationException.__init__(self,DisconnectedExceptionNET)

# * Checked
class LostCommunicationException(CommunicationException):  # Represents errors that occur due to loss of communication 
    _LostCommunicationExceptionNET=None
    def __init__(self,LostCommunicationExceptionNET=AerotechEnsembleExceptionsNET.LostCommunicationException):
        self._LostCommunicationExceptionNET=LostCommunicationExceptionNET
        CommunicationException.__init__(self,LostCommunicationExceptionNET)

# * Checked
class InvalidParameterValueException(ParameterException):  # Represents errors that occur due to parameter values being invalid 
    _InvalidParameterValueExceptionNET=None
    def __init__(self,InvalidParameterValueExceptionNET=AerotechEnsembleExceptionsNET.InvalidParameterValueException):
        self._InvalidParameterValueExceptionNET=InvalidParameterValueExceptionNET
        ParameterException.__init__(self,InvalidParameterValueExceptionNET)

# * Checked
class TaskDebugException(TaskException):  # Represents errors that occur during debugging of a task 
    _TaskDebugExceptionNET=None
    def __init__(self,TaskDebugExceptionNET=AerotechEnsembleExceptionsNET.TaskDebugException):
        self._TaskDebugExceptionNET=TaskDebugExceptionNET
        TaskException.__init__(self,TaskDebugExceptionNET)

# * Checked
class TaskLoadException(TaskException):  # Represents errors that occur during loading of a task 
    _TaskLoadExceptionNET=None
    def __init__(self,TaskLoadExceptionNET=AerotechEnsembleExceptionsNET.TaskLoadException):
        self._TaskLoadExceptionNET=TaskLoadExceptionNET
        TaskException.__init__(self,TaskLoadExceptionNET)

# * Checked
class DebugStepException(TaskDebugException):  # Represents errors that occur during stepping of a task 
    _DebugStepExceptionNET=None
    def __init__(self,DebugStepExceptionNET=AerotechEnsembleExceptionsNET.DebugStepException):
        self._DebugStepExceptionNET=DebugStepExceptionNET
        TaskDebugException.__init__(self,DebugStepExceptionNET)

# * Checked
class DebugVariableException(TaskDebugException):  # Represents errors that occur during resolving of variables in a task 
    _DebugVariableExceptionNET=None
    def __init__(self,DebugVariableExceptionNET=AerotechEnsembleExceptionsNET.DebugVariableException):
        self._DebugVariableExceptionNET=DebugVariableExceptionNET
        TaskDebugException.__init__(self,DebugVariableExceptionNET)  