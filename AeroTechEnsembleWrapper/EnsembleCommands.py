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

from collections.abc import Sequence

import CommonCollections
import Ensemble

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

class EthernetStatus(Enum):
    DataInTransmitter=AerotechEnsembleCommandsNET.EthernetStatus.DataInTransmitter
    DataInReceiver=AerotechEnsembleCommandsNET.EthernetStatus.DataInReceiver

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
    
class OnOff(Enum):
    Off=AerotechEnsembleCommandsNET.OnOff.Off
    On=AerotechEnsembleCommandsNET.OnOff.On

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

class WaitOption(Enum):
    InPosition=AerotechEnsembleCommandsNET.WaitOption.InPosition
    MoveDone=AerotechEnsembleCommandsNET.WaitOption.MoveDone

class WaitType(Enum):
    NoWait=AerotechEnsembleCommandsNET.WaitType.NoWait
    MoveDone=AerotechEnsembleCommandsNET.WaitType.MoveDone
    InPos=AerotechEnsembleCommandsNET.WaitType.InPos
    
class Semaphores(Enum):
    ModbusRegisters=AerotechEnsembleCommandsNET.Semaphores.ModbusRegisters
    GlobalIntegers=AerotechEnsembleCommandsNET.Semaphores.GlobalIntegers
    GlobalDoubles=AerotechEnsembleCommandsNET.Semaphores.GlobalDoubles 

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
        
            
    def Abort(self):  # Aborts motion on the selected axes 
        self._AxesMotionCommandsNET.Abort()
        
    def AutoFocus(self,OnOff:OnOff):  # Turns on or turns off autofocus.
        self._AxesMotionCommandsNET.AutoFocus(OnOff.value)

    def BlockMotion(self,OnOff:OnOff):  # Sets motion blocking to On or OFF.
        self._AxesMotionCommandsNET.BlockMotion(OnOff.value)

    def Disable(self):  # Disables the axes.
        self._AxesMotionCommandsNET.Disable()

    def Enable(self):  # Enables the axes.
        self._AxesMotionCommandsNET.Enable()

    def FaultAck(self):  # Acknowledges and clears the fault on axes.
        self._AxesMotionCommandsNET.FaultAck()

    def FreeRun(self,Speed):  # Freeruns the axes.
        self._AxesMotionCommandsNET.FreeRun(Speed)

    def FreeRunStop(self):  # Freeruns the axes.
        self._AxesMotionCommandsNET.FreeRunStop()

    def Home(self):  # Homes the axes.
        self._AxesMotionCommandsNET.Home()

    def HomeConditional(self):  # Homes the axes.
        self._AxesMotionCommandsNET.HomeConditional()

    @multimethod
    def Linear(self,Distance:list[float]):  # Executes a linear move on axes. 2 
        self._AxesMotionCommandsNET.Linear(Distance)
        
    @multimethod
    def Linear(self,Distance:list[float], CoordinatedSpeed):  # Executes a linear move on axes.
        self._AxesMotionCommandsNET.Linear(Distance, CoordinatedSpeed)
        
    @multimethod
    def MoveAbs(self,Distance:list[float]):  # Executes an absolute move on axes.
        self._AxesMotionCommandsNET.MoveAbs(Distance)
        
    @multimethod
    def MoveAbs(self,Distance:list[float], Speed:list[float]):  # Executes an absolute move on axes.
        self._AxesMotionCommandsNET.MoveAbs(Distance, Speed)
        
    @multimethod
    def MoveInc(self,Distance:list[float]):  # Executes an incremental move on axes.
        self._AxesMotionCommandsNET.MoveInc(Distance)
        
    @multimethod
    def MoveInc(self,Distance:list[float], Speed:list[float]):  # Executes an incremental move on axes.
        self._AxesMotionCommandsNET.MoveInc(Distance, Speed)

    @property
    def Setup(self):  # Contains the Setup Commands
        return AxesMotionSetupCommands(self._AxesMotionCommandsNET.Setup)

    @multimethod
    def WaitForMotionDone(self,waitOption:WaitOption, timeout:int):  # Waits for the move to be done 
        return self._AxesMotionCommandsNET.WaitForMotionDone(waitOption.value,timeout)
    
    @multimethod
    def WaitForMotionDone(self,waitOption:WaitOption):  # Waits for the move to be done  
        return self._AxesMotionCommandsNET.WaitForMotionDone(waitOption.value)

class AxesMotionSetupCommands(CommandCategory):
    _AxesMotionSetupCommandsNET=None
    def __init__(self,AxesMotionSetupCommandsNET=AerotechEnsembleCommandsNET.AxesMotionSetupCommands):
        self._AxesMotionSetupCommandsNET=AxesMotionSetupCommandsNET
        
    @multimethod
    def PosCap(self):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._AxesMotionSetupCommandsNET.PosCap(),float,Ensemble.AxisMask)
    
    @multimethod
    def PosCap(self,reArm:bool):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._AxesMotionSetupCommandsNET.PosCap(reArm),float,Ensemble.AxisMask)

    def RampDist(self,Value:list[float]):  # Specifies distance-based acceleration and deceleration.
        self._AxesMotionSetupCommandsNET.RampDist(Value)
        
    def RampMode(self,Mode:RampMode):  # Specifies the ramp mode calculation type to use.
        self._AxesMotionSetupCommandsNET.RampMode(Mode.value)
        
    def RampRate(self,Value:list[float]):  # Specifies rate-based acceleration and deceleration.
        self._AxesMotionSetupCommandsNET.RampRate(Value)
        
    def RampTime(self,Value:list[float]):  # Specifies time-based acceleration and deceleration.
        self._AxesMotionSetupCommandsNET.RampTime(Value)
        
    def Reconcile(self):  # Reconciles the position of the axes in the list on the plane to servo position.
         self._AxesMotionSetupCommandsNET.Reconcile()

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

