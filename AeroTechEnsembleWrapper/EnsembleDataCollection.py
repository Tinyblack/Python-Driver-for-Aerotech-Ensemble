import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

from enum import Enum
from aenum import extend_enum

import clr
clr.AddReference('System')
from System.ComponentModel import ProgressChangedEventHandler

import Common
import CommonCollections
import Ensemble
import EnsembleCommands 
import EnsembleCommunication 
import EnsembleConfiguration  
import EnsembleDataCollection
import EnsembleExceptions
import EnsembleFileSystem
import EnsembleFirmware
import EnsembleInformation
import EnsembleParameters
import EnsembleStatus
import EnsembleTasks
import EnsembleTasksDebug

from multimethod import multimethod

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.DataCollection as AerotechEnsembleDataCollectionNET
except:
    raise RuntimeError

class OptionalDataNumber(Enum):  # Specifies the number of the optional data source 
    Optional1=AerotechEnsembleDataCollectionNET.OptionalDataNumber.Optional1  # The first optional output 
    Optional2=AerotechEnsembleDataCollectionNET.OptionalDataNumber.Optional2  # The second optional output  

class OptionalDataSource(Enum):  # Optional items for a specific axis
    EncoderSine=AerotechEnsembleDataCollectionNET.OptionalDataSource.EncoderSine  # Encoder Sine
    EncoderCosine=AerotechEnsembleDataCollectionNET.OptionalDataSource.EncoderCosine  # Encoder Cosine
    LoopTransmissionBefore=AerotechEnsembleDataCollectionNET.OptionalDataSource.LoopTransmissionBefore  # Loop Transmission Before
    LoopTransmissionAfter=AerotechEnsembleDataCollectionNET.OptionalDataSource.LoopTransmissionAfter  # Loop Transmission After
    AmplifierTemperature=AerotechEnsembleDataCollectionNET.OptionalDataSource.AmplifierTemperature  # Amplifier Temperature
    AnalogInput2=AerotechEnsembleDataCollectionNET.OptionalDataSource.AnalogInput2  # Analog Input 2
    AnalogInput3=AerotechEnsembleDataCollectionNET.OptionalDataSource.AnalogInput3  # Analog Input 3
    AnalogOutput2=AerotechEnsembleDataCollectionNET.OptionalDataSource.AnalogOutput2  # Analog Output 2
    AnalogOutput3=AerotechEnsembleDataCollectionNET.OptionalDataSource.AnalogOutput3  # Analog Output 3
    PSOStatus=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOStatus  # PSO Status
    PSOCounter1=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOCounter1  # PSO Counter 1
    PSOCounter2=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOCounter2  # PSO Counter 2
    PSOCounter3=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOCounter3  # PSO Counter 3
    PSOWindow1=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOWindow1  # PSO Window 1
    PSOWindow2=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOWindow2  # PSO Window 2
    DataAcquisitionSamples=AerotechEnsembleDataCollectionNET.OptionalDataSource.DataAcquisitionSamples  # Data Acquisition Samples
    PhaseACurrentFeedback=AerotechEnsembleDataCollectionNET.OptionalDataSource.PhaseACurrentFeedback  # Phase A Current Feedback
    PhaseBCurrentFeedback=AerotechEnsembleDataCollectionNET.OptionalDataSource.PhaseBCurrentFeedback  # Phase B Current Feedback
    PositionCalibrationAll=AerotechEnsembleDataCollectionNET.OptionalDataSource.PositionCalibrationAll  # Position Calibration All
    ResolverChannel1=AerotechEnsembleDataCollectionNET.OptionalDataSource.ResolverChannel1  # Resolver Channel 1
    ResolverChannel2=AerotechEnsembleDataCollectionNET.OptionalDataSource.ResolverChannel2  # Resolver Channel 2
    EnDatAbsolutePosition=AerotechEnsembleDataCollectionNET.OptionalDataSource.EnDatAbsolutePosition  # EnDat Absolute Position
    DriveTimer=AerotechEnsembleDataCollectionNET.OptionalDataSource.DriveTimer  # Drive Timer
    PhaseAVoltageCommand=AerotechEnsembleDataCollectionNET.OptionalDataSource.PhaseAVoltageCommand  # Phase A Voltage Command
    PhaseBVoltageCommand=AerotechEnsembleDataCollectionNET.OptionalDataSource.PhaseBVoltageCommand  # Phase B Voltage Command
    PhaseCVoltageCommand=AerotechEnsembleDataCollectionNET.OptionalDataSource.PhaseCVoltageCommand  # Phase C Voltage Command
    AmplifierPeakCurrent=AerotechEnsembleDataCollectionNET.OptionalDataSource.AmplifierPeakCurrent  # Amplifier Peak Current
    FPGAVersion=AerotechEnsembleDataCollectionNET.OptionalDataSource.FPGAVersion  # FPGA Version
    DriveTypeID=AerotechEnsembleDataCollectionNET.OptionalDataSource.DriveTypeID  # Drive Type ID
    PSOWindow1ArrayIndex=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOWindow1ArrayIndex  # PSO Window 1 Array Index
    PSOWindow2ArrayIndex=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOWindow2ArrayIndex  # PSO Window 2 Array Index
    PSODistanceArrayIndex=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSODistanceArrayIndex  # PSO Distance Array Index
    PSOBitArrayIndex=AerotechEnsembleDataCollectionNET.OptionalDataSource.PSOBitArrayIndex  # PSO Bit Array Index
    MXAbsolutePosition=AerotechEnsembleDataCollectionNET.OptionalDataSource.MXAbsolutePosition  # MX Absolute Position
    ServoUpdateRate=AerotechEnsembleDataCollectionNET.OptionalDataSource.ServoUpdateRate  # Servo Update Rate
    FirmwareVersionMajor=AerotechEnsembleDataCollectionNET.OptionalDataSource.FirmwareVersionMajor  # Firmware Version Major
    FirmwareVersionMinor=AerotechEnsembleDataCollectionNET.OptionalDataSource.FirmwareVersionMinor  # Firmware Version Minor
    FirmwareVersionPatc=AerotechEnsembleDataCollectionNET.OptionalDataSource.FirmwareVersionPatc  # Firmware Version Patch
    FirmwareVersionBuild=AerotechEnsembleDataCollectionNET.OptionalDataSource.FirmwareVersionBuild  # Firmware Version Build
    DriveTimerMax=AerotechEnsembleDataCollectionNET.OptionalDataSource.DriveTimerMax  # Drive Timer Max
    MarkerSearchDistance=AerotechEnsembleDataCollectionNET.OptionalDataSource.MarkerSearchDistance  # Marker Search Distance
    LatchedMarkerPosition=AerotechEnsembleDataCollectionNET.OptionalDataSource.LatchedMarkerPosition  # atched Marker Position
    EthernetDebuggingInformation=AerotechEnsembleDataCollectionNET.OptionalDataSource.EthernetDebuggingInformation # Ethernet Debugging Information
    ResoluteAbsolutePosition=AerotechEnsembleDataCollectionNET.OptionalDataSource.ResoluteAbsolutePosition  # Resolute Absolute Position
    FaultPositionFeedback=AerotechEnsembleDataCollectionNET.OptionalDataSource.FaultPositionFeedback  # Fault Position Feedback
    MotorCommutationAngle=AerotechEnsembleDataCollectionNET.OptionalDataSource.MotorCommutationAngle # Motor Commutation Angle
    AnalogOutput4=AerotechEnsembleDataCollectionNET.OptionalDataSource.AnalogOutput4  # Analog Output 4
    PiezoVoltageFeedback=AerotechEnsembleDataCollectionNET.OptionalDataSource.PiezoVoltageFeedback  # Piezo Voltage Feedback
    PiezoVoltageCommand=AerotechEnsembleDataCollectionNET.OptionalDataSource.PiezoVoltageCommand  # Piezo Voltage Command
    ProgramPositionCommand=AerotechEnsembleDataCollectionNET.OptionalDataSource.ProgramPositionCommand  # Program Position Command
    ProgramPositionFeedback=AerotechEnsembleDataCollectionNET.OptionalDataSource.ProgramPositionFeedback  # Program Position Feedback
    IOBoardInstalled=AerotechEnsembleDataCollectionNET.OptionalDataSource.IOBoardInstalled  # I/O Board Installed
    MaximumVoltage=AerotechEnsembleDataCollectionNET.OptionalDataSource.MaximumVoltage  # Maximum Voltage
    BusVoltage=AerotechEnsembleDataCollectionNET.OptionalDataSource.BusVoltage  # Bus Voltage
    FlashConfigStatus=AerotechEnsembleDataCollectionNET.OptionalDataSource.FlashConfigStatus  # Flash Config Status
    TimeSinceReset=AerotechEnsembleDataCollectionNET.OptionalDataSource.TimeSinceReset  # Time Since Reset
    CommandOutputType=AerotechEnsembleDataCollectionNET.OptionalDataSource.CommandOutputType  # Command Output Type
    DriveFeedforwardCurrent=AerotechEnsembleDataCollectionNET.OptionalDataSource.DriveFeedforwardCurrent  # Drive Feedforward Current
    StringDisplayHeight=AerotechEnsembleDataCollectionNET.OptionalDataSource.StringDisplayHeight  # String Display Height
    StringDisplayWidth=AerotechEnsembleDataCollectionNET.OptionalDataSource.StringDisplayWidth  # String Display Width
    BoardRevision=AerotechEnsembleDataCollectionNET.OptionalDataSource.BoardRevision  # Board Revision
    FirmwareRevision=AerotechEnsembleDataCollectionNET.OptionalDataSource.FirmwareRevision  # Firmware Revision
    PositionCommandRaw=AerotechEnsembleDataCollectionNET.OptionalDataSource.PositionCommandRaw  # Position Command Raw
    CapacitanceSensorRawPosition=AerotechEnsembleDataCollectionNET.OptionalDataSource.CapacitanceSensorRawPosition  # Capacitance Sensor Raw Position
    AccuracyCorrectionStartingPosition=AerotechEnsembleDataCollectionNET.OptionalDataSource.AccuracyCorrectionStartingPosition  # Accuracy Correction Starting Position
    AccuracyCorrectionEndingPosition=AerotechEnsembleDataCollectionNET.OptionalDataSource.AccuracyCorrectionEndingPosition  # Accuracy Correction Ending Position 

