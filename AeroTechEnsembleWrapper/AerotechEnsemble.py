import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32,Enum,Decimal,Double

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

from GlobalLogger import GlobalLogger

import time

from multimethod import multimethod

from collections.abc import Sequence


DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    from Aerotech.Ensemble import Controller,AxisMask,ServoRateParameter,SoftwareEnvironment,TaskId 
    from Aerotech.Ensemble.Commands import OnOff, WaitOption ,WaitType, EthernetStatus,LoopTransmissionMode,LoopTransmissionType,ModeType,PsoMode,RampMode,RampType,RegisterType,Semaphores
except:
    raise RuntimeError
    
class AdvancedAnalogCommands():
    def __init__(self):
        pass

class AdvancedCommands():
    def __init__(self):
        pass

class AxesIOCommands():
    def __init__(self):
        pass

class AxesMotionCommands():
    def __init__(self):
        pass

class AxesMotionSetupCommands():
    def __init__(self):
        pass

class AxesRootCommands():
    def __init__(self):
        pass

class AxesSelectionCommands():
    def __init__(self):
        pass

class CommandCategory():
    def __init__(self):
        pass

class DataAcquisitionCommands():
    def __init__(self):
        pass

class EthernetStatus():
    DataInTransmitter=EthernetStatus.DataInTransmitter
    DataInReceiver=EthernetStatus.DataInReceiver

class IOCommands():
    def __init__(self):
        pass
    
class LoopTransmissionMode():
    Off=LoopTransmissionMode.Off
    Sinusoid=LoopTransmissionMode.Sinusoid
    SinusoidGantry=LoopTransmissionMode.SinusoidGantry
    WhiteNoise=LoopTransmissionMode.WhiteNoise
    WhiteNoiseGantry=LoopTransmissionMode.WhiteNoiseGantry

class LoopTransmissionType():
    OpenLoop=LoopTransmissionType.OpenLoop
    ClosedLoop=LoopTransmissionType.ClosedLoop
    CurrentLoop=LoopTransmissionType.CurrentLoop
    AFOpenLoop=LoopTransmissionType.AFOpenLoop
    AFClosedLoop=LoopTransmissionType.AFClosedLoop


class ModeType():
    MotionMode=ModeType.MotionMode
    WaitMode=ModeType.WaitMode
    RampMode=ModeType.RampMode
    VelocityMode=ModeType.RampMode
    ScurveValue=ModeType.ScurveValue
    TimeScaleValue=ModeType.TimeScaleValue
    DefaultVelocityValue=ModeType.DefaultVelocityValue
    AccelRateValue=ModeType.AccelRateValue
    AccelTimeValue=ModeType.AccelTimeValue
    AccelDistValue=ModeType.AccelDistValue
    DecelRateValue=ModeType.DecelRateValue
    DecelTimeValue=ModeType.DecelTimeValue
    DecelDistValue=ModeType.DecelDistValue
    Plane=ModeType.Plane
    
class MotionAdvancedCommands():
    def __init__(self,controller:Controller):
        self.controller=controller
    
