import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System.ComponentModel import ProgressChangedEventHandler

from enum import Enum

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

class CommandCategory():
    _CommandCategoryNET=None
    def __init__(self,CommandCategoryNET=AerotechEnsembleCommandsNET.CommandCategory):
        self._CommandCategoryNET=CommandCategoryNET

class AdvancedAnalogCommands(CommandCategory):
    _AdvancedAnalogCommandsNET=None
    def __init__(self,AdvancedAnalogCommandsNET=AerotechEnsembleCommandsNET.AdvancedAnalogCommands):
        self._AdvancedAnalogCommandsNET=AdvancedAnalogCommandsNET
        CommandCategory.__init__(AdvancedAnalogCommandsNET)

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
        CommandCategory.__init__(AdvancedCommandsNET)
    
    @property
    def Analog(self):  # Contains the Analog Commands 
        return AdvancedAnalogCommands(self._AdvancedCommandsNET.Analog)

class AxesIOCommands(CommandCategory):
    _AxesIOCommandsNET=None
    def __init__(self,AxesIOCommandsNET=AerotechEnsembleCommandsNET.AxesIOCommands):
        self._AxesIOCommandsNET=AxesIOCommandsNET
        CommandCategory.__init__(AxesIOCommandsNET)
        
    def Brake(self,OnOff:OnOff):  # Controls the brake output of axes. 
        return self._AxesIOCommandsNET.Brake(OnOff.value)

class AxesMotionCommands(CommandCategory):
    _AxesMotionCommandsNET=None
    def __init__(self,AxesMotionCommandsNET=AerotechEnsembleCommandsNET.AxesMotionCommands):
        self._AxesMotionCommandsNET=AxesMotionCommandsNET
        CommandCategory.__init__(AxesMotionCommandsNET)
        
            
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
        CommandCategory.__init__(AxesMotionSetupCommandsNET)
        
    @multimethod
    def PosCap(self):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._AxesMotionSetupCommandsNET.PosCap(),float,Ensemble.AxisMask)
    
    @multimethod
    def PosCap(self,reArm:bool):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._AxesMotionSetupCommandsNET.PosCap(reArm),float,Ensemble.AxisMask)

    def RampDist(self,Value:list[float]):  # Specifies distance-based acceleration and deceleration.
        self._AxesMotionSetupCommandsNET.RampDist(Value)
        
    def RampMode(self,Mode:Enum):  # Specifies the ramp mode calculation type to use.
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
        CommandCategory.__init__(AxesRootCommandsNET)
        
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
    def Select(self, axisMasks:list[Enum]):  # Allows the selection of axes on which to execute the command 
        _axisMasks=[mask.value for mask in axisMasks]
        return AxesRootCommands(self._AxesSelectionCommandsNET.Select(_axisMasks))
    
    @multimethod
    def Select(self, axisNames:list[str]):  # Allows the selection of axes on which to execute the command 
        return AxesRootCommands(self._AxesSelectionCommandsNET.Select(axisNames))
    
    @multimethod
    def Select(self, axisNumbers:list[int]):  # Allows the selection of axes on which to execute the command  
        return AxesRootCommands(self._AxesSelectionCommandsNET.Select(axisNumbers))

