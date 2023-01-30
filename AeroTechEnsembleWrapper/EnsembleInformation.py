import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
import System

from enum import Enum
from aenum import extend_enum
from typing import Union,type

from multimethod import multimethod

import CommonCollections
import EnsembleCommunication 
import EnsembleStatus


DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Information as AerotechEnsembleInformationNET
except:
    raise RuntimeError

# ! DONE

class AxisInfo():
    _AxisInfoNET=None
    def __init__(self,AxisInfoNET=AerotechEnsembleInformationNET.AxisInfo):
        self._AxisInfoNET=AxisInfoNET
        
    @property        
    def AxisType(self): # The type of axis 
        return ComponentType[self._AxisInfoNET.AxisType.ToString]

    @property        
    def BusVoltage(self): # The bus voltage
        return int(self._AxisInfoNET.BusVoltage)

    @property        
    def CommandOutputType(self): # The type of output an axis generates.
        return CommandOutputType[self._AxisInfoNET.CommandOutputType.ToString]

    @property        
    def Drive(self): # Returns information about the physical drive on which the axis resides.
        return DriveInformation(self._AxisInfoNET.Drive)

    @property        
    def FlashConfigStatus(self): # Information about FlashConfig status.
        return FlashConfigStatus(self._AxisInfoNET.FlashConfigStatus)

    @property        
    def IOBoardPresent(self): # If the IO board is connected. 
        return self._AxisInfoNET.IOBoardPresent

    @property        
    def LEDToggle(self): # Whether the LED is brinking (toggling) on the given Axis 
        return self._AxisInfoNET.LEDToggle

    @property        
    def MaximumAmperage(self): # The axis maximum amperage 
        return float(self._AxisInfoNET.MaximumAmperage)

    @property        
    def MaximumVoltage(self): # The axis maximum voltage.
        return float(self._AxisInfoNET.MaximumVoltage)

    @property        
    def Name(self): # The axis name.
        return self._AxisInfoNET.Name

    @property        
    def Number(self): # The axis number 
        return self._AxisInfoNET.Number
 
class CommandOutputType(Enum):
    Current=AerotechEnsembleInformationNET.ComponentOutputType.Current  # Current output is generated.
    Voltage=AerotechEnsembleInformationNET.ComponentOutputType.Voltage  # Voltage output is generated. 
extend_enum(CommandOutputType,'None',getattr(AerotechEnsembleInformationNET.CommandOutputType,'None'))

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
    
class ControllerInformation():
    _ControllerInformationNET=None
    def __init__(self,ControllerInformationNET=AerotechEnsembleInformationNET.ControllerInformation):
        self._ControllerInformationNET=ControllerInformationNET
        
    @property
    def Axes(self): # Provides access to information about axes 
        return CommonCollections.NamedConstantCollection(self._ControllerInformationNET.Axes,AxisInfo)

    @property
    def AxisMismatch(self): # Indicates a configuration error on the controller 
        return EnsembleCommunication.AxisMismatch[self._ControllerInformationNET.AxisMismatch.ToString()]

    @property
    def CommunicationType(self): # The communication type that is being used
        return EnsembleCommunication.CommunicationType[self._ControllerInformationNET.CommunicationType.ToString()]

    @property
    def Drives(self): # Provides information about connected drives.
        return DriveInformation(self._ControllerInformationNET.Drives)

    @property
    def Initialization(self): # Provies information about initialization
        return InitializationInformation(self._ControllerInformationNET.Initialization)

    @property
    def IsEpaq(self): # Whether the controller is an Epaq 
        return self._ControllerInformationNET.IsEpaq

    @property
    def MasterType(self): # Specifies the component type of the controller 
        return ComponentType[self._ControllerInformationNET.MasterType.ToString()]

    @property
    def Name(self): # The name of the controller
        return self._ControllerInformationNET.Name

    @property
    def Version(self): # Specifies the versions of the controller  
        return ControllerVersion(self._ControllerInformationNET.Version)

class ControllerVersion():
    _ControllerVersionNET=None
    def __init__(self,ControllerVersionNET=AerotechEnsembleInformationNET.ControllerVersion):
        self._ControllerVersionNET=ControllerVersionNET

    @property
    def FirmwareVersion(self):  #Specifies the firmware version
        return self._ControllerVersionNET.FirmwareVersion.ToString()
    
    @property
    def FPGAVersion(self):  #Specifies the FPGA version 
        return self._ControllerVersionNET.FPGAVersion
    
    @property
    def HardwareVersion(self):  #Specifies the hardware version 
        return self._ControllerVersionNET.HardwareVersion
    
