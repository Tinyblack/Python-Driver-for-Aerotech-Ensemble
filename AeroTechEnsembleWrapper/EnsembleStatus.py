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

import Common
import Ensemble
import EnsembleTasks
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
    import Aerotech.Ensemble.Status as AerotechEnsembleStatusNET
except:
    raise RuntimeError


class AxisDiagPacket():
    _AxisDiagPacketNET=None
    def __init__(self,AxisDiagPacketNET=AerotechEnsembleStatusNET.AxisDiagPacket):
        self._AxisDiagPacketNET=AxisDiagPacketNET
        
    @property
    def AbsoluteFeedback(self):  # The absolute feedback source position 
        return self._AxisDiagPacketNET.AbsoluteFeedback

    @property
    def AccelerationCommand(self):  # The acceleration command 
        return self._AxisDiagPacketNET.AccelerationCommand

    @property
    def AccelerationCommandCounts(self):  # The acceleration command, in counts 
        return self._AxisDiagPacketNET.AccelerationCommandCounts

    @property
    def AccelerationError(self):  # The acceleration error, in user units 
        return self._AxisDiagPacketNET.AccelerationError

    @property
    def AccelerationErrorCounts(self):  # The acceleration error, in counts 
        return self._AxisDiagPacketNET.AccelerationErrorCounts

    @property
    def AccelerationFeedback(self):  # The acceleration Feedback 
        return self._AxisDiagPacketNET.AccelerationFeedback

    @property
    def AccelerationFeedbackCounts(self):  # The acceleration Feedback, in counts 
        return self._AxisDiagPacketNET.AccelerationFeedbackCounts

    @property
    def AmplifierTemperature(self):  # The amplifier temperature 
        return self._AxisDiagPacketNET.AmplifierTemperature

    @property
    def AnalogInput0(self):  # Analog Input #0 
        return self._AxisDiagPacketNET.AnalogInput0

    @property
    def AnalogInput1(self):  # Analog Input #1 
        return self._AxisDiagPacketNET.AnalogInput1

    @property
    def AnalogInput2(self):  # Analog Input #2, available on certain hardware types only 
        return self._AxisDiagPacketNET.AnalogInput2

    @property
    def AnalogInput3(self):  # Analog Input #3, available on certain hardware types only 
        return self._AxisDiagPacketNET.AnalogInput3

    @property
    def AnalogOutput0(self):  # Analog Output #0 
        return self._AxisDiagPacketNET.AnalogOutput0

    @property
    def AnalogOutput1(self):  # Analog Output #1 
        return self._AxisDiagPacketNET.AnalogOutput1

    @property
    def AnalogOutput2(self):  # Analog Output #2, available on certain hardware types only 
        return self._AxisDiagPacketNET.AnalogOutput2

    @property
    def AnalogOutput3(self):  # Analog Output #3, available on certain hardware types only 
        return self._AxisDiagPacketNET.AnalogOutput3

    @property
    def AnalogOutput4(self):  # Analog Output #4, available on certain hardware types only 
        return self._AxisDiagPacketNET.AnalogOutput4

    @property
    def AxisFault(self):  # Axis fault 
        return AxisFault(self._AxisDiagPacketNET.AxisFault)

    @property
    def AxisName(self):  # The name of the axis for which this packet is for 
        return self._AxisDiagPacketNET.AxisName

    @property
    def AxisStatus(self):  # Axis status 
        return AxisStatus(self._AxisDiagPacketNET.AxisStatus)

    @property
    def CurrentCommand(self):  # Current command 
        return self._AxisDiagPacketNET.CurrentCommand

    @property
    def CurrentError(self):  # Current error 
        return self._AxisDiagPacketNET.CurrentError

    @property
    def CurrentFeedback(self):  # Current feedback 
        return self._AxisDiagPacketNET.CurrentFeedback

    @property
    def DigitalInput0(self):  # Digital Input #0 
        return self._AxisDiagPacketNET.DigitalInput0

    @property
    def DigitalInput1(self):  # Digital Input #1 
        return self._AxisDiagPacketNET.DigitalInput1

    @property
    def DigitalInput2(self):  # Digital Input #2 
        return self._AxisDiagPacketNET.DigitalInput2

    @property
    def DigitalOutput0(self):  # Digital Output #0 
        return self._AxisDiagPacketNET.DigitalOutput0

    @property
    def DigitalOutput1(self):  # Digital Output #1 
        return self._AxisDiagPacketNET.DigitalOutput1

    @property
    def DigitalOutput2(self):  # Digital Output #2 
        return self._AxisDiagPacketNET.DigitalOutput2

    @property
    def PiezoVoltageCommand(self):  # The Voltage Command for Piezo stages.
        return self._AxisDiagPacketNET.PiezoVoltageCommand

    @property
    def PiezoVoltageFeedback(self):  # The Voltage Feedback for Piezo stages.
        return self._AxisDiagPacketNET.PiezoVoltageFeedback

    @property
    def PositionCommand(self):  # The position command, in user units 
        return self._AxisDiagPacketNET.PositionCommand

    @property
    def PositionCommandCounts(self):  # The position command, in counts 
        return self._AxisDiagPacketNET.PositionCommandCounts

    @property
    def PositionError(self):  # The position error, in user units 
        return self._AxisDiagPacketNET.PositionError

    @property
    def PositionErrorCounts(self):  # The position error, in counts 
        return self._AxisDiagPacketNET.PositionErrorCounts

    @property
    def PositionFeedback(self):  # The position feedback, in user units 
        return self._AxisDiagPacketNET.PositionFeedback

    @property
    def PositionFeedbackAuxiliary(self):  # The position feedback auxiliary 
        return self._AxisDiagPacketNET.PositionFeedbackAuxiliary

    @property
    def PositionFeedbackCounts(self):  # The position feedback, in counts 
        return self._AxisDiagPacketNET.PositionFeedbackCounts

    @property
    def ProgramPositionCommand(self):  # The program position command, in user units 
        return self._AxisDiagPacketNET.ProgramPositionCommand

    @property
    def ProgramPositionCommandCounts(self):  # The program position command, in counts 
        return self._AxisDiagPacketNET.ProgramPositionCommandCounts

    @property
    def ProgramPositionError(self):  # The program position error, in user units 
        return self._AxisDiagPacketNET.ProgramPositionError

    @property
    def ProgramPositionErrorCounts(self):  # The program position error, in counts 
        return self._AxisDiagPacketNET.ProgramPositionErrorCounts

    @property
    def ProgramPositionFeedback(self):  # The program position feedback, in user units 
        return self._AxisDiagPacketNET.ProgramPositionFeedback

    @property
    def ProgramPositionFeedbackCounts(self):  # The program position feedback, in counts 
        return self._AxisDiagPacketNET.ProgramPositionFeedbackCounts

    @property
    def VelocityCommand(self):  # The velocity command, in user units 
        return self._AxisDiagPacketNET.AelocityCommand

    @property
    def VelocityCommandCounts(self):  # The velocity command, in counts 
        return self._AxisDiagPacketNET.VelocityCommandCounts

    @property
    def VelocityError(self):  # The velocity error, in user units 
        return self._AxisDiagPacketNET.VelocityError

    @property
    def VelocityErrorCounts(self):  # The velocity error, in counts 
        return self._AxisDiagPacketNET.VelocityErrorCounts

    @property
    def VelocityFeedback(self):  # The velocity feedback, in user units 
        return self._AxisDiagPacketNET.VelocityFeedback

    @property
    def VelocityFeedbackCounts(self):  # The velocity feedback, in counts  
        return self._AxisDiagPacketNET.VelocityFeedbackCounts
 