class DataAcquisitionCommands(CommandCategory):
    _DataAcquisitionCommandsNET=None
    def __init__(self,DataAcquisitionCommandsNET=AerotechEnsembleCommandsNET.DataAcquisitionCommands):
        self._DataAcquisitionCommandsNET=DataAcquisitionCommandsNET
        CommandCategory.__init__(DataAcquisitionCommandsNET)

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
        CommandCategory.__init__(IOCommandsNET)

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
    def Brake(self,axisMask:Enum, OnOff:OnOff):  # Controls the brake output of axes.
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
    def __init__(self,MotionAdvancedCommandsNET:AerotechEnsembleCommandsNET.MotionAdvancedCommands):
        self._MotionAdvancedCommandsNET=MotionAdvancedCommandsNET
        CommandCategory.__init__(MotionAdvancedCommandsNET)
        
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
    def __init__(self,MotionCommandNET:AerotechEnsembleCommandsNET.MotionCommands):
        self._MotionCommandNET=MotionCommandNET
        CommandCategory.__init__(MotionCommandNET)
    
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
    def Abort(self,AxisMask:Enum):
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
    def AutoFocus(self,AxisMask:Enum, OnOff:OnOff):
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
    def BlockMotion(self,AxisMask:Enum, OnOff:OnOff):
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
    def Disable(self,AxisMask:Enum):
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
    def Enable(self,AxisMask:Enum):
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
    def FaultAck(self,AxisMask:Enum):
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
    def FreeRun(self,AxisMask:Enum,speed:float):
        self._MotionCommandNET.FreeRun(AxisMask.value,speed)
        
    @multimethod
    def FreeRun(self,AxisMask:Enum,speed:list[float]):
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
    def FreeRunStop(self,AxisMask:Enum):
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
    def Home(self,AxisMask:Enum):
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
    def HomeConditional(self,AxisMask:Enum):
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
    def Linear(self,AxisMask:Enum,distance:float):
        self._MotionCommandNET.Linear(AxisMask.value,distance)
        
    @multimethod
    def Linear(self,AxisMask:Enum,distance:list[float]):
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
    def Linear(self,AxisMask:Enum,distance:float,coordinatedSpeed:float):
        self._MotionCommandNET.Linear(AxisMask.value,distance,coordinatedSpeed)
        
    @multimethod
    def Linear(self,AxisMask:Enum,distance:list[float],coordinatedSpeed:float):
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
    def MoveAbs(self,AxisMask:Enum,distance:float):
        self._MotionCommandNET.MoveAbs(AxisMask.value,distance)
        
    @multimethod
    def MoveAbs(self,AxisMask:Enum,distance:list[float]):
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
    def MoveAbs(self,AxisMask:Enum,distance:float,speed:float):
        self._MotionCommandNET.MoveAbs(AxisMask.value,distance,speed)
        
    @multimethod
    def MoveAbs(self,AxisMask:Enum,distance:list[float],speed:float):
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
    def MoveInc(self,AxisMask:Enum,distance:float):
        self._MotionCommandNET.MoveInc(AxisMask.value,distance)
        
    @multimethod
    def MoveInc(self,AxisMask:Enum,distance:list[float]):
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
    def MoveInc(self,AxisMask:Enum,distance:float,speed:float):
        self._MotionCommandNET.MoveInc(AxisMask.value,distance,speed)
        
    @multimethod
    def MoveInc(self,AxisMask:Enum,distance:list[float],speed:float):
        self._MotionCommandNET.MoveInc(AxisMask.value,distance,speed)

    @property
    def Setup(self):
        return self._MotionCommandNET.Setup

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
    def WaitForMotionDone (self,waitOption:WaitOption,AxisMask:Enum):
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
    def WaitForMotionDone (self,waitOption:WaitOption,AxisMask:Enum,timeout:int):
        self._MotionCommandNET.WaitForMotionDone(waitOption.value,AxisMask.value,timeout)
        
    def WaitMode(self,type:WaitType):
        self._MotionCommandNET.WaitMode(type.value)
    
