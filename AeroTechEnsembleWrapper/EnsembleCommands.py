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

import CommonCollections

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