class AxisFault():  # Represents the faults of an axis
    _AxisFaultNET=None
    def __init__(self,AxisFaultNET=AerotechEnsembleStatusNET.AxisFault):
        self._AxisFaultNET=AxisFaultNET
     # TODO
class AxisStatus():  # Represents an axis status
    _AxisStatusNET=None
    def __init__(self,AxisStatusNET=AerotechEnsembleStatusNET.AxisStatus):
        self._AxisStatusNET=AxisStatusNET
        # TODO
 
class CallbacksPoller():  # Allows to poll for callback information from a controller in the background  
    # TODO
    
class ControlCenter():  # Retrieves diagnostic data, callbacks, and task states in the background from a controller 
    _ControlCenterNET=None
    def __init__(self,ControlCenterNET=AerotechEnsembleStatusNET.ControlCenter):
        self._ControlCenterNET=ControlCenterNET
        
    @property
    def Callbacks(self):  # Allows to setup polling for the different callbacks 
        return CallbacksPoller(self._ControlCenterNET.Callbacks)
    @property
    def Diagnostics(self):  # Allows to setup polling for diagnostic information 
        return DiagPacketPoller(self._ControlCenterNET.Diagnostics)
    @property
    def TaskStates(self):  # Allows to setup polling for task state information 
        return TaskStatesPoller(self._ControlCenterNET.TaskStates)

    def UnsubscribeAll(self):  # Unsubscribes everyone from this class or any of its members  
        self._ControlCenterNET.UnsubscribeAll()

 