class MotionSetupCommands(CommandCategory):
    _MotionSetupCommandsNET=None
    def __init__(self,MotionSetupCommandsNET:AerotechEnsembleCommandsNET.MotionSetupCommands):
        self._MotionSetupCommandsNET=MotionSetupCommandsNET
        CommandCategory.__init__(MotionSetupCommandsNET)
        


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
    def PosCap(self,axisMask:Enum):  # Retrieves the POSCAP positions.
        return CommonCollections.NamedMaskedConstantCollection(self._MotionSetupCommandsNET.PosCap(axisMask.value),float,Ensemble.AxisMask)
 
    @multimethod
    def PosCap(self,axisMask:Enum, reArm:bool):  # Retrieves the POSCAP positions.
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
    def RampDist(self,axisMask:Enum,Value:list[float]):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisMask.value,Value)
        
    @multimethod
    def RampDist(self,axisMask:Enum,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDist(axisMask.value,Value)
        
    def RampDistAccel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDistAccel(Value)
        
    def RampDistDecel(self,Value:float):  # Specifies distance-based acceleration and deceleration.
        self._MotionSetupCommandsNET.RampDistDecel(Value)
        
    @multimethod
    def RampMode(self,Mode:Enum):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(Mode.value)
        
    @multimethod
    def RampMode(self,axisIndexes:list[int], Mode:Enum):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisIndexes,Mode.value)
        
    @multimethod
    def RampMode(self,axisIndex:int, Mode:Enum):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisIndex,Mode.value)
        
    @multimethod
    def RampMode(self,axisNames:list[str], Mode:Enum):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisNames,Mode.value)
        
    @multimethod
    def RampMode(self,axisName:str, Mode:Enum):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampMode(axisName,Mode.value)
        
    @multimethod
    def RampMode(self,axisMask:Enum, Mode:Enum):  # Specifies the ramp mode calculation type to use.
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
    def RampRate(self,axisMask:Enum, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampRate(axisMask.value,Value)
        
    @multimethod
    def RampRate(self,axisMask:Enum, Value:list[float]):  # Specifies the ramp mode calculation type to use.
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
    def RampTime(self,axisMask:Enum, Value:float):  # Specifies the ramp mode calculation type to use.
        self._MotionSetupCommandsNET.RampTime(axisMask.value,Value)
        
    @multimethod
    def RampTime(self,axisMask:Enum, Value:list[float]):  # Specifies the ramp mode calculation type to use.
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
    def Reconcile(self,axisMask:Enum):  # Reconciles the position of the axes in the list on the plane to servo position.
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
    def __init__(self,PSOCommandsNET:AerotechEnsembleCommandsNET.PSOCommands):
        self._PSOCommandsNET=PSOCommandsNET
        CommandCategory.__init__(PSOCommandsNET)
    
    @multimethod
    def Array(self,Axis:int, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.Array(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def Array(self,Axis:str, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.Array(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectDistance(self,Axis:int, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectDistance(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectDistance(self,Axis:str, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectDistance(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectLaser(self,Axis:int, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectLaser(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectLaser(self,Axis:str, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectLaser(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectWindow1(self,Axis:int, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectWindow1(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectWindow1(self,Axis:str, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectWindow1(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectWindow2(self,Axis:int, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectWindow2(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def ArrayFifoSelectWindow2(self,Axis:str, StartIndex:int, NumberOfElements:int):  # Sends data into the PSO array.
        self._PSOCommandsNET.ArrayFifoSelectWindow2(Axis, StartIndex, NumberOfElements)
    
    @multimethod
    def Control(self,Axis:int, Mode:PsoMode):  # Enables and disables the PSO hardware.
        self._PSOCommandsNET.Control(Axis,Mode.value)
    
    @multimethod
    def Control(self,Axis:str, Mode:PsoMode):  # Enables and disables the PSO hardware.
        self._PSOCommandsNET.Control(Axis,Mode.value)
    
    @multimethod
    def DistanceArray(self,Axis:int):  # Sets the distance to travel between firing events.
        self._PSOCommandsNET.DistanceArray(Axis)
    
    @multimethod
    def DistanceArray(self,Axis:str):  # Sets the distance to travel between firing events.
        self._PSOCommandsNET.DistanceArray(Axis)
    
    @multimethod
    def DistanceFixed(self,Axis:int, FireDistance:float):  # Sets the distance to travel between firing events.
        self._PSOCommandsNET.DistanceFixed(Axis,FireDistance)
    
    @multimethod
    def DistanceFixed(self,Axis:str, FireDistance:float):  # Sets the distance to travel between firing events.
        self._PSOCommandsNET.DistanceFixed(Axis,FireDistance)
    
    @multimethod
    def OutputBitMap(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputBitMap(Axis)
    
    @multimethod
    def OutputBitMap(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputBitMap(Axis)
    
    @multimethod
    def OutputBitMap(self,Axis:int, Mode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputBitMap(Axis, Mode)
    
    @multimethod
    def OutputBitMap(self,Axis:str, Mode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputBitMap(Axis, Mode)
    
    @multimethod
    def OutputControl(self,Axis:int, Mode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputControl(Axis, Mode)
    
    @multimethod
    def OutputControl(self,Axis:str, Mode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputControl(Axis, Mode)
    
    @multimethod
    def OutputPulse(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulse(Axis)
    
    @multimethod
    def OutputPulse(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulse(Axis)
    
    @multimethod
    def OutputPulseBitMask(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseBitMask(Axis)
    
    @multimethod
    def OutputPulseBitMask(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseBitMask(Axis)
    
    @multimethod
    def OutputPulseExtSync(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutpOutputPulseExtSyncutPulse(Axis)
    
    @multimethod
    def OutputPulseExtSync(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseExtSync(Axis)
    
    @multimethod
    def OutputPulseWindowBitMask(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowBitMask(Axis)
    
    @multimethod
    def OutputPulseWindowBitMask(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowBitMask(Axis)
    
    @multimethod
    def OutputPulseWindowBitMaskEdgeMode(self,Axis:int, EdgeMode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowBitMaskEdgeMode(Axis,EdgeMode)
    
    @multimethod
    def OutputPulseWindowBitMaskEdgeMode(self,Axis:str, EdgeMode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowBitMaskEdgeMode(Axis,EdgeMode)
    
    @multimethod
    def OutputPulseWindowMask(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowMask(Axis)
    
    @multimethod
    def OutputPulseWindowMask(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowMask(Axis)
    
    @multimethod
    def OutputPulseWindowMaskEdgeMode(self,Axis:int, EdgeMode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowMaskEdgeMode(Axis,EdgeMode)
    
    @multimethod
    def OutputPulseWindowMaskEdgeMode(self,Axis:str, EdgeMode:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowMaskEdgeMode(Axis,EdgeMode)
    
    @multimethod
    def OutputPulseWindowMaskHard(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowMaskHard(Axis)
    
    @multimethod
    def OutputPulseWindowMaskHard(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputPulseWindowMaskHard(Axis)
    
    @multimethod
    def OutputToggle(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputToggle(Axis)
    
    @multimethod
    def OutputToggle(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputToggle(Axis)
    
    @multimethod
    def OutputWindow(self,Axis:int):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputWindow(Axis)
    
    @multimethod
    def OutputWindow(self,Axis:str):  # Sets the PSO output mode.
        self._PSOCommandsNET.OutputWindow(Axis)
    
    @multimethod
    def Pulse(self,Axis:int, TotalTime:float, OnTime:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.Pulse(Axis,TotalTime,OnTime)
    
    @multimethod
    def Pulse(self,Axis:str, TotalTime:float, OnTime:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.Pulse(Axis,TotalTime,OnTime)
    
    @multimethod
    def PulseCyclesOrDelayCyclesAndDelay(self,Axis:int, TotalTime:float, OnTime:float, NumCycles:float, DelayTime:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.PulseCyclesOrDelayCyclesAndDelay(Axis,TotalTime,OnTime, NumCycles, DelayTime)
    
    @multimethod
    def PulseCyclesOrDelayCyclesAndDelay(self,Axis:int, TotalTime:float, OnTime:float, NumCycles:float, DelayTime:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.PulseCyclesOrDelayCyclesAndDelay(Axis,TotalTime,OnTime, NumCycles, DelayTime)
    
    @multimethod
    def PulseCyclesOrDelayCyclesOnly(self,Axis:int, TotalTime:float, OnTime:float, NumCycles:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.PulseCyclesOrDelayCyclesOnly(Axis,TotalTime,OnTime, NumCycles)
    
    @multimethod
    def PulseCyclesOrDelayCyclesOnly(self,Axis:str, TotalTime:float, OnTime:float, NumCycles:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.PulseCyclesOrDelayCyclesOnly(Axis,TotalTime,OnTime, NumCycles)
    
    @multimethod
    def PulseCyclesOrDelayDelayOnly(self,Axis:int, TotalTime:float, OnTime:float, DelayTime:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.PulseCyclesOrDelayDelayOnly(Axis,TotalTime,OnTime, DelayTime)
    
    @multimethod
    def PulseCyclesOrDelayDelayOnly(self,Axis:str, TotalTime:float, OnTime:float, DelayTime:float):  # Configures the pulse sequence that is used for PSO.
        self._PSOCommandsNET.PulseCyclesOrDelayDelayOnly(Axis,TotalTime,OnTime, DelayTime)
    
    @multimethod
    def Status(self,Axis:int):  # Gets the PSO status information.
        self._PSOCommandsNET.Status(Axis)
    
    @multimethod
    def Status(self,Axis:str):  # Gets the PSO status information.
        self._PSOCommandsNET.Status(Axis)
    
    @multimethod
    def TrackDirection(self,Axis:int, DBitMask:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackDirection(Axis,DBitMask)
    
    @multimethod
    def TrackDirection(self,Axis:str, DBitMask:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackDirection(Axis,DBitMask)
    
    @multimethod
    def TrackInput(self,Axis:int, Source1:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackInput(Axis,Source1)
    
    @multimethod
    def TrackInput(self,Axis:str, Source1:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackInput(Axis,Source1)
    
    @multimethod
    def TrackInput(self,Axis:int, Source1:int, Source2:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackInput(Axis,Source1,Source2)
    
    @multimethod
    def TrackInput(self,Axis:str, Source1:int, Source2:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackInput(Axis,Source1,Source2)
    
    @multimethod
    def TrackInput(self,Axis:int, Source1:int, Source2:int, Source3:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackInput(Axis,Source1,Source2,Source3)
    
    @multimethod
    def TrackInput(self,Axis:str, Source1:int, Source2:int, Source3:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackInput(Axis,Source1,Source2,Source3)
    
    @multimethod
    def TrackReset(self,Axis:int, DBitMask:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackReset(Axis,DBitMask)
    
    @multimethod
    def TrackReset(self,Axis:str, DBitMask:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackReset(Axis,DBitMask)
    
    @multimethod
    def TrackScale(self,Axis:int, Source1:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackScale(Axis,Source1)
    
    @multimethod
    def TrackScale(self,Axis:str, Source1:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackScale(Axis,Source1)
    
    @multimethod
    def TrackScale(self,Axis:int, Source1:int, Source2:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackScale(Axis,Source1,Source2)
    
    @multimethod
    def TrackScale(self,Axis:str, Source1:int, Source2:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackScale(Axis,Source1,Source2)
    
    @multimethod
    def TrackScale(self,Axis:int, Source1:int, Source2:int, Source3:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackScale(Axis,Source1,Source2,Source3)
    
    @multimethod
    def TrackScale(self,Axis:str, Source1:int, Source2:int, Source3:int):  # Configures the PSO distance tracking counters.
        self._PSOCommandsNET.TrackScale(Axis,Source1,Source2,Source3)
    
    @multimethod
    def WindowInput(self,Axis:int, WindowNumber:int, Source:int):  # Configures which encoder channel is connected to each window.
        self._PSOCommandsNET.WindowInput(Axis,WindowNumber,Source)
    
    @multimethod
    def WindowInput(self,Axis:str, WindowNumber:int, Source:int):  # Configures which encoder channel is connected to each window.
        self._PSOCommandsNET.WindowInput(Axis,WindowNumber,Source)
    
    @multimethod
    def WindowInputInvert(self,Axis:int, WindowNumber:int, Source:int):  # Configures which encoder channel is connected to each window.
        self._PSOCommandsNET.WindowInputInvert(Axis,WindowNumber,Source)
    
    @multimethod
    def WindowInputInvert(self,Axis:str, WindowNumber:int, Source:int):  # Configures which encoder channel is connected to each window.
        self._PSOCommandsNET.WindowInputInvert(Axis,WindowNumber,Source)
    
    @multimethod
    def WindowLoad(self,Axis:int, WindowNumber:int, Value:int):  # Loads the specified window counter with a value.
        self._PSOCommandsNET.WindowLoad(Axis,WindowNumber,Value)
    
    @multimethod
    def WindowLoad(self,Axis:str, WindowNumber:int, Value:int):  # Loads the specified window counter with a value.
        self._PSOCommandsNET.WindowLoad(Axis,WindowNumber,Value)
    
    @multimethod
    def WindowOff(self,Axis:int, WindowNumber:int):  # Disables the PSO Window Hardware.
        self._PSOCommandsNET.WindowOff(Axis,WindowNumber)
    
    @multimethod
    def WindowOff(self,Axis:str, WindowNumber:int):  # Disables the PSO Window Hardware.
        self._PSOCommandsNET.WindowOff(Axis,WindowNumber)
    
    @multimethod
    def WindowOn(self,Axis:int, WindowNumber:int):  # Enables the PSO Window Hardware.
        self._PSOCommandsNET.WindowOn(Axis,WindowNumber)
    
    @multimethod
    def WindowOn(self,Axis:str, WindowNumber:int):  # Enables the PSO Window Hardware.
        self._PSOCommandsNET.WindowOn(Axis,WindowNumber)
    
    @multimethod
    def WindowOnInvert(self,Axis:int, WindowNumber:int):  # Enables the PSO Window Hardware.
        self._PSOCommandsNET.WindowOnInvert(Axis,WindowNumber)
    
    @multimethod
    def WindowOnInvert(self,Axis:str, WindowNumber:int):  # Enables the PSO Window Hardware.
        self._PSOCommandsNET.WindowOnInvert(Axis,WindowNumber)
    
    @multimethod
    def WindowRange(self,Axis:int, WindowNumber:int, LowValue:float, HighValue:float):  # Specifies the low and high comparison values for specified PSO window.
        self._PSOCommandsNET.WindowRange(Axis,WindowNumber,LowValue,HighValue)
    
    @multimethod
    def WindowRange(self,Axis:str, WindowNumber:int, LowValue:float, HighValue:float):  # Specifies the low and high comparison values for specified PSO window.
        self._PSOCommandsNET.WindowRange(Axis,WindowNumber,LowValue,HighValue)
    
    @multimethod
    def WindowRangeArray(self,Axis:int, WindowNumber:int):  # Specifies the array mode parameters for the specified PSO window.
        self._PSOCommandsNET.WindowRangeArray(Axis,WindowNumber)
    
    @multimethod
    def WindowRangeArray(self,Axis:str, WindowNumber:int):  # Specifies the array mode parameters for the specified PSO window.
        self._PSOCommandsNET.WindowRangeArray(Axis,WindowNumber)
    
    @multimethod
    def WindowRangeArrayEdge(self,Axis:int, WindowNumber:int, EdgeCode:float):  # Specifies the array mode parameters for the specified PSO window.
        self._PSOCommandsNET.WindowRangeArrayEdge(Axis,WindowNumber,EdgeCode)
    
    @multimethod
    def WindowRangeArrayEdge(self,Axis:str, WindowNumber:int, EdgeCode:float):  # Specifies the array mode parameters for the specified PSO window.
        self._PSOCommandsNET.WindowRangeArrayEdge(Axis,WindowNumber,EdgeCode)
    
    @multimethod
    def WindowReset(self,Axis:int, WindowNumber:int, BitMask:int):  # Resets the window counter to 0 based on the encoder marker signal.
        self._PSOCommandsNET.WindowRangeArWindowResetrayEdge(Axis,WindowNumber,BitMask)
    
    @multimethod
    def WindowReset(self,Axis:str, WindowNumber:int, BitMask:int):  # Resets the window counter to 0 based on the encoder marker signal. 
        self._PSOCommandsNET.WindowRangeArWindowResetrayEdge(Axis,WindowNumber,BitMask)
    
class RegisterCommands(CommandCategory):
    _RegisterCommandsNET=None
    def __init__(self,RegisterCommandsNET:AerotechEnsembleCommandsNET.RegisterCommands):
        self._RegisterCommandsNET=RegisterCommandsNET
        CommandCategory.__init__(RegisterCommandsNET)
        

    def Lock(self,Semaphore:Semaphores):  # Locks a specified semaphore.
        self._RegisterCommandsNET.Lock(Semaphore.value)
        
    def ReadDoubleGlobal(self,RegNumber:int):  # Provides access to the global double variable (self,register) set.
        self._RegisterCommandsNET.ReadDoubleGlobal(RegNumber)
        
    @multimethod
    def ReadDoubles(self,address:int, count:int):  # Reads multiple values from DoubleRegisters 
        return self._RegisterCommandsNET.ReadDoubles(address,count)
        
    @multimethod
    def ReadDoubles(self,address:int, count:int, progressChangedEventHandler:ProgressChangedEventHandler):  # Reads multiple values from DoubleRegisters 
        return self._RegisterCommandsNET.ReadDoubles(address,count,progressChangedEventHandler)
        
    def ReadIntegerGlobal(self,RegNumber:int):  # Provides access to the global integer variable (self,register) set.
        return self._RegisterCommandsNET.ReadIntegerGlobal(RegNumber)

    @multimethod
    def ReadIntegers(self,address:int, count:int):  # Reads multiple values from IntegerRegisters 
        return self._RegisterCommandsNET.ReadIntegers(address,count)
        
    @multimethod
    def ReadIntegers(self,address:int, count:int, progressChangedEventHandler:ProgressChangedEventHandler):  # Reads multiple values from IntegerRegisters 
        return self._RegisterCommandsNET.ReadIntegers(address,count,progressChangedEventHandler)
        
    def UnLock(self,Semaphore:Semaphores):  # Unlocks a specified semaphore.
        self._RegisterCommandsNET.UnLock(Semaphore.value)
        
    def WriteDoubleGlobal(self,RegNumber:int, Value:float):  # Provides access to the global double variable (self,register) set.
        self._RegisterCommandsNET.WriteDoubleGlobal(RegNumber,Value)
        
    @multimethod
    def WriteDoubles(self,address:int, values:list[float]):  # Writes multiple values to DoubleRegisters 
        self._RegisterCommandsNET.WriteDoubles(address,values)
        
    @multimethod
    def WriteDoubles(self,address:int, values:list[float], progressChangedEventHandler:ProgressChangedEventHandler):  # Writes multiple values to DoubleRegisters 
        self._RegisterCommandsNET.WriteDoubles(address,values,progressChangedEventHandler)
        
    def WriteIntegerGlobal(self,RegNumber:int, Value:float):  # Provides access to the global integer variable (self,register) set.
        self._RegisterCommandsNET.WriteIntegerGlobal(RegNumber,Value)
        
    @multimethod
    def WriteIntegers(self,address:int, values:list[int]):  # Writes multiple values to IntegerRegisters 
        self._RegisterCommandsNET.WriteIntegers(address,values)
        
    @multimethod
    def WriteIntegers(self,address:int, values:list[int], progressChangedEventHandler:ProgressChangedEventHandler):  # Writes multiple values to IntegerRegisters  
        self._RegisterCommandsNET.WriteIntegers(address,values,progressChangedEventHandler)
    
class RootCommands(CommandCategory):
    _RootCommandsNET=None
    def __init__(self,RootCommandsNET:AerotechEnsembleCommandsNET.RootCommands):
        self._RootCommandsNET=RootCommandsNET
        CommandCategory.__init__(RootCommandsNET)

    def AcknowledgeAll(self):  # Acknowledges all axis faults and clears all task errors.
        self._RootCommandsNET.AcknowledgeAll()
        
    @property
    def Advanced(self):  # Contains the Advanced Commands
        return AdvancedCommands(self._RootCommandsNET.Advanced)
    
    @property
    def Axes(self):  # Allows execution of commands by selecting a set of axes to operate on
        return AxesSelectionCommands(self._RootCommandsNET.Axes)
    
    @property
    def DataAcquisition(self):  # Contains the DataAcquisition Commands
        return DataAcquisitionCommands(self._RootCommandsNET.DataAcquisition)

    def Execute(self,code:str):  # Executes an immediate command 
        return self._RootCommandsNET.Execute(code)
    
    def ExecuteAsync(self,code:str):  # Executes an immediate command asynchronously 
        return self._RootCommandsNET.ExecuteAsync(code)
    
    @property
    def IO(self):  # Contains the IO Commands
        return IOCommands(self._RootCommandsNET.IO)
    
    @property
    def Motion(self):  # Contains the Motion Commands
        return MotionCommands(self._RootCommandsNET.Motion)

    @property
    def PSO(self):  # Contains the PSO Commands
        return PSOCommands(self._RootCommandsNET.PSO)
    
    @property
    def Register(self):  # Contains the Register Commands
        return RegisterCommands(self._RootCommandsNET.Register)
    
    @property
    def Status(self):  # Contains the Status Commands
        return StatusCommands(self._RootCommandsNET.Status)
    
    @property
    def Tuning(self):  # Contains the Tuning Commands 
        return TuningCommands(self._RootCommandsNET.Tuning) 
  
class StatusCommands(CommandCategory):
    _StatusCommandsNET=None
    def __init__(self,StatusCommandsNET=AerotechEnsembleCommandsNET.StatusCommands):
        self._StatusCommandsNET=StatusCommandsNET
        CommandCategory.__init__(self,StatusCommandsNET)

    def EtherStatus(self):  # Gets the Ethernet status.
        return EthernetStatus(self._StatusCommandsNET.EtherStatus())

    def GetMode(self,ModeType:ModeType):  # Gets the setting of one of the modal variables. 
        return self._StatusCommandsNET.GetMode(ModeType.value)
    
    @multimethod
    def PositionMarkerLatched(self,Axis:int):  # Gets the position feedback latched when the marker signal occurred during a home.
        return self._StatusCommandsNET.PositionMarkerLatched(Axis)
    
    @multimethod
    def PositionMarkerLatched(self,Axis:str):  # Gets the position feedback latched when the marker signal occurred during a home.
        return self._StatusCommandsNET.PositionMarkerLatched(Axis)
 
class TuningCommands(CommandCategory):
    _TuningCommandsNET=None
    def __init__(self,TuningCommandsNET=AerotechEnsembleCommandsNET.TuningCommands):
        self._TuningCommandsNET=TuningCommandsNET
        CommandCategory.__init__(self,TuningCommandsNET)

    @multimethod
    def LoopTrans(self,Axis:int, Mode:LoopTransmissionMode, Amplitude:float, Frequency:float, Type:LoopTransmissionType):  # Initiates loop transmission mode.
        self._TuningCommandsNET.LoopTrans(Axis, Mode.value, Amplitude, Frequency, Type.value)
    
    @multimethod
    def LoopTrans(self,Axis:str, Mode:LoopTransmissionMode, Amplitude:float, Frequency:float, Type:LoopTransmissionType):  # Initiates loop transmission mode.
        self._TuningCommandsNET.LoopTrans(Axis, Mode.value, Amplitude, Frequency, Type.value)
        
    @multimethod
    def MComm(self,Axis:int, Current:float):  # Sends a direct current command to the servo loop.
        self._TuningCommandsNET.MComm(Axis,Current)
        
    @multimethod
    def MComm(self,Axis:str, Current:float):  # Sends a direct current command to the servo loop.
        self._TuningCommandsNET.MComm(Axis,Current)
        
    @multimethod
    def MSet(self,Axis:int, Current:float, Angle:int):  # Generates an open-loop current command.
        self._TuningCommandsNET.MSet(Axis,Current, Angle)
        
    @multimethod
    def MSet(self,Axis:str, Current:float, Angle:int):  # Generates an open-loop current command.
        self._TuningCommandsNET.MSet(Axis,Current, Angle)
        
    @multimethod
    def Oscillate(self,Axis:int, Distance:float, Frequency:float, Cycles:int):  # Generates sinusoidal oscillation on an axis.
        self._TuningCommandsNET.Oscillate(Axis,Distance,Frequency,Cycles)
        
    @multimethod
    def Oscillate(self,Axis:str, Distance:float, Frequency:float, Cycles:int):  # Generates sinusoidal oscillation on an axis.
        self._TuningCommandsNET.Oscillate(Axis,Distance,Frequency,Cycles)
        
    @multimethod
    def Oscillate(self,Axis:int, Distance:float, Frequency:float, Cycles:int, NumFreqs:int):  # Generates sinusoidal oscillation on an axis.
        self._TuningCommandsNET.Oscillate(Axis,Distance,Frequency,Cycles, NumFreqs)
        
    @multimethod
    def Oscillate(self,Axis:str, Distance:float, Frequency:float, Cycles:int, NumFreqs:int):  # Generates sinusoidal oscillation on an axis.
        self._TuningCommandsNET.Oscillate(Axis,Distance,Frequency,Cycles, NumFreqs)
        
    @multimethod
    def SetGain(self,Axis:int, GainKp:float, GainKi:float, GainKpos:float, GainAff:float):  # Sets four or nine servo loop gains at the same time.
        self._TuningCommandsNET.SetGain(Axis,GainKp,GainKi,GainKpos,GainAff)
        
    @multimethod
    def SetGain(self,Axis:str, GainKp:float, GainKi:float, GainKpos:float, GainAff:float):  # Sets four or nine servo loop gains at the same time.
        self._TuningCommandsNET.SetGain(Axis,GainKp,GainKi,GainKpos,GainAff)
        
    @multimethod
    def SetGain(self,Axis:int, GainKp:float,GainKi:float,GainKpos:float,GainAff:float,GainKd1:float,GainKpi:float,GainKp1:float, GainVff:float,GainPff:float):  # Sets four or nine servo loop gains at the same time.
        self._TuningCommandsNET.SetGain(Axis,GainKp,GainKi,GainKpos,GainAff,GainKd1,GainKpi,GainKp1,GainVff,GainPff)
        
    @multimethod
    def SetGain(self,Axis:str, GainKp:float,GainKi:float,GainKpos:float,GainAff:float,GainKd1:float,GainKpi:float,GainKp1:float, GainVff:float,GainPff:float):  # Sets four or nine servo loop gains at the same time.
        self._TuningCommandsNET.SetGain(Axis,GainKp,GainKi,GainKpos,GainAff,GainKd1,GainKpi,GainKp1,GainVff,GainPff)
        
        
        