class MotionCommands():
    _Advanced=None
    _Setup=None
    
    def __init__(self,controller:Controller):
        self.controller=controller
        self._Advanced=MotionAdvancedCommands(controller)
        self._Setup=MotionSetupCommands(controller)

    # ! Abort
    @multimethod  
    def Abort(self,axis:int):
        self.controller.Commands.Montion.Abort(axis)

    @multimethod
    def Abort(self,axes:list[int]):
        self.controller.Commands.Montion.Abort(axes)
        
    @multimethod
    def Abort(self,axis:str):
        self.controller.Commands.Montion.Abort(axis)
        
    @multimethod
    def Abort(self,axes:list[str]):
        self.controller.Commands.Montion.Abort(axes)
    
    @multimethod
    def Abort(self,AxisMask:AxisMask):
        self.controller.Commands.Montion.Abort(AxisMask)
        
    @property
    def Advanced(self):
        return self._Advanced
        
    # ! AutoFocus
    @multimethod
    def AutoFocus(self,axis:int, OnOff:OnOff): 
        self.controller.Commands.Motion.AutoFocus(axis,OnOff)
        
    @multimethod
    def AutoFocus(self,axes:list[int], OnOff:OnOff): 
        self.controller.Commands.Motion.AutoFocus(axes,OnOff)
    
    @multimethod
    def AutoFocus(self,axis:str, OnOff:OnOff):
        self.controller.Commands.Motion.AutoFocus(axis,OnOff)
    
    @multimethod
    def AutoFocus(self,axes:list[str], OnOff:OnOff):
        self.controller.Commands.Motion.AutoFocus(axes,OnOff)
    
    @multimethod
    def AutoFocus(self,AxisMask:AxisMask, OnOff:OnOff):
        self.controller.Commands.Motion.AutoFocus(AxisMask,OnOff)
        
    # ! BlockMotion 
    @multimethod
    def BlockMotion(self,axis:int, OnOff:OnOff): 
        self.controller.Commands.Motion.BlockMotion(axis,OnOff)
        
    @multimethod
    def BlockMotion(self,axes:list[int], OnOff:OnOff): 
        self.controller.Commands.Motion.BlockMotion(axes,OnOff)
    
    @multimethod
    def BlockMotion(self,axis:str, OnOff:OnOff):
        self.controller.Commands.Motion.BlockMotion(axis,OnOff)
    
    @multimethod
    def BlockMotion(self,axes:list[str], OnOff:OnOff):
        self.controller.Commands.Motion.BlockMotion(axes,OnOff)
    
    @multimethod
    def BlockMotion(self,AxisMask:AxisMask, OnOff:OnOff):
        self.controller.Commands.Motion.BlockMotion(AxisMask,OnOff)
        
    # ! CCWCenter
    @multimethod
    def CCWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float):
        self.controller.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CCWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float):
        self.controller.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CCWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
    @multimethod
    def CCWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CCWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
        
    # ! CCWRadius
    @multimethod
    def CCWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float):
        self.controller.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CCWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float):
        self.controller.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CCWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
    @multimethod
    def CCWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CCWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
        
    # ! CWCenter
    @multimethod
    def CWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float):
        self.controller.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float):
        self.controller.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center)
    @multimethod
    def CWCenter(self,axis1:int, axis1End:float, axis2:int, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
    @multimethod
    def CWCenter(self,axis1:str, axis1End:float, axis2:str, axis2End:float, axis1Center:float, axis2Center:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CWCenter(axis1, axis1End, axis2, axis2End, axis1Center, axis2Center,coordinatedSpeed)
        
    # ! CWRadius
    @multimethod
    def CWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float):
        self.controller.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float):
        self.controller.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius)
    @multimethod
    def CWRadius(self,axis1:int, axis1End:float, axis2:int, axis2End:float, radius:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed)
    @multimethod
    def CWRadius(self,axis1:str, axis1End:float, axis2:str, axis2End:float, radius:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.CWRadius(axis1, axis1End, axis2, axis2End, radius,coordinatedSpeed) 

    # ! Disable
    @multimethod
    def Disable(self,axis:int): 
        self.controller.Commands.Motion.Disable(axis)
        
    @multimethod
    def Disable(self,axes:list[int]): 
        self.controller.Commands.Motion.Disable(axes)
    
    @multimethod
    def Disable(self,axis:str):
        self.controller.Commands.Motion.Disable(axis)
    
    @multimethod
    def Disable(self,axes:list[str]):
        self.controller.Commands.Motion.Disable(axes)
    
    @multimethod
    def Disable(self,AxisMask:AxisMask):
        self.controller.Commands.Motion.Disable(AxisMask)

    # ! Enable
    @multimethod
    def Enable(self,axis:int): 
        self.controller.Commands.Motion.Enable(axis)
        
    @multimethod
    def Enable(self,axes:list[int]): 
        self.controller.Commands.Motion.Enable(axes)
    
    @multimethod
    def Enable(self,axis:str):
        self.controller.Commands.Motion.Enable(axis)
    
    @multimethod
    def Enable(self,axes:list[str]):
        self.controller.Commands.Motion.Enable(axes)
    
    @multimethod
    def Enable(self,AxisMask:AxisMask):
        self.controller.Commands.Motion.Enable(AxisMask)
        
    # ! FaultAck
    @multimethod
    def FaultAck(self,axis:int): 
        self.controller.Commands.Motion.FaultAck(axis)
        
    @multimethod
    def FaultAck(self,axes:list[int]): 
        self.controller.Commands.Motion.FaultAck(axes)
    
    @multimethod
    def FaultAck(self,axis:str):
        self.controller.Commands.Motion.FaultAck(axis)
    
    @multimethod
    def FaultAck(self,axes:list[str]):
        self.controller.Commands.Motion.FaultAck(axes)
    
    @multimethod
    def FaultAck(self,AxisMask:AxisMask):
        self.controller.Commands.Motion.FaultAck(AxisMask)
        
    # ! FreeRun
    @multimethod
    def FreeRun(self,axis:int,speed:float): 
        self.controller.Commands.Motion.FreeRun(axis,speed)
        
    @multimethod
    def FreeRun(self,axes:list[int],speed:list[float]): 
        self.controller.Commands.Motion.FreeRun(axes,speed)
    
    @multimethod
    def FreeRun(self,axis:str,speed:float):
        self.controller.Commands.Motion.FreeRun(axis,speed)
    
    @multimethod
    def FreeRun(self,axes:list[str],speed:list[float]):
        self.controller.Commands.Motion.FreeRun(axes,speed)
    
    @multimethod
    def FreeRun(self,AxisMask:AxisMask,speed:float):
        self.controller.Commands.Motion.FreeRun(AxisMask,speed)
        
    @multimethod
    def FreeRun(self,AxisMask:AxisMask,speed:list[float]):
        self.controller.Commands.Motion.FreeRun(AxisMask,speed)
        
    # ! FreeRunStop
    @multimethod
    def FreeRunStop(self,axis:int): 
        self.controller.Commands.Motion.FreeRunStop(axis)
        
    @multimethod
    def FreeRunStop(self,axes:list[int]): 
        self.controller.Commands.Motion.FreeRunStop(axes)
    
    @multimethod
    def FreeRunStop(self,axis:str):
        self.controller.Commands.Motion.FreeRunStop(axis)
    
    @multimethod
    def FreeRunStop(self,axes:list[str]):
        self.controller.Commands.Motion.FreeRunStop(axes)
    
    @multimethod
    def FreeRunStop(self,AxisMask:AxisMask):
        self.controller.Commands.Motion.FreeRunStop(AxisMask)
        
    # ! Home
    @multimethod
    def Home(self,axis:int): 
        self.controller.Commands.Motion.Home(axis)
        
    @multimethod
    def Home(self,axes:list[int]): 
        self.controller.Commands.Motion.Home(axes)
    
    @multimethod
    def Home(self,axis:str):
        self.controller.Commands.Motion.Home(axis)
    
    @multimethod
    def Home(self,axes:list[str]):
        self.controller.Commands.Motion.Home(axes)
    
    @multimethod
    def Home(self,AxisMask:AxisMask):
        self.controller.Commands.Motion.Home(AxisMask)
            
    # ! HomeConditional
    @multimethod
    def HomeConditional(self,axis:int): 
        self.controller.Commands.Motion.HomeConditional(axis)
        
    @multimethod
    def HomeConditional(self,axes:list[int]): 
        self.controller.Commands.Motion.HomeConditional(axes)
    
    @multimethod
    def HomeConditional(self,axis:str):
        self.controller.Commands.Motion.HomeConditional(axis)
    
    @multimethod
    def HomeConditional(self,axes:list[str]):
        self.controller.Commands.Motion.HomeConditional(axes)
    
    @multimethod
    def HomeConditional(self,AxisMask:AxisMask):
        self.controller.Commands.Motion.HomeConditional(AxisMask)
        
        
    # ! Linear
    @multimethod
    def Linear(self,axis:int,distance:float): 
        self.controller.Commands.Motion.Linear(axis,distance)
        
    @multimethod
    def Linear(self,axes:list[int],distance:list[float]): 
        self.controller.Commands.Motion.Linear(axes,distance)
    
    @multimethod
    def Linear(self,axis:str,distance:float):
        self.controller.Commands.Motion.Linear(axis,distance)
    
    @multimethod
    def Linear(self,axes:list[str],distance:list[float]):
        self.controller.Commands.Motion.Linear(axes,distance)
    
    @multimethod
    def Linear(self,AxisMask:AxisMask,distance:float):
        self.controller.Commands.Motion.Linear(AxisMask,distance)
        
    @multimethod
    def Linear(self,AxisMask:AxisMask,distance:list[float]):
        self.controller.Commands.Motion.Linear(AxisMask,distance)

    @multimethod
    def Linear(self,axis:int,distance:float,coordinatedSpeed:float): 
        self.controller.Commands.Motion.Linear(axis,distance,coordinatedSpeed)
        
    @multimethod
    def Linear(self,axes:list[int],distance:list[float],coordinatedSpeed:float): 
        self.controller.Commands.Motion.Linear(axes,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,axis:str,distance:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.Linear(axis,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,axes:list[str],distance:list[float],coordinatedSpeed:float):
        self.controller.Commands.Motion.Linear(axes,distance,coordinatedSpeed)
    
    @multimethod
    def Linear(self,AxisMask:AxisMask,distance:float,coordinatedSpeed:float):
        self.controller.Commands.Motion.Linear(AxisMask,distance,coordinatedSpeed)
        
    @multimethod
    def Linear(self,AxisMask:AxisMask,distance:list[float],coordinatedSpeed:float):
        self.controller.Commands.Motion.Linear(AxisMask,distance,coordinatedSpeed)
        
    # ! MoveAbs
    @multimethod
    def MoveAbs(self,axis:int,distance:float): 
        self.controller.Commands.Motion.MoveAbs(axis,distance)
        
    @multimethod
    def MoveAbs(self,axes:list[int],distance:list[float]): 
        self.controller.Commands.Motion.MoveAbs(axes,distance)
    
    @multimethod
    def MoveAbs(self,axis:str,distance:float):
        self.controller.Commands.Motion.MoveAbs(axis,distance)
    
    @multimethod
    def MoveAbs(self,axes:list[str],distance:list[float]):
        self.controller.Commands.Motion.MoveAbs(axes,distance)
    
    @multimethod
    def MoveAbs(self,AxisMask:AxisMask,distance:float):
        self.controller.Commands.Motion.MoveAbs(AxisMask,distance)
        
    @multimethod
    def MoveAbs(self,AxisMask:AxisMask,distance:list[float]):
        self.controller.Commands.Motion.MoveAbs(AxisMask,distance)

    @multimethod
    def MoveAbs(self,axis:int,distance:float,speed:float): 
        self.controller.Commands.Motion.MoveAbs(axis,distance,speed)
        
    @multimethod
    def MoveAbs(self,axes:list[int],distance:list[float],speed:float): 
        self.controller.Commands.Motion.MoveAbs(axes,distance,speed)
    
    @multimethod
    def MoveAbs(self,axis:str,distance:float,speed:float):
        self.controller.Commands.Motion.MoveAbs(axis,distance,speed)
    
    @multimethod
    def MoveAbs(self,axes:list[str],distance:list[float],speed:float):
        self.controller.Commands.Motion.MoveAbs(axes,distance,speed)
    
    @multimethod
    def MoveAbs(self,AxisMask:AxisMask,distance:float,speed:float):
        self.controller.Commands.Motion.MoveAbs(AxisMask,distance,speed)
        
    @multimethod
    def MoveAbs(self,AxisMask:AxisMask,distance:list[float],speed:float):
        self.controller.Commands.Motion.MoveAbs(AxisMask,distance,speed)
        
    # ! MoveInc
    @multimethod
    def MoveInc(self,axis:int,distance:float): 
        self.controller.Commands.Motion.MoveInc(axis,distance)
        
    @multimethod
    def MoveInc(self,axes:list[int],distance:list[float]): 
        self.controller.Commands.Motion.MoveInc(axes,distance)
    
    @multimethod
    def MoveInc(self,axis:str,distance:float):
        self.controller.Commands.Motion.MoveInc(axis,distance)
    
    @multimethod
    def MoveInc(self,axes:list[str],distance:list[float]):
        self.controller.Commands.Motion.MoveInc(axes,distance)
    
    @multimethod
    def MoveInc(self,AxisMask:AxisMask,distance:float):
        self.controller.Commands.Motion.MoveInc(AxisMask,distance)
        
    @multimethod
    def MoveInc(self,AxisMask:AxisMask,distance:list[float]):
        self.controller.Commands.Motion.MoveInc(AxisMask,distance)

    @multimethod
    def MoveInc(self,axis:int,distance:float,speed:float): 
        self.controller.Commands.Motion.MoveInc(axis,distance,speed)
        
    @multimethod
    def MoveInc(self,axes:list[int],distance:list[float],speed:float): 
        self.controller.Commands.Motion.MoveInc(axes,distance,speed)
    
    @multimethod
    def MoveInc(self,axis:str,distance:float,speed:float):
        self.controller.Commands.Motion.MoveInc(axis,distance,speed)
    
    @multimethod
    def MoveInc(self,axes:list[str],distance:list[float],speed:float):
        self.controller.Commands.Motion.MoveInc(axes,distance,speed)
    
    @multimethod
    def MoveInc(self,AxisMask:AxisMask,distance:float,speed:float):
        self.controller.Commands.Motion.MoveInc(AxisMask,distance,speed)
        
    @multimethod
    def MoveInc(self,AxisMask:AxisMask,distance:list[float],speed:float):
        self.controller.Commands.Motion.MoveInc(AxisMask,distance,speed)

    @property
    def Setup(self):
        return self._Setup

    def Start(self):
        self.controller.Commands.Start()
    
    # ! WaitForMotionDone 
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:int): 
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axis)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[int]): 
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axes)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:str):
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axis)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[str]):
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axes)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,AxisMask:AxisMask):
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,AxisMask)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:int,timeout:int): 
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axis,timeout)
        
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[int],timeout:int): 
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axes,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axis:str,timeout:int):
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axis,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,axes:list[str],timeout:int):
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,axes,timeout)
    
    @multimethod
    def WaitForMotionDone (self,waitOption:WaitOption,AxisMask:AxisMask,timeout:int):
        self.controller.Commands.Motion.WaitForMotionDone(waitOption,AxisMask,timeout)
        
    def WaitMode(self,type:WaitType):
        self.controller.Commands.Motion.WaitMode(type)
    
