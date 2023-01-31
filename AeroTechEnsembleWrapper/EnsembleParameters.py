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
    _AxisAutofocusLoopParameterCategoryNET=None
    def __init__(self,AxisAutofocusLoopParameterCategoryNET=AerotechEnsembleParametersNET.AxisAutofocusLoopParameterCategory):
        self._AxisAutofocusLoopParameterCategoryNET=AxisAutofocusLoopParameterCategoryNET
        ParameterCategory.__init__(self,AxisAutofocusLoopParameterCategoryNET)
    
    @property
    def AutofocusDeadband(self): # Allows access to the AutofocusDeadband Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusDeadband,float)
    
    @property
    def AutofocusGainKi(self): # Allows access to the AutofocusGainKi Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusGainKi,float)
    
    @property
    def AutofocusGainKi2(self): # Allows access to the AutofocusGainKi2 Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusGainKi2,float)
    
    @property
    def AutofocusGainKp(self): # Allows access to the AutofocusGainKp Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusGainKp,float)
    
    @property
    def AutofocusHoldInput(self): # Allows access to the AutofocusHoldInput Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusHoldInput,int)
    
    @property
    def AutofocusInitialRampTime(self): # Allows access to the AutofocusInitialRampTime Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusInitialRampTime,int)
    
    @property
    def AutofocusInput(self): # Allows access to the AutofocusInput Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusInput,int)
    
    @property
    def AutofocusLimitHigh(self): # Allows access to the AutofocusLimitHigh Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusLimitHigh,float)
    
    @property
    def AutofocusLimitLow(self): # Allows access to the AutofocusLimitLow Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusLimitLow,float)   
    
    @property
    def AutofocusSetup(self): # Allows access to the AutofocusSetup Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusSetup,int)
    
    @property
    def AutofocusSpeedClamp(self): # Allows access to the AutofocusSpeedClamp Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusSpeedClamp,float) 
    
    @property
    def AutofocusTarget(self): # Allows access to the AutofocusTarget Parameter 
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusTarget,float) 
 
class AxisCurrentLoopParameterCategory(ParameterCategory):  # Contains the Current Loop Parameters
    _AxisCurrentLoopParameterCategoryNET=None
    def __init__(self,AxisCurrentLoopParameterCategoryNET=AerotechEnsembleParametersNET.AxisCurrentLoopParameterCategory):
        self._AxisCurrentLoopParameterCategoryNET=AerotechEnsembleParametersNET
        ParameterCategory.__init__(self,AxisCurrentLoopParameterCategoryNET)
 
    @property
    def AmplifierDeadtime(self): # Allows access to the AmplifierDeadtime Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.AmplifierDeadtime,float)
         
    @property
    def CurrentGainKi(self): # Allows access to the CurrentGainKi Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentGainKi,float)
    
    @property
    def CurrentGainKp(self): # Allows access to the CurrentGainKp Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentGainKp,float)
    
    @property
    def CurrentOffsetA(self): # Allows access to the CurrentOffsetA Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentOffsetA,float)
    
    @property
    def CurrentOffsetB(self): # Allows access to the CurrentOffsetB Parameter 
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentOffsetB,float)
 
class AxisDynamicControlsToolboxCommandShapingParameterCategory(ParameterCategory):  # Contains the Command Shaping Parameters
 
class AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategory(ParameterCategory):  # Contains the Dynamic Gain Scheduling Parameters
 
class AxisDynamicControlsToolboxHarmonicCancellationParameterCategory(ParameterCategory):  # Contains the Harmonic Cancellation Parameters
 
class AxisDynamicControlsToolboxParameterCategory(ParameterCategory):  # Contains the Dynamic Controls Toolbox Parameters
 
class AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategory(ParameterCategory):  # Contains the Threshold Gain Scheduling Parameters
 
class AxisEnhancedThroughputModuleParameterCategory(ParameterCategory):  # Contains the Enhanced Throughput Module Parameters
 
class AxisEnhancedTrackingControlParameterCategory(ParameterCategory):  # Contains the Enhanced Tracking Control Parameters
 
class AxisFaultInputsParameterCategory(ParameterCategory):  # Contains the Inputs Parameters
 
class AxisFaultOutputsParameterCategory(ParameterCategory):  # Contains the Outputs Parameters
 
class AxisFaultParameterCategory(ParameterCategory):  # Contains the Fault Parameters
 