class ControllerDiagPacket(CommonCollections.NamedMaskedConstantCollection):  # The diagnostic packet of the controller 
    _ControllerDiagPacketNET=None
    def __init__(self,ControllerDiagPacketNET):
        self._ControllerDiagPacketNET=ControllerDiagPacketNET
        CommonCollections.NamedMaskedConstantCollection.__init__(self,ControllerDiagPacketNET,AxisDiagPacket,Ensemble.AxisMask)
        
    @property
    def DebugFlags(self):  # The debugging flags on the controller 
        return DebugFlags(self._ControllerDiagPacketNET.DebugFlags)
    
    @property
    def Joystick(self):  # The status of the joystick input 
        return JoystickDiagPacket(self._ControllerDiagPacketNET.Joystick)
    
    @property
    def PacketTime(self):  # The time of the packet since controller boot up 
        return self._ControllerDiagPacketNET.PacketTime
    
    @property
    def PlaneStatus(self):  # The status of the planes on the controller 
        return PlaneStatus(self._ControllerDiagPacketNET.PlaneStatus)
    
    @property
    def ProgramCounter(self):  # The program counts of the user tasks 
        return CommonCollections.NamedConstantCollection(self._ControllerDiagPacketNET.ProgramCounter,int)
    
    @property
    def ProgramPosition(self):  # The program positions of the user tasks  
        return CommonCollections.NamedConstantCollection(self._ControllerDiagPacketNET.ProgramPosition,Common.FilePoint)

class ControllerEventArgs():  # The base class for classes containing event data related to controllers. 
    _ControllerEventArgsNET=None
    def __init__(self,ControllerEventArgsNET=AerotechEnsembleStatusNET.ControllerEventArgs):
        self._ControllerEventArgsNET=ControllerEventArgsNET
        
    @property
    def Controller(self):
        return Ensemble.Controller(self._ControllerEventArgsNET.Controller)
        
class DebugFlags():  # Represents the debug flags on the controller
    _DebugFlagsNET=None
    
    @multimethod
    def __init__(self,DebugFlagsNET=AerotechEnsembleStatusNET.DebugFlags):
        self._DebugFlagsNET=DebugFlagsNET
        
    @multimethod
    def __init__(self):  # Creates a new instance with all things unset (false)
        self._DebugFlagsNET=AerotechEnsembleStatusNET.DebugFlags()
        
    @multimethod
    def __init__(self,maskValue:int):  # Creates a new instance with given mask value
        self._DebugFlagsNET=AerotechEnsembleStatusNET.DebugFlags(maskValue)
        
    @property
    def ActiveBits(self):  # Returns a list of the active bit names.
        # TODO deal with ReadOnlyCollection 
        return self._DebugFlagsNET.ActiveBits
    
    @property
    def BitHelpLinks(self):  # Returns a dictionary of bit value names (keys) and the associated help file link (values) 
        # TODO deal with IDictionary 
        return self._DebugFlagsNET.BitHelpLinks
    
    @property
    def BitValues(self):  # Returns a listing of the bit names and their corresponding values 
        # TODO deal with IDictionary 
        return self._DebugFlagsNET.BitValues
      
    @property
    def CollectionDone(self):  # Collection Done
        return self._DebugFlagsNET.CollectionDone
    
    @property
    def CollectionTriggered(self):  # Collection Triggered
        return self._DebugFlagsNET.CollectionTriggered
    
    @property
    def InputBoxCallbackPending(self):  # Input Box Callback Pending
        return self._DebugFlagsNET.InputBoxCallbackPending
    
    @property
    def MaskValue(self):  # The underlying mask value 
        return self._DebugFlagsNET.MaskValue
    
    @property
    def PrintStringCallbackPending(self):  # Print String Callback Pending
        return self._DebugFlagsNET.PrintStringCallbackPending
    
    @multimethod
    def ToString(self):  # 
        return self._DebugFlagsNET.ToString()
    
    @multimethod
    def ToString(self,userReadableFormat:bool):  # Converts to a string representation 
        return self._DebugFlagsNET.ToString(userReadableFormat)
    
    @property
    def ValueNames(self):  # Returns a mapping of values to their human readable form. 
        # TODO deal with IDictionary 
        return self._DebugFlagsNET.ValueNames
    