class MotionSetupCommands():
    def __init__(self,controller:Controller):
        self.controller=controller
    
class OnOff():
    Off=OnOff.Off
    On=OnOff.On

class PSOCommands():
    def __init__(self):
        pass
    
class PsoMode():
    Reset=PsoMode.Reset
    Off=PsoMode.Off
    Arm=PsoMode.Arm
    Fire=PsoMode.Fire
    On=PsoMode.On
    FireContinuous=PsoMode. FireContinuous

class RampMode():
    Dist=RampMode.Dist
    Rate=RampMode.Rate
    Time=RampMode.Time

class RampType():
    Linear=RampType.Linear
    Scurve=RampType.Scurve
    Sine=RampType.Sine

class RegisterCommands():
    def __init__(self):
        pass
    
class RegisterType():
    GlobalIntegers=RegisterType.GlobalIntegers
    GlobalDoubles=RegisterType.GlobalDoubles
    ConversionRegisters=RegisterType.ConversionRegisters
    ModbusMasterInputWords=RegisterType.ModbusMasterInputWords
    ModbusMasterOutputWords=RegisterType.ModbusMasterOutputWords
    ModbusMasterInputBits=RegisterType.ModbusMasterInputBits
    ModbusMasterOutputBits=RegisterType.ModbusMasterOutputBits
    ModbusMasterStatusWords=RegisterType.ModbusMasterStatusWords
    ModbusMasterStatusBits=RegisterType.ModbusMasterStatusBits
    ModbusMasterVirtualInputs=RegisterType.ModbusMasterVirtualInputs 
    ModbusMasterVirtualOutputs=RegisterType.ModbusMasterVirtualOutputs
    ModbusSlaveInputWords=RegisterType.ModbusSlaveInputWords
    ModbusSlaveOutputWords=RegisterType.ModbusSlaveOutputWords
    ModbusSlaveInputBits=RegisterType.ModbusSlaveInputBits
    ModbusSlaveOutputBits=RegisterType.ModbusSlaveOutputBits