class AxesSelectionCommands(Sequence):
    _AxesSelectionCommands=None
    def __init__(self,AxesSelectionCommandsNET=AerotechEnsembleCommandsNET.AxesSelectionCommands):
        self._AxesSelectionCommandsNET=AxesSelectionCommandsNET
        Sequence.__init__(self)

    def __getitem__(self, i):
        return AxesRootCommands(self._AxesSelectionCommandsNET[i])

    def __len__(self):
        pass

    @multimethod
    def Select(self, axisMasks:list[Ensemble.AxisMask]):  # Allows the selection of axes on which to execute the command 
        _axisMasks=[mask.value for mask in axisMasks]
        return AxesRootCommands(self._AxesSelectionCommandsNET.Select(_axisMasks))
    
    @multimethod
    def Select(self, axisNames:list[str]):  # Allows the selection of axes on which to execute the command 
        return AxesRootCommands(self._AxesSelectionCommandsNET.Select(axisNames))
    
    @multimethod
    def Select(self, axisNumbers:list[int]):  # Allows the selection of axes on which to execute the command  
        return AxesRootCommands(self._AxesSelectionCommandsNET.Select(axisNumbers))

class CommandCategory():
    _CommandCategoryNET=None
    def __init__(self,CommandCategoryNET=AerotechEnsembleCommandsNET.CommandCategory):
        self._CommandCategoryNET=CommandCategoryNET

class DataAcquisitionCommands(CommandCategory):
    _DataAcquisitionCommandsNET=None
    def __init__(self,DataAcquisitionCommandsNET=AerotechEnsembleCommandsNET.DataAcquisitionCommands):
        self._DataAcquisitionCommandsNET=DataAcquisitionCommandsNET

    @multimethod
    def ArrayRead(self,Axis:int, VariableStart:int, NumberOfElements:int):  # Transfers drive array values into the specified controller array variables.
        self._DataAcquisitionCommandsNET.ArrayRead(Axis,VariableStart,NumberOfElements)

    @multimethod
    def ArrayRead(self,Axis:str, VariableStart:int, NumberOfElements:int):  # Transfers drive array values into the specified controller array variables.
        self._DataAcquisitionCommandsNET.ArrayRead(Axis,VariableStart,NumberOfElements)
        
    @multimethod
    def ArraySetup(self,Axis:int, NumberOfElements:int):  # Enables data collection.
        self._DataAcquisitionCommandsNET.ArraySetup(Axis,NumberOfElements)
        
    @multimethod
    def ArraySetup(self,Axis:str, NumberOfElements:int):  # Enables data collection.
        self._DataAcquisitionCommandsNET.ArraySetup(Axis,NumberOfElements)
        
    @multimethod
    def Input(self,Axis:int, SourceSignal:int):  # Specifies the data element collected when a trigger occurs.
        self._DataAcquisitionCommandsNET.Input(Axis,SourceSignal)
        
    @multimethod
    def Input(self,Axis:str, SourceSignal:int):  # Specifies the data element collected when a trigger occurs.
        self._DataAcquisitionCommandsNET.Input(Axis,SourceSignal)
        
    @multimethod
    def Off(self,Axis:int):  # Turns off data acquisition. All previously specified DATAACQ command configurations are cleared and must be re-specified if required.
        self._DataAcquisitionCommandsNET.Off(Axis)
        
    @multimethod
    def Off(self,Axis:str):  # Turns off data acquisition. All previously specified DATAACQ command configurations are cleared and must be re-specified if required.
        self._DataAcquisitionCommandsNET.Off(Axis)
        
    @multimethod
    def Trigger(self,Axis:int, TriggerSignal:int):  # Specifies which signal is monitored to collect data.
        self._DataAcquisitionCommandsNET.Trigger(Axis,TriggerSignal)
        
    @multimethod
    def Trigger(self,Axis:str, TriggerSignal:int):  # Specifies which signal is monitored to collect data. 
        self._DataAcquisitionCommandsNET.Trigger(Axis,TriggerSignal)
        
