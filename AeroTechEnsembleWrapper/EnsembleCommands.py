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

import time

from enum import Enum
from aenum import extend_enum

from multimethod import multimethod

import CommonCollections

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble as AerotechEnsembleNET
    import Aerotech.Ensemble.Commands as AerotechEnsembleCommandsNET
except:
    raise RuntimeError

class AdvancedAnalogCommands(CommandCategory):
    _AdvancedAnalogCommandsNET=None
    def __init__(self,AdvancedAnalogCommandsNET=AerotechEnsembleCommandsNET.AdvancedAnalogCommands):
        self._AdvancedAnalogCommandsNET=AdvancedAnalogCommandsNET

    @multimethod
    def AnalogControlOff(self,Axis:int):  # Configures an axis to generate its position command based on an analog input signal.
        self._AdvancedAnalogCommandsNET.AnalogControlOff(Axis)
    @multimethod
    def AnalogControlOff(self,Axis:str):  # Configures an axis to generate its position command based on an analog input signal.
        self._AdvancedAnalogCommandsNET.AnalogControlOff(Axis)
    @multimethod
    def AnalogControlOn(self,Axis:int, AnalogInput:int, ScaleFactor:float, OffsetValue:float):  # Configures an axis to generate its position command based on an analog input signal.
        self._AdvancedAnalogCommandsNET.AnalogControlOn(Axis, AnalogInput, ScaleFactor, OffsetValue)
    @multimethod
    def AnalogControlOn(self,Axis:str, AnalogInput:int, ScaleFactor:float, OffsetValue:float):  # Configures an axis to generate its position command based on an analog input signal.
        self._AdvancedAnalogCommandsNET.AnalogControlOn(Axis, AnalogInput, ScaleFactor, OffsetValue)
    @multimethod
    def AnalogControlOn(self,Axis:int, AnalogInput:int, ScaleFactor:float, OffsetValue:float, SpeedValue:float):  # Configures an axis to generate its position command based on an analog input signal.
        self._AdvancedAnalogCommandsNET.AnalogControlOn(Axis, AnalogInput, ScaleFactor, OffsetValue, SpeedValue)
    @multimethod
    def AnalogControlOn(self,Axis:str, AnalogInput:int, ScaleFactor:float, OffsetValue:float, SpeedValue:float):  # Configures an axis to generate its position command based on an analog input signal.
        self._AdvancedAnalogCommandsNET.AnalogControlOn(Axis, AnalogInput, ScaleFactor, OffsetValue, SpeedValue)
    @multimethod
    def AnalogTrack(self,Axis:int, AnalogInput:int, ScaleFactor:float, OffsetValue:float):  # Configures the system to continuously set an analog output to be a real-time internal servo loop value.
        self._AdvancedAnalogCommandsNET.AnalogTrack(Axis, AnalogInput, ScaleFactor, OffsetValue)
    @multimethod
    def AnalogTrack(self,Axis:str, AnalogInput:int, ScaleFactor:float, OffsetValue:float):  # Configures the system to continuously set an analog output to be a real-time internal servo loop value.
        self._AdvancedAnalogCommandsNET.AnalogTrack(Axis, AnalogInput, ScaleFactor, OffsetValue)
    @multimethod
    def AnalogTrack(self,Axis:int, AnalogInput:int, ScaleFactor:float, OffsetValue:float, SpeedValue:float):  # Configures the system to continuously set an analog output to be a real-time internal servo loop value.
        self._AdvancedAnalogCommandsNET.AnalogTrack(Axis, AnalogInput, ScaleFactor, OffsetValue, SpeedValue)
    @multimethod
    def AnalogTrack(self,Axis:str, AnalogInput:int, ScaleFactor:float, OffsetValue:float, SpeedValue:float):  # Configures the system to continuously set an analog output to be a real-time internal servo loop value.
        self._AdvancedAnalogCommandsNET.AnalogTrack(Axis, AnalogInput, ScaleFactor, OffsetValue, SpeedValue)
    @multimethod
    def AnalogTrack(self,Axis:int, AnalogInput:int, ScaleFactor:float, OffsetValue:float, SpeedValue:float, MinVoltage:float, MaxVoltage:float):  # Configures the system to continuously set an analog output to be a real-time internal servo loop value.
        self._AdvancedAnalogCommandsNET.AnalogTrack(Axis, AnalogInput, ScaleFactor, OffsetValue, SpeedValue, MinVoltage, MaxVoltage)
    @multimethod
    def AnalogTrack(self,Axis:str, AnalogInput:int, ScaleFactor:float, OffsetValue:float, SpeedValue:float, MinVoltage:float, MaxVoltage:float):  # Configures the system to continuously set an analog output to be a real-time internal servo loop value. 
        self._AdvancedAnalogCommandsNET.AnalogTrack(Axis, AnalogInput, ScaleFactor, OffsetValue, SpeedValue, MinVoltage, MaxVoltage)

class AdvancedCommands(CommandCategory):
    _AdvancedCommandsNET=None
    def __init__(self,AdvancedCommandsNET=AerotechEnsembleCommandsNET.AdvancedCommands):
        self._AdvancedCommandsNET=AdvancedCommandsNET
    
    @property
    def Analog(self):  # Contains the Analog Commands 
        return AdvancedAnalogCommands(self._AdvancedCommandsNET.Analog)

class AxesIOCommands(CommandCategory):
    _AxesIOCommandsNET=None
    def __init__(self,AxesIOCommandsNET=AerotechEnsembleCommandsNET.AxesIOCommands):
        self._AxesIOCommandsNET=AxesIOCommandsNET
        
    def Brake(self,OnOff:OnOff):  # Controls the brake output of axes. 
        return self._AxesIOCommandsNET.Brake(OnOff.value)

class AxesMotionCommands(CommandCategory):
    _AxesMotionCommandsNET=None
    def __init__(self,AxesMotionCommandsNET=AerotechEnsembleCommandsNET.AxesMotionCommands):
        self._AxesMotionCommandsNET=AxesMotionCommandsNET
        
        
Abort()()()():  # Aborts motion on the selected axes 

AutoFocus(OnOff):  # Turns on or turns off autofocus.

BlockMotion(OnOff):  # Sets motion blocking to On or OFF.

Disable()()()():  # Disables the axes.

Enable()()()():  # Enables the axes.

FaultAck()()()():  # Acknowledges and clears the fault on axes.