class OptionalMemoryDataSource(Enum):  # Optional items for a specific axis
    Integer=AerotechEnsembleDataCollectionNET.OptionalMemoryDataSource.Integer  # Drive Memory Integer
    Float=AerotechEnsembleDataCollectionNET.OptionalMemoryDataSource.Float  # Drive Memory Float
    Double=AerotechEnsembleDataCollectionNET.OptionalMemoryDataSource.Double  # Drive Memory Double
    Byte=AerotechEnsembleDataCollectionNET.OptionalMemoryDataSource.Byte  # Drive Memory Integer
    Short=AerotechEnsembleDataCollectionNET.OptionalMemoryDataSource.Short  # Drive Memory Integer 
extend_enum(OptionalMemoryDataSource,'None',getattr(AerotechEnsembleDataCollectionNET.OptionalMemoryDataSource,'None'))

class ScopeTrigId(Enum):  # Specifies the known scope trig application Ids 
    Default=AerotechEnsembleDataCollectionNET.ScopeTrigId.Default  # No application Id was specified
    DigitalScope=AerotechEnsembleDataCollectionNET.ScopeTrigId.DigitalScope  # Digital Scope was specified
    MotionDesigner=AerotechEnsembleDataCollectionNET.ScopeTrigId.MotionDesigner  # Motion Designer was specified
    MotionSimulator=AerotechEnsembleDataCollectionNET.ScopeTrigId.MotionSimulator  # Motion Simulator was specified 

