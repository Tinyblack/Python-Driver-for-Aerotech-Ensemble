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
    import Aerotech.Ensemble as AerotechEnsembleNET
    import Aerotech.Ensemble.Commands as AerotechEnsembleCommandsNET
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
    DataInTransmitter=AerotechEnsembleCommandsNET.EthernetStatus.DataInTransmitter
    DataInReceiver=AerotechEnsembleCommandsNET.EthernetStatus.DataInReceiver

class IOCommands():
    def __init__(self):
        pass
    
class LoopTransmissionMode():
    Off=AerotechEnsembleCommandsNET.LoopTransmissionMode.Off
    Sinusoid=AerotechEnsembleCommandsNET.LoopTransmissionMode.Sinusoid
    SinusoidGantry=AerotechEnsembleCommandsNET.LoopTransmissionMode.SinusoidGantry
    WhiteNoise=AerotechEnsembleCommandsNET.LoopTransmissionMode.WhiteNoise
    WhiteNoiseGantry=AerotechEnsembleCommandsNET.LoopTransmissionMode.WhiteNoiseGantry

class LoopTransmissionType():
    OpenLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.OpenLoop
    ClosedLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.ClosedLoop
    CurrentLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.CurrentLoop
    AFOpenLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.AFOpenLoop
    AFClosedLoop=AerotechEnsembleCommandsNET.LoopTransmissionType.AFClosedLoop


class ModeType():
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
    
class MotionAdvancedCommands():
    _ControllerNET=None
    def __init__(self,controller:AerotechEnsembleNET.Controller):
        self._ControllerNET=controller
        
    @multimethod
    def MoveOutLim(self,Axis:int):
        self._ControllerNET.Commands.Motion.Advanced.MoveOutLim(Axis)
    
    @multimethod
    def MoveOutLim(self,Axis:str):
        self._ControllerNET.Commands.Motion.Advanced.MoveOutLim(Axis)
    
    @multimethod
    def MoveToLimCCW(self,Axis:int):
        self._ControllerNET.Commands.Motion.Advanced.MoveToLimCCW(Axis)
    
    @multimethod
    def MoveToLimCCW(self,Axis:str):
        self._ControllerNET.Commands.Motion.Advanced.MoveToLimCCW(Axis)

    @multimethod
    def MoveToLimCW(self,Axis:int):
        self._ControllerNET.Commands.Motion.Advanced.MoveToLimCW(Axis)
    
    @multimethod
    def MoveToLimCW(self,Axis:str):
        self._ControllerNET.Commands.Motion.Advanced.MoveToLimCW(Axis)

class MotionCommands():
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
    
class MotionSetupCommands():
    def __init__(self,controller:AerotechEnsembleNET.Controller):
        self._ControllerNET=controller
    
class OnOff():
    Off=AerotechEnsembleCommandsNET.OnOff.Off
    On=AerotechEnsembleCommandsNET.OnOff.On

class PSOCommands():
    def __init__(self):
        pass
    
class PsoMode():
    Reset=AerotechEnsembleCommandsNET.PsoMode.Reset
    Off=AerotechEnsembleCommandsNET.PsoMode.Off
    Arm=AerotechEnsembleCommandsNET.PsoMode.Arm
    Fire=AerotechEnsembleCommandsNET.PsoMode.Fire
    On=AerotechEnsembleCommandsNET.PsoMode.On
    FireContinuous=AerotechEnsembleCommandsNET.PsoMode.FireContinuous

class RampMode():
    Dist=AerotechEnsembleCommandsNET.RampMode.Dist
    Rate=AerotechEnsembleCommandsNET.RampMode.Rate
    Time=AerotechEnsembleCommandsNET.RampMode.Time

class RampType():
    Linear=AerotechEnsembleCommandsNET.RampType.Linear
    Scurve=AerotechEnsembleCommandsNET.RampType.Scurve
    Sine=AerotechEnsembleCommandsNET.RampType.Sine

class RegisterCommands():
    def __init__(self):
        pass
    
class RegisterType():
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

class RootCommands():
    _ControllerNET=None
    def __init__(self,controller:AerotechEnsembleNET.Controller):
        self._ControllerNET=controller
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
        return MotionCommands(self._ControllerNET)
 
    def AcknowledgeAll(self):
        self._ControllerNET.Commands.AcknowledgeAll()
        
    def Execute(self,code:str):
        self._ControllerNET.Commands.Execute(code)
 
    def ExecuteAsync(self,code:str):
        self._ControllerNET.Commands.ExecuteAsync(code)
    
class Semaphores():
    ModbusRegisters=AerotechEnsembleCommandsNET.Semaphores.ModbusRegisters
    GlobalIntegers=AerotechEnsembleCommandsNET.Semaphores.GlobalIntegers
    GlobalDoubles=AerotechEnsembleCommandsNET.Semaphores.GlobalDoubles 

class StatusCommands():
    def __init__(self):
        pass
    
class TuningCommands():
    def __init__(self):
        pass
    
class WaitOption():
    InPosition=AerotechEnsembleCommandsNET.WaitOption.InPosition
    MoveDone=AerotechEnsembleCommandsNET.WaitOption.MoveDone

class WaitType():
    NoWait=AerotechEnsembleCommandsNET.WaitType.NoWait
    MoveDone=AerotechEnsembleCommandsNET.WaitType.MoveDone
    InPos=AerotechEnsembleCommandsNET.WaitType.InPos