FreeRun(array<Double>[]()[][]):  # Freeruns the axes.

FreeRunStop()()()():  # Freeruns the axes.

Home()()()():  # Homes the axes.

HomeConditional()()()():  # Homes the axes.

Linear(array<Double>[]()[][]):  # Executes a linear move on axes.

Linear(array<Double>[]()[][], Double):  # Executes a linear move on axes.

MoveAbs(array<Double>[]()[][]):  # Executes an absolute move on axes.

MoveAbs(array<Double>[]()[][], array<Double>[]()[][]):  # Executes an absolute move on axes.

MoveInc(array<Double>[]()[][]):  # Executes an incremental move on axes.

MoveInc(array<Double>[]()[][], array<Double>[]()[][]):  # Executes an incremental move on axes.

Setup:  # Contains the Setup Commands

WaitForMotionDone(WaitOption, Int32):  # Waits for the move to be done 

WaitForMotionDone(WaitOption):  # Waits for the move to be done  


class AxesMotionSetupCommands(CommandCategory):
    _AxesMotionSetupCommandsNET=None
    def __init__(self,AxesMotionSetupCommandsNET=AerotechEnsembleCommandsNET.AxesMotionSetupCommands):
        self._AxesMotionSetupCommandsNET=AxesMotionSetupCommandsNET
        
PosCap()()()():  # Retrieves the POSCAP positions.

PosCap(Boolean):  # Retrieves the POSCAP positions.

RampDist(array<Double>[]()[][]):  # Specifies distance-based acceleration and deceleration.

RampMode(RampMode):  # Specifies the ramp mode calculation type to use.

RampRate(array<Double>[]()[][]):  # Specifies rate-based acceleration and deceleration.

RampTime(array<Double>[]()[][]):  # Specifies time-based acceleration and deceleration.

Reconcile()()()():  # Reconciles the position of the axes in the list on the plane to servo position.
 


class AxesRootCommands(CommandCategory):
    _AxesRootCommandsNET=None
    def __init__(self,AxesRootCommandsNET=AerotechEnsembleCommandsNET.AxesRootCommands):
        self._AxesRootCommandsNET=AxesRootCommandsNET
        
    @property
    def IO(self):  # Contains the IO Commands 
        return AxesIOCommands(self._AxesRootCommandsNET.IO)
    
    @property
    def Motion(self):  # Contains the Motion Commands
        return AxesMotionCommands(self._AxesRootCommandsNET.Motion)

class AxesSelectionCommands():
    def __init__(self):
        pass

class CommandCategory():
    _CommandCategoryNET=None
    def __init__(self,CommandCategoryNET=AerotechEnsembleCommandsNET.CommandCategory):
        self._CommandCategoryNET=CommandCategoryNET

class DataAcquisitionCommands(CommandCategory):
    _DataAcquisitionCommandsNET=None
    def __init__(self,DataAcquisitionCommandsNET=AerotechEnsembleCommandsNET.DataAcquisitionCommands):
        self._DataAcquisitionCommandsNET=DataAcquisitionCommandsNET

ArrayRead(Int32, Int32, Int32):  # Transfers drive array values into the specified controller array variables.

ArrayRead(String, Int32, Int32):  # Transfers drive array values into the specified controller array variables.

ArraySetup(Int32, Int32):  # Enables data collection.

ArraySetup(String, Int32):  # Enables data collection.

Input(Int32, Int32):  # Specifies the data element collected when a trigger occurs.

Input(String, Int32):  # Specifies the data element collected when a trigger occurs.

Off(Int32):  # Turns off data acquisition. All previously specified DATAACQ command configurations are cleared and must be re-specified if required.

Off(String):  # Turns off data acquisition. All previously specified DATAACQ command configurations are cleared and must be re-specified if required.

Trigger(Int32, Int32):  # Specifies which signal is monitored to collect data.

Trigger(String, Int32):  # Specifies which signal is monitored to collect data. 

        
class EthernetStatus(Enum):
    DataInTransmitter=AerotechEnsembleCommandsNET.EthernetStatus.DataInTransmitter
    DataInReceiver=AerotechEnsembleCommandsNET.EthernetStatus.DataInReceiver

class IOCommands(CommandCategory):
    _IOCommandsNET=None
    def __init__(self,IOCommandsNET=AerotechEnsembleCommandsNET.IOCommands):
        self._IOCommandsNET=IOCommandsNET

AnalogInput(Int32, Int32):  # Reads the analog input voltage.
 
AnalogInput(String, Int32):  # Reads the analog input voltage.

AnalogOutput(Int32, array<Int32>[]()[][], array<Double>[]()[][]):  # Sets the value of the analog output.

AnalogOutput(String, array<Int32>[]()[][], array<Double>[]()[][]):  # Sets the value of the analog output.

Brake(array<Int32>[]()[][], OnOff):  # Controls the brake output of axes.

Brake(Int32, OnOff):  # Controls the brake output of axes.

Brake(array<String>[]()[][], OnOff):  # Controls the brake output of axes.

Brake(String, OnOff):  # Controls the brake output of axes.

Brake(AxisMask, OnOff):  # Controls the brake output of axes.

DigitalInput(Int32, Int32):  # Reads the digital input value.

DigitalInput(String, Int32):  # Reads the digital input value.

DigitalInputBit(Int32, Int32, Int32):  # Reads the digital input value.

DigitalInputBit(String, Int32, Int32):  # Reads the digital input value.

DigitalOutputByBits(Int32, Int32, array<Int32>[]()[][], array<Int32>[]()[][]):  # Sets the digital output.

DigitalOutputByBits(String, Int32, array<Int32>[]()[][], array<Int32>[]()[][]):  # Sets the digital output.

DigitalOutputEntire(Int32, Int32, Int32):  # Sets the digital output.

DigitalOutputEntire(String, Int32, Int32):  # Sets the digital output. 

    
class LoopTransmissionMode(Enum):
    Off=AerotechEnsembleCommandsNET.LoopTransmissionMode.Off
    Sinusoid=AerotechEnsembleCommandsNET.LoopTransmissionMode.Sinusoid
    SinusoidGantry=AerotechEnsembleCommandsNET.LoopTransmissionMode.SinusoidGantry
    WhiteNoise=AerotechEnsembleCommandsNET.LoopTransmissionMode.WhiteNoise
    WhiteNoiseGantry=AerotechEnsembleCommandsNET.LoopTransmissionMode.WhiteNoiseGantry