class AxesData():  # Retrieves data for all the axes 
    _AxesDataNET=None
    def __init__(self,AxesDataNET=AerotechEnsembleDataCollectionNET.AxesData):
        self._AxesDataNET=AxesDataNET 
    
    @property
    def AnalogInput(self):  # Provides access to retrieving Analog Input 
 
    @property
    def AnalogOutput(self):  # Provides access to retrieving Analog Output 
 
    @property
    def AxisFault(self):  # Provides access to retrieving Axis Fault 
 
    @property
    def AxisStatus(self):  # Provides access to retrieving Axis Status 
 
    @property
    def Command(self):  # Provides access to retrieving Position, Velocity, and Acceleration Commands 
 
    @property
    def CurrentCommand(self):  # Provides access to retrieving Current Command 
 
    @property
    def CurrentFeedback(self):  # Provides access to retrieving Current Feedback 
 
    @property
    def DigitalInput(self):  # Provides access to retrieving Digital Input 
 
    @property
    def DigitalOutput(self):  # Provides access to retrieving Digital Output 
 
    @property
    def OptionalData(self):  # Provides access to retrieving Optional Data 
 
    @property
    def PositionFeedbackAuxiliary(self):  # Provides access to retrieving Position Feedback Auxiliary 
 
    @property
    def ProgramCounter(self):  # Provides access to retrieving Program Counter 
 
    def Retrieve(self)  Waits for all the data to be collected, then retrieves all data for all axes 
    
    def Retrieve(self,Int32)  Waits for all the data to be collected, then retrieves all data for all axes 
    
    def Retrieve(self,Int32, ProgressChangedEventHandler)  Waits for all the data to be collected, then retrieves all data for all axes 
 