class IOCommands(CommandCategory):
    _IOCommandsNET=None
    def __init__(self,IOCommandsNET=AerotechEnsembleCommandsNET.IOCommands):
        self._IOCommandsNET=IOCommandsNET

    @multimethod
    def AnalogInput(self,Axis:int, Channel:int):  # Reads the analog input voltage.
        self._IOCommandsNET.AnalogInput(Axis, Channel)
        
    @multimethod
    def AnalogInput(self,Axis:str, Channel:int):  # Reads the analog input voltage.
        self._IOCommandsNET.AnalogInput(Axis, Channel)
        
    @multimethod
    def AnalogOutput(self,Axis:int, Channel:list[int], Value:list[float]):  # Sets the value of the analog output.
        self._IOCommandsNET.AnalogOutput(Axis, Channel,Value)
        
    @multimethod
    def AnalogOutput(self,Axis:str, Channel:list[int], Value:list[float]):  # Sets the value of the analog output.
        self._IOCommandsNET.AnalogOutput(Axis, Channel,Value)
        
    @multimethod
    def Brake(self,axisIndexes:list[int], OnOff:OnOff):  # Controls the brake output of axes.
        self._IOCommandsNET.Brake(axisIndexes,OnOff.value)
        
    @multimethod
    def Brake(self,axisIndex:int, OnOff:OnOff):  # Controls the brake output of axes.
        self._IOCommandsNET.Brake(axisIndex,OnOff.value)
        
    @multimethod
    def Brake(self,axisNames:list[str], OnOff:OnOff):  # Controls the brake output of axes.
        self._IOCommandsNET.Brake(axisNames,OnOff.value)
        
    @multimethod
    def Brake(self,axisName:str, OnOff:OnOff):  # Controls the brake output of axes.
        self._IOCommandsNET.Brake(axisName,OnOff.value)
        
    @multimethod
    def Brake(self,axisMask:Ensemble.AxisMask, OnOff:OnOff):  # Controls the brake output of axes.
        self._IOCommandsNET.Brake(axisMask,OnOff.value)
        
    @multimethod
    def DigitalInput(self,Axis:int, Port:int):  # Reads the digital input value.
        self._IOCommandsNET.DigitalInput(Axis,Port)
        
    @multimethod
    def DigitalInput(self,Axis:str, Port:int):  # Reads the digital input value.
        self._IOCommandsNET.DigitalInput(Axis,Port)
        
    @multimethod
    def DigitalInputBit(self,Axis:int, Port:int, Bit:int):  # Reads the digital input value.
        self._IOCommandsNET.DigitalInputBit(Axis,Port,Bit)
        
    @multimethod
    def DigitalInputBit(self,Axis:str, Port:int, Bit:int):  # Reads the digital input value.
        self._IOCommandsNET.DigitalInputBit(Axis,Port,Bit)
        
    @multimethod
    def DigitalOutputByBits(self,Axis:int, Port:int, Bits:list[int], Values:list[int]):  # Sets the digital output.
        self._IOCommandsNET.DigitalOutputByBits(Axis,Port,Bits,Values)
        
    @multimethod
    def DigitalOutputByBits(self,Axis:str, Port:int, Bits:list[int], Values:list[int]):  # Sets the digital output.
        self._IOCommandsNET.DigitalOutputByBits(Axis,Port,Bits,Values)
        
    @multimethod
    def DigitalOutputEntire(self,Axis:int, Port:int, Values:list[int]):  # Sets the digital output.
        self._IOCommandsNET.DigitalOutputEntire(Axis,Port,Values)
        
    @multimethod
    def DigitalOutputEntire(self,Axis:str, Port:int, Values:list[int]):  # Sets the digital output. 
        self._IOCommandsNET.DigitalOutputEntire(Axis,Port,Values)
    
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
    
    _MotionCommandNET=None
    def __init__(self,MotionCommandNET:AerotechEnsembleNET.MotionCommand):
        self._MotionCommandNET=MotionCommandNET
    
    # ! Abort
    @multimethod  
    def Abort(self,axis:int):
        self._MotionCommandNET.Abort(axis)

    @multimethod
    def Abort(self,axes:list[int]):
        self._MotionCommandNET.Abort(axes)
        
    @multimethod
    def Abort(self,axis:str):
        self._MotionCommandNET.Abort(axis)
        
    @multimethod
    def Abort(self,axes:list[str]):
        self._MotionCommandNET.Abort(axes)
    
    @multimethod
    def Abort(self,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.Abort(AxisMask.value)
        
    @property
    def Advanced(self):
        return MotionAdvancedCommands(self._MotionCommandNET.Advanced)
        
    # ! AutoFocus
    @multimethod
    def AutoFocus(self,axis:int, OnOff:OnOff): 
        self._MotionCommandNET.AutoFocus(axis,OnOff.value)
        
    @multimethod
    def AutoFocus(self,axes:list[int], OnOff:OnOff): 
        self._MotionCommandNET.AutoFocus(axes,OnOff.value)
    
    @multimethod
    def AutoFocus(self,axis:str, OnOff:OnOff):
        self._MotionCommandNET.AutoFocus(axis,OnOff.value)
    
    @multimethod
    def AutoFocus(self,axes:list[str], OnOff:OnOff):
        self._MotionCommandNET.AutoFocus(axes,OnOff.value)
    
    @multimethod
    def AutoFocus(self,AxisMask:Ensemble.AxisMask, OnOff:OnOff):
        self._MotionCommandNET.AutoFocus(AxisMask.value,OnOff.value)
        
    # ! BlockMotion 
    @multimethod
    def BlockMotion(self,axis:int, OnOff:OnOff): 
        self._MotionCommandNET.BlockMotion(axis,OnOff.value)
        
    @multimethod
    def BlockMotion(self,axes:list[int], OnOff:OnOff): 
        self._MotionCommandNET.BlockMotion(axes,OnOff.value)
    
    @multimethod
    def BlockMotion(self,axis:str, OnOff:OnOff):
        self._MotionCommandNET.BlockMotion(axis,OnOff.value)
    
    @multimethod
    def BlockMotion(self,axes:list[str], OnOff:OnOff):
        self._MotionCommandNET.BlockMotion(axes,OnOff.value)
    
    @multimethod
    def BlockMotion(self,AxisMask:Ensemble.AxisMask, OnOff:OnOff):
        self._MotionCommandNET.BlockMotion(AxisMask.value,OnOff.value)
        
    # ! CCWCenter
    @multimethod
    def CCWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float):
        self._MotionCommandNET.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CCWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float):
        self._MotionCommandNET.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CCWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._MotionCommandNET.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
    @multimethod
    def CCWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._MotionCommandNET.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
        
    # ! CCWRadius
    @multimethod
    def CCWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float):
        self._MotionCommandNET.CCWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CCWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float):
        self._MotionCommandNET.CCWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CCWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float,coordinatedSpeed:float):
        self._MotionCommandNET.CCWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
    @multimethod
    def CCWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float,coordinatedSpeed:float):
        self._MotionCommandNET.CCWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
        
    # ! CWCenter
    @multimethod
    def CWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float):
        self._MotionCommandNET.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float):
        self._MotionCommandNET.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._MotionCommandNET.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
    @multimethod
    def CWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self._MotionCommandNET.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
        
    # ! CWRadius
    @multimethod
    def CWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float):
        self._MotionCommandNET.CWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float):
        self._MotionCommandNET.CWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float,coordinatedSpeed:float):
        self._MotionCommandNET.CWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
    @multimethod
    def CWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float,coordinatedSpeed:float):
        self._MotionCommandNET.CWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed) 

    # ! Disable
    @multimethod
    def Disable(self,axis:int): 
        self._MotionCommandNET.Disable(axis)
        
    @multimethod
    def Disable(self,axes:list[int]): 
        self._MotionCommandNET.Disable(axes)
    
    @multimethod
    def Disable(self,axis:str):
        self._MotionCommandNET.Disable(axis)
    
    @multimethod
    def Disable(self,axes:list[str]):
        self._MotionCommandNET.Disable(axes)
    
    @multimethod
    def Disable(self,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.Disable(AxisMask.value)

    # ! Enable
    @multimethod
    def Enable(self,axis:int): 
        self._MotionCommandNET.Enable(axis)
        
    @multimethod
    def Enable(self,axes:list[int]): 
        self._MotionCommandNET.Enable(axes)
    
    @multimethod
    def Enable(self,axis:str):
        self._MotionCommandNET.Enable(axis)
    
    @multimethod
    def Enable(self,axes:list[str]):
        self._MotionCommandNET.Enable(axes)
    
    @multimethod
    def Enable(self,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.Enable(AxisMask.value)
        
    # ! FaultAck
    @multimethod
    def FaultAck(self,axis:int): 
        self._MotionCommandNET.FaultAck(axis)
        
    @multimethod
    def FaultAck(self,axes:list[int]): 
        self._MotionCommandNET.FaultAck(axes)
    
    @multimethod
    def FaultAck(self,axis:str):
        self._MotionCommandNET.FaultAck(axis)
    
    @multimethod
    def FaultAck(self,axes:list[str]):
        self._MotionCommandNET.FaultAck(axes)
    
    @multimethod
    def FaultAck(self,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.FaultAck(AxisMask.value)
        
    # ! FreeRun
    @multimethod
    def FreeRun(self,axis:int,speed:float): 
        self._MotionCommandNET.FreeRun(axis,speed)
        
    @multimethod
    def FreeRun(self,axes:list[int],speed:list[float]): 
        self._MotionCommandNET.FreeRun(axes,speed)
    
    @multimethod
    def FreeRun(self,axis:str,speed:float):
        self._MotionCommandNET.FreeRun(axis,speed)
    
    @multimethod
    def FreeRun(self,axes:list[str],speed:list[float]):
        self._MotionCommandNET.FreeRun(axes,speed)
    
    @multimethod
    def FreeRun(self,AxisMask:Ensemble.AxisMask,speed:float):
        self._MotionCommandNET.FreeRun(AxisMask.value,speed)
        
    @multimethod
    def FreeRun(self,AxisMask:Ensemble.AxisMask,speed:list[float]):
        self._MotionCommandNET.FreeRun(AxisMask.value,speed)
        
    # ! FreeRunStop
    @multimethod
    def FreeRunStop(self,axis:int): 
        self._MotionCommandNET.FreeRunStop(axis)
        
    @multimethod
    def FreeRunStop(self,axes:list[int]): 
        self._MotionCommandNET.FreeRunStop(axes)
    
    @multimethod
    def FreeRunStop(self,axis:str):
        self._MotionCommandNET.FreeRunStop(axis)
    
    @multimethod
    def FreeRunStop(self,axes:list[str]):
        self._MotionCommandNET.FreeRunStop(axes)
    
    @multimethod
    def FreeRunStop(self,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.FreeRunStop(AxisMask.value)
        
    # ! Home
    @multimethod
    def Home(self,axis:int): 
        self._MotionCommandNET.Home(axis)
        
    @multimethod
    def Home(self,axes:list[int]): 
        self._MotionCommandNET.Home(axes)
    
    @multimethod
    def Home(self,axis:str):
        self._MotionCommandNET.Home(axis)
    
    @multimethod
    def Home(self,axes:list[str]):
        self._MotionCommandNET.Home(axes)
    
    @multimethod
    def Home(self,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.Home(AxisMask.value)
            
    # ! HomeConditional
    @multimethod
    def HomeConditional(self,axis:int): 
        self._MotionCommandNET.HomeConditional(axis)
        
    @multimethod
    def HomeConditional(self,axes:list[int]): 
        self._MotionCommandNET.HomeConditional(axes)
    
    @multimethod
    def HomeConditional(self,axis:str):
        self._MotionCommandNET.HomeConditional(axis)
    
    @multimethod
    def HomeConditional(self,axes:list[str]):
        self._MotionCommandNET.HomeConditional(axes)
    
    @multimethod
    def HomeConditional(self,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.HomeConditional(AxisMask.value)
        
        
    # ! Linear
    @multimethod
    def Linear(self,axis:int,distance:float): 
        self._MotionCommandNET.Linear(axis,distance)
        
    @multimethod
    def Linear(self,axes:list[int],distance:list[float]): 
        self._MotionCommandNET.Linear(axes,distance)
    
    @multimethod
    def Linear(self,axis:str,distance:float):
        self._MotionCommandNET.Linear(axis,distance)
    
    @multimethod
    def Linear(self,axes:list[str],distance:list[float]):
        self._MotionCommandNET.Linear(axes,distance)
    
    @multimethod
    def Linear(self,AxisMask:Ensemble.AxisMask,distance:float):
        self._MotionCommandNET.Linear(AxisMask.value,distance)
        
    @multimethod
    def Linear(self,AxisMask:Ensemble.AxisMask,distance:list[float]):
        self._MotionCommandNET.Linear(AxisMask.value,distance)

    @multimethod
    def Linear(self,axis:int,distance:float,coordinatedSpeed:float): 
        self._MotionCommandNET.Linear(axis,distance,coordinatedSpeed)
        
    @multimethod
    def Linear(self,axes:list[int],distance:list[float],coordinatedSpeed:float): 
        self._MotionCommandNET.Linear(axes,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,axis:str,distance:float,coordinatedSpeed:float):
        self._MotionCommandNET.Linear(axis,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,axes:list[str],distance:list[float],coordinatedSpeed:float):
        self._MotionCommandNET.Linear(axes,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,AxisMask:Ensemble.AxisMask,distance:float,coordinatedSpeed:float):
        self._MotionCommandNET.Linear(AxisMask.value,distance,coordinatedSpeed)
        
    @multimethod
    def Linear(self,AxisMask:Ensemble.AxisMask,distance:list[float],coordinatedSpeed:float):
        self._MotionCommandNET.Linear(AxisMask.value,distance,coordinatedSpeed)
        
    # ! MoveAbs
    @multimethod
    def MoveAbs(self,axis:int,distance:float): 
        self._MotionCommandNET.MoveAbs(axis,distance)
        
    @multimethod
    def MoveAbs(self,axes:list[int],distance:list[float]): 
        self._MotionCommandNET.MoveAbs(axes,distance)
    
    @multimethod
    def MoveAbs(self,axis:str,distance:float):
        self._MotionCommandNET.MoveAbs(axis,distance)
    
    @multimethod
    def MoveAbs(self,axes:list[str],distance:list[float]):
        self._MotionCommandNET.MoveAbs(axes,distance)
    
    @multimethod
    def MoveAbs(self,AxisMask:Ensemble.AxisMask,distance:float):
        self._MotionCommandNET.MoveAbs(AxisMask.value,distance)
        
    @multimethod
    def MoveAbs(self,AxisMask:Ensemble.AxisMask,distance:list[float]):
        self._MotionCommandNET.MoveAbs(AxisMask.value,distance)

    @multimethod
    def MoveAbs(self,axis:int,distance:float,speed:float): 
        self._MotionCommandNET.MoveAbs(axis,distance,speed)
        
    @multimethod
    def MoveAbs(self,axes:list[int],distance:list[float],speed:float): 
        self._MotionCommandNET.MoveAbs(axes,distance,speed)
    
    @multimethod
    def MoveAbs(self,axis:str,distance:float,speed:float):
        self._MotionCommandNET.MoveAbs(axis,distance,speed)
    
    @multimethod
    def MoveAbs(self,axes:list[str],distance:list[float],speed:float):
        self._MotionCommandNET.MoveAbs(axes,distance,speed)
    
    @multimethod
    def MoveAbs(self,AxisMask:Ensemble.AxisMask,distance:float,speed:float):
        self._MotionCommandNET.MoveAbs(AxisMask.value,distance,speed)
        
    @multimethod
    def MoveAbs(self,AxisMask:Ensemble.AxisMask,distance:list[float],speed:float):
        self._MotionCommandNET.MoveAbs(AxisMask.value,distance,speed)
        
    # ! MoveInc
    @multimethod
    def MoveInc(self,axis:int,distance:float): 
        self._MotionCommandNET.MoveInc(axis,distance)
        
    @multimethod
    def MoveInc(self,axes:list[int],distance:list[float]): 
        self._MotionCommandNET.MoveInc(axes,distance)
    
    @multimethod
    def MoveInc(self,axis:str,distance:float):
        self._MotionCommandNET.MoveInc(axis,distance)
    
    @multimethod
    def MoveInc(self,axes:list[str],distance:list[float]):
        self._MotionCommandNET.MoveInc(axes,distance)
    
    @multimethod
    def MoveInc(self,AxisMask:Ensemble.AxisMask,distance:float):
        self._MotionCommandNET.MoveInc(AxisMask.value,distance)
        
    @multimethod
    def MoveInc(self,AxisMask:Ensemble.AxisMask,distance:list[float]):
        self._MotionCommandNET.MoveInc(AxisMask.value,distance)

    @multimethod
    def MoveInc(self,axis:int,distance:float,speed:float): 
        self._MotionCommandNET.MoveInc(axis,distance,speed)
        
    @multimethod
    def MoveInc(self,axes:list[int],distance:list[float],speed:float): 
        self._MotionCommandNET.MoveInc(axes,distance,speed)
    
    @multimethod
    def MoveInc(self,axis:str,distance:float,speed:float):
        self._MotionCommandNET.MoveInc(axis,distance,speed)
    
    @multimethod
    def MoveInc(self,axes:list[str],distance:list[float],speed:float):
        self._MotionCommandNET.MoveInc(axes,distance,speed)
    
    @multimethod
    def MoveInc(self,AxisMask:Ensemble.AxisMask,distance:float,speed:float):
        self._MotionCommandNET.MoveInc(AxisMask.value,distance,speed)
        
    @multimethod
    def MoveInc(self,AxisMask:Ensemble.AxisMask,distance:list[float],speed:float):
        self._MotionCommandNET.MoveInc(AxisMask.value,distance,speed)

    @property
    def Setup(self):
        return self._Setup

    def Start(self):
        self._ControllerNET.Commands.Start()
    
    # ! WaitForMotionDone 
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:int): 
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axis)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[int]): 
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axes)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:str):
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axis)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[str]):
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axes)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,AxisMask:Ensemble.AxisMask):
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,AxisMask.value)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:int,timeout:int): 
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axis,timeout)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[int],timeout:int): 
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axes,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:str,timeout:int):
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axis,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[str],timeout:int):
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,axes,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,AxisMask:Ensemble.AxisMask,timeout:int):
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,AxisMask.value,timeout)
        
    def WaitMode(self,type:WaitType):
        self._MotionCommandNET.WaitMode(type.value)
    