class LoopTransmissionType(Enum):
    OpenLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.OpenLoop
    ClosedLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.ClosedLoop
    CurrentLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.CurrentLoop
    AFOpenLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.AFOpenLoop
    AFClosedLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.AFClosedLoop


class ModeType(Enum):
    MotionMode=AerotechEnsembleCommandsNET.ModeType.MotionMode
    WaitMode=AerotechEnsembleCommandsNET.ModeType.WaitMode
    RampMode=AerotechEnsembleCommandsNET.ModeType.RampMode
    VelocityMode=AerotechEnsembleCommandsNET.ModeType.RampMode
    ScurveValue=AerotechEnsembleCommandsNET.ModeType.ScurveValue
    TimeScaleValue=AerotechEnsembleCommandsNET.ModeType.TimeScaleValue
    DefaultVelocityValue=AerotechEnsembleCommandsNET.ModeType.DefaultVelocityValue
    AccelRateValue=AerotechEnsembleCommandsNET.ModeType.AccelRateValue
    AccelTimeValue=AerotechEnsembleCommandsNET.ModeType.AccelTimeValue
    AccelDistValue=AerotechEnsembleCommandsNET.ModeType.AccelDistValue
    DecelRateValue=AerotechEnsembleCommandsNET.ModeType.DecelRateValue
    DecelTimeValue=AerotechEnsembleCommandsNET.ModeType.DecelTimeValue
    DecelDistValue=AerotechEnsembleCommandsNET.ModeType.DecelDistValue
    Plane=AerotechEnsembleCommandsNET.ModeType.Plane
    
class MotionAdvancedCommands(CommandCategory):
    _MotionAdvancedCommandsNET=None
    def __init__(self,MotionAdvancedCommandsNET:AerotechEnsembleNET.MotionAdvancedCommands):
        self._MotionAdvancedCommandsNET=MotionAdvancedCommandsNET
        
    @multimethod
    def MoveOutLim(self,Axis:int):
        self._MotionAdvancedCommandsNET.MoveOutLim(Axis)
    
    @multimethod
    def MoveOutLim(self,Axis:str):
        self._MotionAdvancedCommandsNET.MoveOutLim(Axis)
    
    @multimethod
    def MoveToLimCCW(self,Axis:int):
        self._MotionAdvancedCommandsNET.MoveToLimCCW(Axis)
    
    @multimethod
    def MoveToLimCCW(self,Axis:str):
        self._MotionAdvancedCommandsNET.MoveToLimCCW(Axis)

    @multimethod
    def MoveToLimCW(self,Axis:int):
        self._MotionAdvancedCommandsNET.MoveToLimCW(Axis)
    
    @multimethod
    def MoveToLimCW(self,Axis:str):
        self._MotionAdvancedCommandsNET.MoveToLimCW(Axis)