class RootCommands():
    def __init__(self,controller:Controller):
        self.controller=controller
        #self.Motion=MotionCommands(controller)
        #self.Advanced=AdvancedCommands(controller)
        #self.Axes=AxesSelectionCommands(controller)
        #self.DataAcquisition=DataAcquisitionCommands(controller)
        #self.IO=IOCommands(controller)
        #self.PSO=PSOCommands(controller)
        #self.Register=RegisterCommands(controller)
        #self.Status=StatusCommands(controller)
        #self.Tuning=TuningCommands(controller)
    
    @property
    def Motion(self):
        return MotionCommands(self.controller)
 
    def AcknowledgeAll(self):
        self.controller.Commands.AcknowledgeAll()
        
    def Execute(self,code:str):
        self.controller.Commands.Execute(code)
 
    def ExecuteAsync(self,code:str):
        self.controller.Commands.ExecuteAsync(code)
    
class Semaphores():
    ModbusRegisters=Semaphores.ModbusRegisters
    GlobalIntegers=Semaphores.GlobalIntegers
    GlobalDoubles=Semaphores.GlobalDoubles 

class StatusCommands():
    def __init__(self):
        pass
    
class TuningCommands():
    def __init__(self):
        pass
    
class WaitOption():
    InPosition=WaitOption.InPosition
    MoveDone=WaitOption.MoveDone

