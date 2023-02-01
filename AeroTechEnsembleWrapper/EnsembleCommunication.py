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

# * Checked
class AxisMismatch(Enum):
    FirmwareVersion=AerotechEnsembleCommunicationNET.AxisMismatch.FirmwareVersion 
    AxisMask=AerotechEnsembleCommunicationNET.AxisMismatch.AxisMask 
extend_enum(AxisMismatch,'None',getattr(AerotechEnsembleCommunicationNET.AxisMismatch,'None'))

# * Checked
class CommunicationType(Enum):
    Ethernet=AerotechEnsembleCommunicationNET.CommunicationType.Ethernet
    Usb=AerotechEnsembleCommunicationNET.CommunicationType.Usb
    
# * Checked
class NetworkNodeAddress():
    _NetworkNodeAddressNET=None
    def __init__(self,NetworkNodeAddressNET=AerotechEnsembleCommunicationNET.NetworkNodeAddress):
        self._NetworkNodeAddressNET=NetworkNodeAddressNET
    
    @property
    def CommunicationType(self):
        return CommunicationType[self._NetworkNodeAddressNET.CommunicationType.ToString()]
 
    @property
    def Name(self):
        return self._NetworkNodeAddressNET.Name

# * Checked
class NetworkNode(NetworkNodeAddress):
    _NetworkNodeNET=None
    def __init__(self,NetworkNodeNET=AerotechEnsembleCommunicationNET.NetworkNode):
        self._NetworkNodeNET=NetworkNodeNET
        NetworkNodeAddress.__init__(self,NetworkNodeNET)
    
    def ChangeEthernet(self,ipAddress:int, subnetMask:int, gateway:int):
        self._NetworkNodeNET.ChangeEthernet(Net.IPAdress(ipAddress),Net.IPAdress(subnetMask),Net.IPAdress(gateway))
 
    @property
    def DHCPActive(self):
        return self._NetworkNodeNET.DHCPActive
 
    #DHCPActiveChanged  Raised when DHCPActive changes 
    @property
    def GatewayAddress(self):
      return self._NetworkNodeNET.GatewayAddress.get_Address()
 
    #GatewayAddressChanged  Raised when GatewayAddress changes 
    @property
    def IPAddress(self):
        return self._NetworkNodeNET.IPAddress.get_Address()
 
    #IPAddressChanged  Raised when IPAddress changes 
    @property
    def IsEpaq(self):
        return self._NetworkNodeNET.IsEpaq
 
    #IsNamedLockedChanged  Raised when IsNameLocked changes 
    
    @property
    def IsNameLocked(self):
        return self._NetworkNodeNET.IsNameLocked
    
    @property
    def LEDToggle(self):
        return self._NetworkNodeNET.LEDToggle
 
    #LEDToggleChanged  Raised when LEDToggle changes 
    
    def LockName(self,lockCode:str):
        return self._NetworkNodeNET.LockName(lockCode)
    
    @property
    def MACAddress(self):
        return self._NetworkNodeNET.MACAddress.ToString()
 
    @property
    def MasterType(self):
      return EnsembleInformation.ComponentType[self._NetworkNodeNET.MasterType.ToString()] 

    @property
    def Name(self):
        return self._NetworkNodeNET.Name
 
    #NameChanged  Raised whenever Name changes 
    
    @property
    def SubnetAddress(self):
        return self._NetworkNodeNET.SubnetAddress.get_Address()
 
    #SubnetAddressChanged  Raised when SubnetAddress changes 
 
    def UnLockName(self,lockCode:str):
        return self._NetworkNodeNET.UnLockName(lockCode)
    
    @property
    def UsbId(self):
        return self._NetworkNodeNET.UsbId
    
    @property
    def Version(self):
        return EnsembleInformation.ControllerVersion(self._NetworkNodeNET.Version)
    
# * Checked
class NetworkSetup(CommonCollections.NamedConstantCollection): 
    _NetworkSetupNET=None
    def __init__(self,NetworkSetupNET=AerotechEnsembleCommunicationNET.NetworkSetup):
        self._NetworkSetupNET=NetworkSetupNET
        CommonCollections.NamedConstantCollection.__init__(self,NetworkSetupNET,NetworkNodeAddress)
        
    @property
    def AutoCommit(self):   #Whether to automatically commit the changes 
        return self._NetworkSetupNET.AutoCommit
    
    @property
    def Capacity(self):   #Returns the size of the NetworkNode list, because there are no null entries, this is the same as Count. 
        return self._NetworkSetupNET.Capacity
    
    def Commit(self): #Commits the current setup to the configuration file 
        self._NetworkSetupNET.Commit()
    
    @property
    def Count(self):  #Returns the number of NetworkNodes in the Configuration file. 
        return self._NetworkSetupNET.Count
    
    def Dispose(self):   #Disposes the current NetworkSetup instance. 
        self._NetworkSetupNET.Dispose()
 
    #GetEnumerator()()()()  #Returns an Enumerator of current NetworkNodeAddresses. 
 
    def IsMapped(self,nodeAddress:NetworkNodeAddress):  #Checks whether the given address is mapped 
        return self._NetworkSetupNET.IsMapped(nodeAddress._NetworkNodeAddressNET)
    
    @multimethod
    def Map(self,nodeAddress:NetworkNodeAddress):  #Maps a new controller to the list of active controllers 
        self._NetworkSetupNET.Map(nodeAddress._NetworkNodeAddressNET)
    
    @multimethod
    def Map(self,node:NetworkNode):  #Maps a new controller to the list of active controllers 
        self._NetworkSetupNET.Map(node._NetworkNodeNET)
    
    def Refresh(self):  #Reloads the profile file 
        self._NetworkSetupNET.Refresh()
    
    def Unmap(self,nodeAddress:NetworkNodeAddress):  #Unmaps a controller 
        self._NetworkSetupNET.Unmap(nodeAddress._NetworkNodeAddressNET)
    
    def UnmapAll(self):   #Unmaps all mapped controllers  
        self._NetworkSetupNET.UnmapAll()