class AxisFaultThresholdsParameterCategory(ParameterCategory):  # Contains the Thresholds Parameters
 
class AxisFeedbackCapSensorParameterCategory(ParameterCategory):  # Contains the Cap Sensor Parameters
 
class AxisFeedbackEnDatEncoderParameterCategory(ParameterCategory):  # Contains the EnDat Encoder Parameters
 
class AxisFeedbackMultiplierParameterCategory(ParameterCategory):  # Contains the Multiplier Parameters
 
class AxisFeedbackParameterCategory(ParameterCategory):  # Contains the Feedback Parameters
 
class AxisFeedbackResoluteEncoderParameterCategory(ParameterCategory):  # Contains the Resolute Encoder Parameters
 
class AxisFeedbackResolverParameterCategory(ParameterCategory):  # Contains the Resolver Parameters
 
class AxisIOAnalogFiltersParameterCategory(ParameterCategory):  # Contains the Analog Filters Parameters
 
class AxisIOBrakeParameterCategory(ParameterCategory):  # Contains the Brake Parameters
 
class AxisIOParameterCategory(ParameterCategory):  # Contains the I/O Parameters
 
class AxisLimitsParameterCategory(ParameterCategory):  # Contains the Limits Parameters
 
class AxisMotionGearCamParameterCategory(ParameterCategory):  # Contains the Gear/Cam Parameters
 
class AxisMotionHomeParameterCategory(ParameterCategory):  # Contains the Home Parameters
 
class AxisMotionInPositionParameterCategory(ParameterCategory):  # Contains the In Position Parameters
 
class AxisMotionParameterCategory(ParameterCategory):  # Contains the Motion Parameters
 
class AxisMotorParameterCategory(ParameterCategory):  # Contains the Motor Parameters
 
class AxisMotorPiezoParameterCategory(ParameterCategory):  # Contains the Piezo Parameters
 
class AxisMotorStepperParameterCategory(ParameterCategory):  # Contains the Stepper Parameters
 
class AxisParameterCategory(ParameterCategory):  # Contains the Axis Parameters The root category of parameters for a given axis 
 
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

    
    
    
    
 
class AxisServoLoopAmpProtectionParameterCategory(ParameterCategory):  # Contains the Amp Protection Parameters
 
class AxisServoLoopFiltersParameterCategory(ParameterCategory):  # Contains the Filters Parameters
 
class AxisServoLoopGainsParameterCategory(ParameterCategory):  # Contains the Gains Parameters
 
class AxisServoLoopParameterCategory(ParameterCategory):  # Contains the Servo Loop Parameters
 
class AxisUnitsParameterCategory(ParameterCategory):  # Contains the Units Parameters
 
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
    
    PastLimittoMarker  Home Past Limit to Marker
 
ToLimitandReversetoMarker  Home to Limit and Reverse to Marker
 
ToMarkerOnly  Home to Marker Only
 
ToLimitOnly  Home to Limit Only
 
AtCurrentPosition  Home at Current Position
 
AtCurrentPositionAbsolute  Home at Current Position Absolute 

    

class MotorType(Enum):  # Represents the motor type
    
    ACBrushlessHallEffect  AC Brushless (Hall-Effect Switches)
 
ACBrushlessAutoMSET  AC Brushless (Auto-MSET)
 
DCBrush  DC Brush
 
StepperMotor  Stepper Motor
 
TwoPhaseACBrushless  2-Phase AC Brushless
 
ACBrushlessCommutationSearch  AC Brushless (Commutation Search)
 
PiezoActuator  Piezo Actuator 

 
class NamedXmlSections():  # Provides name based access to UserDataSections.
 
class Parameter():  # Represents a generic parameter 
    _ParameterNET=None
    def __init__(self,ParameterNET=AerotechEnsembleParametersNET.Parameter):
        self._ParameterNET=ParameterNET
    
    @property
    def Bounds(self):  # Contains the bounds of this parameter 
        return ParameterBounds(self._ParameterNET.Bounds)
    @property
    def Context(self):  # The context of the parameter
        return ParameterContext[self._ParameterNET.Context.ToString()]
    @property
    def ContextKey(self):  # The Task ID or axis index of the parameter
        return self._ParameterNET.ContextKey
    @property
    def Default(self):  # The parameter default value 
        return self._ParameterNET.Default
 
    def getBounds(self):  # The method that does the work to get the bounds 
        return ParameterBounds(self._ParameterNET.getBounds())

    def getValue(self):  # [Internal] The method that does the work to get the value 
        return self._ParameterNET.getValue()

    @property
    def Name(self):  # The parameter name 
        return self._ParameterNET.Name
 
    def setValue(self,Object):  # The method that does the work to set the value 
        # TODO
        self._ParameterNET.setValue(Object)
 
    @property
    def Value(self):  # The parameter value 
        return self._ParameterNET.Value
    
    @property
    def ValueType(self):  # The type of the parameter 
        return PrimitiveType[self._ParameterNET.ValueType.ToString()]
 
