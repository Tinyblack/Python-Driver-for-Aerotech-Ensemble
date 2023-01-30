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
from aenum import extend_enum

import Ensemble
import EnsembleTasksDebug
import EnsembleStatus
import EnsembleFileSystem
import CommonCollections

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Parameters as AerotechEnsembleParametersNET
except:
    raise RuntimeError

class AxisAutofocusLoopParameterCategory(ParameterCategory):  # Contains the Autofocus Loop Parameters
    @property
    def AutofocusDeadband(self): # Allows access to the AutofocusDeadband Parameter
 
    @property
    def AutofocusGainKi(self): # Allows access to the AutofocusGainKi Parameter
 
    @property
    def AutofocusGainKi2(self): # Allows access to the AutofocusGainKi2 Parameter
 
    @property
    def AutofocusGainKp(self): # Allows access to the AutofocusGainKp Parameter
 
    @property
    def AutofocusHoldInput(self): # Allows access to the AutofocusHoldInput Parameter
 
    @property
    def AutofocusInitialRampTime(self): # Allows access to the AutofocusInitialRampTime Parameter
 
    @property
    def AutofocusInput(self): # Allows access to the AutofocusInput Parameter
 
    @property
    def AutofocusLimitHigh(self): # Allows access to the AutofocusLimitHigh Parameter
 
    @property
    def AutofocusLimitLow(self): # Allows access to the AutofocusLimitLow Parameter
 
    @property
    def AutofocusSetup(self): # Allows access to the AutofocusSetup Parameter
 
    @property
    def AutofocusSpeedClamp(self): # Allows access to the AutofocusSpeedClamp Parameter
 
    @property
    def AutofocusTarget(self): # Allows access to the AutofocusTarget Parameter 

 
 
 
class AxisCurrentLoopParameterCategory():  # Contains the Current Loop Parameters
 
class AxisDynamicControlsToolboxCommandShapingParameterCategory():  # Contains the Command Shaping Parameters
 
class AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategory():  # Contains the Dynamic Gain Scheduling Parameters
 
class AxisDynamicControlsToolboxHarmonicCancellationParameterCategory():  # Contains the Harmonic Cancellation Parameters
 
class AxisDynamicControlsToolboxParameterCategory():  # Contains the Dynamic Controls Toolbox Parameters
 
class AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategory():  # Contains the Threshold Gain Scheduling Parameters
 
class AxisEnhancedThroughputModuleParameterCategory():  # Contains the Enhanced Throughput Module Parameters
 
class AxisEnhancedTrackingControlParameterCategory():  # Contains the Enhanced Tracking Control Parameters
 
class AxisFaultInputsParameterCategory():  # Contains the Inputs Parameters
 
class AxisFaultOutputsParameterCategory():  # Contains the Outputs Parameters
 
class AxisFaultParameterCategory():  # Contains the Fault Parameters
 
class AxisFaultThresholdsParameterCategory():  # Contains the Thresholds Parameters
 
class AxisFeedbackCapSensorParameterCategory():  # Contains the Cap Sensor Parameters
 
class AxisFeedbackEnDatEncoderParameterCategory():  # Contains the EnDat Encoder Parameters
 
class AxisFeedbackMultiplierParameterCategory():  # Contains the Multiplier Parameters
 
class AxisFeedbackParameterCategory():  # Contains the Feedback Parameters
 
class AxisFeedbackResoluteEncoderParameterCategory():  # Contains the Resolute Encoder Parameters
 
class AxisFeedbackResolverParameterCategory():  # Contains the Resolver Parameters
 
class AxisIOAnalogFiltersParameterCategory():  # Contains the Analog Filters Parameters
 
class AxisIOBrakeParameterCategory():  # Contains the Brake Parameters
 
class AxisIOParameterCategory():  # Contains the I/O Parameters
 
class AxisLimitsParameterCategory():  # Contains the Limits Parameters
 
class AxisMotionGearCamParameterCategory():  # Contains the Gear/Cam Parameters
 
class AxisMotionHomeParameterCategory():  # Contains the Home Parameters
 
class AxisMotionInPositionParameterCategory():  # Contains the In Position Parameters
 
class AxisMotionParameterCategory():  # Contains the Motion Parameters
 