class MotionCommands(CommandCategory):
    
    # TODO
    _ControllerNET=None
    
    def __init__(self,controller:AerotechEnsembleNET.Controller):
        self._ControllerNET=controller
        self._Setup=MotionSetupCommands(controller)

    # ! Abort
    @multimethod  
    def Abort(self,axis:int):
        self._ControllerNET.Commands.Montion.Abort(axis)

    @multimethod
    def Abort(self,axes:list[int]):
        self._ControllerNET.Commands.Montion.Abort(axes)
        
    @multimethod
    def Abort(self,axis:str):
        self._ControllerNET.Commands.Montion.Abort(axis)
        
    @multimethod
    def Abort(self,axes:list[str]):
        self._ControllerNET.Commands.Montion.Abort(axes)
    
    @multimethod
    def Abort(self,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Montion.Abort(AxisMask)
        
    @property
    def Advanced(self):
        return MotionAdvancedCommands(self._ControllerNET)
        
    # ! AutoFocus
    @multimethod
    def AutoFocus(self,axis:int, OnOff:AerotechEnsembleCommandsNET.OnOff): 
        self._ControllerNET.Commands.Motion.AutoFocus(axis,OnOff)
        
    @multimethod
    def AutoFocus(self,axes:list[int], OnOff:AerotechEnsembleCommandsNET.OnOff): 
        self._ControllerNET.Commands.Motion.AutoFocus(axes,OnOff)
    
    @multimethod
    def AutoFocus(self,axis:str, OnOff:AerotechEnsembleCommandsNET.OnOff):
        self._ControllerNET.Commands.Motion.AutoFocus(axis,OnOff)
    
    @multimethod
    def AutoFocus(self,axes:list[str], OnOff:AerotechEnsembleCommandsNET.OnOff):
        self._ControllerNET.Commands.Motion.AutoFocus(axes,OnOff)
    
    @multimethod
    def AutoFocus(self,AxisMask:AerotechEnsembleNET.AxisMask, OnOff:AerotechEnsembleCommandsNET.OnOff):
        self._ControllerNET.Commands.Motion.AutoFocus(AxisMask,OnOff)
        
    # ! BlockMotion 
    @multimethod
    def BlockMotion(self,axis:int, OnOff:AerotechEnsembleCommandsNET.OnOff): 
        self._ControllerNET.Commands.Motion.BlockMotion(axis,OnOff)
        
    @multimethod
    def BlockMotion(self,axes:list[int], OnOff:AerotechEnsembleCommandsNET.OnOff): 
        self._ControllerNET.Commands.Motion.BlockMotion(axes,OnOff)
    
    @multimethod
    def BlockMotion(self,axis:str, OnOff:AerotechEnsembleCommandsNET.OnOff):
        self._ControllerNET.Commands.Motion.BlockMotion(axis,OnOff)
    
    @multimethod
    def BlockMotion(self,axes:list[str], OnOff:AerotechEnsembleCommandsNET.OnOff):
        self._ControllerNET.Commands.Motion.BlockMotion(axes,OnOff)
    
    @multimethod
    def BlockMotion(self,AxisMask:AerotechEnsembleNET.AxisMask, OnOff:AerotechEnsembleCommandsNET.OnOff):
        self._ControllerNET.Commands.Motion.BlockMotion(AxisMask,OnOff)
        
    # ! CCWCenter
    @multimethod
    def CCWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float):
        self._ControllerNET.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CCWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float):
        self._ControllerNET.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CCWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
    @multimethod
    def CCWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
        
    # ! CCWRadius
    @multimethod
    def CCWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float):
        self._ControllerNET.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CCWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float):
        self._ControllerNET.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CCWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
    @multimethod
    def CCWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
        
    # ! CWCenter
    @multimethod
    def CWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float):
        self._ControllerNET.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float):
        self._ControllerNET.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
    @multimethod
    def CWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
        
    # ! CWRadius
    @multimethod
    def CWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float):
        self._ControllerNET.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float):
        self._ControllerNET.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
    @multimethod
    def CWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed) 

    # ! Disable
    @multimethod
    def Disable(self,axis:int): 
        self._ControllerNET.Commands.Motion.Disable(axis)
        
    @multimethod
    def Disable(self,axes:list[int]): 
        self._ControllerNET.Commands.Motion.Disable(axes)
    
    @multimethod
    def Disable(self,axis:str):
        self._ControllerNET.Commands.Motion.Disable(axis)
    
    @multimethod
    def Disable(self,axes:list[str]):
        self._ControllerNET.Commands.Motion.Disable(axes)
    
    @multimethod
    def Disable(self,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Motion.Disable(AxisMask)

    # ! Enable
    @multimethod
    def Enable(self,axis:int): 
        self._ControllerNET.Commands.Motion.Enable(axis)
        
    @multimethod
    def Enable(self,axes:list[int]): 
        self._ControllerNET.Commands.Motion.Enable(axes)
    
    @multimethod
    def Enable(self,axis:str):
        self._ControllerNET.Commands.Motion.Enable(axis)
    
    @multimethod
    def Enable(self,axes:list[str]):
        self._ControllerNET.Commands.Motion.Enable(axes)
    
    @multimethod
    def Enable(self,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Motion.Enable(AxisMask)
        
    # ! FaultAck
    @multimethod
    def FaultAck(self,axis:int): 
        self._ControllerNET.Commands.Motion.FaultAck(axis)
        
    @multimethod
    def FaultAck(self,axes:list[int]): 
        self._ControllerNET.Commands.Motion.FaultAck(axes)
    
    @multimethod
    def FaultAck(self,axis:str):
        self._ControllerNET.Commands.Motion.FaultAck(axis)
    
    @multimethod
    def FaultAck(self,axes:list[str]):
        self._ControllerNET.Commands.Motion.FaultAck(axes)
    
    @multimethod
    def FaultAck(self,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Motion.FaultAck(AxisMask)
        
    # ! FreeRun
    @multimethod
    def FreeRun(self,axis:int,speed:float): 
        self._ControllerNET.Commands.Motion.FreeRun(axis,speed)
        
    @multimethod
    def FreeRun(self,axes:list[int],speed:list[float]): 
        self._ControllerNET.Commands.Motion.FreeRun(axes,speed)
    
    @multimethod
    def FreeRun(self,axis:str,speed:float):
        self._ControllerNET.Commands.Motion.FreeRun(axis,speed)
    
    @multimethod
    def FreeRun(self,axes:list[str],speed:list[float]):
        self._ControllerNET.Commands.Motion.FreeRun(axes,speed)
    
    @multimethod
    def FreeRun(self,AxisMask:AerotechEnsembleNET.AxisMask,speed:float):
        self._ControllerNET.Commands.Motion.FreeRun(AxisMask,speed)
        
    @multimethod
    def FreeRun(self,AxisMask:AerotechEnsembleNET.AxisMask,speed:list[float]):
        self._ControllerNET.Commands.Motion.FreeRun(AxisMask,speed)
        
    # ! FreeRunStop
    @multimethod
    def FreeRunStop(self,axis:int): 
        self._ControllerNET.Commands.Motion.FreeRunStop(axis)
        
    @multimethod
    def FreeRunStop(self,axes:list[int]): 
        self._ControllerNET.Commands.Motion.FreeRunStop(axes)
    
    @multimethod
    def FreeRunStop(self,axis:str):
        self._ControllerNET.Commands.Motion.FreeRunStop(axis)
    
    @multimethod
    def FreeRunStop(self,axes:list[str]):
        self._ControllerNET.Commands.Motion.FreeRunStop(axes)
    
    @multimethod
    def FreeRunStop(self,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Motion.FreeRunStop(AxisMask)
        
    # ! Home
    @multimethod
    def Home(self,axis:int): 
        self._ControllerNET.Commands.Motion.Home(axis)
        
    @multimethod
    def Home(self,axes:list[int]): 
        self._ControllerNET.Commands.Motion.Home(axes)
    
    @multimethod
    def Home(self,axis:str):
        self._ControllerNET.Commands.Motion.Home(axis)
    
    @multimethod
    def Home(self,axes:list[str]):
        self._ControllerNET.Commands.Motion.Home(axes)
    
    @multimethod
    def Home(self,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Motion.Home(AxisMask)
            
    # ! HomeConditional
    @multimethod
    def HomeConditional(self,axis:int): 
        self._ControllerNET.Commands.Motion.HomeConditional(axis)
        
    @multimethod
    def HomeConditional(self,axes:list[int]): 
        self._ControllerNET.Commands.Motion.HomeConditional(axes)
    
    @multimethod
    def HomeConditional(self,axis:str):
        self._ControllerNET.Commands.Motion.HomeConditional(axis)
    
    @multimethod
    def HomeConditional(self,axes:list[str]):
        self._ControllerNET.Commands.Motion.HomeConditional(axes)
    
    @multimethod
    def HomeConditional(self,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Motion.HomeConditional(AxisMask)
        
        
    # ! Linear
    @multimethod
    def Linear(self,axis:int,distance:float): 
        self._ControllerNET.Commands.Motion.Linear(axis,distance)
        
    @multimethod
    def Linear(self,axes:list[int],distance:list[float]): 
        self._ControllerNET.Commands.Motion.Linear(axes,distance)
    
    @multimethod
    def Linear(self,axis:str,distance:float):
        self._ControllerNET.Commands.Motion.Linear(axis,distance)
    
    @multimethod
    def Linear(self,axes:list[str],distance:list[float]):
        self._ControllerNET.Commands.Motion.Linear(axes,distance)
    
    @multimethod
    def Linear(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:float):
        self._ControllerNET.Commands.Motion.Linear(AxisMask,distance)
        
    @multimethod
    def Linear(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:list[float]):
        self._ControllerNET.Commands.Motion.Linear(AxisMask,distance)

    @multimethod
    def Linear(self,axis:int,distance:float,coordinatedSpeed:float): 
        self._ControllerNET.Commands.Motion.Linear(axis,distance,coordinatedSpeed)
        
    @multimethod
    def Linear(self,axes:list[int],distance:list[float],coordinatedSpeed:float): 
        self._ControllerNET.Commands.Motion.Linear(axes,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,axis:str,distance:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.Linear(axis,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,axes:list[str],distance:list[float],coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.Linear(axes,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:float,coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.Linear(AxisMask,distance,coordinatedSpeed)
        
    @multimethod
    def Linear(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:list[float],coordinatedSpeed:float):
        self._ControllerNET.Commands.Motion.Linear(AxisMask,distance,coordinatedSpeed)
        
    # ! MoveAbs
    @multimethod
    def MoveAbs(self,axis:int,distance:float): 
        self._ControllerNET.Commands.Motion.MoveAbs(axis,distance)
        
    @multimethod
    def MoveAbs(self,axes:list[int],distance:list[float]): 
        self._ControllerNET.Commands.Motion.MoveAbs(axes,distance)
    
    @multimethod
    def MoveAbs(self,axis:str,distance:float):
        self._ControllerNET.Commands.Motion.MoveAbs(axis,distance)
    
    @multimethod
    def MoveAbs(self,axes:list[str],distance:list[float]):
        self._ControllerNET.Commands.Motion.MoveAbs(axes,distance)
    
    @multimethod
    def MoveAbs(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:float):
        self._ControllerNET.Commands.Motion.MoveAbs(AxisMask,distance)
        
    @multimethod
    def MoveAbs(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:list[float]):
        self._ControllerNET.Commands.Motion.MoveAbs(AxisMask,distance)

    @multimethod
    def MoveAbs(self,axis:int,distance:float,speed:float): 
        self._ControllerNET.Commands.Motion.MoveAbs(axis,distance,speed)
        
    @multimethod
    def MoveAbs(self,axes:list[int],distance:list[float],speed:float): 
        self._ControllerNET.Commands.Motion.MoveAbs(axes,distance,speed)
    
    @multimethod
    def MoveAbs(self,axis:str,distance:float,speed:float):
        self._ControllerNET.Commands.Motion.MoveAbs(axis,distance,speed)
    
    @multimethod
    def MoveAbs(self,axes:list[str],distance:list[float],speed:float):
        self._ControllerNET.Commands.Motion.MoveAbs(axes,distance,speed)
    
    @multimethod
    def MoveAbs(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:float,speed:float):
        self._ControllerNET.Commands.Motion.MoveAbs(AxisMask,distance,speed)
        
    @multimethod
    def MoveAbs(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:list[float],speed:float):
        self._ControllerNET.Commands.Motion.MoveAbs(AxisMask,distance,speed)
        
    # ! MoveInc
    @multimethod
    def MoveInc(self,axis:int,distance:float): 
        self._ControllerNET.Commands.Motion.MoveInc(axis,distance)
        
    @multimethod
    def MoveInc(self,axes:list[int],distance:list[float]): 
        self._ControllerNET.Commands.Motion.MoveInc(axes,distance)
    
    @multimethod
    def MoveInc(self,axis:str,distance:float):
        self._ControllerNET.Commands.Motion.MoveInc(axis,distance)
    
    @multimethod
    def MoveInc(self,axes:list[str],distance:list[float]):
        self._ControllerNET.Commands.Motion.MoveInc(axes,distance)
    
    @multimethod
    def MoveInc(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:float):
        self._ControllerNET.Commands.Motion.MoveInc(AxisMask,distance)
        
    @multimethod
    def MoveInc(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:list[float]):
        self._ControllerNET.Commands.Motion.MoveInc(AxisMask,distance)

    @multimethod
    def MoveInc(self,axis:int,distance:float,speed:float): 
        self._ControllerNET.Commands.Motion.MoveInc(axis,distance,speed)
        
    @multimethod
    def MoveInc(self,axes:list[int],distance:list[float],speed:float): 
        self._ControllerNET.Commands.Motion.MoveInc(axes,distance,speed)
    
    @multimethod
    def MoveInc(self,axis:str,distance:float,speed:float):
        self._ControllerNET.Commands.Motion.MoveInc(axis,distance,speed)
    
    @multimethod
    def MoveInc(self,axes:list[str],distance:list[float],speed:float):
        self._ControllerNET.Commands.Motion.MoveInc(axes,distance,speed)
    
    @multimethod
    def MoveInc(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:float,speed:float):
        self._ControllerNET.Commands.Motion.MoveInc(AxisMask,distance,speed)
        
    @multimethod
    def MoveInc(self,AxisMask:AerotechEnsembleNET.AxisMask,distance:list[float],speed:float):
        self._ControllerNET.Commands.Motion.MoveInc(AxisMask,distance,speed)

    @property
    def Setup(self):
        return self._Setup

    def Start(self):
        self._ControllerNET.Commands.Start()
    
    # ! WaitForMotionDone 
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axis:int): 
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axis)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axes:list[int]): 
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axes)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axis:str):
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axis)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axes:list[str]):
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axes)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,AxisMask:AerotechEnsembleNET.AxisMask):
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,AxisMask)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axis:int,timeout:int): 
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axis,timeout)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axes:list[int],timeout:int): 
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axes,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axis:str,timeout:int):
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axis,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,axes:list[str],timeout:int):
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,axes,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:AerotechEnsembleCommandsNET.WaitOption,AxisMask:AerotechEnsembleNET.AxisMask,timeout:int):
        self._ControllerNET.Commands.Motion.WaitForMotionDone(waitOption,AxisMask,timeout)
        
    def WaitMode(self,type:AerotechEnsembleCommandsNET.WaitType):
        self._ControllerNET.Commands.Motion.WaitMode(type)
    