class ParameterBounds():  # Represents the bounds of a generic parameter 
    _ParameterBoundsNET=None
    def __init__(self,ParameterBoundsNET=AerotechEnsembleParametersNET.ParameterBounds):
        self._ParameterBoundsNET=ParameterBoundsNET

    @property
    def Exists(self):  # Whether the parameter has bounds 
        return self._ParameterBoundsNET.Exists
    
    @property
    def Max(self):  # The parameter maximum value, if any 
        return self._ParameterBoundsNET.Max
    
    @property
    def Min(self):  # The parameter minimum value, if any 
        return self._ParameterBoundsNET.Min

class ParameterContext(Enum):  # Represents the context of a parameter (system, axis, or task) 
    System=AerotechEnsembleParametersNET.ParameterContext.System  # A system parameter 
    Axis=AerotechEnsembleParametersNET.ParameterContext.Axis  # An axis parameter 
    Task=AerotechEnsembleParametersNET.ParameterContext.Task # A task parameter  

class ParameterFile():  # Root parameter category that handles parameters from a file 
 
class ParameterRetrievalErrorEventArgs():  # Provides data for parameter retrieval errors 
 
class ParametersAllCollection(CommonCollections.NamedConstantCollection):  # Represents a category that contains parameters in a non-nested fashion 
    _ParametersAllCollectionNET=None
    def __init__(self,ParametersAllCollection):
        self._ParametersAllCollectionNET=ParametersAllCollection
        CommonCollections.NamedConstantCollection.__init__(self,ParametersAllCollection,Parameter)
 
class PiezoDefaultServoState(Enum):  # Represents the piezo default servo state.
    Off=AerotechEnsembleParametersNET.PiezoDefaultServoState.Off  # Servo Off
    On=AerotechEnsembleParametersNET.PiezoDefaultServoState.Off  # Servo On 

class PositionFeedbackChannel(Enum):  # Represents the position feedback channel type
    Default=AerotechEnsembleParametersNET.PositionFeedbackChannel.Default  # Default
    Channel0=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel0  # Channel 0
    Channel1=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel1  # Channel 1
    Channel2=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel2  # Channel 2
    Channel3=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel3  # Channel 3
    Channel4=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel4  # Channel 4 

class PositionFeedbackType(Enum):  # Represents the position feedback type
    LocalEncoderCounter=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Local Encoder Counter
    EncoderMultiplier=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Encoder Multiplier
    AnalogInput=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Analog Input
    EnDatAbsoluteEncoder=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # EnDat Absolute Encoder
    HallEffectSwitches=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Hall-Effect Switches
    Resolver=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Resolver
    ResoluteAbsoluteEncoder=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Resolute Absolute Encoder
    CapacitanceSensor=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Capacitance Sensor 
extend_enum(PositionFeedbackType,'None',getattr(AerotechEnsembleParametersNET.PositionFeedbackType,'None'))

class PrimitiveType(Enum):  # Represents a primitive type in AeroBasic 
    Integer=AerotechEnsembleParametersNET.PrimitiveType.Integer  # 32-bit integer 
    Double=AerotechEnsembleParametersNET.PrimitiveType.Double  # 64-bit floating point, ANSI/IEEE Standard 754-1985 
    Single=AerotechEnsembleParametersNET.PrimitiveType.Single  # 32-bit floating point, ANSI/IEEE Standard 754-1985 
    Long=AerotechEnsembleParametersNET.PrimitiveType.Long  # 64-bit integer 
    String=AerotechEnsembleParametersNET.PrimitiveType.String  # ASCII null-terminated string 