class AxesDataContainer():  # A container of some data for several axes 

class AxesDataResults():  # Contains collected data for all axes 

class AxesOptionalRetriever():  # Allows retrieval of Optional Data for several axes 

class AxisAnalogInputData():  # Stores analog input #0 and #1 data 
    _AxisAnalogInputDataNET=None
    def __init__(self,AxisAnalogInputDataNET=AerotechEnsembleDataCollectionNET.AxisAnalogInputData):
        self._AxisAnalogInputDataNET=AxisAnalogInputDataNET 
    
    @property
    def Input0(self):  # Analog Input #0 
        return self._AxisAnalogInputDataNET.Input0
    
    @property
    def Input1(self):  # Analog Input #1 
        return self._AxisAnalogInputDataNET.Input1
    
class AxisAnalogOutputData():  # Stores analog output #0 and #1 data 
    _AxisAnalogOutputDataNET=None
    def __init__(self,AxisAnalogOutputDataNET=AerotechEnsembleDataCollectionNET.AxisAnalogOutputData):
        self._AxisAnalogOutputDataNET=AxisAnalogOutputDataNET 
    
    @property
    def Output0(self):  # Analog Output #0 
        return self._AxisAnalogOutputDataNET.Output0
    
    @property
    def Output1(self):  # Analog Output #1 
        return self._AxisAnalogOutputDataNET.Output1
    