class DriveInformation():
    _DriveInformationNET=None
    def __init__(self,DriveInformationNET=AerotechEnsembleInformationNET.DriveInformation):
        self._DriveInformationNET=DriveInformationNET
        
    @property     
    def Axes(self): # Returns information about the axes that are present on the drive. 
        return CommonCollections.NamedConstantCollection(self._DriveInformationNET.Axes,AxisInfo)

    @property  
    def IOBoardPresent(self): # If the IO board is connected.
        return self._DriveInformationNET.IOBoardPresent
        
    @property  
    def Type(self): # What type the drive is
        return ComponentType[self._DriveInformationNET.Type.ToString()]
        
    @property  
    def Version(self): # Specifies the version of the drive. 
        return ControllerVersion(self._DriveInformationNET.Version)

class EnumInformation():
    _EnumInformationNET=None
    def __init__(self,EnumInformationNET=AerotechEnsembleInformationNET.EnumInformation):
        self._EnumInformationNET=EnumInformationNET
        
    def GetEnumName(self,enumType:System.Type): # Get the string representation of an enumeration.
        return self._EnumInformationNET.GetEnumName
    
    def GetValueName(self,enumValue:System.Enum):  # Get the string representation of a value.
        return self._EnumInformationNET.GetValueName
    
    def GetValueNames(self,enumType:System.Type):  # Get the string representations of values of an enumeration.
        return self._EnumInformationNET.GetValueNames
 
class FlashConfigStatus():
    _FlashConfigStatusNET=None
    def __init__(self,FlashConfigStatusNET:Union[AerotechEnsembleInformationNET.FlashConfigStatus,int]=None):
        if type(FlashConfigStatusNET) in [type(int),type(None)]:
            if type(FlashConfigStatusNET) in [type(int)]:
                self._FlashConfigStatusNET=AerotechEnsembleInformationNET.FlashConfigStatus(FlashConfigStatusNET)
            if  type(FlashConfigStatusNET) in [type(None)]:
                self._FlashConfigStatusNET=AerotechEnsembleInformationNET.FlashConfigStatus()
        else:
            self._FlashConfigStatusNET=FlashConfigStatusNET
            
    @property    
    def ActiveBits(self):  # Returns a list of the active bit names.
        # TODO Deal with 'ReadOnlyCollection'
        return str(self._FlashConfigStatusNET.ActiveBits)
    
    @property
    def BitHelpLinks(self):  # Returns a dictionary of bit value names (keys) and the associated help file link (values) 
        # TODO Deal with 'IDictionary'
        return self._FlashConfigStatusNET.BitHelpLinks
    
    @property
    def BitValues(self):  # Returns a listing of the bit names and their corresponding values 
        # TODO Deal with 'IDictionary'
        return self._FlashConfigStatusNET.BitValues
    
    @property
    def DataValid(self):  # FlashConfig data is valid.
        return self._FlashConfigStatusNET.DataValid

    @property
    def MaskValue(self):  #   The underlying mask value 
        return self._FlashConfigStatusNET.MaskValue
        
    #None  If all the other properties are not set (false) 
    
    @property
    def SerialMismatch(self):  #   Connected Stage serial number does not match expected Stage serial number.
        return self._FlashConfigStatusNET.SerialMismatch
    
    @property
    def Supported(self):  #   FlashConfig memory is present; feature is supported.
        return self._FlashConfigStatusNET.Supported
        
    @multimethod
    def ToString(self):  # Converts to a string representation 
        return self._FlashConfigStatusNET.ToString()
    
    @multimethod
    def ToString(self,userReadableFormat:bool):  #  Converts to a string representation 
        return self._FlashConfigStatusNET.ToString(userReadableFormat)
    
    @property
    def ValueNames(self):  # Returns a mapping of values to their human readable form.  
        # TODO Deal with 'IDictionary'
        return self._FlashConfigStatusNET.ValueNames

class InitializationInformation():
    _InitializationInformationNET=None
    def __init__(self,InitializationInformationNET=AerotechEnsembleInformationNET.InitializationInformation):
        self._InitializationInformationNET=InitializationInformationNET
    
    @property
    def Warning(self):
        return EnsembleStatus.ErrorInformation(self._InitializationInformationNET.Warning)
    



 

