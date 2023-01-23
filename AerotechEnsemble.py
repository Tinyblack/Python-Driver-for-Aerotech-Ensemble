import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import pythonnet
import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32,Enum,Decimal,Double

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

from GlobalLogger import GlobalLogger

import time

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


class AerotechEnsemble():
    defaultPath:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
    controllerDllName:str='Aerotech.Ensemble'
    controllerDllVersion:str=''
    controllerNET=None
    controllerAxes=None
    controllerAxisX=Axis()
    controllerAxisY=Axis()
    controllerAxisZ=Axis()
    
    logger=GlobalLogger.logger_init()
    
    def __init__(self):
        pass
    
    def enableAxes(self,*axes):
        self.controllerAxes.Select(axes).Motion.Enable()

    def enableAxis(self,axis):
        axis.Motion.Enable()

    def moveAxesRelative(self,*axes,distance,speed,wait):
        self.controllerAxes.Select(axes).Motion.Linear(distance,speed)

    def moveAxisRelative(self,axis,distance,speed,wait):
        axis.Motion.Linear([distance],speed)


    
    def moveAxisAbsolute(self):
        pass
    
    def moveAxesAbsolute(self):
        pass
    
    def getAxisPosition(self):
        pass
    
    def getAxesPosition(self):
        pass
    
    def getAxisCurrent(self):
        pass
    
    def getAxesCurrent(self):
        pass

    def updateStatus(self):
        _data=self.controllerNET.DataCollection.RetrieveDiagnostics()
        self.controllerAxisX.status.updateStatus(_data.get_Item("X"))
        self.controllerAxisY.status.updateStatus(_data.get_Item("Y"))
        self.controllerAxisZ.status.updateStatus(_data.get_Item("Z"))
    

    @classmethod
    def connect(cls,index:int=0,libraryPath:str=defaultPath):
        if libraryPath.upper() not in [path.upper() for path in sys.path]:
            sys.path.extend(libraryPath)
            
        try:
            clr.AddReference(cls.controllerDllName)
            from Aerotech.Ensemble import Controller
            Controller.Connect()
            cls.controllerNET=Controller.ConnectedControllers[index]
            cls.controllerAxes=cls.controllerNET.Commands.Axes
            cls.controllerAxisX.axisNET=cls.controllerAxes[0]
            cls.controllerAxisY.axisNET=cls.controllerAxes[1]
            cls.controllerAxisZ.axisNET=cls.controllerAxes[2]
            cls.driverVersion=cls.getVersionNumber(os.path.join(libraryPath,cls.controllerDllName + '.dll'))
            cls.logger.info(f'|{cls.__name__}| Aerotech Ensemble Driver Successfully Loaded.')
            cls.logger.info(f'|{cls.__name__}| Aerotech Ensemble Driver version: {cls.driverVersion}.')
        except:
            cls.logger.error(f'|{cls.__name__}| Unable to load Aerotech Ensemble Driver.')

        return cls()
            
    @staticmethod
    def getVersionNumber(filename):
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return ".".join([str(HIWORD (ms)), str(LOWORD (ms)), str(HIWORD (ls)), str(LOWORD (ls))])
            
if __name__=='__main__':
    stage=AerotechEnsemble.connect()
    #stage.enableAxis(stage.controllerAxisX)
    #stage.enableAxis(stage.controllerAxisY)
    #stage.enableAxis(stage.controllerAxisZ)
    stage.enableAxes("X","Y","Z")
    stage.moveAxesRelative("X","Y","Z",distance=[0.1,0.1,0.1],speed=1,wait=True)
    #stage.moveAxisRelative(stage.controllerAxisX.axisNET,distance=10,speed=0.1,wait=True)
    stage.updateStatus()
    print(stage.controllerAxisX.status.toString())
    a=1