class MotionSetupCommands(CommandCategory):
    _MotionSetupCommandsNET=None
    def __init__(self,MotionSetupCommandsNET:AerotechEnsembleNET.MotionSetupCommands):
        self._MotionSetupCommandsNET=MotionSetupCommandsNET
        


Absolute()()()():  # Sets motion commands to be in absolute mode.


Incremental()()()():  # Sets motion commands to be in incremental mode.


Plane(Int32):  # Sets the current plane of motion.

PosCap(Int32):  # Retrieves the POSCAP position.

PosCap(Int32, Boolean):  # Retrieves the POSCAP positions.

PosCap(array<Int32>[]()[][]):  # Retrieves the POSCAP positions.

PosCap(array<Int32>[]()[][], Boolean):  # Retrieves the POSCAP positions.

PosCap(AxisMask):  # Retrieves the POSCAP positions.

PosCap(AxisMask, Boolean):  # Retrieves the POSCAP positions.

PosCap(String):  # Retrieves the POSCAP positions.

PosCap(String, Boolean):  # Retrieves the POSCAP positions.

PosCap(array<String>[]()[][]):  # Retrieves the POSCAP positions.

PosCap(array<String>[]()[][], Boolean):  # Retrieves the POSCAP positions.

PosOffsetClear(Int32):  # Sets or clears an arbitrary program offset position.