class SystemCalibrationParameterCategory(ParameterCategory):  # Contains the Calibration Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationAsciiParameterCategory(ParameterCategory):  # Contains the ASCII Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationEthernetIPParameterCategory(ParameterCategory):  # Contains the Ethernet/IP Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationEthernetSocketsParameterCategory(ParameterCategory):  # Contains the Ethernet Sockets Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationGpibParameterCategory(ParameterCategory):  # Contains the GPIB Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationModbusMasterParameterCategory(ParameterCategory):  # Contains the Modbus Master Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationModbusSlaveParameterCategory(ParameterCategory):  # Contains the Modbus Slave Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationParameterCategory(ParameterCategory):  # Contains the Communication Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationRS232ParameterCategory(ParameterCategory):  # Contains the RS-232 Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
        
class SystemCommunicationWebServerParameterCategory(ParameterCategory):  # Contains the Web Server Parameters
    _SystemCommunicationWebServerParameterCategoryNET=None
    def __init__(self,SystemCommunicationWebServerParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationWebServerParameterCategory):
        self._SystemCommunicationWebServerParameterCategoryNET=SystemCommunicationWebServerParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationWebServerParameterCategoryNET)
        
    @property
    def WebServerPort(self): # Allows access to the WebServerPort Parameter
        return TypedParameter(self._SystemCommunicationWebServerParameterCategoryNET.WebServerPort,int)
        
    @property
    def WebServerSetup(self): # Allows access to the WebServerSetup Parameter
        return TypedParameter(self._SystemCommunicationWebServerParameterCategoryNET.WebServerSetup,int)
 
class SystemJoystickParameterCategory(ParameterCategory):  # Contains the Joystick Parameters
    _SystemJoystickParameterCategoryNET=None
    def __init__(self,SystemJoystickParameterCategoryNET=AerotechEnsembleParametersNET.SystemJoystickParameterCategory):
        self._SystemJoystickParameterCategoryNET=SystemJoystickParameterCategoryNET
        ParameterCategory.__init__(self,SystemJoystickParameterCategoryNET)
        
    @property
    def JoystickInput0Deadband(self): # Allows access to the JoystickInput0Deadband Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput0Deadband,float)
    
    @property
    def JoystickInput0MaxVoltage(self): # Allows access to the JoystickInput0MaxVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput0MaxVoltage,float)
    
    @property
    def JoystickInput0MinVoltage(self): # Allows access to the JoystickInput0MinVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.DJoystickInput0MinVoltage,float)
    
    @property
    def JoystickInput1Deadband(self): # Allows access to the JoystickInput1Deadband Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput1Deadband,float)
    
    @property
    def JoystickInput1MaxVoltage(self): # Allows access to the JoystickInput1MaxVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput1MaxVoltage,float)
    
    @property
    def JoystickInput1MinVoltage(self): # Allows access to the JoystickInput1MinVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput1MinVoltage,float)
    
    @property
    def JoystickSetup(self): # Allows access to the JoystickSetup Parameter 
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickSetup,int)
        
class SystemMemoryAllocationParameterCategory(ParameterCategory):  # Contains the Memory Allocation Parameters
    _SystemMemoryAllocationParameterCategoryNET=None
    def __init__(self,SystemMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.SystemMemoryAllocationParameterCategory):
        self._SystemMemoryAllocationParameterCategoryNET=SystemMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,SystemMemoryAllocationParameterCategoryNET)
        
    @property
    def DataCollectionPoints(self): # Allows access to the DataCollectionPoints Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.DataCollectionPoints,int)
    
    @property
    def GlobalDoubles(self): # Allows access to the GlobalDoubles Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.GlobalDoubles,int)
    
    @property
    def GlobalIntegers(self): # Allows access to the GlobalIntegers Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.GlobalIntegers,int)
    
    @property
    def GlobalStrings(self): # Allows access to the GlobalStrings Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.GlobalStrings,int)

    @property
    def PrintBufferSize(self): # Allows access to the PrintBufferSize Parameter 
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.PrintBufferSize,int)