class MotionSetupCommands(CommandCategory):
    _MotionSetupCommandsNET=None
    def __init__(self,MotionSetupCommandsNET:AerotechEnsembleNET.MotionSetupCommands):
        self._MotionSetupCommandsNET=MotionSetupCommandsNET
        


    def Absolute(self):  # Sets motion commands to be in absolute mode.
        self._MotionSetupCommandsNET.Absolute()

    def Incremental(self):  # Sets motion commands to be in incremental mode.
        self._MotionSetupCommandsNET.Incremental()

    def Plane(self,PlaneNumber:int):  # Sets the current plane of motion.
        self._MotionSetupCommandsNET.Plane(PlaneNumber)
        
    @multimethod
    def PosCap(self,axisIndex:int):  # Retrieves the POSCAP position.
        return self._MotionSetupCommandsNET.PosCap(axisIndex)
 
    @multimethod
    def PosCap(self,axisIndex:int, reArm:bool):  # Retrieves the POSCAP positions.
        return self._MotionSetupCommandsNET.PosCap(axisIndex,reArm)
 
    @multimethod
    def PosCap(self,axisIndexes:list[int]):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._MotionSetupCommandsNET.PosCap(axisIndexes),float,Ensemble.AxisMask)
 
    @multimethod
    def PosCap(self,axisIndexes:list[int], reArm:bool):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._MotionSetupCommandsNET.PosCap(axisIndexes,reArm),float,Ensemble.AxisMask)
 
    @multimethod
    def PosCap(self,axisMask:Ensemble.AxisMask):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._MotionSetupCommandsNET.PosCap(axisMask.value),float,Ensemble.AxisMask)
 
    @multimethod
    def PosCap(self,axisMask:Ensemble.AxisMask, reArm:bool):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._MotionSetupCommandsNET.PosCap(axisMask.value,reArm),float,Ensemble.AxisMask)
 
    @multimethod
    def PosCap(self,axisName:str):  # Retrieves the POSCAP positions.
        return self._MotionSetupCommandsNET.PosCap(axisName)
 
    @multimethod
    def PosCap(self,axisName:str, reArm:bool):  # Retrieves the POSCAP positions.
        return self._MotionSetupCommandsNET.PosCap(axisName,reArm)
 
    @multimethod
    def PosCap(self,axisNames:list[str]):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._MotionSetupCommandsNET.PosCap(axisNames),float,Ensemble.AxisMask)
 
    @multimethod
    def PosCap(self,axisNames:list[str], reArm:bool):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._MotionSetupCommandsNET.PosCap(axisNames,reArm),float,Ensemble.AxisMask)
 
    @multimethod
    def PosOffsetClear(self,Axis:int):  # Sets or clears an arbitrary program offset position.
        self._MotionSetupCommandsNET.PosOffsetClear(Axis)
 
    @multimethod
    def PosOffsetClear(self,Axis:str):  # Sets or clears an arbitrary program offset position.
        self._MotionSetupCommandsNET.PosOffsetClear(Axis)
        
    @multimethod
    def PosOffsetSet(self,Axis:int, Value:float):  # Sets or clears an arbitrary program offset position.
        self._MotionSetupCommandsNET.PosOffsetSet(Axis, Value)
        
    @multimethod
    def PosOffsetSet(self,Axis:str, Value:float):  # Sets or clears an arbitrary program offset position.
        self._MotionSetupCommandsNET.PosOffsetSet(Axis, Value)
        
    @multimethod
    def RampDist(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(Value)

    @multimethod
    def RampDist(self,axisIndexes:list[int],Value:list[float]):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisIndexes,Value)
        
    @multimethod
    def RampDist(self,axisIndex:int,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisIndex,Value)
        
    @multimethod
    def RampDist(self,axisNames:list[str],Value:list[float]):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisNames,Value)
        
    @multimethod
    def RampDist(self,axisName:str,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisName,Value)
        
    @multimethod
    def RampDist(self,axisMask:Ensemble.AxisMask,Value:list[float]):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisMask.value,Value)
        
    @multimethod
    def RampDist(self,axisMask:Ensemble.AxisMask,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisMask.value,Value)
        
    def RampDistAccel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDistAccel(Value)
        
    def RampDistDecel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDistDecel(Value)
        
    @multimethod
    def RampMode(self,Mode:RampMode):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(Mode.value)
        
    @multimethod
    def RampMode(self,axisIndexes:list[int], Mode:RampMode):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisIndexes,Mode.value)
        
    @multimethod
    def RampMode(self,axisIndex:int, Mode:RampMode):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisIndex,Mode.value)
        
    @multimethod
    def RampMode(self,axisNames:list[str], Mode:RampMode):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisNames,Mode.value)
        
    @multimethod
    def RampMode(self,axisName:str, Mode:RampMode):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisName,Mode.value)
        
    @multimethod
    def RampMode(self,axisMask:Ensemble.AxisMask, Mode:RampMode):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisMask.value,Mode.value)
        
    @multimethod
    def RampRate(self,Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(Value)
        
    @multimethod
    def RampRate(self,axisIndexes:list[int], Value:list[float]):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(axisIndexes,Value)
        
    @multimethod
    def RampRate(self,axisIndex:int, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(axisIndex,Value)
        
    @multimethod
    def RampRate(self,axisNames:list[str], Value:list[float]):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(axisNames,Value)
        
    @multimethod
    def RampRate(self,axisName:str, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(axisName,Value)
        
    @multimethod
    def RampRate(self,axisMask:Ensemble.AxisMask, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(axisMask.value,Value)
        
    @multimethod
    def RampRate(self,axisMask:Ensemble.AxisMask, Value:list[float]):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(axisMask.value,Value)

    def RampRateAccel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampRateAccel(Value)
        
    def RampRateDecel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampRateDecel(Value)

    @multimethod
    def RampTime(self,Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(Value)
        
    @multimethod
    def RampTime(self,axisIndexes:list[int], Value:list[float]):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(axisIndexes,Value)
        
    @multimethod
    def RampTime(self,axisIndex:int, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(axisIndex,Value)
        
    @multimethod
    def RampTime(self,axisNames:list[str], Value:list[float]):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(axisNames,Value)
        
    @multimethod
    def RampTime(self,axisName:str, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(axisName,Value)
        
    @multimethod
    def RampTime(self,axisMask:Ensemble.AxisMask, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(axisMask.value,Value)
        
    @multimethod
    def RampTime(self,axisMask:Ensemble.AxisMask, Value:list[float]):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(axisMask.value,Value)

    def RampTimeAccel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampRateAccel(Value)
        
    def RampTimeDecel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampRateDecel(Value)

    @multimethod
    def Reconcile(self,axisIndexes:list[int]):  # Reconciles the position of the axes in the list on the plane to servo position.
        self._MotionSetupCommandsNET.Reconcile(axisIndexes)

    @multimethod
    def Reconcile(self,axisIndex:int):  # Reconciles the position of the axes in the list on the plane to servo position.
        self._MotionSetupCommandsNET.Reconcile(axisIndex)
        
    @multimethod
    def Reconcile(self,axisNames:list[str]):  # Reconciles the position of the axes in the list on the plane to servo position.
        self._MotionSetupCommandsNET.Reconcile(axisNames)
        
    @multimethod
    def Reconcile(self,axisName:str):  # Reconciles the position of the axes in the list on the plane to servo position.
        self._MotionSetupCommandsNET.Reconcile(axisName)
        
    @multimethod
    def Reconcile(self,axisMask:Ensemble.AxisMask):  # Reconciles the position of the axes in the list on the plane to servo position.
        self._MotionSetupCommandsNET.Reconcile(axisMask)
        
    @multimethod
    def ScaleFactorClear(self,Axis:int):  # Sets or clears the scale factor for an axis.
        self._MotionSetupCommandsNET.ScaleFactorClear(Axis)
        
    @multimethod
    def ScaleFactorClear(self,Axis:str):  # Sets or clears the scale factor for an axis.
        self._MotionSetupCommandsNET.ScaleFactorClear(Axis)
        
    @multimethod
    def ScaleFactorSet(self,Axis:int, Value:float):  # Sets or clears the scale factor for an axis.
        self._MotionSetupCommandsNET.ScaleFactorSet(Axis, Value)

    @multimethod
    def ScaleFactorSet(self,Axis:str, Value:float):  # Sets or clears the scale factor for an axis.
        self._MotionSetupCommandsNET.ScaleFactorSet(Axis, Value)
        
    def Scurve(self,Value:float):  # Specifies the S-curve value to use.
        self._MotionSetupCommandsNET.Scurve(Value)

    @multimethod
    def Servo(self,Axis:int, OnOff:OnOff):  # Changes between open-loop and closed-loop mode for piezo stages.
        self._MotionSetupCommandsNET.Servo(Axis,OnOff.value)

    @multimethod
    def Servo(self,Axis:str, OnOff:OnOff):  # Changes between open-loop and closed-loop mode for piezo stages.
        self._MotionSetupCommandsNET.Servo(Axis,OnOff.value)
        
    @multimethod
    def SetExtPos(self,Axis:int, Value:float):  # Sets an arbitrary position value, in encoder counts, in external position register.
        self._MotionSetupCommandsNET.SetExtPos(Axis,Value)

    @multimethod
    def SetExtPos(self,Axis:str, Value:float):  # Sets an arbitrary position value, in encoder counts, in external position register.
        self._MotionSetupCommandsNET.SetExtPos(Axis,Value)

    def TimeScale(self,Percentage:float):  # Specifies the time scale to use. 
        self._MotionSetupCommandsNET.TimeScale(Percentage)

class PSOCommands(CommandCategory):
    _PSOCommandsNET=None
    def __init__(self,PSOCommandsNET:AerotechEnsembleNET.PSOCommands):
        self._PSOCommandsNET=PSOCommandsNET
    
    @multimethod
    def Array(self,Axis:int, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def Array(self,Axis:str, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectDistance(self,Axis:int, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectDistance(self,Axis:str, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectLaser(self,Axis:int, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectLaser(self,Axis:str, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectWindow1(self,Axis:int, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectWindow1(self,Axis:str, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectWindow2(self,Axis:int, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def ArrayFifoSelectWindow2(self,Axis:str, Int32, Int32):  # Sends data into the PSO array.
        return self._PSOCommandsNET.
    
    @multimethod
    def Control(self,Axis:int, PsoMode):  # Enables and disables the PSO hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def Control(self,Axis:str, PsoMode):  # Enables and disables the PSO hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def DistanceArray(self,Axis:int):  # Sets the distance to travel between firing events.
        return self._PSOCommandsNET.
    
    @multimethod
    def DistanceArray(self,Axis:str):  # Sets the distance to travel between firing events.
        return self._PSOCommandsNET.
    
    @multimethod
    def DistanceFixed(self,Axis:int, Double):  # Sets the distance to travel between firing events.
        return self._PSOCommandsNET.
    
    @multimethod
    def DistanceFixed(self,Axis:str, Double):  # Sets the distance to travel between firing events.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputBitMap(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputBitMap(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputBitMap(self,Axis:int, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputBitMap(self,Axis:str, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputControl(self,Axis:int, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputControl(self,Axis:str, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulse(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulse(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseBitMask(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseBitMask(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseExtSync(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseExtSync(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowBitMask(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowBitMask(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowBitMaskEdgeMode(self,Axis:int, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowBitMaskEdgeMode(self,Axis:str, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowMask(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowMask(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowMaskEdgeMode(self,Axis:int, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowMaskEdgeMode(self,Axis:str, Int32):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowMaskHard(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputPulseWindowMaskHard(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputToggle(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputToggle(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputWindow(self,Axis:int):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def OutputWindow(self,Axis:str):  # Sets the PSO output mode.
        return self._PSOCommandsNET.
    
    @multimethod
    def Pulse(self,Axis:int, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def Pulse(self,Axis:str, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def PulseCyclesOrDelayCyclesAndDelay(self,Axis:int, Double, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def PulseCyclesOrDelayCyclesAndDelay(self,Axis:str, Double, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def PulseCyclesOrDelayCyclesOnly(self,Axis:int, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def PulseCyclesOrDelayCyclesOnly(self,Axis:str, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def PulseCyclesOrDelayDelayOnly(self,Axis:int, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def PulseCyclesOrDelayDelayOnly(self,Axis:str, Double, Double, Double):  # Configures the pulse sequence that is used for PSO.
        return self._PSOCommandsNET.
    
    @multimethod
    def Status(self,Axis:int):  # Gets the PSO status information.
        return self._PSOCommandsNET.
    
    @multimethod
    def Status(self,Axis:str):  # Gets the PSO status information.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackDirection(self,Axis:int, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackDirection(self,Axis:str, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackInput(self,Axis:int, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackInput(self,Axis:str, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackInput(self,Axis:int, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackInput(self,Axis:str, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackInput(self,Axis:int, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackInput(self,Axis:str, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackReset(self,Axis:int, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackReset(self,Axis:str, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackScale(self,Axis:int, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackScale(self,Axis:str, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackScale(self,Axis:int, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackScale(self,Axis:str, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackScale(self,Axis:int, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def TrackScale(self,Axis:str, Int32, Int32, Int32):  # Configures the PSO distance tracking counters.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowInput(self,Axis:int, Int32, Int32):  # Configures which encoder channel is connected to each window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowInput(self,Axis:str, Int32, Int32):  # Configures which encoder channel is connected to each window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowInputInvert(self,Axis:int, Int32, Int32):  # Configures which encoder channel is connected to each window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowInputInvert(self,Axis:str, Int32, Int32):  # Configures which encoder channel is connected to each window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowLoad(self,Axis:int, Int32, Int32):  # Loads the specified window counter with a value.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowLoad(self,Axis:str, Int32, Int32):  # Loads the specified window counter with a value.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowOff(self,Axis:int, Int32):  # Disables the PSO Window Hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowOff(self,Axis:str, Int32):  # Disables the PSO Window Hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowOn(self,Axis:int, Int32):  # Enables the PSO Window Hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowOn(self,Axis:str, Int32):  # Enables the PSO Window Hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowOnInvert(self,Axis:int, Int32):  # Enables the PSO Window Hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowOnInvert(self,Axis:str, Int32):  # Enables the PSO Window Hardware.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowRange(self,Axis:int, Int32, Double, Double):  # Specifies the low and high comparison values for specified PSO window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowRange(self,Axis:str, Int32, Double, Double):  # Specifies the low and high comparison values for specified PSO window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowRangeArray(self,Axis:int, Int32):  # Specifies the array mode parameters for the specified PSO window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowRangeArray(self,Axis:str, Int32):  # Specifies the array mode parameters for the specified PSO window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowRangeArrayEdge(self,Axis:int, Int32, Double):  # Specifies the array mode parameters for the specified PSO window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowRangeArrayEdge(self,Axis:str, Int32, Double):  # Specifies the array mode parameters for the specified PSO window.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowReset(self,Axis:int, Int32, Int32):  # Resets the window counter to 0 based on the encoder marker signal.
        return self._PSOCommandsNET.
    
    @multimethod
    def WindowReset(self,Axis:str, Int32, Int32):  # Resets the window counter to 0 based on the encoder marker signal. 
        return self._PSOCommandsNET.
    

class RegisterCommands(CommandCategory):
    _RegisterCommandsNET=None
    def __init__(self,RegisterCommandsNET:AerotechEnsembleNET.RegisterCommands):
        self._RegisterCommandsNET=RegisterCommandsNET
        
        # TODO
    
class RootCommands(CommandCategory):
    _RootCommandsNET=None
    def __init__(self,RootCommandsNET:AerotechEnsembleNET.RootCommands):
        self._RootCommandsNET=RootCommandsNET
            
        # TODO
    @property
    def Motion(self):
        return MotionCommands(self._ControllerNET)
 
    def AcknowledgeAll(self):
        self._ControllerNET.Commands.AcknowledgeAll()
        
    def Execute(self,code:str):
        self._ControllerNET.Commands.Execute(code)
 
    def ExecuteAsync(self,code:str):
        self._ControllerNET.Commands.ExecuteAsync(code)
    
class StatusCommands(CommandCategory):
    _StatusCommandsNET=None
    def __init__(self,StatusCommandsNET=AerotechEnsembleCommandsNET.StatusCommands):
        self._StatusCommandsNET=StatusCommandsNET
        CommandCategory.__init__(self,StatusCommandsNET)
            
        # TODO
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
                
        # TODO
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