# * Checked
class DiagPacketPoller():  # Allows to poll for diagnostic information from a controller in the background 
    _DiagPacketPollerNET=None
    def __init__(self,DiagPacketPollerNET=AerotechEnsembleStatusNET.DiagPacketPoller):
        self._DiagPacketPollerNET=DiagPacketPollerNET

    @property
    def AutoStart(self):  # Whether to start polling when someone subscribes to the NewTaskStatesArrived
        return self._DiagPacketPollerNET.AutoStart
 
    # ErrorOccurred  Raised when an error occurs during retrieval of data from the controller 
 
    @property
    def IsExecutingEvent(self):  # Tells whether there is currenty an event being executed 
        return self._DiagPacketPollerNET.IsExecutingEvent
 
    @property
    def IsSuspended(self):  # Whether the polling is suspended 
        return self._DiagPacketPollerNET.IsSuspended
 
    @property
    def Latest(self):  # The latest task states packet that was retrieved from the controller 
        return ControllerDiagPacket(self._DiagPacketPollerNET.Latest)

    # NewTaskStatesArrived  Event that gets called when new task states has been retrieved 
 
    @classmethod
    @property
    def RefreshInterval(self):  # he interval of retrieving of data 
        return AerotechEnsembleStatusNET.DiagPacketPoller.RefreshInterval
            
    def Resume(self):  # Resumes the polling for task state information 
        self._DiagPacketPollerNET.Resume()
 
    def Suspend(self):  # Suspends the polling for task state information 
        self._DiagPacketPollerNET.Suspend()
    
# * Checked   
class ErrorEventArgs(ControllerEventArgs):  # Provides data for the error events 
    _ErrorEventArgsNET=None
    def __init__(self,ErrorEventArgsNET=AerotechEnsembleStatusNET.ErrorEventArgs):
        self._ErrorEventArgsNET=ErrorEventArgsNET
        ControllerEventArgs.__init__(self,ErrorEventArgsNET)
        
    @property
    def Exception(self): # The exception that caused the error to happen  
        return self._ErrorEventArgsNET.Exception

# * Checked
class ErrorInformation(): # Provides error information.
    _ErrorInformationNET=None
    def __init__(self,ErrorInformationNET=AerotechEnsembleStatusNET.ErrorInformation):
        self._ErrorInformationNET=ErrorInformationNET
        
    @property
    def Description(self): # The description of the error.
        return self._ErrorInformationNET.Description
    
    @property
    def ErrorCode(self):   # The error code identifier.
        return self._ErrorInformationNET.ErrorCode

    @property
    def HelpKey(self):   # Specifies the key to look for in the help file for a more detailed description.
        return self._ErrorInformationNET.HelpKey
    
    @property
    def HelpLink(self):   # Gets the link to the help associated with this error.
        return self._ErrorInformationNET.HelpLink

    def ToString(self):  # Returns a string representation of this class.
        return self._ErrorInformationNET.ToString()