class SystemParameterCategory(ParameterCategory):  # Contains the System Parameters
    _SystemParameterCategoryNET=None
    def __init__(self,SystemParameterCategoryNET=AerotechEnsembleParametersNET.SystemParameterCategory):
        self._SystemParameterCategoryNET=SystemParameterCategoryNET
        ParameterCategory.__init__(self,SystemParameterCategoryNET)
        
    @property
    def Calibration(self): # Contains the Calibration Parameters
        return SystemCalibrationParameterCategory(self._SystemParameterCategoryNET.Calibration)

    @property
    def Communication(self): # Contains the Communication Parameters
        return SystemCommunicationParameterCategory(self._SystemParameterCategoryNET.Communication) 

    @property
    def DisplayAxes(self): # Allows access to the DisplayAxes Parameter
        return TypedParameter(self._SystemParameterCategoryNET.DisplayAxes,int)

    @property
    def ExternalSyncFrequency(self): # Allows access to the ExternalSyncFrequency Parameter
        return TypedParameter(self._SystemParameterCategoryNET.ExternalSyncFrequency,int)

    @property
    def FaultAckMoveOutOfLimit(self): # Allows access to the FaultAckMoveOutOfLimit Parameter
        return TypedParameter(self._SystemParameterCategoryNET.FaultAckMoveOutOfLimit,int)

    @property
    def Joystick(self): # Contains the Joystick Parameters
        return SystemJoystickParameterCategory(self._SystemParameterCategoryNET.Joystick)

    @property
    def MemoryAllocation(self): # Contains the Memory Allocation Parameters
        return SystemMemoryAllocationParameterCategory(self._SystemParameterCategoryNET.MemoryAllocation)

    @property
    def RequiredAxes(self): # Allows access to the RequiredAxes Parameter
        return TypedParameter(self._SystemParameterCategoryNET.RequiredAxes,int)

    @property
    def SoftwareExternalFaultInput(self): # Allows access to the SoftwareExternalFaultInput Parameter
        return TypedParameter(self._SystemParameterCategoryNET.SoftwareExternalFaultInput,int)

    @property
    def TaskExecutionSetup(self): # Allows access to the TaskExecutionSetup Parameter
        return TypedParameter(self._SystemParameterCategoryNET.TaskExecutionSetup,int)

    @property
    def User(self): # Contains the User Parameters 
        return SystemUserParameterCategory(self._SystemParameterCategoryNET.User)
        
class SystemUserParameterCategory(ParameterCategory):  # Contains the User Parameters
    _SystemUserParameterCategoryNET=None
    def __init__(self,SystemUserParameterCategoryNET=AerotechEnsembleParametersNET.SystemUserParameterCategory):
        self._SystemUserParameterCategoryNET=SystemUserParameterCategoryNET
        ParameterCategory.__init__(self,SystemUserParameterCategoryNET)
        
    @property
    def UserDouble0(self): # Allows access to the UserDouble0 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserDouble0,float)
    
    @property
    def UserDouble1(self): # Allows access to the UserDouble1 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserDouble1,float)
    
    @property
    def UserInteger0(self): # Allows access to the UserInteger0 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserInteger0,int)
    
    @property
    def UserInteger1(self): # Allows access to the UserInteger1 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserInteger1,int)
    
    @property
    def UserString0(self): # Allows access to the UserString0 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserString0,str)
    
    @property
    def UserString1(self): # Allows access to the UserString1 Parameter 
        return TypedParameter(self._SystemUserParameterCategoryNET.UserString1,str)
    
 
class TaskMemoryAllocationParameterCategory(ParameterCategory):  # Contains the Memory Allocation Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
          
    @property
    def CodeSize(self): # Allows access to the CodeSize Parameter
        return TypedParameter(self._TaskMemoryAllocationParameterCategoryNET.CodeSize,int)
    
    @property
    def DataSize(self): # Allows access to the DataSize Parameter
        return TypedParameter(self._TaskMemoryAllocationParameterCategoryNET.DataSize,int)
    
    @property
    def StackSize(self): # Allows access to the StackSize Parameter
        return TypedParameter(self._TaskMemoryAllocationParameterCategoryNET.StackSize,int)
 
