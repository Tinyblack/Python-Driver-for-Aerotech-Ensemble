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

from enum import Enum

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
    import Aerotech.Ensemble.Information as AerotechEnsembleInformationNET
except:
    raise RuntimeError

class ComponentType(Enum):
    CP=AerotechEnsembleInformationNET.ComponentType.CP # Compact pulse width modulation
 
    MP=AerotechEnsembleInformationNET.ComponentType.MP # Micro pulse width modulation
    
    Control=AerotechEnsembleInformationNET.ComponentType.Control # Ensemble control board
    
    CL=AerotechEnsembleInformationNET.ComponentType.CL  # Compact Linear
    
    HPE=AerotechEnsembleInformationNET.ComponentType.HPE  # High performance pulse width modulation enhanced 
    
    HLE=AerotechEnsembleInformationNET.ComponentType.HLE  # High performance linear enhanced 
    
    ML=AerotechEnsembleInformationNET.ComponentType.ML  # Micro pulse linear
    
    PMT=AerotechEnsembleInformationNET.ComponentType.PMT  # Obsolete
    
    Lab=AerotechEnsembleInformationNET.ComponentType.Lab  # Ensemble Lab controller
    
    QLab=AerotechEnsembleInformationNET.ComponentType.QLab  # Ensemble QLab controller
    
    QDe=AerotechEnsembleInformationNET.ComponentType.QDe  # High Performance Single Axis Piezo Drive
    
    QL=AerotechEnsembleInformationNET.ComponentType.QL  # Single Axis Piezo Drive
    
    QLe=AerotechEnsembleInformationNET.ComponentType.QLe  # High Performance Single Axis Piezo Drive 
    
class ControllerVersion ():

    @property
    def FirmwareVersion(self):  #Specifies the firmware version
        return AerotechEnsembleInformationNET.ControllerVersion.FirmwareVersion.ToString()
    
    @property
    def FPGAVersion(self):  #Specifies the FPGA version 
        return AerotechEnsembleInformationNET.ControllerVersion.FPGAVersion
    
    @property
    def HardwareVersion(self):  #Specifies the hardware version 
        return AerotechEnsembleInformationNET.ControllerVersion.HardwareVersion
 