class AxisMotorParameterCategory():  # Contains the Motor Parameters
 
class AxisMotorPiezoParameterCategory():  # Contains the Piezo Parameters
 
class AxisMotorStepperParameterCategory():  # Contains the Stepper Parameters
 
class AxisParameterCategory( ):  # Contains the Axis Parameters The root category of parameters for a given axis 
 
    @property
    def AutofocusLoop(self): # Contains the Autofocus Loop Parameters
        return AxisAutofocusLoopParameterCategory(AerotechEnsembleParametersNET.BaseParameters.AutofocusLoop)
    
    @property
    def AxisName(self): # The axis name 
 
  # AxisNameChanged  Raised when AxisName property changes 
 
    @property
    def AxisNumber(self): # The axis number 
 
    @property
    def AxisType(self): # Allows access to the AxisType Parameter
 
    @property
    def BacklashDistance(self): # Allows access to the BacklashDistance Parameter
 
    @property
    def CurrentLoop(self): # Contains the Current Loop Parameters
 
    @property
    def DynamicControlsToolbox(self): # Contains the Dynamic Controls Toolbox Parameters
 
    @property
    def EnhancedThroughputModule(self): # Contains the Enhanced Throughput Module Parameters
 
    @property
    def EnhancedTrackingControl(self): # Contains the Enhanced Tracking Control Parameters

    @property
    def Fault(self): # Contains the Fault Parameters
 
    @property
    def Feedback(self): # Contains the Feedback Parameters
 
    @property
    def GantryMasterAxis(self): # Allows access to the GantryMasterAxis Parameter
 
    @property
    def GantrySetup(self): # Allows access to the GantrySetup Parameter

    @property
    def IO(self): # Contains the I/O Parameters
 
    @property
    def Limits(self): # Contains the Limits Parameters
 
    @property
    def Motion(self): # Contains the Motion Parameters
 
    @property
    def Motor(self): # Contains the Motor Parameters
 
    @property
    def PiezoSetup(self): # Allows access to the PiezoSetup Parameter
 
    @property
    def RequiredStageSerialNumber(self): # Allows access to the RequiredStageSerialNumber Parameter
 
    @property
    def RolloverCounts(self): # Allows access to the RolloverCounts Parameter
 
    @property
    def RolloverMode(self): # Allows access to the RolloverMode Parameter
 
    @property
    def ServoLoop(self): # Contains the Servo Loop Parameters
 
    @property
    def Units(self): # Contains the Units Parameters 

    
    
    
    
 
class AxisServoLoopAmpProtectionParameterCategory():  # Contains the Amp Protection Parameters
 
class AxisServoLoopFiltersParameterCategory():  # Contains the Filters Parameters
 
class AxisServoLoopGainsParameterCategory():  # Contains the Gains Parameters
 
class AxisServoLoopParameterCategory():  # Contains the Servo Loop Parameters
 
class AxisUnitsParameterCategory():  # Contains the Units Parameters
 
# ! DONE
class BaseParameters():  # Represents the root category of parameters 
    _BaseParametersNET=None
    
    def __init__(self,BaseParametersNET=AerotechEnsembleParametersNET.BaseParameters.Defaults):
        self._BaseParametersNET=BaseParametersNET
        
    @property
    def Axes(self): # Provides access to the axes parameters 
        return CommonCollections.NamedConstantCollection(AerotechEnsembleParametersNET.BaseParameters.Axes,AxisParameterCategory)

    @classmethod
    @property
    def Defaults(cls): # Provides the defaults of the parameters 
        return cls(AerotechEnsembleParametersNET.BaseParameters.Defaults)

    @property
    def System(self): # The parameters that are per controller
        return SystemParameterCategory(AerotechEnsembleParametersNET.BaseParameters.System)
    
    @property
    def Tasks(self): # The task parameters
        return CommonCollections.NamedConstantCollection(AerotechEnsembleParametersNET.BaseParameters.Tasks,TaskParameterCategory)
 
class ControllerAxisParameterCategory():  # The root category of parameters for a given controller axis 
 
class ControllerAxisParameterCategoryCollection():  # Collection of ControllerAxisParameterCategory
 
