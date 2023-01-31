import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32,Decimal,Double

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

from GlobalLogger import GlobalLogger

import time

from multimethod import multimethod

from enum import Enum
from aenum import extend_enum

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
DEFAULT_DLL_NAME:str='Aerotech.Common'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Common as AerotechCommonNET
except:
    raise RuntimeError

Exception


class AerotechException():  # Represents an exception thrown by Aerotech, Inc. products 
     AerotechException()()()()  Default constructor 
 
  AerotechException(String)  Instantiates the exception with a given message 
 
  AerotechException(String, Exception)  Instantiates the exception with a given message and an inner exception 
 
  AerotechException(SerializationInfo, StreamingContext)  For serialization purposes 
 
      @property
    def Data  Gets a collection of key/value pairs that provide additional, user-defined information about the exception.
(Inherited from Exception.)
 

  GetBaseException()()()()  When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions.
(Inherited from Exception.)
 
 
  GetObjectData(SerializationInfo, StreamingContext)  When overridden in a derived class, sets the SerializationInfo with information about the exception.
(Inherited from Exception.)
 
  GetType()()()()  Gets the runtime type of the current instance.
(Inherited from Exception.)
 
      @property
    def HelpLink  Gets or sets a link to the help file associated with this exception.
(Inherited from Exception.)
 
      @property
    def HResult  Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception.
(Inherited from Exception.)
 
    @property
    def InnerException  Gets the Exception instance that caused the current exception.
(Inherited from Exception.)
 
    @property
    def Message  Gets a message that describes the current exception.
(Inherited from Exception.)
 
    @property
    def Source  Gets or sets the name of the application or the object that causes the error.
(Inherited from Exception.)
 
    @property
    def StackTrace  Gets a string representation of the frames on the call stack at the time the current exception was thrown.
(Inherited from Exception.)
 
    @property
    def TargetSite  Gets the method that throws the current exception.
(Inherited from Exception.)
 
  ToString()()()()  Creates and returns a string representation of the current exception.
(Inherited from Exception.) 

class Calibration():  # Processes axis calibration files
    _CalibrationNET=None
    def __init__(self,CalibrationNET=None):
        self._CalibrationNET=CalibrationNET
        
    @classmethod
    def GetFormat(self,path:str):  # Specifies the format of a calibration file
        return CalibrationFileFormat[self._CalibrationNET.GetFormat(path).ToString()]
    @classmethod
    def Process(self,fileName:str):  # Processes an axis calibration file  
        return self._CalibrationNET.Process(fileName)
 
class CalibrationFileFormat(Enum):  # Specifies the calibration file format
    Calibration1D=AerotechCommonNET.CalibrationFileFormat.Calibration1D  # 1 dimensional calibration file format
    Calibration2D=AerotechCommonNET.CalibrationFileFormat.Calibration2D  # 2 dimensional calibration file format
    Unknown=AerotechCommonNET.CalibrationFileFormat.UnknownD  # Unknown/Invalid calibration file format 

class Camming():  # Processes axis camming files 
    _CammingNET=None
    def __init__(self,CammingNET=None):
        self._CammingNET=CammingNET
        
    @classmethod
    def Process(self,filename:str):
        return self._CammingNET.Process(filename)
    
class FilePoint():  # Represents a position in a file (by line number) 
    _FilePointNET=None
    @multimethod
    def __init__(self,FilePointNET=AerotechCommonNET.FilePoint):
        self._FilePointNET=FilePointNET
        
    @multimethod   
    def __init__(self,path:str,line:int):
        FilePoint(self._FilePointNET.FilePoint(path, line))  # Creates a new file point given name and line number 
    
    def Clone(self):  # Clones the current object 
        FilePoint(self._FilePointNET.Clone())

    @property
    def LineNumber(self):  # Returns the line number 
        return self._FilePointNET.LineNumber

    @property
    def Path(self):  # Returns the path to the file
        return self._FilePointNET.Path  
 
class INamed():  # Represents a named object  
    def __init__(self,TName,pyClass):
        self.TName,=TName,
        self.pyClass=pyClass
        
    @property
    def Name (self):
        return self.pyClass(self.TName.Name)