class AxisCommandData():  # Contains position, velocity, and acceleration command data 
    _AxisCommandDataNET=None
    def __init__(self,AxisCommandDataNET=AerotechEnsembleDataCollectionNET.AxisCommandData):
        self._AxisCommandDataNET=AxisCommandDataNET 
    
    @property
    def Acceleration(self):  # The acceleration command of the axis, in user units 
        return self._AxisCommandDataNET.Acceleration
    
    @property
    def AccelerationCounts(self):  # The acceleration command of the axis, in counts 
        return self._AxisCommandDataNET.AccelerationCounts
    
    @property
    def Position(self):  # The position command of the axis, in user units 
        return self._AxisCommandDataNET.osition
    
    @property
    def PositionCounts(self):  # The position command of the axis, in counts 
        return self._AxisCommandDataNET.PositionCounts
    
    @property
    def Velocity(self):  # The velocity command of the axis, in user units 
        return self._AxisCommandDataNET.Velocity
    
    @property
    def VelocityCounts(self):  # The velocity command of the axis, in counts  
        return self._AxisCommandDataNET.VelocityCounts

class AxisDataResults():  # Contains collected data for an axis 
    _AxisDataResultsNET=None
    def __init__(self,AxisDataResultsNET=AerotechEnsembleDataCollectionNET.AxisDataResults):
        self._AxisDataResultsNET=AxisDataResultsNET 
    
    @property
    def AnalogInput(self):  # Gets the analog input #0 and #1 for the axis 
        return AxisAnalogInputData(self._AxisDataResultsNET.AnalogInput)
    
    @property
    def AnalogOutput(self):  # Gets the analog output #0 and #1 for the axis 
        return AxisAnalogInputData(self._AxisDataResultsNET.AnalogOutput)
    
    @property
    def AxisFault(self):  # Gets the fault for the axis 
        return EnsembleStatus.AxisFault(self._AxisDataResultsNET.AxisFault)
    
    @property
    def AxisStatus(self):  # Gets the status for the axis 
        return EnsembleStatus.AxisStatus(self._AxisDataResultsNET.AxisStatus)
    
    @property
    def CollectionPeriod(self):  # The collection period used to collect the data, in seconds 
        return self._AxisDataResultsNET.CollectionPeriod
    
    @property
    def Command(self):  # Gets the position, velocity, and acceleration command 
        return AxisCommandData(self._AxisDataResultsNET.Command)
    
    @property
    def Count(self):  # The number of points collected 
        return self._AxisDataResultsNET.Count
    
    @property
    def CurrentCommand(self):  # Gets the current command for the axis 
        return self._AxisDataResultsNET.CurrentCommand
    
    @property
    def CurrentError(self):  # Gets the current error for the axis 
        return self._AxisDataResultsNET.CurrentError
    
    @property
    def CurrentFeedback(self):  # Gets the current feedback for the axis 
        return self._AxisDataResultsNET.CurrentFeedback
    
    @property
    def DigitalInput(self):  # Gets the digital inputs #0, #1, and #2 for the axis 
        return AxisDigitalInputData(self._AxisDataResultsNET.DigitalInput)
    
    @property
    def DigitalOutput(self):  # Gets the digital outputs #0, #1, and #2 for the axis 
        return AxisDigitalOutputData(self._AxisDataResultsNET.DigitalOutput)
    
    @property
    def OptionalData1(self):  # Gets the optinoal data #1 for the axis 
        return self._AxisDataResultsNET.OptionalData1
    
    @property
    def OptionalData2(self):  # Gets the optional data #2 for the axis 
        return self._AxisDataResultsNET.OptionalData2
    
    @property
    def PositionError(self):  # Gets the position error for the axis, in user units 
        return self._AxisDataResultsNET.PositionError
    
    @property
    def PositionErrorCounts(self):  # Gets the position error for the axis, in counts 
        return self._AxisDataResultsNET.PositionErrorCounts
    
    @property
    def PositionFeedbackAuxiliary(self):  # Gets the position feedback auxiliary for the axis 
        return self._AxisDataResultsNET.PositionFeedbackAuxiliary
    
    @property
    def VelocityError(self):  # Gets the velocity error for the axis, in user units 
        return self._AxisDataResultsNET.VelocityError
    
    @property
    def VelocityErrorCounts(self):  # Gets the velocity error for the axis, in counts  
        return self._AxisDataResultsNET.VelocityErrorCounts
    