class TaskMotionParameterCategory(ParameterCategory):  # Contains the Motion Parameters
    _TaskMotionParameterCategoryNET=None
    def __init__(self,TaskMotionParameterCategoryNET=AerotechEnsembleParametersNET.TaskMotionParameterCategory):
        self._TaskMotionParameterCategoryNET=TaskMotionParameterCategoryNET
        ParameterCategory.__init__(self,TaskMotionParameterCategoryNET)
        
    @property
    def DefaultCoordinatedRampDistance(self): # Allows access to the DefaultCoordinatedRampDistance Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampDistance,float)
    
    @property
    def DefaultCoordinatedRampMode(self): # Allows access to the DefaultCoordinatedRampMode Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampMode,int)
    
    @property
    def DefaultCoordinatedRampRate(self): # Allows access to the DefaultCoordinatedRampRate Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampRate,float)
    
    @property
    def DefaultCoordinatedRampTime(self): # Allows access to the DefaultCoordinatedRampTime Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampTime,float)
    
    @property
    def DefaultCoordinatedSpeed(self): # Allows access to the DefaultCoordinatedSpeed Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedSpeed,float)
    
    @property
    def DefaultDependentCoordinatedRampRate(self): # Allows access to the DefaultDependentCoordinatedRampRate Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultDependentCoordinatedRampRate,float)
    
    @property
    def DefaultDependentCoordinatedSpeed(self): # Allows access to the DefaultDependentCoordinatedSpeed Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultDependentCoordinatedSpeed,float)
    
    @property
    def DefaultSCurve(self): # Allows access to the DefaultSCurve Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultSCurve,float)
    
    @property
    def DefaultWaitMode(self): # Allows access to the DefaultWaitMode Parameter 
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultWaitMode,int)

class TaskParameterCategory(ParameterCategory):  # Contains the Task Parameters
    _TaskParameterCategoryNET=None
    def __init__(self,TaskParameterCategoryNET=AerotechEnsembleParametersNET.TaskParameterCategory):
        self._TaskParameterCategoryNET=TaskParameterCategoryNET
        ParameterCategory.__init__(self,TaskParameterCategoryNET)
        
    @property
    def AutoRunProgram(self): # Allows access to the AutoRunProgram Parameter
        return TypedParameter(self._TaskParameterCategoryNET.AutoRunProgram,str)
    
    @property
    def MemoryAllocation(self): # Contains the Memory Allocation Parameters
        return TaskMemoryAllocationParameterCategory(self._TaskParameterCategoryNET.MemoryAllocation)
    
    @property
    def Motion(self): # Contains the Motion Parameters
        return TaskMotionParameterCategory(self._TaskParameterCategoryNET.Motion)
    
    @property
    def TaskErrorAbortAxes(self): # Allows access to the TaskErrorAbortAxes Parameter
        return TypedParameter(self._TaskParameterCategoryNET.TaskErrorAbortAxes,int)
    
    @property
    def TaskId(self): # The task for which this category is for
        return Ensemble.TaskId[self._TaskParameterCategoryNET.TaskId.ToString()]
    
    @property
    def TaskStopAbortAxes(self): # Allows access to the TaskStopAbortAxes Parameter
        return TypedParameter(self._TaskParameterCategoryNET.TaskStopAbortAxes,int)
    
    @property
    def TaskTerminationAxes(self): # Allows access to the TaskTerminationAxes Parameter
        return TypedParameter(self._TaskParameterCategoryNET.TaskTerminationAxes,int)
    
class TypedParameter(Parameter):  # Represents a typed parameter 
    _TypedParameterNET=None
    _pyClass=None
    def __init__(self,TypedParameterNET,pyClass):
        self._TypedParameterNET=TypedParameterNET
        self._pyClass=pyClass
        Parameter.__init__(self,self._TypedParameterNET)
        
    @property
    def Bounds(self):  # Specifies the parameter bounds
        return TypedParameterBounds(self._TypedParameterNET.Bounds,self._pyClass)
    
    @property
    def Default(self):  # The parameter's default value 
        return self._pyClass(self._TypedParameterNET.Default)
 
    def getBounds(self):  # The method that does the work to get the bounds (Overrides Parameter.getBounds()()()().)
        return ParameterBounds(self._TypedParameterNET.getBounds())
    
    @property
    def Value(self):  # The parameter value 
        return self._pyClass(self._TypedParameterNET.Value)
   
class TypedParameterBounds(ParameterBounds):  # Represents bounds of a typed parameter 
    _TypedParameterBoundsNET=None
    _pyClass=None
    def __init__(self,TypedParameterBoundsNET,pyClass):
        self._TypedParameterBoundsNET=TypedParameterBoundsNET
        self._pyClass=pyClass
        ParameterBounds.__init__(self,self._TypedParameterBoundsNET)
        
    @property
    def Max(self):  # Parameter maximum value 
        return self._pyClass(self._TypedParameterBoundsNET.Max)
    
    @property
    def Min(self):  # Parameter minimum value  
        return self._pyClass(self._TypedParameterBoundsNET.Min)
        
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
