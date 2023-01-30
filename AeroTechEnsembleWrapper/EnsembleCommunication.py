import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

from enum import Enum
from aenum import extend_enum

import clr
clr.AddReference('System')
from System import Net

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

from multimethod import multimethod

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Communication as AerotechEnsembleCommunicationNET
except:
    raise RuntimeError


class AxisMismatch(Enum):
    FirmwareVersion=AerotechEnsembleCommunicationNET.AxisMismatch.FirmwareVersion 
    AxisMask=AerotechEnsembleCommunicationNET.AxisMismatch.AxisMask 
extend_enum(AxisMismatch,'None',getattr(AerotechEnsembleCommunicationNET.AxisMismatch,'None'))
    
class CommunicationType(Enum):
    Ethernet=AerotechEnsembleCommunicationNET.CommunicationType.Ethernet
    Usb=AerotechEnsembleCommunicationNET.CommunicationType.Usb

class NetworkNodeAddress():
    @property
    def CommunicationType(self):
        return CommunicationType[AerotechEnsembleCommunicationNET.NetworkNodeAddress.CommunicationType.ToString()]
 
    @property
    def Name(self):
        return AerotechEnsembleCommunicationNET.NetworkNodeAddress.Name

class NetworkNode(NetworkNodeAddress):
    def ChangeEthernet(self,ipAddress:int, subnetMask:int, gateway:int):
        AerotechEnsembleCommunicationNET.NetworkNode.ChangeEthernet(Net.IPAdress(ipAddress),Net.IPAdress(subnetMask),Net.IPAdress(gateway))
 
    @property
    def DHCPActive(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.DHCPActive
 
    #DHCPActiveChanged  Raised when DHCPActive changes 
    @property
    def GatewayAddress(self):
      return AerotechEnsembleCommunicationNET.NetworkNode.GatewayAddress.get_Address()
 
    #GatewayAddressChanged  Raised when GatewayAddress changes 
    @property
    def IPAddress(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.IPAddress.get_Address()
 
    #IPAddressChanged  Raised when IPAddress changes 
    @property
    def IsEpaq(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.IsEpaq
 
    #IsNamedLockedChanged  Raised when IsNameLocked changes 
    
    @property
    def IsNameLocked(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.IsNameLocked
    
    @property
    def LEDToggle(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.LEDToggle
 
    #LEDToggleChanged  Raised when LEDToggle changes 
    
    def LockName(self,lockCode:str):
        return AerotechEnsembleCommunicationNET.NetworkNode.LockName(lockCode)
    
    @property
    def MACAddress(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.MACAddress.ToString()
 
    @property
    def MasterType(self):
      return EnsembleInformation.ComponentType[AerotechEnsembleCommunicationNET.NetworkNode.MasterType.ToString()] 

    @property
    def Name(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.Name
 
    #NameChanged  Raised whenever Name changes 
    
    @property
    def SubnetAddress(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.SubnetAddress.get_Address()
 
    #SubnetAddressChanged  Raised when SubnetAddress changes 
 
    def UnLockName(self,lockCode:str):
        return AerotechEnsembleCommunicationNET.NetworkNode.UnLockName(lockCode)
    
    @property
    def UsbId(self):
        return AerotechEnsembleCommunicationNET.NetworkNode.UsbId
    
    @property
    def Version(self):
        return EnsembleInformation.ControllerVersion(AerotechEnsembleCommunicationNET.NetworkNode.Version)

class NetworkSetup(): 
    @property
    def AutoCommit(self):   #Whether to automatically commit the changes 
        pass 
    
    @property
    def Capacity(self):   #Returns the size of the NetworkNode list, because there are no null entries, this is the same as Count. 
        pass
    
    def Commit(self): #Commits the current setup to the configuration file 
        pass
    
    @property
    def Count(self):  #Returns the number of NetworkNodes in the Configuration file. 
        pass
    
    def Dispose(self):   #Disposes the current NetworkSetup instance. 
        pass
 
  #GetEnumerator()()()()  #Returns an Enumerator of current NetworkNodeAddresses. 
 
    def IsMapped(self,NetworkNodeAddress):  #Checks whether the given address is mapped 
        pass
    
    @multimethod
    def Map(self,NetworkNodeAddress):  #Maps a new controller to the list of active controllers 
        pass
    
    @multimethod
    def Map(self,NetworkNode):  #Maps a new controller to the list of active controllers 
        pass
    
    def Refresh(self):  #Reloads the profile file 
        pass
    
    def Unmap(self,NetworkNodeAddress):  #Unmaps a controller 
        pass
    
    def UnmapAll(self):   #Unmaps all mapped controllers  
        pass