class AxisDigitalInputData():  # Stores digital input #0, #1, and #2 data 
    _AxisDigitalInputDataNET=None
    def __init__(self,AxisDigitalInputDataNET=AerotechEnsembleDataCollectionNET.AxisDigitalInputData):
        self._AxisDigitalInputDataNET=AxisDigitalInputDataNET 
    
    @property
    def Input0(self):  # Digital Input #0 
        return self._AxisDigitalInputDataNET.Input0
    
    @property
    def Input1(self):  # Digital Input #1 
        return self._AxisDigitalInputDataNET.Input1
    
    @property
    def Input2(self):  # Digital Input #2  
        return self._AxisDigitalInputDataNET.Input2
    
class AxisDigitalOutputData():  # Stores digital output #0, #1, and #2 data 
    _AxisDigitalOutputDataNET=None
    def __init__(self,AxisDigitalOutputDataNET=AerotechEnsembleDataCollectionNET.AxisDigitalOutputData):
        self._AxisDigitalOutputDataNET=AxisDigitalOutputDataNET 
    
    @property
    def Output0(self):  # Digital output #0 
        return self._AxisDigitalOutputDataNET.Output0
    
    @property
    def Output1(self):  # Digital output #1 
        return self._AxisDigitalOutputDataNET.Output1
    
    @property
    def Output2(self):  # Digital output #2  
        return self._AxisDigitalOutputDataNET.Output2

class AxisFeedbackData():  # Stores the position and velocity feedback data 
    
    _AxisFeedbackDataNET=None
    def __init__(self,AxisFeedbackDataNET=AerotechEnsembleDataCollectionNET.AxisFeedbackData):
        self._AxisFeedbackDataNET=AxisFeedbackDataNET 
    
    @property
    def Position(self):  # The position feedback of the axis, in user units 
        return self._AxisFeedbackDataNET.Position
 
    @property
    def PositionCounts(self):  # The position feedback of the axis, in counts  
        return self._AxisFeedbackDataNET.PositionCounts
    
    @property
    def Velocity(self):  # The velocity feedback of the axis, in user units 
        return self._AxisFeedbackDataNET.Velocity
 
    @property
    def VelocityCounts(self):  # The velocity feedback of the axis, in counts  
        return self._AxisFeedbackDataNET.VelocityCounts


class ControllerDataResults():  # Contains collected data for the controller
    _ControllerDataResultsNET=None
    def __init__(self,ControllerDataResultsNET=AerotechEnsembleDataCollectionNET.ControllerDataResults):
        self._ControllerDataResultsNET=ControllerDataResultsNET 
    
    @property
    def Axes(self):  # Contains data for the axes 
        return AxesDataResults(self._ControllerDataResultsNET.Axes)
 
    @property
    def CollectionPeriod(self):  # Gives the collection period of the data, in seconds 
        return self._ControllerDataResultsNET.CollectionPeriod
 
    @property
    def Count(self):  # Returns the number of points collected
        return self._ControllerDataResultsNET.Count
        
    @property
    def ProgramCounter(self):  # Retreives the program counter data  
        return self._ControllerDataResultsNET.ProgramCounter
    

class ControllerProgramCounterRetriever():  # Allows retrieval of Program Counter for the master 
    _ControllerProgramCounterRetrieverNET=None
    def __init__(self,ControllerProgramCounterRetrieverNET=AerotechEnsembleDataCollectionNET.ControllerProgramCounterRetriever):
        self._ControllerProgramCounterRetrieverNET=ControllerProgramCounterRetrieverNET
    
    def Retrieve(self):  # Waits for all the Program Counter data to be collected, then retrieves it 
        self._ControllerProgramCounterRetrieverNET.Retrieve()
        
    def Retrieve(self,pointsToRetrieve:int):  # Waits for the specified number of Program Counter data points to be collected, then retrieves it 
        self._ControllerProgramCounterRetrieverNET.Retrieve(pointsToRetrieve)
        
    def Retrieve(self,pointsToRetrieve:int, collectionPeriod:float):  # Waits for the specified number of Program Counter data points to be collected, then retrieves it 
        self._ControllerProgramCounterRetrieverNET.Retrieve(pointsToRetrieve,collectionPeriod)
        
    def Retrieve(self,pointsToRetrieve:int, collectionPeriod:float, progressChangedEventHandler:ProgressChangedEventHandler):  # Waits for the specified number of Program Counter data points to be collected, then retrieves it  
        self._ControllerProgramCounterRetrieverNET.Retrieve(pointsToRetrieve,collectionPeriod,progressChangedEventHandler)