PosOffsetClear(String):  # Sets or clears an arbitrary program offset position.

PosOffsetSet(Int32, Double):  # Sets or clears an arbitrary program offset position.

PosOffsetSet(String, Double):  # Sets or clears an arbitrary program offset position.

RampDist(Double):  # Specifies distance-based acceleration and deceleration.

RampDist(array<Int32>[]()[][], array<Double>[]()[][]):  # Specifies distance-based acceleration and deceleration.

RampDist(Int32, Double):  # Specifies distance-based acceleration and deceleration.

RampDist(array<String>[]()[][], array<Double>[]()[][]):  # Specifies distance-based acceleration and deceleration.

RampDist(String, Double):  # Specifies distance-based acceleration and deceleration.

RampDist(AxisMask, array<Double>[]()[][]):  # Specifies distance-based acceleration and deceleration.

RampDist(AxisMask, Double):  # Specifies distance-based acceleration and deceleration.

RampDistAccel(Double):  # Specifies distance-based acceleration and deceleration.

RampDistDecel(Double):  # Specifies distance-based acceleration and deceleration.

RampMode(RampMode):  # Specifies the ramp mode calculation type to use.

RampMode(array<Int32>[]()[][], RampMode):  # Specifies the ramp mode calculation type to use.

RampMode(Int32, RampMode):  # Specifies the ramp mode calculation type to use.

RampMode(array<String>[]()[][], RampMode):  # Specifies the ramp mode calculation type to use.

RampMode(String, RampMode):  # Specifies the ramp mode calculation type to use.

RampMode(AxisMask, RampMode):  # Specifies the ramp mode calculation type to use.

RampRate(Double):  # Specifies rate-based acceleration and deceleration.

RampRate(array<Int32>[]()[][], array<Double>[]()[][]):  # Specifies rate-based acceleration and deceleration.

RampRate(Int32, Double):  # Specifies rate-based acceleration and deceleration.

RampRate(array<String>[]()[][], array<Double>[]()[][]):  # Specifies rate-based acceleration and deceleration.

RampRate(String, Double):  # Specifies rate-based acceleration and deceleration.

RampRate(AxisMask, array<Double>[]()[][]):  # Specifies rate-based acceleration and deceleration.

RampRate(AxisMask, Double):  # Specifies rate-based acceleration and deceleration.

RampRateAccel(Double):  # Specifies rate-based acceleration and deceleration.

RampRateDecel(Double):  # Specifies rate-based acceleration and deceleration.

RampTime(Double):  # Specifies time-based acceleration and deceleration.

RampTime(array<Int32>[]()[][], array<Double>[]()[][]):  # Specifies time-based acceleration and deceleration.

RampTime(Int32, Double):  # Specifies time-based acceleration and deceleration.

RampTime(array<String>[]()[][], array<Double>[]()[][]):  # Specifies time-based acceleration and deceleration.

RampTime(String, Double):  # Specifies time-based acceleration and deceleration.

RampTime(AxisMask, array<Double>[]()[][]):  # Specifies time-based acceleration and deceleration.

RampTime(AxisMask, Double):  # Specifies time-based acceleration and deceleration.

RampTimeAccel(Double):  # Specifies time-based acceleration and deceleration.

RampTimeDecel(Double):  # Specifies time-based acceleration and deceleration.

Reconcile(array<Int32>[]()[][]):  # Reconciles the position of the axes in the list on the plane to servo position.

Reconcile(Int32):  # Reconciles the position of the axes in the list on the plane to servo position.

Reconcile(array<String>[]()[][]):  # Reconciles the position of the axes in the list on the plane to servo position.

Reconcile(String):  # Reconciles the position of the axes in the list on the plane to servo position.

Reconcile(AxisMask):  # Reconciles the position of the axes in the list on the plane to servo position.

ScaleFactorClear(Int32):  # Sets or clears the scale factor for an axis.

ScaleFactorClear(String):  # Sets or clears the scale factor for an axis.

ScaleFactorSet(Int32, Double):  # Sets or clears the scale factor for an axis.

ScaleFactorSet(String, Double):  # Sets or clears the scale factor for an axis.

Scurve(Double):  # Specifies the S-curve value to use.

Servo(Int32, OnOff):  # Changes between open-loop and closed-loop mode for piezo stages.

Servo(String, OnOff):  # Changes between open-loop and closed-loop mode for piezo stages.

SetExtPos(Int32, Double):  # Sets an arbitrary position value, in encoder counts, in external position register.

SetExtPos(String, Double):  # Sets an arbitrary position value, in encoder counts, in external position register.

TimeScale(Double):  # Specifies the time scale to use. 

    
class OnOff(Enum):
    Off=AerotechEnsembleCommandsNET.OnOff.Off
    On=AerotechEnsembleCommandsNET.OnOff.On

class PSOCommands(CommandCategory):
    _PSOCommandsNET=None
    def __init__(self,PSOCommandsNET:AerotechEnsembleNET.PSOCommands):
        self._PSOCommandsNET=PSOCommandsNET
    
Array(Int32, Int32, Int32):  # Sends data into the PSO array.