# * Checked
class InputBoxCallbackEventArgs(ControllerEventArgs): # Provides data for InputBoxCallback
    _InputBoxCallbackEventArgsNET=None
    def __init__(self,InputBoxCallbackEventArgsNET=AerotechEnsembleStatusNET.InputBoxCallbackEventArgs):
        self._InputBoxCallbackEventArgsNET=InputBoxCallbackEventArgsNET
        ControllerEventArgs.__init__(self,InputBoxCallbackEventArgsNET)
        
    @property
    def DefaultValue(self):  # The default value to return by the command  
        return self._InputBoxCallbackEventArgsNET.DefaultValue
    
    @property
    def Handled(self):  # Whether this callback has already been handled by another event handler  
        return self._InputBoxCallbackEventArgsNET.Handled
    
    @property
    def Prompt(self):  # The prompt to ask the user  
        return self._InputBoxCallbackEventArgsNET.Prompt
    
    @property
    def ReturnValue(self):  # The value to return to the callback  
        return self._InputBoxCallbackEventArgsNET.ReturnValue
 
# * Checked
class JoystickButton(Enum): # Specifies the button on a joystick 
    ButtonA=AerotechEnsembleStatusNET.JoystickButton.ButtonA #Button A 
    ButtonB=AerotechEnsembleStatusNET.JoystickButton.ButtonB #Button B 
    ButtonC=AerotechEnsembleStatusNET.JoystickButton.ButtonC #Button C (both A and B)  
extend_enum(JoystickButton,'None',getattr(AerotechEnsembleStatusNET.JoystickButton,'None'))

# * Checked
class JoystickDiagPacket(): # Represents the diagnostic information about the joystick 
    _JoystickDiagPacketNET=None
    def __init__(self,JoystickDiagPacketNET=AerotechEnsembleStatusNET.JoystickDiagPacket):
        self._JoystickDiagPacketNET=JoystickDiagPacketNET
        
    @property
    def Button(self):   # Specifies which button on the joystick is pressed  
        return JoystickButton[self._JoystickDiagPacketNET.Button.ToString()]
    @property
    def Horizontal(self):   # The horizontal axis value 
        return self._JoystickDiagPacketNET.Horizontal
    @property
    def IsActive(self):   # Whether joystick is in active on any axis 
        return self._JoystickDiagPacketNET.IsActive
    @property
    def IsConnected(self):   # Whether the joystick is connected
        return self._JoystickDiagPacketNET.IsConnected
    @property
    def Vertical(self):   # The vertical axis value  
        return self._JoystickDiagPacketNET.Vertical

# * Checked
class NewDiagPacketArrivedEventArgs(ControllerEventArgs): # Provides data for NewDiagPacketArrived
    _NewDiagPacketArrivedEventArgsNET=None
    def __init__(self,NewDiagPacketArrivedEventArgsNET=AerotechEnsembleStatusNET.NewDiagPacketArrivedEventArgs):
        self._NewDiagPacketArrivedEventArgsNET=NewDiagPacketArrivedEventArgsNET
        ControllerEventArgs.__init__(self,NewDiagPacketArrivedEventArgsNET)
        
    @property
    def Data(self):   # The most recent diagnostics retrieved from the controller  
        return ControllerDiagPacket(self._NewDiagPacketArrivedEventArgsNET.Data)
    
# * Checked
class NewTaskStatesArrivedEventArgs(ControllerEventArgs): # Provides data for NewTaskStatesArrived
    _NewTaskStatesArrivedEventArgsNET=None
    def __init__(self,NewTaskStatesArrivedEventArgsNET=AerotechEnsembleStatusNET.NewTaskStatesArrivedEventArgs):
        self._NewTaskStatesArrivedEventArgsNET=NewTaskStatesArrivedEventArgsNET
        ControllerEventArgs.__init__(self,NewTaskStatesArrivedEventArgsNET)
    
    @property
    def TaskStates(self):   # The most recent task state information retrieved from the controller  
        return CommonCollections.NamedConstantCollection(self._NewTaskStatesArrivedEventArgsNET.TaskStates,EnsembleTasks.TaskState)
    
