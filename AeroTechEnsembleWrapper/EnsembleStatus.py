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