class Data(AxesData):  # Provides access to all the data of the controller
    _DataNET=None
    def __init__(self,DataNET=AerotechEnsembleDataCollectionNET.Data):
        self._DataNET=DataNET
        super(AxesData,self).__init__(self._DataNET)
    
    @property
    def PointsAllocated(self):   # Specifies the maximum number of points to collect  
        return AerotechEnsembleDataCollectionNET.PointsAllocated
    
    @multimethod
    def RetrieveDiagnostics(self,previous:EnsembleStatus.ControllerDiagPacket):   # Retrieves diagnostic information for the controller 
        AerotechEnsembleDataCollectionNET.RetrieveDiagnostics(previous.value)
    
    @multimethod 
    def RetrieveDiagnostics(self):  # Retrieves diagnostic information for the controller 
        AerotechEnsembleDataCollectionNET.RetrieveDiagnostics()
        
    @multimethod
    def RetrieveDiagnostics(self,allInfo:bool):   # Retrieves diagnostic information for the controller 
        AerotechEnsembleDataCollectionNET.RetrieveDiagnostics(allInfo)
 
    def StartCollection(self,period:float):   # Starts the data collection at a specified rate
        AerotechEnsembleDataCollectionNET.StartCollection(period)
 
    @property
    def Status(self):  # Provides the current status of data collection
        return DataCollectionStatus(AerotechEnsembleDataCollectionNET.Status)
        
    def Stop(self):  # Stops the current data collection
        AerotechEnsembleDataCollectionNET.Stop()
    
    @property
    def TaskCollection(self):  # Specifies the task for which to collect the program position 
        return Ensemble.TaskId[AerotechEnsembleDataCollectionNET.TaskCollection.ToString()]
 
    @multimethod 
    def WaitForData(points:int):  # Waits for a specific amount of data points to be collected 
        AerotechEnsembleDataCollectionNET.TaskCollection.WaitForData(points)
        
    @multimethod 
    def WaitForData(points:int, waiter:ProgressChangedEventHandler):  # Waits for a specific amount of data points to be collected  
        AerotechEnsembleDataCollectionNET.TaskCollection.WaitForData(points,waiter)

class DataCollectionStatus():  # Contains status of data collection
    _DataCollectionStatusNET=None
    def __init__(self,DataCollectionStatusNET=AerotechEnsembleDataCollectionNET.DataCollectionStatus):
        self._DataCollectionStatusNET=DataCollectionStatusNET
    
    @property
    def IsScopeTrigInitiated(self):  # Whether the collection was started by a scopetrig command 
        return self._DataCollectionStatusNET.IsScopeTrigInitiated
        
    @property
    def PointsAllocated(self):  # Specifies the maximum number of points to collect 
        return self._DataCollectionStatusNET.PointsAllocated
        
    @property
    def PointsCollected(self):  # The number of points currently collected 
        return self._DataCollectionStatusNET.PointsCollected
        
    @property
    def ScopeTrigId(self):  # The Id with which ScopeTrig was initiated 
        return ScopeTrigId[self._DataCollectionStatusNET.ScopeTrigId.ToString()]

# class IDataRetriever():  # Retrieves some specific data from the Controller 