# * Checked
class PlaneStatus(): # Represents plane status
    _PlaneStatusNET=None
    
    @multimethod
    def __init__(self,PlaneStatusNET:AerotechEnsembleStatusNET.PlaneStatus=AerotechEnsembleStatusNET.PlaneStatus):
        self._PlaneStatusNET=PlaneStatusNET
        
    @multimethod
    def __init__(self):  # Creates a new instance with all things unset (false)
        self._PlaneStatusNET=AerotechEnsembleStatusNET.PlaneStatus()
        
    @multimethod
    def __init__(self,maskValue:int):  # Creates a new instance with given mask value
        self._PlaneStatusNET=AerotechEnsembleStatusNET.PlaneStatus(maskValue)

    @property
    def AccelerationPhaseActive(self):  # Acceleration Phase Active
        return self._PlaneStatusNET.AccelerationPhaseActive
    @property
    def ActiveBits(self):  # Returns a list of the active bit names.
        # TODO deal with ReadonlyCollections
        return self._PlaneStatusNET.ActiveBits
    @property
    def BitHelpLinks(self):  # Returns a dictionary of bit value names (keys) and the associated help file link (values) 
        # TODO deal with IDictionary
        return self._PlaneStatusNET.BitHelpLinks
    @property
    def BitValues(self):  # Returns a listing of the bit names and their corresponding values 
        # TODO deal with IDictionary
        return self._PlaneStatusNET.BitValues
    @property
    def DecelerationPhaseActive(self):  # Deceleration Phase Active
        return self._PlaneStatusNET.DecelerationPhaseActive
    @property
    def HoldModeActive(self):  # Hold Mode Active
        return self._PlaneStatusNET.HoldModeActive
    @property
    def MaskValue(self):  # The underlying mask value 
        return self._PlaneStatusNET.MaskValue
    @property
    def MotionAborting(self):  # Motion Aborting
        return self._PlaneStatusNET.MotionAborting
    @property
    def MotionActive(self):  # Motion Active
        return self._PlaneStatusNET.MotionActive
    @multimethod
    def ToString(self):  # Converts to a string representation 
        return self._PlaneStatusNET.ToString()
    @multimethod 
    def ToString(self,userReadableFormat:bool):  # Converts to a string representation 
        return self._PlaneStatusNET.ToString(userReadableFormat)
    @property
    def ValueNames(self):  # Returns a mapping of values to their human readable form. 
        # TODO deal with IDictionary
        return self._PlaneStatusNET.ValueName
    @property
    def VelocityProfilingActive(self):  # Velocity Profiling Active 
        return self._PlaneStatusNET.VelocityProfilingActive
    
# * Checked
class PrintCallbackEventArgs(ControllerEventArgs): # Provides data for PrintCallback
    _PrintCallbackEventArgsNET=None
    def __init__(self,PrintCallbackEventArgsNET=AerotechEnsembleStatusNET.PrintCallbackEventArgs):
        self._PrintCallbackEventArgsNET=PrintCallbackEventArgsNET
        ControllerEventArgs.__init__(self,PrintCallbackEventArgsNET)
        
    @property
    def Message(self):
        return self._PrintCallbackEventArgsNET.Message()
    
# * Checked
class TaskStatesPoller(): # Allows to poll for task state information from a controller in the background  
    _TaskStatesPollerNET=None
    def __init__(self,TaskStatesPollerNET=AerotechEnsembleStatusNET.TaskStatesPoller):
        self._TaskStatesPollerNET=TaskStatesPollerNET

    @property
    def AutoStart(self):  # Whether to start polling when someone subscribes to the NewTaskStatesArrived
        return self._TaskStatesPollerNET.AutoStart
 
    # ErrorOccurred  Raised when an error occurs during retrieval of data from the controller 
 
    @property
    def IsExecutingEvent(self):  # Tells whether there is currenty an event being executed 
        return self._TaskStatesPollerNET.IsExecutingEvent
 
    @property
    def IsSuspended(self):  # Whether the polling is suspended 
        return self._TaskStatesPollerNET.IsSuspended
 
    @property
    def Latest(self):  # The latest task states packet that was retrieved from the controller 
        return NewTaskStatesArrivedEventArgs(self._TaskStatesPollerNET.Latest)

    # NewTaskStatesArrived  Event that gets called when new task states has been retrieved 
 
    @classmethod
    @property
    def RefreshInterval(self):  # he interval of retrieving of data 
        return AerotechEnsembleStatusNET.TaskStatesPoller.RefreshInterval
            
    def Resume(self):  # Resumes the polling for task state information 
        self._TaskStatesPollerNET.Resume()
 
    def Suspend(self):  # Suspends the polling for task state information 
        self._TaskStatesPollerNET.Suspend()
 