class ControllerParameters():  # Root parameter category that handles parameters on a controller 

 


class HomeType(Enum):  # Represents the home type

class MotorType(Enum):  # Represents the motor type
 
class NamedXmlSections():  # Provides name based access to UserDataSections.
 
class Parameter():  # Represents a generic parameter 
 
class ParameterBounds():  # Represents the bounds of a generic parameter 
 
class ParameterCategory():  # The base type for categories containing parameters 
    
     All  Contains all the parameters in this category and its child categories 
 

 
  Categories  Gets the subcategories of this category. 
 

 
   Create<(Of <<'(TType>)>>)(IEnumerable<(Of <<'(TType>)>>))  Creates a user defined category 
 

  Name  The name of the category 
 

    
    
    
 
class ParameterContext(Enum):  # Represents the context of a parameter (system, axis, or task) 
 
class ParameterFile():  # Root parameter category that handles parameters from a file 
 
class ParameterRetrievalErrorEventArgs():  # Provides data for parameter retrieval errors 
 
class ParametersAllCollection():  # Represents a category that contains parameters in a non-nested fashion 
 
class PiezoDefaultServoState(Enum):  # Represents the piezo default servo state.
 
class PositionFeedbackChannel(Enum):  # Represents the position feedback channel type
 
class PositionFeedbackType(Enum):  # Represents the position feedback type
 
class PrimitiveType(Enum):  # Represents a primitive type in AeroBasic 
 
class SystemCalibrationParameterCategory():  # Contains the Calibration Parameters
 
class SystemCommunicationAsciiParameterCategory():  # Contains the ASCII Parameters
 
class SystemCommunicationEthernetIPParameterCategory():  # Contains the Ethernet/IP Parameters
 
class SystemCommunicationEthernetSocketsParameterCategory():  # Contains the Ethernet Sockets Parameters
 
class SystemCommunicationGpibParameterCategory():  # Contains the GPIB Parameters
 
class SystemCommunicationModbusMasterParameterCategory():  # Contains the Modbus Master Parameters
 
class SystemCommunicationModbusSlaveParameterCategory():  # Contains the Modbus Slave Parameters
 
class SystemCommunicationParameterCategory():  # Contains the Communication Parameters
 
class SystemCommunicationRS232ParameterCategory():  # Contains the RS-232 Parameters
 
class SystemCommunicationWebServerParameterCategory():  # Contains the Web Server Parameters
 
class SystemJoystickParameterCategory():  # Contains the Joystick Parameters
 
class SystemMemoryAllocationParameterCategory():  # Contains the Memory Allocation Parameters
 
class SystemParameterCategory():  # Contains the System Parameters
 
class SystemUserParameterCategory():  # Contains the User Parameters
 
class TaskMemoryAllocationParameterCategory():  # Contains the Memory Allocation Parameters
 
class TaskMotionParameterCategory():  # Contains the Motion Parameters
 
class TaskParameterCategory():  # Contains the Task Parameters
 
class TypedParameter():  # Represents a typed parameter 
 
class TypedParameterBounds():  # Represents bounds of a typed parameter 
    
    
    
# ! DONE
class VelocityFeedbackChannel(Enum):  # Represents the velocity feedback channel type
    Default=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Default  # Default
    Channel0=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel0  #   Channel 0
    Channel1=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel1  #   Channel 1
    Channel2=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel2  #   Channel 2
    Channel3=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel3  #   Channel 3
    Channel4=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel4  #   Channel 4 

# ! DONE
class VelocityFeedbackType(Enum):  # Represents the velocity feedback type 
    LocalEncoderCounter=AerotechEnsembleParametersNET.VelocityFeedbackType.LocalEncoderCounter # Encoder Counter
    EncoderMultiplier=AerotechEnsembleParametersNET.VelocityFeedbackType.EncoderMultiplier  # Encoder Multiplier
    AnalogInput=AerotechEnsembleParametersNET.VelocityFeedbackType.AnalogInput  # Analog Input
    Resolver=AerotechEnsembleParametersNET.VelocityFeedbackType.Resolver # Resolver 
extend_enum(VelocityFeedbackType,'None',getattr(AerotechEnsembleParametersNET.VelocityFeedbackType,'None'))
