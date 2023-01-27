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
 
class AxisStatus():  # Represents an axis status
    _AxisStatusNET=None
    def __init__(self,AxisStatusNET=AerotechEnsembleStatusNET.AxisStatus):
        self._AxisStatusNET=AxisStatusNET
 
class CallbacksPoller():  # Allows to poll for callback information from a controller in the background 
 
class ControlCenter():  # Retrieves diagnostic data, callbacks, and task states in the background from a controller 
 
class ControllerDiagPacket():  # The diagnostic packet of the controller 

class ControllerEventArgs():  # The base class for classes containing event data related to controllers. 
 
class DebugFlags():  # Represents the debug flags on the controller
 
class DiagPacketPoller():  # Allows to poll for diagnostic information from a controller in the background 
 
class ErrorEventArgs():  # Provides data for the error events 
  
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

    def ToString(self)  # Returns a string representation of this class.
        return self._ErrorInformationNET.ToString()

        
 
class InputBoxCallbackEventArgs(): # Provides data for InputBoxCallback
 
class JoystickButton(Enum): # Specifies the button on a joystick 
    ButtonA=AerotechEnsembleStatusNET.JoystickButton.ButtonA #Button A 
    ButtonB=AerotechEnsembleStatusNET.JoystickButton.ButtonB #Button B 
    ButtonC=AerotechEnsembleStatusNET.JoystickButton.ButtonC #Button C (both A and B)  
extend_enum(JoystickButton,'None',getattr(AerotechEnsembleStatusNET.JoystickButton,'None'))

 
class JoystickDiagPacket(): # Represents the diagnostic information about the joystick 
 
class NewDiagPacketArrivedEventArgs(): # Provides data for NewDiagPacketArrived
 
class NewTaskStatesArrivedEventArgs(): # Provides data for NewTaskStatesArrived
 
class PlaneStatus(): # Represents plane status
 
class PrintCallbackEventArgs(): # Provides data for PrintCallback
 
class TaskStatesPoller(): # Allows to poll for task state information from a controller in the background  



'''
    AbsoluteFeedback=None
    AccelerationCommand=None
    AccelerationCommandCounts=None
    AccelerationError=None
    AccelerationErrorCounts=None
    AccelerationFeedback=None
    AccelerationFeedbackCounts=None
    AmplifierTemperature=None
    AnalogInput0=None
    AnalogInput1=None
    AnalogInput2=None
    AnalogInput3=None
    AnalogOutput0=None
    AnalogOutput1=None
    AnalogOutput2=None
    AnalogOutput3=None
    AnalogOutput4=None
    AxisFault=None
    AxisName=None
    AxisStatus=None
    CurrentCommand=None
    CurrentError=None
    CurrentFeedback=None
    DigitalInput0=None
    DigitalInput1=None
    DigitalInput2=None
    DigitalOutput0=None
    DigitalOutput1=None
    DigitalOutput2=None
    PiezoVoltageCommand=None
    PiezoVoltageFeedback=None
    PositionCommand=None
    PositionCommandCounts=None 
    PositionError=None
    PositionErrorCounts=None
    PositionFeedback=None
    PositionFeedbackAuxiliary=None 
    PositionFeedbackCounts=None
    ProgramPositionCommand=None
    ProgramPositionCommandCounts=None
    ProgramPositionError=None
    ProgramPositionErrorCounts=None
    ProgramPositionFeedback=None
    ProgramPositionFeedbackCounts=None
    VelocityCommand=None
    VelocityCommandCounts=None
    VelocityError=None
    VelocityErrorCounts=None
    VelocityFeedback=None
    VelocityFeedbackCounts=None  

    def __init__(self):
        pass

    def toString(self):
        return vars(self)
        
    def updateStatus(self,data):
        self.AbsoluteFeedback=data.AbsoluteFeedback
        self.AccelerationCommand=data.AccelerationCommand
        self.AccelerationCommandCounts=data.AccelerationCommandCounts
        self.AccelerationError=data.AccelerationError
        self.AccelerationErrorCounts=data.AccelerationErrorCounts
        self.AccelerationFeedback=data.AccelerationFeedback
        self.AccelerationFeedbackCounts=data.AccelerationFeedbackCounts
        self.AmplifierTemperature=data.AmplifierTemperature
        self.AnalogInput0=data.AnalogInput0
        self.AnalogInput1=data.AnalogInput1
        self.AnalogInput2=data.AnalogInput2
        self.AnalogInput3=data.AnalogInput3
        self.AnalogOutput0=data.AnalogOutput0
        self.AnalogOutput1=data.AnalogOutput1
        self.AnalogOutput2=data.AnalogOutput2
        self.AnalogOutput3=data.AnalogOutput3
        self.AnalogOutput4=data.AnalogOutput4
        self.AxisFault=data.AxisFault
        self.AxisName=data.AxisName
        self.AxisStatus=data.AxisStatus
        self.CurrentCommand=data.CurrentCommand
        self.CurrentError=data.CurrentError
        self.CurrentFeedback=data.CurrentFeedback
        self.DigitalInput0=data.DigitalInput0
        self.DigitalInput1=data.DigitalInput1
        self.DigitalInput2=data.DigitalInput2
        self.DigitalOutput0=data.DigitalOutput0
        self.DigitalOutput1=data.DigitalOutput1
        self.DigitalOutput2=data.DigitalOutput2
        self.PiezoVoltageCommand=data.PiezoVoltageCommand
        self.PiezoVoltageFeedback=data.PiezoVoltageFeedback
        self.PositionCommand=data.PositionCommand
        self.PositionCommandCounts=data.PositionCommandCounts
        self.PositionError=data.PositionError
        self.PositionErrorCounts=data.PositionErrorCounts
        self.PositionFeedback=data.PositionFeedback
        self.PositionFeedbackAuxiliary=data.PositionFeedbackAuxiliary
        self.PositionFeedbackCounts=data.PositionFeedbackCounts
        self.ProgramPositionCommand=data.ProgramPositionCommand
        self.ProgramPositionCommandCounts=data.ProgramPositionCommandCounts
        self.ProgramPositionError=data.ProgramPositionError
        self.ProgramPositionErrorCounts=data.ProgramPositionErrorCounts
        self.ProgramPositionFeedback=data.ProgramPositionFeedback
        self.ProgramPositionFeedbackCounts=data.ProgramPositionFeedbackCounts
        self.VelocityCommand=data.VelocityCommand
        self.VelocityCommandCounts=data.VelocityCommandCounts
        self.VelocityError=data.VelocityError
        self.VelocityErrorCounts=data.VelocityErrorCounts
        self.VelocityFeedback=data.VelocityFeedback
        self.VelocityFeedbackCounts=data.VelocityFeedbackCounts
'''