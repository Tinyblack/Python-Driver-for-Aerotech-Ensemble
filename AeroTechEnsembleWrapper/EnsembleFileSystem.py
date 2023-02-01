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

import CommonCollections

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.FileSystem as AerotechEnsembleFileSystemNET
except:
    raise RuntimeError

# * Checked
class FileRetrieveMode(Enum):  # Specifies the mode for retreival of the file from the controller 
    NoOverwrite=AerotechEnsembleFileSystemNET.FileRetrieveMode.NoOverwrite  # Do not overwrite files 
    Overwrite=AerotechEnsembleFileSystemNET.FileRetrieveMode.Overwrite  # Overwrite files 
    Append=AerotechEnsembleFileSystemNET.FileRetrieveMode.Append  # Append to existing files  

# * Checked
class SystemAttributes(Enum):  # Represents standard file attributes  
    Compressed=AerotechEnsembleFileSystemNET.SystemAttributes.Compressed  # Compressed 
    Hidden=AerotechEnsembleFileSystemNET.SystemAttributes.Hidden  # File is hidden 
    NoCrcData=AerotechEnsembleFileSystemNET.SystemAttributes.NoCrcData  # No CRC data is present 
    PcCreated=AerotechEnsembleFileSystemNET.SystemAttributes.PcCreated  # File was not created by the controller  

# * Checked
class FileInfo():
    _FileInfoNET=None
    def __init__(self,FileInfoNET=AerotechEnsembleFileSystemNET.FileInfo):
        self._FileInfoNET=FileInfoNET
        
    @property
    def CreationTime(self):  # When the file was created 
        # TODO deal with System DateTime
        return self._FileInfoNET.CreationTime
    @property
    def Name(self):  # File name 
        return self._FileInfoNET.Name
    @property
    def Size(self):  # File size in bytes 
        return self._FileInfoNET.Size
    @property
    def SystemAttributes(self):  # System attributes 
        return SystemAttributes[self._FileInfoNET.SystemAttributes.ToString()]
    @property
    def UserAttributes(self):  # Any user attributes  
        return self._FileInfoNET.UserAttributes

# * Checked
class FileManager(CommonCollections.NamedConstantCollection):  # Provides access to the file system on the controller
    _FileManagerNET=None
    def __init__(self,FileManagerNET=AerotechEnsembleFileSystemNET.FileManager):
        self._FileManagerNET=FileManagerNET
        CommonCollections.NamedConstantCollection.__init__(self,FileManagerNET,FileInfo)
    
    @multimethod
    def Delete(self,name:str):  # Deletes the file 
        self._FileManagerNET.Delete(name)
        
    @multimethod
    def Delete(self,file:FileInfo):  # Deletes the file 
        self._FileManagerNET.Delete(file._FileInfoNET)

    def Format(self):  # Formats the file system 
        self._FileManagerNET.Format()
 
    @property
    def FreeSpace(self):
        return self._FileManagerNET.FreeSpace
        
    @multimethod
    def ListFiles(self):  #Retrieves information about all files from the controller 
        return FileInfo(self._FileManagerNET.ListFiles())
 
    @multimethod
    def ListFiles(self,progressChangedEventHandler:ProgressChangedEventHandler):  #Retrieves information about all files from the controller 
        return FileInfo(self._FileManagerNET.ListFiles(progressChangedEventHandler))

    def Optimize(self):  #Optimizes the file system 
        self._FileManagerNET.Optimize()
        
    @multimethod
    def Retrieve(self,name:str,toFolder:str):  # Retrieves the file from the controller 
        self._FileManagerNET.Retrieve(name,toFolder)
        
    @multimethod
    def Retrieve(self,file:FileInfo,toFolder:str):  # Retrieves a file from the controller 
        self._FileManagerNET.Retrieve(file._FileInfoNET,toFolder)
        
    @multimethod
    def Retrieve(self,name:str,toFolder:str, mode:FileRetrieveMode):  # Retrieves the file from the controller 
        self._FileManagerNET.Retrieve(name,toFolder,mode.value)
        
    @multimethod
    def Retrieve(self,file:FileInfo,toFolder:str, mode:FileRetrieveMode):  # retrieves the file from the controller 
        self._FileManagerNET.Retrieve(file._FileInfoNET,toFolder)
        
    @multimethod
    def Retrieve(self,name:str,toFolder:str, mode:FileRetrieveMode, progressChangedEventHandler:ProgressChangedEventHandler):  # Retrieves the file from the controller 
        # TODO Fix the event handler declaration here (Might need a wrapper here)
        self._FileManagerNET.Retrieve(name,toFolder,mode.value,progressChangedEventHandler)
        
    @multimethod
    def Retrieve(self,file:FileInfo,toFolder:str, mode:FileRetrieveMode, progressChangedEventHandler:ProgressChangedEventHandler):  # Retrieves the file from the controller 
        # TODO Fix the event handler declaration here (Might need a wrapper here)
        self._FileManagerNET.Retrieve(file._FileInfoNET,toFolder,mode.value,progressChangedEventHandler)
 
    @multimethod
    def Send(self,fileName:str):  # Sends a file to the controller 
        self._FileManagerNET.Send(fileName)
        
    @multimethod
    def Send(self,fileName:str, userAttributes:int, hidden:bool, progressChangedEventHandler:ProgressChangedEventHandler):  # Sends a file to the controller 
        # TODO Fix the event handler declaration here (Might need a wrapper here)
        self._FileManagerNET.Send(fileName,userAttributes,hidden,progressChangedEventHandler)
        
    @multimethod
    def Send(self,fileName:str, userAttributes:int):  # Sends a file to the controller 
        self._FileManagerNET.Send(fileName,userAttributes)
        
    @multimethod
    def Send(self,fileName:str, userAttributes:int, hidden:bool):  # Sends a file to the controller 
        self._FileManagerNET.Send(fileName, userAttributes, hidden)