Array(String, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectDistance(Int32, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectDistance(String, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectLaser(Int32, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectLaser(String, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectWindow1(Int32, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectWindow1(String, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectWindow2(Int32, Int32, Int32):  # Sends data into the PSO array.

ArrayFifoSelectWindow2(String, Int32, Int32):  # Sends data into the PSO array.

Control(Int32, PsoMode):  # Enables and disables the PSO hardware.

Control(String, PsoMode):  # Enables and disables the PSO hardware.

DistanceArray(Int32):  # Sets the distance to travel between firing events.

DistanceArray(String):  # Sets the distance to travel between firing events.

DistanceFixed(Int32, Double):  # Sets the distance to travel between firing events.

DistanceFixed(String, Double):  # Sets the distance to travel between firing events.

OutputBitMap(Int32):  # Sets the PSO output mode.

OutputBitMap(String):  # Sets the PSO output mode.

OutputBitMap(Int32, Int32):  # Sets the PSO output mode.

OutputBitMap(String, Int32):  # Sets the PSO output mode.

OutputControl(Int32, Int32):  # Sets the PSO output mode.

OutputControl(String, Int32):  # Sets the PSO output mode.

OutputPulse(Int32):  # Sets the PSO output mode.

OutputPulse(String):  # Sets the PSO output mode.

OutputPulseBitMask(Int32):  # Sets the PSO output mode.

OutputPulseBitMask(String):  # Sets the PSO output mode.

OutputPulseExtSync(Int32):  # Sets the PSO output mode.

OutputPulseExtSync(String):  # Sets the PSO output mode.

OutputPulseWindowBitMask(Int32):  # Sets the PSO output mode.

OutputPulseWindowBitMask(String):  # Sets the PSO output mode.

OutputPulseWindowBitMaskEdgeMode(Int32, Int32):  # Sets the PSO output mode.

OutputPulseWindowBitMaskEdgeMode(String, Int32):  # Sets the PSO output mode.

OutputPulseWindowMask(Int32):  # Sets the PSO output mode.

OutputPulseWindowMask(String):  # Sets the PSO output mode.

OutputPulseWindowMaskEdgeMode(Int32, Int32):  # Sets the PSO output mode.

OutputPulseWindowMaskEdgeMode(String, Int32):  # Sets the PSO output mode.

OutputPulseWindowMaskHard(Int32):  # Sets the PSO output mode.

OutputPulseWindowMaskHard(String):  # Sets the PSO output mode.

OutputToggle(Int32):  # Sets the PSO output mode.

OutputToggle(String):  # Sets the PSO output mode.

OutputWindow(Int32):  # Sets the PSO output mode.

OutputWindow(String):  # Sets the PSO output mode.

Pulse(Int32, Double, Double):  # Configures the pulse sequence that is used for PSO.

Pulse(String, Double, Double):  # Configures the pulse sequence that is used for PSO.

PulseCyclesOrDelayCyclesAndDelay(Int32, Double, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.

PulseCyclesOrDelayCyclesAndDelay(String, Double, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.

PulseCyclesOrDelayCyclesOnly(Int32, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.

PulseCyclesOrDelayCyclesOnly(String, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.

PulseCyclesOrDelayDelayOnly(Int32, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.

PulseCyclesOrDelayDelayOnly(String, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.

Status(Int32):  # Gets the PSO status information.

Status(String):  # Gets the PSO status information.

TrackDirection(Int32, Int32):  # Configures the PSO distance tracking counters.

TrackDirection(String, Int32):  # Configures the PSO distance tracking counters.

TrackInput(Int32, Int32):  # Configures the PSO distance tracking counters.

TrackInput(String, Int32):  # Configures the PSO distance tracking counters.

TrackInput(Int32, Int32, Int32):  # Configures the PSO distance tracking counters.

TrackInput(String, Int32, Int32):  # Configures the PSO distance tracking counters.

TrackInput(Int32, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.

TrackInput(String, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.

TrackReset(Int32, Int32):  # Configures the PSO distance tracking counters.

TrackReset(String, Int32):  # Configures the PSO distance tracking counters.

TrackScale(Int32, Int32):  # Configures the PSO distance tracking counters.

TrackScale(String, Int32):  # Configures the PSO distance tracking counters.

TrackScale(Int32, Int32, Int32):  # Configures the PSO distance tracking counters.

TrackScale(String, Int32, Int32):  # Configures the PSO distance tracking counters.

TrackScale(Int32, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.

TrackScale(String, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.

WindowInput(Int32, Int32, Int32):  # Configures which encoder channel is connected to each window.

WindowInput(String, Int32, Int32):  # Configures which encoder channel is connected to each window.

WindowInputInvert(Int32, Int32, Int32):  # Configures which encoder channel is connected to each window.

WindowInputInvert(String, Int32, Int32):  # Configures which encoder channel is connected to each window.

WindowLoad(Int32, Int32, Int32):  # Loads the specified window counter with a value.

WindowLoad(String, Int32, Int32):  # Loads the specified window counter with a value.

WindowOff(Int32, Int32):  # Disables the PSO Window Hardware.

WindowOff(String, Int32):  # Disables the PSO Window Hardware.

WindowOn(Int32, Int32):  # Enables the PSO Window Hardware.

WindowOn(String, Int32):  # Enables the PSO Window Hardware.

WindowOnInvert(Int32, Int32):  # Enables the PSO Window Hardware.

WindowOnInvert(String, Int32):  # Enables the PSO Window Hardware.

WindowRange(Int32, Int32, Double, Double):  # Specifies the low and high comparison values for specified PSO window.

WindowRange(String, Int32, Double, Double):  # Specifies the low and high comparison values for specified PSO window.

WindowRangeArray(Int32, Int32):  # Specifies the array mode parameters for the specified PSO window.

WindowRangeArray(String, Int32):  # Specifies the array mode parameters for the specified PSO window.

WindowRangeArrayEdge(Int32, Int32, Double):  # Specifies the array mode parameters for the specified PSO window.

WindowRangeArrayEdge(String, Int32, Double):  # Specifies the array mode parameters for the specified PSO window.

WindowReset(Int32, Int32, Int32):  # Resets the window counter to 0 based on the encoder marker signal.

WindowReset(String, Int32, Int32):  # Resets the window counter to 0 based on the encoder marker signal. 

    

class PsoMode(Enum):
    Reset=AerotechEnsembleCommandsNET.PsoMode.Reset
    Off=AerotechEnsembleCommandsNET.PsoMode.Off
    Arm=AerotechEnsembleCommandsNET.PsoMode.Arm
    Fire=AerotechEnsembleCommandsNET.PsoMode.Fire
    On=AerotechEnsembleCommandsNET.PsoMode.On
    FireContinuous=AerotechEnsembleCommandsNET.PsoMode.FireContinuous

class RampMode(Enum):
    Dist=AerotechEnsembleCommandsNET.RampMode.Dist
    Rate=AerotechEnsembleCommandsNET.RampMode.Rate
    Time=AerotechEnsembleCommandsNET.RampMode.Time

class RampType(Enum):
    Linear=AerotechEnsembleCommandsNET.RampType.Linear
    Scurve=AerotechEnsembleCommandsNET.RampType.Scurve
    Sine=AerotechEnsembleCommandsNET.RampType.Sine

class RegisterCommands(CommandCategory):
    _RegisterCommandsNET=None
    def __init__(self,RegisterCommandsNET:AerotechEnsembleNET.RegisterCommands):
        self._RegisterCommandsNET=RegisterCommandsNET
    
class RegisterType(Enum):
    GlobalIntegers=AerotechEnsembleCommandsNET.RegisterType.GlobalIntegers
    GlobalDoubles=AerotechEnsembleCommandsNET.RegisterType.GlobalDoubles
    ConversionRegisters=AerotechEnsembleCommandsNET.RegisterType.ConversionRegisters
    ModbusMasterInputWords=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterInputWords
    ModbusMasterOutputWords=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterOutputWords
    ModbusMasterInputBits=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterInputBits
    ModbusMasterOutputBits=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterOutputBits
    ModbusMasterStatusWords=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterStatusWords
    ModbusMasterStatusBits=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterStatusBits
    ModbusMasterVirtualInputs=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterVirtualInputs 
    ModbusMasterVirtualOutputs=AerotechEnsembleCommandsNET.RegisterType.ModbusMasterVirtualOutputs
    ModbusSlaveInputWords=AerotechEnsembleCommandsNET.RegisterType.ModbusSlaveInputWords
    ModbusSlaveOutputWords=AerotechEnsembleCommandsNET.RegisterType.ModbusSlaveOutputWords
    ModbusSlaveInputBits=AerotechEnsembleCommandsNET.RegisterType.ModbusSlaveInputBits
    ModbusSlaveOutputBits=AerotechEnsembleCommandsNET.RegisterType.ModbusSlaveOutputBits

class RootCommands(CommandCategory):
    _RootCommandsNET=None
    def __init__(self,RootCommandsNET:AerotechEnsembleNET.RootCommands):
        self._RootCommandsNET=RootCommandsNET
    
    @property
    def Motion(self):
        return MotionCommands(self._ControllerNET)
 
    def AcknowledgeAll(self):
        self._ControllerNET.Commands.AcknowledgeAll()
        
    def Execute(self,code:str):
        self._ControllerNET.Commands.Execute(code)
 
    def ExecuteAsync(self,code:str):
        self._ControllerNET.Commands.ExecuteAsync(code)
    
class Semaphores(Enum):
    ModbusRegisters=AerotechEnsembleCommandsNET.Semaphores.ModbusRegisters
    GlobalIntegers=AerotechEnsembleCommandsNET.Semaphores.GlobalIntegers
    GlobalDoubles=AerotechEnsembleCommandsNET.Semaphores.GlobalDoubles 

class StatusCommands(CommandCategory):
    _StatusCommandsNET=None
    def __init__(self,StatusCommandsNET=AerotechEnsembleCommandsNET.StatusCommands):
        self._StatusCommandsNET=StatusCommandsNET
        CommandCategory.__init__(self,StatusCommandsNET)
    
    def EtherStatus():  # Gets the Ethernet status.

    @multimethod
    def PositionMarkerLatched(Int32):  # Gets the position feedback latched when the marker signal occurred during a home.
 
    @multimethod
    def PositionMarkerLatched(String):  # Gets the position feedback latched when the marker signal occurred during a home.
 

class TuningCommands(CommandCategory):
    _TuningCommandsNET=None
    def __init__(self,TuningCommandsNET=AerotechEnsembleCommandsNET.TuningCommands):
        self._TuningCommandsNET=TuningCommandsNET
        CommandCategory.__init__(self,TuningCommandsNET)
        
    @multimethod
    def LoopTrans(Int32, LoopTransmissionMode, Double, Double, LoopTransmissionType):  # Initiates loop transmission mode.
    
    @multimethod
    def LoopTrans(String, LoopTransmissionMode, Double, Double, LoopTransmissionType):  # Initiates loop transmission mode.
    
    @multimethod
    def MComm(Int32, Double):  # Sends a direct current command to the servo loop.
    
    @multimethod
    def  MComm(String, Double):  # Sends a direct current command to the servo loop.
    
    @multimethod
    def MSet(Int32, Double, Int32):  # Generates an open-loop current command.
    
    @multimethod
    def MSet(String, Double, Int32):  # Generates an open-loop current command.
    
    @multimethod
    def Oscillate(Int32, Double, Double, Int32):  # Generates sinusoidal oscillation on an axis.
    
    @multimethod
    def Oscillate(String, Double, Double, Int32):  # Generates sinusoidal oscillation on an axis.
    
    @multimethod
    def Oscillate(Int32, Double, Double, Int32, Int32):  # Generates sinusoidal oscillation on an axis.
    
    @multimethod
    def Oscillate(String, Double, Double, Int32, Int32):  # Generates sinusoidal oscillation on an axis.
    
    @multimethod
    def SetGain(Int32, Double, Double, Double, Double):  # Sets four or nine servo loop gains at the same time.
    
    @multimethod
    def SetGain(String, Double, Double, Double, Double):  # Sets four or nine servo loop gains at the same time.
    
    @multimethod
    def SetGain(Int32, Double, Double, Double, Double, Double, Double, Double, Double, Double):  # Sets four or nine servo loop gains at the same time.
    
    @multimethod
    def SetGain(String, Double, Double, Double, Double, Double, Double, Double, Double, Double):  # Sets four or nine servo loop gains at the same time.

    
class WaitOption(Enum):
    InPosition=AerotechEnsembleCommandsNET.WaitOption.InPosition
    MoveDone=AerotechEnsembleCommandsNET.WaitOption.MoveDone

class WaitType(Enum):
    NoWait=AerotechEnsembleCommandsNET.WaitType.NoWait
    MoveDone=AerotechEnsembleCommandsNET.WaitType.MoveDone
    InPos=AerotechEnsembleCommandsNET.WaitType.InPos