class WaitType():
    NoWait=WaitType.NoWait
    MoveDone=WaitType.MoveDone
    InPos=WaitType.InPos
       
class AxisDiagPacket():
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

class Axis():
    def __init__(self):
        self.status=AxisDiagPacket()
        self.axisNET=None
        
class AerotechCommonCollections():
    class INamedCollection(Sequence):
        def __init__(self,INamed):
            self.INamed=INamed
            super().__init__()

        def __getitem__(self, i):
            return AerotechEnsemble.Controller(self.INamed[i])
        
        def __len__(self):
            return len(self.INamed)

    class INamedConstantCollection(Sequence):
        def __init__(self,INamedConstant):
            self.INamedConstant=INamedConstant
            super().__init__()

        def __getitem__(self, i):
            return AerotechEnsemble.Controller(self.INamedConstant[i])
        
        def __len__(self):
            return len(self.INamedConstant)

    class INamedMaskableConstantCollection(Sequence):
        def __init__(self,INamedMaskableConstant):
            self.INamedMaskableConstant=INamedMaskableConstant
            super().__init__()

        def __getitem__(self, i):
            return AerotechEnsemble.Controller(self.INamedMaskableConstant[i])
        
        def __len__(self):
            return len(self.INamedMaskableConstant)

    class INamedMaskedConstantCollection(Sequence):
        def __init__(self,INamedMaskedConstant):
            self.INamedMaskedConstant=INamedMaskedConstant
            super().__init__()

        def __getitem__(self, i):
            return AerotechEnsemble.Controller(self.INamedMaskedConstant[i])
        
        def __len__(self):
            return len(self.INamedMaskedConstant)
    
