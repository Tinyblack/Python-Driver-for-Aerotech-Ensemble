import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
import System

from multimethod import multimethod

from enum import Enum

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Common'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Common as AerotechCommonNET
except:
    raise RuntimeError

# * Checked
class AerotechException():  # Represents an exception thrown by Aerotech, Inc. products 
    _AerotechExceptionNET=None
    @multimethod
    def __init__(self,AerotechExceptionNET=AerotechCommonNET.AerotechException):
        self._AerotechExceptionNET=AerotechExceptionNET
        
    @multimethod
    def __init__(self):  # Default constructor 
        self._AerotechExceptionNET=AerotechCommonNET.AerotechException()
        
    @multimethod
    def __init__(self,message:str):  # Instantiates the exception with a given message 
        self._AerotechExceptionNET=AerotechCommonNET.AerotechException(message)
 
    @multimethod
    def __init__(self,message:str, innerException:System.Exception):  # Instantiates the exception with a given message and an inner exception 
        self._AerotechExceptionNET=AerotechCommonNET.AerotechException(message,innerException)
    
    @property
    def Data(self):  # Gets a collection of key/value pairs that provide additional, user-defined information about the exception.
        return self._AerotechExceptionNET.Data

    def GetBaseException(self):  # When overridden in a derived class, returns the Exception that is the root cause of one or more subsequent exceptions.
        return self._AerotechExceptionNET.GetBaseException()
 
    def GetType(self):  # Gets the runtime type of the current instance.
        return self._AerotechExceptionNET.GetType()
 
    @property
    def HelpLink(self):  # Gets or sets a link to the help file associated with this exception.
        return self._AerotechExceptionNET.HelpLink
 
    @property
    def HResult(self):  # Gets or sets HRESULT, a coded numerical value that is assigned to a specific exception.
        return self._AerotechExceptionNET.HResult
 
    @property
    def InnerException(self):  # Gets the Exception instance that caused the current exception.
        return self._AerotechExceptionNET.InnerException
 
    @property
    def Message(self):  # Gets a message that describes the current exception.
        return self._AerotechExceptionNET.Message
 
    @property
    def Source(self):  # Gets or sets the name of the application or the object that causes the error.
        return self._AerotechExceptionNET.Source
 
    @property
    def StackTrace(self):  # Gets a string representation of the frames on the call stack at the time the current exception was thrown.
        return self._AerotechExceptionNET.StackTrace
 
    @property
    def TargetSite(self):  # Gets the method that throws the current exception.
        return self._AerotechExceptionNET.TargetSite
 
    def ToString(self):  # Creates and returns a string representation of the current exception.
        return self._AerotechExceptionNET.ToString()

# * Checked
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
# * Checked
class CalibrationFileFormat(Enum):  # Specifies the calibration file format
    Calibration1D=AerotechCommonNET.CalibrationFileFormat.Calibration1D  # 1 dimensional calibration file format
    Calibration2D=AerotechCommonNET.CalibrationFileFormat.Calibration2D  # 2 dimensional calibration file format
    Unknown=AerotechCommonNET.CalibrationFileFormat.UnknownD  # Unknown/Invalid calibration file format 
    
# * Checked
class Camming():  # Processes axis camming files 
    _CammingNET=None
    def __init__(self,CammingNET=None):
        self._CammingNET=CammingNET
        
    @classmethod
    def Process(self,filename:str):
        return self._CammingNET.Process(filename)
    
# * Checked  
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