class AerotechEnsemble():
    _Controller=None
    class AxisMask():
        NONE= getattr(AxisMask,'None')
        A0=AxisMask.A0
        A1=AxisMask.A1
        A2=AxisMask.A2
        A3=AxisMask.A3
        A4=AxisMask.A4
        A5=AxisMask.A5
        A6=AxisMask.A6
        A7=AxisMask.A7
        A8=AxisMask.A8
        A9=AxisMask.A9
        ALL=AxisMask.All
    
    class Controller():
        _Controller:Controller=None
        def __init__(self,controller:Controller):
            self._Controller=controller

        def ChangePassword(self,oldPassword:str,newPassword:str):
            self._Controller.ChangePassword(oldPassword,newPassword)

        @property
        def Commands(self):
            return RootCommands(self._Controller)

        @classmethod
        @property
        def Configuration(cls):
            return None

        @classmethod  
        @property
        def ConnectedControllers(cls):
            return AerotechCommonCollections.INamedConstantCollection(Controller.ConnectedControllers)

        @classmethod
        def Connect(cls):
            Controller.Connect()


        @property
        def ControlCenter(self):
            pass # To collections
        
        @property
        def DataCollection(self):
            pass # To collections
        
        @classmethod
        def Disconnect(cls):
            Controller.Connect()
            cls.ConnectedControllers=None
        
        def EnumerateAxes(self):
            self._Controller.EnumerateAxes()

        @property
        def FileManager(self):
            pass # To collections
        
        @classmethod
        def Identify(cls):
            pass

        @property
        def Information(self):
            pass # To collections
        
        @property
        def IsConnected(self):
            return self._Controller.IsConnected()

        #def IsConnectedChanged  Raised when IsConnected changes 

        #def INamed<(Of <<'(String>)>>)..::..Name
        
        @property
        def Parameters(self):
            pass # To collections

        @multimethod
        def Reset(self):
            self._Controller.Reset()
        
        @multimethod
        def Reset(self,restartPrograms:bool):
            self._Controller.Reset(restartPrograms)
            
        @property
        def Tasks(self):
            pass # To collections

    
    class ServoRateParameter():
        OnekHz=ServoRateParameter.OnekHz
        TwokHz=ServoRateParameter.TwokHz
        FourkHz=ServoRateParameter.FourkHz
        FivekHz=ServoRateParameter.FivekHz
        TenkHz=ServoRateParameter.TenkHz
        TwentykHz=ServoRateParameter.TwentykHz
        
    class TaskId():
        TLibrary=TaskId.TLibrary
        T01=TaskId.T01
        T02=TaskId.T02
        T03=TaskId.T03
        T04=TaskId.T04
        TAuxiliary=TaskId.TAuxiliary
        
    class SoftwareEnvironment():
        # @classmethod
        # @property
        # This is equivalent to [static public property] in a certain namespace

        @classmethod
        @property
        def BinDir(cls):
            return SoftwareEnvironment.BinDir 
        
        @classmethod
        @property
        def InstallDir(cls):
            return SoftwareEnvironment.InstallDir 
        
        @classmethod
        @property
        def IsLoaderRunning(cls):
            return SoftwareEnvironment.IsLoaderRunning 
        
        @classmethod
        @property
        def NumberOfProcesses(cls):
            return SoftwareEnvironment.NumberOfProcesses 
        
        @classmethod
        @property
        def ProductKey(cls):
            return SoftwareEnvironment.ProductKey 
        
        @classmethod
        @property
        def Version(cls):
            return SoftwareEnvironment.Version 
            
if __name__=='__main__':

    AerotechEnsemble.Controller.Connect()
    controller=AerotechEnsemble.Controller.ConnectedControllers[0]
    controller.Commands.Motion.Enable(0)
    controller.Commands.Motion.Enable("Y")
    controller.Commands.Motion.Enable(AerotechEnsemble.AxisMask.A2)

    controller.Commands.Motion.Home(0)
    controller.Commands.Motion.Home("Y")
    controller.Commands.Motion.Home(AerotechEnsemble.AxisMask.A2)

    controller.Commands.Motion.Disable(0)
    controller.Commands.Motion.Disable("Y")
    controller.Commands.Motion.Disable(AerotechEnsemble.AxisMask.A2)
    
    a=1