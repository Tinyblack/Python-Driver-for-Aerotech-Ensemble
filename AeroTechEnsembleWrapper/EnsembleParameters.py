import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System.ComponentModel import ProgressChangedEventHandler
from System.IO import FileInfo
from System import Version

from multimethod import multimethod
from enum import Enum
from aenum import extend_enum

import Ensemble
import EnsembleTasksDebug
import EnsembleStatus
import EnsembleFileSystem
import CommonCollections

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Parameters as AerotechEnsembleParametersNET
except:
    raise RuntimeError

# ! DONE
class AxisAutofocusLoopParameterCategory(ParameterCategory):  # Contains the Autofocus Loop Parameters
    _AxisAutofocusLoopParameterCategoryNET=None
    def __init__(self,AxisAutofocusLoopParameterCategoryNET=AerotechEnsembleParametersNET.AxisAutofocusLoopParameterCategory):
        self._AxisAutofocusLoopParameterCategoryNET=AxisAutofocusLoopParameterCategoryNET
        ParameterCategory.__init__(self,AxisAutofocusLoopParameterCategoryNET)
    
    @property
    def AutofocusDeadband(self): # Allows access to the AutofocusDeadband Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusDeadband,float)
    
    @property
    def AutofocusGainKi(self): # Allows access to the AutofocusGainKi Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusGainKi,float)
    
    @property
    def AutofocusGainKi2(self): # Allows access to the AutofocusGainKi2 Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusGainKi2,float)
    
    @property
    def AutofocusGainKp(self): # Allows access to the AutofocusGainKp Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusGainKp,float)
    
    @property
    def AutofocusHoldInput(self): # Allows access to the AutofocusHoldInput Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusHoldInput,int)
    
    @property
    def AutofocusInitialRampTime(self): # Allows access to the AutofocusInitialRampTime Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusInitialRampTime,int)
    
    @property
    def AutofocusInput(self): # Allows access to the AutofocusInput Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusInput,int)
    
    @property
    def AutofocusLimitHigh(self): # Allows access to the AutofocusLimitHigh Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusLimitHigh,float)
    
    @property
    def AutofocusLimitLow(self): # Allows access to the AutofocusLimitLow Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusLimitLow,float)   
    
    @property
    def AutofocusSetup(self): # Allows access to the AutofocusSetup Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusSetup,int)
    
    @property
    def AutofocusSpeedClamp(self): # Allows access to the AutofocusSpeedClamp Parameter
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusSpeedClamp,float) 
    
    @property
    def AutofocusTarget(self): # Allows access to the AutofocusTarget Parameter 
        return TypedParameter(self._AxisAutofocusLoopParameterCategoryNET.AutofocusTarget,float) 
    
# ! DONE
class AxisCurrentLoopParameterCategory(ParameterCategory):  # Contains the Current Loop Parameters
    _AxisCurrentLoopParameterCategoryNET=None
    def __init__(self,AxisCurrentLoopParameterCategoryNET=AerotechEnsembleParametersNET.AxisCurrentLoopParameterCategory):
        self._AxisCurrentLoopParameterCategoryNET=AerotechEnsembleParametersNET
        ParameterCategory.__init__(self,AxisCurrentLoopParameterCategoryNET)
 
    @property
    def AmplifierDeadtime(self): # Allows access to the AmplifierDeadtime Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.AmplifierDeadtime,float)
         
    @property
    def CurrentGainKi(self): # Allows access to the CurrentGainKi Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentGainKi,float)
    
    @property
    def CurrentGainKp(self): # Allows access to the CurrentGainKp Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentGainKp,float)
    
    @property
    def CurrentOffsetA(self): # Allows access to the CurrentOffsetA Parameter
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentOffsetA,float)
    
    @property
    def CurrentOffsetB(self): # Allows access to the CurrentOffsetB Parameter 
        return TypedParameter(self._AxisCurrentLoopParameterCategoryNET.CurrentOffsetB,float)

# ! DONE
class AxisDynamicControlsToolboxCommandShapingParameterCategory(ParameterCategory):  # Contains the Command Shaping Parameters
    _AxisDynamicControlsToolboxCommandShapingParameterCategoryNET=None
    def __init__(self,AxisDynamicControlsToolboxCommandShapingParameterCategoryNET=AerotechEnsembleParametersNET.AxisDynamicControlsToolboxCommandShapingParameterCategory):
        self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET=AerotechEnsembleParametersNET
        ParameterCategory.__init__(self,AxisDynamicControlsToolboxCommandShapingParameterCategoryNET)
        
    @property
    def CommandShaper0Damping(self): # Allows access to the CommandShaper0Damping Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaper0Damping,float)

    @property
    def CommandShaper0Frequency(self): # Allows access to the CommandShaper0Frequency Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaper0Frequency,float)

    @property
    def CommandShaper0Type(self): # Allows access to the CommandShaper0Type Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaper0Type,int)

    @property
    def CommandShaper1Damping(self): # Allows access to the CommandShaper1Damping Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaper1Damping,float)

    @property
    def CommandShaper1Frequency(self): # Allows access to the CommandShaper1Frequency Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaper1Frequency,float)

    @property
    def CommandShaper1Type(self): # Allows access to the CommandShaper1Type Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaper1Type,int)

    @property
    def CommandShaperCoeff00(self): # Allows access to the CommandShaperCoeff00 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff00,float)

    @property
    def CommandShaperCoeff01(self): # Allows access to the CommandShaperCoeff01 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff01,float)

    @property
    def CommandShaperCoeff02(self): # Allows access to the CommandShaperCoeff02 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff02,float)

    @property
    def CommandShaperCoeff03(self): # Allows access to the CommandShaperCoeff03 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff03,float)

    @property
    def CommandShaperCoeff04(self): # Allows access to the CommandShaperCoeff04 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff04,float)

    @property
    def CommandShaperCoeff05(self): # Allows access to the CommandShaperCoeff05 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff05,float)

    @property
    def CommandShaperCoeff06(self): # Allows access to the CommandShaperCoeff06 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff06,float)

    @property
    def CommandShaperCoeff07(self): # Allows access to the CommandShaperCoeff07 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff07,float)

    @property
    def CommandShaperCoeff08(self): # Allows access to the CommandShaperCoeff08 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff08,float)

    @property
    def CommandShaperCoeff09(self): # Allows access to the CommandShaperCoeff09 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff09,float)

    @property
    def CommandShaperCoeff10(self): # Allows access to the CommandShaperCoeff10 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff10,float)

    @property
    def CommandShaperCoeff11(self): # Allows access to the CommandShaperCoeff11 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff11,float)

    @property
    def CommandShaperCoeff12(self): # Allows access to the CommandShaperCoeff12 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff12,float)

    @property
    def CommandShaperCoeff13(self): # Allows access to the CommandShaperCoeff13 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff13,float)

    @property
    def CommandShaperCoeff14(self): # Allows access to the CommandShaperCoeff14 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff14,float)

    @property
    def CommandShaperCoeff15(self): # Allows access to the CommandShaperCoeff15 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperCoeff15,float)

    @property
    def CommandShaperSetup(self): # Allows access to the CommandShaperSetup Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaper0Damping,int)

    @property
    def CommandShaperTime00(self): # Allows access to the CommandShaperTime00 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime00,float)

    @property
    def CommandShaperTime01(self): # Allows access to the CommandShaperTime01 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime01,float)

    @property
    def CommandShaperTime02(self): # Allows access to the CommandShaperTime02 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime02,float)

    @property
    def CommandShaperTime03(self): # Allows access to the CommandShaperTime03 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime03,float)

    @property
    def CommandShaperTime04(self): # Allows access to the CommandShaperTime04 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime04,float)

    @property
    def CommandShaperTime05(self): # Allows access to the CommandShaperTime05 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime05,float)

    @property
    def CommandShaperTime06(self): # Allows access to the CommandShaperTime06 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime06,float)

    @property
    def CommandShaperTime07(self): # Allows access to the CommandShaperTime07 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime07,float)

    @property
    def CommandShaperTime08(self): # Allows access to the CommandShaperTime08 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime08,float)

    @property
    def CommandShaperTime09(self): # Allows access to the CommandShaperTime09 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime09,float)

    @property
    def CommandShaperTime10(self): # Allows access to the CommandShaperTime10 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime10,float)

    @property
    def CommandShaperTime11(self): # Allows access to the CommandShaperTime11 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime11,float)

    @property
    def CommandShaperTime12(self): # Allows access to the CommandShaperTime12 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime12,float)

    @property
    def CommandShaperTime13(self): # Allows access to the CommandShaperTime13 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime13,float)

    @property
    def CommandShaperTime14(self): # Allows access to the CommandShaperTime14 Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime14,float)

    @property
    def CommandShaperTime15(self): # Allows access to the CommandShaperTime15 Parameter 
        return TypedParameter(self._AxisDynamicControlsToolboxCommandShapingParameterCategoryNET.CommandShaperTime15,float)
    
# ! DONE
class AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategory(ParameterCategory):  # Contains the Dynamic Gain Scheduling Parameters
    _AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET=None
    def __init__(self,AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET=AerotechEnsembleParametersNET.AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategory):
        self._AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET=AerotechEnsembleParametersNET
        ParameterCategory.__init__(self,AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET)

    @property
    def DynamicGainKiScale(self): # Allows access to the DynamicGainKiScale Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET.DynamicGainKiScale,float)

    @property
    def DynamicGainKposScale(self): # Allows access to the DynamicGainKposScale Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET.DynamicGainKposScale,float)

    @property
    def DynamicGainKpScale(self): # Allows access to the DynamicGainKpScale Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET.DynamicGainKpScale,float)

    @property
    def DynamicScheduleSetup(self): # Allows access to the DynamicScheduleSetup Parameter 
        return TypedParameter(self._AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategoryNET.DynamicScheduleSetup,int)
    
# ! DONE
class AxisDynamicControlsToolboxHarmonicCancellationParameterCategory(ParameterCategory):  # Contains the Harmonic Cancellation Parameters
    _AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET=None
    def __init__(self,AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET=AerotechEnsembleParametersNET.AxisDynamicControlsToolboxHarmonicCancellationParameterCategory):
        self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET=AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET
        ParameterCategory.__init__(self,AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET)
        
    @property
    def HarmonicCancellation0Gain(self): # Allows access to the HarmonicCancellation0Gain Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation0Gain,float)
        
    @property
    def HarmonicCancellation0Period(self): # Allows access to the HarmonicCancellation0Period Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation0Period,float)
        
    @property
    def HarmonicCancellation0Phase(self): # Allows access to the HarmonicCancellation0Phase Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation0Phase,float)
        
    @property
    def HarmonicCancellation0Type(self): # Allows access to the HarmonicCancellation0Type Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation0Type,int)
        
    @property
    def HarmonicCancellation1Gain(self): # Allows access to the HarmonicCancellation1Gain Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation1Gain,float)
        
    @property
    def HarmonicCancellation1Period(self): # Allows access to the HarmonicCancellation1Period Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation1Period,float)
        
    @property
    def HarmonicCancellation1Phase(self): # Allows access to the HarmonicCancellation1Phase Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation1Phase,float)
        
    @property
    def HarmonicCancellation1Type(self): # Allows access to the HarmonicCancellation1Type Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation1Type,int)
        
    @property
    def HarmonicCancellation2Gain(self): # Allows access to the HarmonicCancellation2Gain Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation2Gain,float)
        
    @property
    def HarmonicCancellation2Period(self): # Allows access to the HarmonicCancellation2Period Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation2Period,float)
        
    @property
    def HarmonicCancellation2Phase(self): # Allows access to the HarmonicCancellation2Phase Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation2Phase,float)
        
    @property
    def HarmonicCancellation2Type(self): # Allows access to the HarmonicCancellation2Type Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation2Type,int)
        
    @property
    def HarmonicCancellation3Gain(self): # Allows access to the HarmonicCancellation3Gain Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation3Gain,float)
        
    @property
    def HarmonicCancellation3Period(self): # Allows access to the HarmonicCancellation3Period Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation3Period,float)
        
    @property
    def HarmonicCancellation3Phase(self): # Allows access to the HarmonicCancellation3Phase Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation3Phase,float)
        
    @property
    def HarmonicCancellation3Type(self): # Allows access to the HarmonicCancellation3Type Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation3Type,int)
        
    @property
    def HarmonicCancellation4Gain(self): # Allows access to the HarmonicCancellation4Gain Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation4Gain,float)
        
    @property
    def HarmonicCancellation4Period(self): # Allows access to the HarmonicCancellation4Period Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation4Period,float)
        
    @property
    def HarmonicCancellation4Phase(self): # Allows access to the HarmonicCancellation4Phase Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation4Phase,float)
        
    @property
    def HarmonicCancellation4Type(self): # Allows access to the HarmonicCancellation4Type Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellation4Type,int)
        
    @property
    def HarmonicCancellationSetup(self): # Allows access to the HarmonicCancellationSetup Parameter 
        return TypedParameter(self._AxisDynamicControlsToolboxHarmonicCancellationParameterCategoryNET.HarmonicCancellationSetup,int)

# ! DONE     
class AxisDynamicControlsToolboxParameterCategory(ParameterCategory):  # Contains the Dynamic Controls Toolbox Parameters
    _AxisDynamicControlsToolboxParameterCategoryNET=None
    def __init__(self,AxisDynamicControlsToolboxParameterCategoryNET=AerotechEnsembleParametersNET.AxisDynamicControlsToolboxParameterCategory):
        self._AxisDynamicControlsToolboxParameterCategoryNET=AxisDynamicControlsToolboxParameterCategoryNET
        ParameterCategory.__init__(self,AxisDynamicControlsToolboxParameterCategoryNET)
        
    @property
    def CommandShaping(self): # Contains the Command Shaping Parameters 
        return AxisDynamicControlsToolboxCommandShapingParameterCategory(self._AxisDynamicControlsToolboxParameterCategoryNET.CommandShaping)
    
    @property
    def DynamicGainScheduling(self): # Contains the Dynamic Gain Scheduling Parameters 
        return AxisDynamicControlsToolboxDynamicGainSchedulingParameterCategory(self._AxisDynamicControlsToolboxParameterCategoryNET.DynamicGainScheduling)
        
    @property
    def HarmonicCancellation(self): # Contains the Harmonic Cancellation Parameters 
        return AxisDynamicControlsToolboxHarmonicCancellationParameterCategory(self._AxisDynamicControlsToolboxParameterCategoryNET.HarmonicCancellation)
        
    @property
    def ThresholdGainScheduling(self): # Contains the Threshold Gain Scheduling Parameters 
        return AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategory(self._AxisDynamicControlsToolboxParameterCategoryNET.ThresholdGainScheduling)

# ! DONE      
class AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategory(ParameterCategory):  # Contains the Threshold Gain Scheduling Parameters
    _AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET=None
    def __init__(self,AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET=AerotechEnsembleParametersNET.AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategory):
        self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET=AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET
        ParameterCategory.__init__(self,AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET)
        
    @property
    def ThresholdRegion2High(self): # Allows access to the ThresholdRegion2High Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion2High,float)
    
    @property
    def ThresholdRegion2Low(self): # Allows access to the ThresholdRegion2Low Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion2Low,float)
    
    @property
    def ThresholdRegion3GainKi(self): # Allows access to the ThresholdRegion3GainKi Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion3GainKi,float)
    
    @property
    def ThresholdRegion3GainKp(self): # Allows access to the ThresholdRegion3GainKp Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion3GainKp,float)
    
    @property
    def ThresholdRegion3GainKpi(self): # Allows access to the ThresholdRegion3GainKpi Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion3GainKpi,float)
    
    @property
    def ThresholdRegion3GainKpos(self): # Allows access to the ThresholdRegion3GainKpos Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion3GainKpos,float)
    
    @property
    def ThresholdRegion4High(self): # Allows access to the ThresholdRegion4High Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion4High,float)
    
    @property
    def ThresholdRegion4Low(self): # Allows access to the ThresholdRegion4Low Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion4Low,float)
    
    @property
    def ThresholdRegion5GainKi(self): # Allows access to the ThresholdRegion5GainKi Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion5GainKi,float)
    
    @property
    def ThresholdRegion5GainKp(self): # Allows access to the ThresholdRegion5GainKp Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion5GainKp,float)
    
    @property
    def ThresholdRegion5GainKpi(self): # Allows access to the ThresholdRegion5GainKpi Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion5GainKpi,float)
    
    @property
    def ThresholdRegion5GainKpos(self): # Allows access to the ThresholdRegion5GainKpos Parameter
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdRegion5GainKpos,float)
    
    @property
    def ThresholdScheduleSetup(self): # Allows access to the ThresholdScheduleSetup Parameter 
        return TypedParameter(self._AxisDynamicControlsToolboxThresholdGainSchedulingParameterCategoryNET.ThresholdScheduleSetup,float)
    
# ! DONE     
class AxisEnhancedThroughputModuleParameterCategory(ParameterCategory):  # Contains the Enhanced Throughput Module Parameters
    _AxisEnhancedThroughputModuleParameterCategoryNET=None
    def __init__(self,AxisEnhancedThroughputModuleParameterCategoryNET=AerotechEnsembleParametersNET.AxisEnhancedThroughputModuleParameterCategory):
        self._AxisEnhancedThroughputModuleParameterCategoryNET=AxisEnhancedThroughputModuleParameterCategoryNET
        ParameterCategory.__init__(self,AxisEnhancedThroughputModuleParameterCategoryNET)
        
    @property
    def EnhancedThroughputChannel(self): # Allows access to the EnhancedThroughputChannel Parameter
        return TypedParameter(self._AxisEnhancedThroughputModuleParameterCategoryNET.EnhancedThroughputChannel,int)
 
    @property
    def EnhancedThroughputCurrentClamp(self): # Allows access to the EnhancedThroughputCurrentClamp Parameter
        return TypedParameter(self._AxisEnhancedThroughputModuleParameterCategoryNET.EnhancedThroughputCurrentClamp,float)
 
    @property
    def EnhancedThroughputGain(self): # Allows access to the EnhancedThroughputGain Parameter 
        return TypedParameter(self._AxisEnhancedThroughputModuleParameterCategoryNET.EnhancedThroughputGain,float)
        
# ! DONE
class AxisEnhancedTrackingControlParameterCategory(ParameterCategory):  # Contains the Enhanced Tracking Control Parameters
    _AxisEnhancedTrackingControlParameterCategoryNET=None
    def __init__(self,AxisEnhancedTrackingControlParameterCategoryNET=AerotechEnsembleParametersNET.AxisEnhancedTrackingControlParameterCategory):
        self._AxisEnhancedTrackingControlParameterCategoryNET=AxisEnhancedTrackingControlParameterCategoryNET
        ParameterCategory.__init__(self,AxisEnhancedTrackingControlParameterCategoryNET)
        
    @property
    def EnhancedTrackingBandwidth(self): # Allows access to the EnhancedTrackingBandwidth Parameter
        return TypedParameter(self._AxisEnhancedTrackingControlParameterCategoryNET.EnhancedTrackingBandwidth,float)
 
    @property
    def EnhancedTrackingScale(self): # Allows access to the EnhancedTrackingScale Parameter
        return TypedParameter(self._AxisEnhancedTrackingControlParameterCategoryNET.EnhancedTrackingScale,float)
    
    @property
    def EnhancedTrackingSetup(self): # Allows access to the EnhancedTrackingSetup Parameter 
        return TypedParameter(self._AxisEnhancedTrackingControlParameterCategoryNET.EnhancedTrackingSetup,int)
        
# ! DONE
class AxisFaultInputsParameterCategory(ParameterCategory):  # Contains the Inputs Parameters
    _AxisFaultInputsParameterCategoryNET=None
    def __init__(self,AxisFaultInputsParameterCategoryNET=AerotechEnsembleParametersNET.AxisFaultInputsParameterCategory):
        self._AxisFaultInputsParameterCategoryNET=AxisFaultInputsParameterCategoryNET
        ParameterCategory.__init__(self,AxisFaultInputsParameterCategoryNET)
        
    @property
    def ESTOPFaultInput(self): # Allows access to the ESTOPFaultInput Parameter
        return TypedParameter(self._AxisFaultInputsParameterCategoryNET.ESTOPFaultInput,int)
    
    @property
    def ExternalFaultAnalogInput(self): # Allows access to the ExternalFaultAnalogInput Parameter
        return TypedParameter(self._AxisFaultInputsParameterCategoryNET.ExternalFaultAnalogInput,int)
    
    @property
    def ExternalFaultDigitalInput(self): # Allows access to the ExternalFaultDigitalInput Parameter 
        return TypedParameter(self._AxisFaultInputsParameterCategoryNET.ExternalFaultDigitalInput,int)

# ! DONE
class AxisFaultOutputsParameterCategory(ParameterCategory):  # Contains the Outputs Parameters
    _AxisFaultOutputsParameterCategoryNET=None
    def __init__(self,AxisFaultOutputsParameterCategoryNET=AerotechEnsembleParametersNET.AxisFaultOutputsParameterCategory):
        self._AxisFaultOutputsParameterCategoryNET=AxisFaultOutputsParameterCategoryNET
        ParameterCategory.__init__(self,AxisFaultOutputsParameterCategoryNET)
        
    @property
    def FaultMaskOutput(self): # Allows access to the FaultMaskOutput Parameter
        return TypedParameter(self._AxisFaultOutputsParameterCategoryNET.FaultMaskOutput,int)
        
    @property
    def FaultOutputSetup(self): # Allows access to the FaultOutputSetup Parameter
        return TypedParameter(self._AxisFaultOutputsParameterCategoryNET.FaultOutputSetup,int)
        
    @property
    def FaultOutputState(self): # Allows access to the FaultOutputState Parameter 
        return TypedParameter(self._AxisFaultOutputsParameterCategoryNET.FaultOutputState,int)

# ! DONE
class AxisFaultParameterCategory(ParameterCategory):  # Contains the Fault Parameters
    _AxisFaultParameterCategoryNET=None
    def __init__(self,AxisFaultParameterCategoryNET=AerotechEnsembleParametersNET.AxisFaultParameterCategory):
        self._AxisFaultParameterCategoryNET=AxisFaultParameterCategoryNET
        ParameterCategory.__init__(self,AxisFaultParameterCategoryNET)
        
    @property
    def FaultAbortAxes(self): # Allows access to the FaultAbortAxes Parameter
        return TypedParameter(self._AxisFaultParameterCategoryNET.FaultAbortAxes,int)

    @property
    def FaultMask(self): # Allows access to the FaultMask Parameter
        return TypedParameter(self._AxisFaultParameterCategoryNET.FaultMask,int)
        
    @property
    def FaultMaskDecel(self): # Allows access to the FaultMaskDecel Parameter
        return TypedParameter(self._AxisFaultParameterCategoryNET.FaultMaskDecel,int)
        
    @property
    def FaultMaskDisable(self): # Allows access to the FaultMaskDisable Parameter
        return TypedParameter(self._AxisFaultParameterCategoryNET.FaultMaskDisable,int)
        
    @property
    def FaultMaskDisableDelay(self): # Allows access to the FaultMaskDisableDelay Parameter
        return TypedParameter(self._AxisFaultParameterCategoryNET.FaultMaskDisableDelay,int)
        
    @property
    def FaultSetup(self): # Allows access to the FaultSetup Parameter 
        return TypedParameter(self._AxisFaultParameterCategoryNET.FaultSetup,int)
        
    @property
    def Inputs(self): # Contains the Inputs Parameters 
        return AxisFaultInputsParameterCategory(self._AxisFaultParameterCategoryNET.Inputs)
        
    @property
    def Outputs(self): # Contains the Outputs Parameters
        return AxisFaultOutputsParameterCategory(self._AxisFaultParameterCategoryNET.Outputs)
        
    @property
    def Thresholds(self): # Contains the Thresholds Parameters 
        return AxisFaultThresholdsParameterCategory(self._AxisFaultParameterCategoryNET.Thresholds)
        
class AxisFaultThresholdsParameterCategory(ParameterCategory):  # Contains the Thresholds Parameters
    _AxisFaultThresholdsParameterCategoryNET=None
    def __init__(self,AxisFaultThresholdsParameterCategoryNET=AerotechEnsembleParametersNET.AxisFaultThresholdsParameterCategory):
        self._AxisFaultThresholdsParameterCategoryNET=AxisFaultThresholdsParameterCategoryNET
        ParameterCategory.__init__(self,AxisFaultThresholdsParameterCategoryNET)

    @property
    def AverageCurrentThreshold(self): # Allows access to the AverageCurrentThreshold Parameter
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.AverageCurrentThreshold,float)
        
    @property
    def AverageCurrentTime(self): # Allows access to the AverageCurrentTime Parameter 
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.AverageCurrentTime,int)
        
    @property
    def ExternalFaultThreshold(self): # Allows access to the ExternalFaultThreshold Parameter 
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.ExternalFaultThreshold,float)
        
    @property
    def MarkerSearchThreshold(self): # Allows access to the MarkerSearchThreshold Parameter 
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.MarkerSearchThreshold,float)
        
    @property
    def PositionErrorThreshold(self): # Allows access to the PositionErrorThreshold Parameter 
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.PositionErrorThreshold,float)
        
    @property
    def VelocityCommandThreshold(self): # Allows access to the VelocityCommandThreshold Parameter
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.VelocityCommandThreshold,float)
        
    @property
    def VelocityCommandThresholdBeforeHome(self): # Allows access to the VelocityCommandThresholdBeforeHome Parameter
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.VelocityCommandThresholdBeforeHome,float)
        
    @property
    def VelocityErrorThreshold(self): # Allows access to the VelocityErrorThreshold Parameter 
        return TypedParameter(self._AxisFaultThresholdsParameterCategoryNET.VelocityErrorThreshold,float)
    
        
class AxisFeedbackCapSensorParameterCategory(ParameterCategory):  # Contains the Cap Sensor Parameters
    _AxisFeedbackCapSensorParameterCategoryNET=None
    def __init__(self,AxisFeedbackCapSensorParameterCategoryNET=AerotechEnsembleParametersNET.AxisFeedbackCapSensorParameterCategory):
        self._AxisFeedbackCapSensorParameterCategoryNET=AxisFeedbackCapSensorParameterCategoryNET
        ParameterCategory.__init__(self,AxisFeedbackCapSensorParameterCategoryNET)
        
    @property
    def CapSensorFilterLength(self): # Allows access to the CapSensorFilterLength Parameter
        return TypedParameter(self._AxisFeedbackCapSensorParameterCategoryNET.CapSensorFilterLength,int)
        
    @property
    def CapSensorSetup(self): # Allows access to the CapSensorSetup Parameter
        return TypedParameter(self._AxisFeedbackCapSensorParameterCategoryNET.CapSensorSetup,int)
        
    @property
    def CapSensorThresholdHigh(self): # Allows access to the CapSensorThresholdHigh Parameter
        return TypedParameter(self._AxisFeedbackCapSensorParameterCategoryNET.CapSensorThresholdHigh,float)
        
    @property
    def CapSensorThresholdLow(self): # Allows access to the CapSensorThresholdLow Parameter 
        return TypedParameter(self._AxisFeedbackCapSensorParameterCategoryNET.CapSensorThresholdLow,float)
        
        
class AxisFeedbackEnDatEncoderParameterCategory(ParameterCategory):  # Contains the EnDat Encoder Parameters
    _AxisFeedbackEnDatEncoderParameterCategoryNET=None
    def __init__(self,AxisFeedbackEnDatEncoderParameterCategoryNET=AerotechEnsembleParametersNET.AxisFeedbackEnDatEncoderParameterCategory):
        self._AxisFeedbackEnDatEncoderParameterCategoryNET=AxisFeedbackEnDatEncoderParameterCategoryNET
        ParameterCategory.__init__(self,AxisFeedbackEnDatEncoderParameterCategoryNET)
        
    @property
    def EnDatEncoderIncrementalResolution(self): # Allows access to the EnDatEncoderIncrementalResolution Parameter
        return TypedParameter(self._AxisFeedbackEnDatEncoderParameterCategoryNET.EnDatEncoderIncrementalResolution,int)
    
    @property
    def EnDatEncoderResolution(self): # Allows access to the EnDatEncoderResolution Parameter
        return TypedParameter(self._AxisFeedbackEnDatEncoderParameterCategoryNET.EnDatEncoderResolution,int)
    
    @property
    def EnDatEncoderSetup(self): # Allows access to the EnDatEncoderSetup Parameter
        return TypedParameter(self._AxisFeedbackEnDatEncoderParameterCategoryNET.EnDatEncoderSetup,int)
    
    @property
    def EnDatEncoderTurns(self): # Allows access to the EnDatEncoderTurns Parameter 
        return TypedParameter(self._AxisFeedbackEnDatEncoderParameterCategoryNET.EnDatEncoderTurns,int)
        
class AxisFeedbackMultiplierParameterCategory(ParameterCategory):  # Contains the Multiplier Parameters
    _AxisFeedbackMultiplierParameterCategoryNET=None
    def __init__(self,AxisFeedbackMultiplierParameterCategoryNET=AerotechEnsembleParametersNET.AxisFeedbackMultiplierParameterCategory):
        self._AxisFeedbackMultiplierParameterCategoryNET=AxisFeedbackMultiplierParameterCategoryNET
        ParameterCategory.__init__(self,AxisFeedbackMultiplierParameterCategoryNET)
        
    @property
    def EmulatedQuadratureChannel(self): # Allows access to the EmulatedQuadratureChannel Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EmulatedQuadratureChannel,int)
    
    @property
    def EmulatedQuadratureDivider(self): # Allows access to the EmulatedQuadratureDivider Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EmulatedQuadratureDivider,float)
    
    @property
    def EncoderCosineGain(self): # Allows access to the EncoderCosineGain Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderCosineGain,int)
    
    @property
    def EncoderCosineOffset(self): # Allows access to the EncoderCosineOffset Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderCosineOffset,int)
    
    @property
    def EncoderMarkerAlignment(self): # Allows access to the EncoderMarkerAlignment Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderMarkerAlignment,int)
    
    @property
    def EncoderMultiplicationFactor(self): # Allows access to the EncoderMultiplicationFactor Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderMultiplicationFactor,float)
    
    @property
    def EncoderMultiplierSetup(self): # Allows access to the EncoderMultiplierSetup Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderMultiplierSetup,int)
    
    @property
    def EncoderPhase(self): # Allows access to the EncoderPhase Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderPhase,int)
    
    @property
    def EncoderRadiusThresholdHigh(self): # Allows access to the EncoderRadiusThresholdHigh Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderRadiusThresholdHigh,int)
    
    @property
    def EncoderRadiusThresholdLow(self): # Allows access to the EncoderRadiusThresholdLow Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderRadiusThresholdLow,int)
    
    @property
    def EncoderSineGain(self): # Allows access to the EncoderSineGain Parameter
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderSineGain,int)
    
    @property
    def EncoderSineOffset(self): # Allows access to the EncoderSineOffset Parameter 
        return TypedParameter(self._AxisFeedbackMultiplierParameterCategoryNET.EncoderSineOffset,int)
        
        
class AxisFeedbackParameterCategory(ParameterCategory):  # Contains the Feedback Parameters
    _AxisFeedbackParameterCategoryNET=None
    def __init__(self,AxisFeedbackParameterCategoryNET=AerotechEnsembleParametersNET.AxisFeedbackParameterCategory):
        self._AxisFeedbackParameterCategoryNET=AxisFeedbackParameterCategoryNET
        ParameterCategory.__init__(self,AxisFeedbackParameterCategoryNET)
        
    
    @property
    def AbsoluteFeedbackOffset(self): # Allows access to the AbsoluteFeedbackOffset Parameter

    @property
    def CapSensor(self): # Contains the Cap Sensor Parameters

    @property
    def EnDatEncoder(self): # Contains the EnDat Encoder Parameters

    @property
    def ExternalVelocityAverageTime(self): # Allows access to the ExternalVelocityAverageTime Parameter

    @property
    def FeedbackSetup(self): # Allows access to the FeedbackSetup Parameter

    @property
    def Multiplier(self): # Contains the Multiplier Parameters

    @property
    def PositionFeedbackChannel(self): # Allows access to the PositionFeedbackChannel Parameter

    @property
    def PositionFeedbackType(self): # Allows access to the PositionFeedbackType Parameter

    @property
    def ResoluteEncoder(self): # Contains the Resolute Encoder Parameters

    @property
    def Resolver(self): # Contains the Resolver Parameters

    @property
    def VelocityFeedbackChannel(self): # Allows access to the VelocityFeedbackChannel Parameter

    @property
    def VelocityFeedbackType(self): # Allows access to the VelocityFeedbackType Parameter 

        
        
class AxisFeedbackResoluteEncoderParameterCategory(ParameterCategory):  # Contains the Resolute Encoder Parameters
    _AxisFeedbackResoluteEncoderParameterCategoryNET=None
    def __init__(self,AxisFeedbackResoluteEncoderParameterCategoryNET=AerotechEnsembleParametersNET.AxisFeedbackResoluteEncoderParameterCategory):
        self._AxisFeedbackResoluteEncoderParameterCategoryNET=AxisFeedbackResoluteEncoderParameterCategoryNET
        ParameterCategory.__init__(self,AxisFeedbackResoluteEncoderParameterCategoryNET)
        
        
    @property
    def ResoluteEncoderResolution(self): # Allows access to the ResoluteEncoderResolution Parameter

    @property
    def ResoluteEncoderSetup(self): # Allows access to the ResoluteEncoderSetup Parameter

    @property
    def ResoluteEncoderUserResolution(self): # Allows access to the ResoluteEncoderUserResolution Parameter 

        
        
class AxisFeedbackResolverParameterCategory(ParameterCategory):  # Contains the Resolver Parameters
    _AxisFeedbackResolverParameterCategoryNET=None
    def __init__(self,AxisFeedbackResolverParameterCategoryNET=AerotechEnsembleParametersNET.AxisFeedbackResolverParameterCategory):
        self._AxisFeedbackResolverParameterCategoryNET=AxisFeedbackResolverParameterCategoryNET
        ParameterCategory.__init__(self,AxisFeedbackResolverParameterCategoryNET)

    @property
    def ResolverCoarseChannel(self): # Allows access to the ResolverCoarseChannel Parameter

    @property
    def ResolverFeedbackOffset(self): # Allows access to the ResolverFeedbackOffset Parameter

    @property
    def ResolverFeedbackRatio(self): # Allows access to the ResolverFeedbackRatio Parameter

    @property
    def ResolverReferenceGain(self): # Allows access to the ResolverReferenceGain Parameter

    @property
    def ResolverReferencePhase(self): # Allows access to the ResolverReferencePhase Parameter

    @property
    def ResolverSetup(self): # Allows access to the ResolverSetup Parameter 

        
        
class AxisIOAnalogFiltersParameterCategory(ParameterCategory):  # Contains the Analog Filters Parameters
    _AxisIOAnalogFiltersParameterCategoryNET=None
    def __init__(self,AxisIOAnalogFiltersParameterCategoryNET=AerotechEnsembleParametersNET.AxisIOAnalogFiltersParameterCategory):
        self._AxisIOAnalogFiltersParameterCategoryNET=AxisIOAnalogFiltersParameterCategoryNET
        ParameterCategory.__init__(self,AxisIOAnalogFiltersParameterCategoryNET)
        
    @property
    def Analog0Filter0CoeffD1(self): # Allows access to the Analog0Filter0CoeffD1 Parameter

    @property
    def Analog0Filter0CoeffD2(self): # Allows access to the Analog0Filter0CoeffD2 Parameter

    @property
    def Analog0Filter0CoeffN0(self): # Allows access to the Analog0Filter0CoeffN0 Parameter

    @property
    def Analog0Filter0CoeffN1(self): # Allows access to the Analog0Filter0CoeffN1 Parameter

    @property
    def Analog0Filter0CoeffN2(self): # Allows access to the Analog0Filter0CoeffN2 Parameter

    @property
    def Analog0Filter1CoeffD1(self): # Allows access to the Analog0Filter1CoeffD1 Parameter

    @property
    def Analog0Filter1CoeffD2(self): # Allows access to the Analog0Filter1CoeffD2 Parameter

    @property
    def Analog0Filter1CoeffN0(self): # Allows access to the Analog0Filter1CoeffN0 Parameter

    @property
    def Analog0Filter1CoeffN1(self): # Allows access to the Analog0Filter1CoeffN1 Parameter

    @property
    def Analog0Filter1CoeffN2(self): # Allows access to the Analog0Filter1CoeffN2 Parameter

    @property
    def Analog1Filter0CoeffD1(self): # Allows access to the Analog1Filter0CoeffD1 Parameter

    @property
    def Analog1Filter0CoeffD2(self): # Allows access to the Analog1Filter0CoeffD2 Parameter

    @property
    def Analog1Filter0CoeffN0(self): # Allows access to the Analog1Filter0CoeffN0 Parameter

    @property
    def Analog1Filter0CoeffN1(self): # Allows access to the Analog1Filter0CoeffN1 Parameter

    @property
    def Analog1Filter0CoeffN2(self): # Allows access to the Analog1Filter0CoeffN2 Parameter

    @property
    def Analog1Filter1CoeffD1(self): # Allows access to the Analog1Filter1CoeffD1 Parameter

    @property
    def Analog1Filter1CoeffD2(self): # Allows access to the Analog1Filter1CoeffD2 Parameter

    @property
    def Analog1Filter1CoeffN0(self): # Allows access to the Analog1Filter1CoeffN0 Parameter

    @property
    def Analog1Filter1CoeffN1(self): # Allows access to the Analog1Filter1CoeffN1 Parameter

    @property
    def Analog1Filter1CoeffN2(self): # Allows access to the Analog1Filter1CoeffN2 Parameter

    @property
    def AnalogFilterSetup(self): # Allows access to the AnalogFilterSetup Parameter 

   
class AxisIOBrakeParameterCategory(ParameterCategory):  # Contains the Brake Parameters
    _AxisIOBrakeParameterCategoryNET=None
    def __init__(self,AxisIOBrakeParameterCategoryNET=AerotechEnsembleParametersNET.AxisIOBrakeParameterCategory):
        self._AxisIOBrakeParameterCategoryNET=AxisIOBrakeParameterCategoryNET
        ParameterCategory.__init__(self,AxisIOBrakeParameterCategoryNET)
        
    @property
    def BrakeDisableDelay(self): # Allows access to the BrakeDisableDelay Parameter

    @property
    def BrakeEnableDelay(self): # Allows access to the BrakeEnableDelay Parameter

    @property
    def BrakeOutput(self): # Allows access to the BrakeOutput Parameter 

    @property
    def EnableBrakeControl(self): # Allows access to the EnableBrakeControl Parameter 
  
class AxisIOParameterCategory(ParameterCategory):  # Contains the I/O Parameters
    _AxisIOParameterCategoryNET=None
    def __init__(self,AxisIOParameterCategoryNET=AerotechEnsembleParametersNET.AxisIOParameterCategory):
        self._AxisIOParameterCategoryNET=AxisIOParameterCategoryNET
        ParameterCategory.__init__(self,AxisIOParameterCategoryNET)
        
    @property
    def Analog0InputOffset(self): # Allows access to the Analog0InputOffset Parameter

    @property
    def Analog1InputOffset(self): # Allows access to the Analog1InputOffset Parameter

    @property
    def Analog2InputOffset(self): # Allows access to the Analog2InputOffset Parameter

    @property
    def Analog3InputOffset(self): # Allows access to the Analog3InputOffset Parameter

    @property
    def AnalogFilters(self): # Contains the Analog Filters Parameters

    @property
    def Brake(self): # Contains the Brake Parameters 

    @property
    def IOSetup(self): # Allows access to the IOSetup Parameter 

    @property
    def SSINet1Setup(self): # Allows access to the SSINet1Setup Parameter

    @property
    def SSINet2Setup(self): # Allows access to the SSINet2Setup Parameter 


class AxisLimitsParameterCategory(ParameterCategory):  # Contains the Limits Parameters
    _AxisLimitsParameterCategoryNET=None
    def __init__(self,AxisLimitsParameterCategoryNET=AerotechEnsembleParametersNET.AxisLimitsParameterCategory):
        self._AxisLimitsParameterCategoryNET=AxisLimitsParameterCategoryNET
        ParameterCategory.__init__(self,AxisLimitsParameterCategoryNET)
        
    @property
    def EndOfTravelLimitSetup(self): # Allows access to the EndOfTravelLimitSetup Parameter

    @property
    def LimitDebounceDistance(self): # Allows access to the LimitDebounceDistance Parameter

    @property
    def LimitDebounceTime(self): # Allows access to the LimitDebounceTime Parameter

    @property
    def LimitDecelDistance(self): # Allows access to the LimitDecelDistance Parameter 
        
    @property
    def SoftwareLimitHigh(self): # Allows access to the SoftwareLimitHigh Parameter

    @property
    def SoftwareLimitLow(self): # Allows access to the SoftwareLimitLow Parameter

    @property
    def SoftwareLimitSetup(self): # Allows access to the SoftwareLimitSetup Parameter 
        
        
class AxisMotionGearCamParameterCategory(ParameterCategory):  # Contains the Gear/Cam Parameters
    _AxisMotionGearCamParameterCategoryNET=None
    def __init__(self,AxisMotionGearCamParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotionGearCamParameterCategory):
        self._AxisMotionGearCamParameterCategoryNET=AxisMotionGearCamParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotionGearCamParameterCategoryNET)
        
    @property
    def GearCamAnalogDeadband(self): # Allows access to the GearCamAnalogDeadband Parameter

    @property
    def GearCamIndex(self): # Allows access to the GearCamIndex Parameter

    @property
    def GearCamScaleFactor(self): # Allows access to the GearCamScaleFactor Parameter

    @property
    def GearCamSource(self): # Allows access to the GearCamSource Parameter 

        
class AxisMotionHomeParameterCategory(ParameterCategory):  # Contains the Home Parameters
    _AxisMotionHomeParameterCategoryNET=None
    def __init__(self,AxisMotionHomeParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotionHomeParameterCategory):
        self._AxisMotionHomeParameterCategoryNET=AxisMotionHomeParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotionHomeParameterCategoryNET)
        
    @property
    def HomeOffset(self): # Allows access to the HomeOffset Parameter

    @property
    def HomePositionSet(self): # Allows access to the HomePositionSet Parameter

    @property
    def HomeRampRate(self): # Allows access to the HomeRampRate Parameter

    @property
    def HomeSetup(self): # Allows access to the HomeSetup Parameter

    @property
    def HomeSpeed(self): # Allows access to the HomeSpeed Parameter

    @property
    def HomeType(self): # Allows access to the HomeType Parameter 

        
class AxisMotionInPositionParameterCategory(ParameterCategory):  # Contains the In Position Parameters
    _AxisMotionInPositionParameterCategoryNET=None
    def __init__(self,AxisMotionInPositionParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotionInPositionParameterCategory):
        self._AxisMotionInPositionParameterCategoryNET=AxisMotionInPositionParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotionInPositionParameterCategoryNET)
        
    
    @property
    def InPosition2Distance(self): # Allows access to the InPosition2Distance Parameter

    @property
    def InPosition2Time(self): # Allows access to the InPosition2Time Parameter

    @property
    def InPositionDistance(self): # Allows access to the InPositionDistance Parameter

    @property
    def InPositionTime(self): # Allows access to the InPositionTime Parameter 

        
class AxisMotionParameterCategory(ParameterCategory):  # Contains the Motion Parameters
    _AxisMotionParameterCategoryNET=None
    def __init__(self,AxisMotionParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotionParameterCategory):
        self._AxisMotionParameterCategoryNET=AxisMotionParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotionParameterCategoryNET)
        
        
    @property
    def DefaultRampDistance(self): # Allows access to the DefaultRampDistance Parameter

    @property
    def DefaultRampMode(self): # Allows access to the DefaultRampMode Parameter

    @property
    def DefaultRampRate(self): # Allows access to the DefaultRampRate Parameter

    @property
    def DefaultRampTime(self): # Allows access to the DefaultRampTime Parameter

    @property
    def DefaultRampType(self): # Allows access to the DefaultRampType Parameter

    @property
    def DefaultSpeed(self): # Allows access to the DefaultSpeed Parameter 

    @property
    def GearCam(self): # Contains the Gear/Cam Parameters 

    @property
    def Home(self): # Contains the Home Parameters

    @property
    def InPosition(self): # Contains the In Position Parameters 

    @property
    def JoystickHighSpeed(self): # Allows access to the JoystickHighSpeed Parameter

    @property
    def JoystickLowSpeed(self): # Allows access to the JoystickLowSpeed Parameter

    @property
    def MaxJogDistance(self): # Allows access to the MaxJogDistance Parameter

    @property
    def MaxJogSpeed(self): # Allows access to the MaxJogSpeed Parameter 

    @property
    def ReverseMotionDirection(self): # Allows access to the ReverseMotionDirection Parameter 



        
        
class AxisMotorParameterCategory(ParameterCategory):  # Contains the Motor Parameters
    _AxisMotorParameterCategoryNET=None
    def __init__(self,AxisMotorParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotorParameterCategory):
        self._AxisMotorParameterCategoryNET=AxisMotorParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotorParameterCategoryNET)
        
    @property
    def AutoMsetCurrent(self): # Allows access to the AutoMsetCurrent Parameter

    @property
    def AutoMsetTime(self): # Allows access to the AutoMsetTime Parameter

    @property
    def CommutationOffset(self): # Allows access to the CommutationOffset Parameter 

    @property
    def CountsPerRev(self): # Allows access to the CountsPerRev Parameter

    @property
    def CyclesPerRev(self): # Allows access to the CyclesPerRev Parameter 

    @property
    def MaxCurrentClamp(self): # Allows access to the MaxCurrentClamp Parameter 

    @property
    def MotorType(self): # Allows access to the MotorType Parameter 

    @property
    def Piezo(self): # Contains the Piezo Parameters

    @property
    def Stepper(self): # Contains the Stepper Parameters 


        
        
class AxisMotorPiezoParameterCategory(ParameterCategory):  # Contains the Piezo Parameters
    _AxisMotorPiezoParameterCategoryNET=None
    def __init__(self,AxisMotorPiezoParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotorPiezoParameterCategory):
        self._AxisMotorPiezoParameterCategoryNET=AxisMotorPiezoParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotorPiezoParameterCategoryNET)
        
    @property
    def PiezoDefaultServoState(self): # Allows access to the PiezoDefaultServoState Parameter

    @property
    def PiezoSlewRateClamp(self): # Allows access to the PiezoSlewRateClamp Parameter

    @property
    def PiezoVoltageClampHigh(self): # Allows access to the PiezoVoltageClampHigh Parameter

    @property
    def PiezoVoltageClampLow(self): # Allows access to the PiezoVoltageClampLow Parameter

    @property
    def PiezoVoltsPerUnit(self): # Allows access to the PiezoVoltsPerUnit Parameter 

        
        
class AxisMotorStepperParameterCategory(ParameterCategory):  # Contains the Stepper Parameters
    _AxisMotorStepperParameterCategoryNET=None
    def __init__(self,AxisMotorStepperParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotorStepperParameterCategory):
        self._AxisMotorStepperParameterCategoryNET=AxisMotorStepperParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotorStepperParameterCategoryNET)
        
    @property
    def StepperDampingCutoffFrequency(self): # Allows access to the StepperDampingCutoffFrequency Parameter

    @property
    def StepperDampingGain(self): # Allows access to the StepperDampingGain Parameter

    @property
    def StepperHoldingCurrent(self): # Allows access to the StepperHoldingCurrent Parameter

    @property
    def StepperResolution(self): # Allows access to the StepperResolution Parameter

    @property
    def StepperRunningCurrent(self): # Allows access to the StepperRunningCurrent Parameter

    @property
    def StepperRunningCurrentDelay(self): # Allows access to the StepperRunningCurrentDelay Parameter

    @property
    def StepperVerificationSpeed(self): # Allows access to the StepperVerificationSpeed Parameter 

        
        
class AxisParameterCategory(ParameterCategory):  # Contains the Axis Parameters The root category of parameters for a given axis 
    _AxisMotorStepperParameterCategoryNET=None
    def __init__(self,AxisMotorStepperParameterCategoryNET=AerotechEnsembleParametersNET.AxisMotorStepperParameterCategory):
        self._AxisMotorStepperParameterCategoryNET=AxisMotorStepperParameterCategoryNET
        ParameterCategory.__init__(self,AxisMotorStepperParameterCategoryNET)
           
    @property
    def AutofocusLoop(self): # Contains the Autofocus Loop Parameters
        return AxisAutofocusLoopParameterCategory(AerotechEnsembleParametersNET.BaseParameters.AutofocusLoop)
    
    @property
    def AxisName(self): # The axis name 
 
  # AxisNameChanged  Raised when AxisName property changes 
 
    @property
    def AxisNumber(self): # The axis number 
 
    @property
    def AxisType(self): # Allows access to the AxisType Parameter
 
    @property
    def BacklashDistance(self): # Allows access to the BacklashDistance Parameter
 
    @property
    def CurrentLoop(self): # Contains the Current Loop Parameters
 
    @property
    def DynamicControlsToolbox(self): # Contains the Dynamic Controls Toolbox Parameters
 
    @property
    def EnhancedThroughputModule(self): # Contains the Enhanced Throughput Module Parameters
 
    @property
    def EnhancedTrackingControl(self): # Contains the Enhanced Tracking Control Parameters

    @property
    def Fault(self): # Contains the Fault Parameters
 
    @property
    def Feedback(self): # Contains the Feedback Parameters
 
    @property
    def GantryMasterAxis(self): # Allows access to the GantryMasterAxis Parameter
 
    @property
    def GantrySetup(self): # Allows access to the GantrySetup Parameter

    @property
    def IO(self): # Contains the I/O Parameters
 
    @property
    def Limits(self): # Contains the Limits Parameters
 
    @property
    def Motion(self): # Contains the Motion Parameters
 
    @property
    def Motor(self): # Contains the Motor Parameters
 
    @property
    def PiezoSetup(self): # Allows access to the PiezoSetup Parameter
 
    @property
    def RequiredStageSerialNumber(self): # Allows access to the RequiredStageSerialNumber Parameter
 
    @property
    def RolloverCounts(self): # Allows access to the RolloverCounts Parameter
 
    @property
    def RolloverMode(self): # Allows access to the RolloverMode Parameter
 
    @property
    def ServoLoop(self): # Contains the Servo Loop Parameters
 
    @property
    def Units(self): # Contains the Units Parameters 

class AxisServoLoopAmpProtectionParameterCategory(ParameterCategory):  # Contains the Amp Protection Parameters
    _AxisServoLoopAmpProtectionParameterCategoryNET=None
    def __init__(self,AxisServoLoopAmpProtectionParameterCategoryyNET=AerotechEnsembleParametersNET.AxisServoLoopAmpProtectionParameterCategory):
        self._AxisServoLoopAmpProtectionParameterCategoryyNET=AxisServoLoopAmpProtectionParameterCategoryyNET
        ParameterCategory.__init__(self,AxisServoLoopAmpProtectionParameterCategoryyNET)
        
    @property
    def LinearAmpBusVoltage(self): # Allows access to the LinearAmpBusVoltage Parameter

    @property
    def LinearAmpDeratingFactor(self): # Allows access to the LinearAmpDeratingFactor Parameter

    @property
    def LinearAmpMaxPower(self): # Allows access to the LinearAmpMaxPower Parameter

    @property
    def MotorBackEMFConstant(self): # Allows access to the MotorBackEMFConstant Parameter

    @property
    def MotorResistance(self): # Allows access to the MotorResistance Parameter 

        
        
class AxisServoLoopFiltersParameterCategory(ParameterCategory):  # Contains the Filters Parameters
    _AxisServoLoopFiltersParameterCategoryNET=None
    def __init__(self,AxisServoLoopFiltersParameterCategoryNET=AerotechEnsembleParametersNET.AxisServoLoopFiltersParameterCategory):
        self._AxisServoLoopFiltersParameterCategoryNET=AxisServoLoopFiltersParameterCategoryNET
        ParameterCategory.__init__(self,AxisServoLoopFiltersParameterCategoryNET)
        
    @property
    def ServoFilter0CoeffD1(self): # Allows access to the ServoFilter0CoeffD1 Parameter

    @property
    def ServoFilter0CoeffD2(self): # Allows access to the ServoFilter0CoeffD2 Parameter

    @property
    def ServoFilter0CoeffN0(self): # Allows access to the ServoFilter0CoeffN0 Parameter

    @property
    def ServoFilter0CoeffN1(self): # Allows access to the ServoFilter0CoeffN1 Parameter

    @property
    def ServoFilter0CoeffN2(self): # Allows access to the ServoFilter0CoeffN2 Parameter

    @property
    def ServoFilter1CoeffD1(self): # Allows access to the ServoFilter1CoeffD1 Parameter

    @property
    def ServoFilter1CoeffD2(self): # Allows access to the ServoFilter1CoeffD2 Parameter

    @property
    def ServoFilter1CoeffN0(self): # Allows access to the ServoFilter1CoeffN0 Parameter

    @property
    def ServoFilter1CoeffN1(self): # Allows access to the ServoFilter1CoeffN1 Parameter

    @property
    def ServoFilter1CoeffN2(self): # Allows access to the ServoFilter1CoeffN2 Parameter

    @property
    def ServoFilter2CoeffD1(self): # Allows access to the ServoFilter2CoeffD1 Parameter

    @property
    def ServoFilter2CoeffD2(self): # Allows access to the ServoFilter2CoeffD2 Parameter

    @property
    def ServoFilter2CoeffN0(self): # Allows access to the ServoFilter2CoeffN0 Parameter

    @property
    def ServoFilter2CoeffN1(self): # Allows access to the ServoFilter2CoeffN1 Parameter

    @property
    def ServoFilter2CoeffN2(self): # Allows access to the ServoFilter2CoeffN2 Parameter

    @property
    def ServoFilter3CoeffD1(self): # Allows access to the ServoFilter3CoeffD1 Parameter

    @property
    def ServoFilter3CoeffD2(self): # Allows access to the ServoFilter3CoeffD2 Parameter

    @property
    def ServoFilter3CoeffN0(self): # Allows access to the ServoFilter3CoeffN0 Parameter

    @property
    def ServoFilter3CoeffN1(self): # Allows access to the ServoFilter3CoeffN1 Parameter

    @property
    def ServoFilter3CoeffN2(self): # Allows access to the ServoFilter3CoeffN2 Parameter

    @property
    def ServoFilter4CoeffD1(self): # Allows access to the ServoFilter4CoeffD1 Parameter

    @property
    def ServoFilter4CoeffD2(self): # Allows access to the ServoFilter4CoeffD2 Parameter

    @property
    def ServoFilter4CoeffN0(self): # Allows access to the ServoFilter4CoeffN0 Parameter

    @property
    def ServoFilter4CoeffN1(self): # Allows access to the ServoFilter4CoeffN1 Parameter

    @property
    def ServoFilter4CoeffN2(self): # Allows access to the ServoFilter4CoeffN2 Parameter

    @property
    def ServoFilter5CoeffD1(self): # Allows access to the ServoFilter5CoeffD1 Parameter

    @property
    def ServoFilter5CoeffD2(self): # Allows access to the ServoFilter5CoeffD2 Parameter

    @property
    def ServoFilter5CoeffN0(self): # Allows access to the ServoFilter5CoeffN0 Parameter

    @property
    def ServoFilter5CoeffN1(self): # Allows access to the ServoFilter5CoeffN1 Parameter

    @property
    def ServoFilter5CoeffN2(self): # Allows access to the ServoFilter5CoeffN2 Parameter

    @property
    def ServoFilter6CoeffD1(self): # Allows access to the ServoFilter6CoeffD1 Parameter

    @property
    def ServoFilter6CoeffD2(self): # Allows access to the ServoFilter6CoeffD2 Parameter

    @property
    def ServoFilter6CoeffN0(self): # Allows access to the ServoFilter6CoeffN0 Parameter

    @property
    def ServoFilter6CoeffN1(self): # Allows access to the ServoFilter6CoeffN1 Parameter

    @property
    def ServoFilter6CoeffN2(self): # Allows access to the ServoFilter6CoeffN2 Parameter

    @property
    def ServoFilter7CoeffD1(self): # Allows access to the ServoFilter7CoeffD1 Parameter

    @property
    def ServoFilter7CoeffD2(self): # Allows access to the ServoFilter7CoeffD2 Parameter

    @property
    def ServoFilter7CoeffN0(self): # Allows access to the ServoFilter7CoeffN0 Parameter

    @property
    def ServoFilter7CoeffN1(self): # Allows access to the ServoFilter7CoeffN1 Parameter

    @property
    def ServoFilter7CoeffN2(self): # Allows access to the ServoFilter7CoeffN2 Parameter

    @property
    def ServoFilterSetup(self): # Allows access to the ServoFilterSetup Parameter 

# ! DONE  
class AxisServoLoopGainsParameterCategory(ParameterCategory):  # Contains the Gains Parameters
    _AxisServoLoopGainsParameterCategoryNET=None
    def __init__(self,AxisServoLoopGainsParameterCategoryNET=AerotechEnsembleParametersNET.AxisServoLoopGainsParameterCategory):
        self._AxisServoLoopGainsParameterCategoryNET=AxisServoLoopGainsParameterCategoryNET
        ParameterCategory.__init__(self,AxisServoLoopGainsParameterCategoryNET)
        
    @property
    def GainAff(self): # Allows access to the GainAff Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainAff,float)
    
    @property
    def GainKd1(self): # Allows access to the GainKd1 Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKd1,float)
    
    @property
    def GainKi(self): # Allows access to the GainKi Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKi,float)
    
    @property
    def GainKp(self): # Allows access to the GainKp Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKp,float)
    
    @property
    def GainKp1(self): # Allows access to the GainKp1 Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKp1,float)
    
    @property
    def GainKpi(self): # Allows access to the GainKpi Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKpi,float)
    
    @property
    def GainKpos(self): # Allows access to the GainKpos Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKpos,float)
    
    @property
    def GainKsi1(self): # Allows access to the GainKsi1 Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKsi1,float)
    
    @property
    def GainKsi2(self): # Allows access to the GainKsi2 Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKsi2,float)
    
    @property
    def GainKv(self): # Allows access to the GainKv Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainKv,float)
    
    @property
    def GainPff(self): # Allows access to the GainPff Parameter
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainPff,float)
    
    @property
    def GainVff(self): # Allows access to the GainVff Parameter 
              return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.GainVff,float)
      
    @property
    def StaticFrictionCompensation(self): # Allows access to the StaticFrictionCompensation Parameter 
        return TypedParameter(self._AxisServoLoopGainsParameterCategoryNET.StaticFrictionCompensation,float)
    
# ! DONE   
class AxisServoLoopParameterCategory(ParameterCategory):  # Contains the Servo Loop Parameters
    _AxisServoLoopParameterCategoryNET=None
    def __init__(self,AxisServoLoopParameterCategoryNET=AerotechEnsembleParametersNET.AxisServoLoopParameterCategory):
        self._AxisServoLoopParameterCategoryNET=AxisServoLoopParameterCategoryNET
        ParameterCategory.__init__(self,AxisServoLoopParameterCategoryNET)

    @property
    def AmpProtection(self): # Contains the Amp Protection Parameters
        return AxisServoLoopAmpProtectionParameterCategory(self._AxisServoLoopParameterCategoryNET.AmpProtection)
    
    @property
    def FeedforwardAdvance(self): # Allows access to the FeedforwardAdvance Parameter
        return TypedParameter(self._AxisServoLoopParameterCategoryNET.FeedforwardAdvance,float)
    
    @property
    def Filters(self): # Contains the Filters Parameters 
        return AxisServoLoopFiltersParameterCategory(self._AxisServoLoopParameterCategoryNET.Filters)
    
    @property
    def Gains(self): # Contains the Gains Parameters 
        return AxisServoLoopGainsParameterCategory(self._AxisServoLoopParameterCategoryNET.Gains) 
    
    @property
    def ServoRate(self): # Allows access to the ServoRate Parameter
        return TypedParameter(self._AxisServoLoopParameterCategoryNET.ServoRate,int)
    
    @property
    def ServoSetup(self): # Allows access to the ServoSetup Parameter 
        return TypedParameter(self._AxisServoLoopParameterCategoryNET.ServoSetup,int)
 
# ! DONE   
class AxisUnitsParameterCategory(ParameterCategory):  # Contains the Units Parameters
    _AxisUnitsParameterCategoryNET=None
    def __init__(self,AxisUnitsParameterCategoryNET=AerotechEnsembleParametersNET.AxisUnitsParameterCategory):
        self._AxisUnitsParameterCategoryNET=AxisUnitsParameterCategoryNET
        ParameterCategory.__init__(self,AxisUnitsParameterCategoryNET)
        
    @property
    def CountsPerUnit(self): # Allows access to the CountsPerUnit Parameter
        return TypedParameter(self._AxisUnitsParameterCategoryNET.CountsPerUnit,float)
    
    @property
    def DecimalPlaces(self): # Allows access to the DecimalPlaces Parameter 
        return TypedParameter(self._AxisUnitsParameterCategoryNET.DecimalPlaces,int)
    
    @property
    def UnitsName(self): # Allows access to the UnitsName Parameter 
        return TypedParameter(self._AxisUnitsParameterCategoryNET.UnitsName,str)
        
# ! DONE
class BaseParameters():  # Represents the root category of parameters 
    _BaseParametersNET=None
    def __init__(self,BaseParametersNET=AerotechEnsembleParametersNET.BaseParameters.Defaults):
        self._BaseParametersNET=BaseParametersNET
        
    @property
    def Axes(self): # Provides access to the axes parameters 
        return CommonCollections.NamedConstantCollection(AerotechEnsembleParametersNET.BaseParameters.Axes,AxisParameterCategory)

    @classmethod
    @property
    def Defaults(cls): # Provides the defaults of the parameters 
        return cls(AerotechEnsembleParametersNET.BaseParameters.Defaults)

    @property
    def System(self): # The parameters that are per controller
        return SystemParameterCategory(AerotechEnsembleParametersNET.BaseParameters.System)
    
    @property
    def Tasks(self): # The task parameters
        return CommonCollections.NamedConstantCollection(AerotechEnsembleParametersNET.BaseParameters.Tasks,TaskParameterCategory)
 
# ! DONE 
class ControllerAxisParameterCategory(AxisParameterCategory):  # The root category of parameters for a given controller axis 
    _ControllerAxisParameterCategoryNET=None
    def __init__(self,ControllerAxisParameterCategoryNET):
        self._ControllerAxisParameterCategoryNET=ControllerAxisParameterCategoryNET
        AxisParameterCategory.__init__(self)
    
    @property
    def AssignedNumber(self):  # The assigned axis number  
        return self._ControllerAxisParameterCategoryNET.AssignedNumber
        
# ! DONE 
class ControllerAxisParameterCategoryCollection(CommonCollections.NamedMaskedConstantCollection):  # Collection of ControllerAxisParameterCategory
    _ControllerAxisParameterCategoryCollectionNET=None
    def __init__(self,ControllerAxisParameterCategoryCollectionNET):
        self._ControllerAxisParameterCategoryCollectionNET=ControllerAxisParameterCategoryCollectionNET
        CommonCollections.NamedMaskedConstantCollection.__init__(self,ControllerAxisParameterCategoryCollectionNET,ControllerAxisParameterCategory,Ensemble.AxisMask)
    
    @property
    def RequiredAxes(self):  # Which axes have to exist for the proper operation of the system 
        return Ensemble.AxisMask[self._ControllerAxisParameterCategoryCollectionNET.RequiredAxes.ToString()]
     
    @property
    def RequireUniqueNumbers(self):  # Whether it is required for axes to have unique axis numbers  
        return self._ControllerAxisParameterCategoryCollectionNET.RequireUniqueNumbers

# ! DONE 
class ControllerParameters(BaseParameters):  # Root parameter category that handles parameters on a controller 
    _ControllerParametersNET=None
    def __init__(self,ControllerParametersNET:AerotechEnsembleParametersNET.ControllerParameters=AerotechEnsembleParametersNET.ControllerParameters):
        self._ControllerParametersNET=ControllerParametersNET
        BaseParameters.__init__(self,self._ControllerParametersNET)
     
    @property
    def Axes(self):  # Provides access to the axes parameters 
        return ControllerAxisParameterCategoryCollection(self._ControllerParametersNET.Axes) 
 
    def Commit(self):  # Commits parameters on the controller 
        self._ControllerParametersNET.Commit()
        
    @multimethod
    def RetrieveFromController(self):  # Retrieves all parameters and creates a local copy 
        return BaseParameters(self._ControllerParametersNET.RetrieveFromController())
    @multimethod
    def RetrieveFromController(self,progressChangedEventHandler:ProgressChangedEventHandler):  # Retrieves all parameters and creates a local storage 
        return BaseParameters(self._ControllerParametersNET.RetrieveFromController(progressChangedEventHandler))
    
    # @multimethod
    # def RetrieveFromController(ProgressChangedEventHandler, EventHandler<(Of <<'(ParameterRetrievalErrorEventArgs>)>>)):  # Retrieves all parameters and creates a local storage 
 
    def SaveToFile(self,fileName:str):  # Retrieves the current parameters from the controller, and then saves the parameters to the specifed file 
        self._ControllerParametersNET.SaveToFile(fileName)
        
    @multimethod
    def SendToController(self,parameterFilePath:str):  # Sends parameters from a parameter file 
        return self._ControllerParametersNET.SendToController(parameterFilePath)
    
    @multimethod
    def SendToController(self,parameterFilePath:str, progressChangedEventhandler:ProgressChangedEventHandler):  # Sends parameters from a parameter file 
        return self._ControllerParametersNET.SendToController(parameterFilePath, progressChangedEventhandler)
    
    @multimethod
    def SendToController(self,parameters:BaseParameters):  # Sends parameters from a parameter source
        return self._ControllerParametersNET.SendToController(parameters)
    
    @multimethod
    def SendToController(self,parameters:BaseParameters, progressChangedEventhandler:ProgressChangedEventHandler):  # Sends parameters from a parameter source
        return self._ControllerParametersNET.SendToController(parameters, progressChangedEventhandler)
    
    @multimethod
    def SendToController(self,parameterCategories:ParameterCategory):  # Sends parameters from a parameter category 
        return self._ControllerParametersNET.SendToController(parameterCategories)
    
    @multimethod
    def SendToController(self,parameterCategories:ParameterCategory,progressChangedEventhandler:ProgressChangedEventHandler):  # Sends parameters from a parameter category 
        return self._ControllerParametersNET.SendToController(parameterCategories, progressChangedEventhandler)
    
    # @multimethod
    # def SendToController<(Of <<'(TType>)>>)(IEnumerable<(Of <<'(TType>)>>)):  # Sends parameters from parameter categories 

    
    # @multimethod
    # def SendToController<(Of <<'(TType>)>>)(IEnumerable<(Of <<'(TType>)>>), ProgressChangedEventHandler):  # Sends parameters from parameter categories  

# ! DONE 
class HomeType(Enum):  # Represents the home type
    PastLimittoMarker=AerotechEnsembleParametersNET.HomeType.PastLimittoMarker  # Home Past Limit to Marker
    ToLimitandReversetoMarker=AerotechEnsembleParametersNET.HomeType.ToLimitandReversetoMarker # Home to Limit and Reverse to Marker
    ToMarkerOnly=AerotechEnsembleParametersNET.HomeType.ToMarkerOnly  # Home to Marker Only
    ToLimitOnly=AerotechEnsembleParametersNET.HomeType.ToLimitOnly # Home to Limit Only
    AtCurrentPosition=AerotechEnsembleParametersNET.HomeType.AtCurrentPosition  # Home at Current Position
    AtCurrentPositionAbsolute=AerotechEnsembleParametersNET.HomeType.AtCurrentPositionAbsolute  # Home at Current Position Absolute 

# ! DONE 
class MotorType(Enum):  # Represents the motor type
    ACBrushlessHallEffect=AerotechEnsembleParametersNET.MotorType.ACBrushlessHallEffect  # AC Brushless (Hall-Effect Switches)
    ACBrushlessAutoMSET=AerotechEnsembleParametersNET.MotorType.ACBrushlessAutoMSET  # AC Brushless (Auto-MSET)
    DCBrush=AerotechEnsembleParametersNET.MotorType.DCBrush  # DC Brush
    StepperMotor=AerotechEnsembleParametersNET.MotorType.StepperMotor  # Stepper Motor
    TwoPhaseACBrushless=AerotechEnsembleParametersNET.MotorType.TwoPhaseACBrushless  # 2-Phase AC Brushless
    ACBrushlessCommutationSearch=AerotechEnsembleParametersNET.MotorType.ACBrushlessCommutationSearch  # AC Brushless (Commutation Search)
    PiezoActuator=AerotechEnsembleParametersNET.MotorType.PiezoActuator  # Piezo Actuator 

# * This class will be completed in the future
class NamedXmlSections():  # Provides name based access to UserDataSections.
    # TODO Skip as it is too complex
    pass
 
# ! DONE 
class Parameter():  # Represents a generic parameter 
    _ParameterNET=None
    def __init__(self,ParameterNET=AerotechEnsembleParametersNET.Parameter):
        self._ParameterNET=ParameterNET
    
    @property
    def Bounds(self):  # Contains the bounds of this parameter 
        return ParameterBounds(self._ParameterNET.Bounds)
    @property
    def Context(self):  # The context of the parameter
        return ParameterContext[self._ParameterNET.Context.ToString()]
    @property
    def ContextKey(self):  # The Task ID or axis index of the parameter
        return self._ParameterNET.ContextKey
    @property
    def Default(self):  # The parameter default value 
        return self._ParameterNET.Default
 
    def getBounds(self):  # The method that does the work to get the bounds 
        return ParameterBounds(self._ParameterNET.getBounds())

    def getValue(self):  # [Internal] The method that does the work to get the value 
        return self._ParameterNET.getValue()

    @property
    def Name(self):  # The parameter name 
        return self._ParameterNET.Name
 
    def setValue(self,Object):  # The method that does the work to set the value 
        self._ParameterNET.setValue(Object)
 
    @property
    def Value(self):  # The parameter value 
        return self._ParameterNET.Value
    
    @property
    def ValueType(self):  # The type of the parameter 
        return PrimitiveType[self._ParameterNET.ValueType.ToString()]

# ! DONE 
class ParameterBounds():  # Represents the bounds of a generic parameter 
    _ParameterBoundsNET=None
    def __init__(self,ParameterBoundsNET=AerotechEnsembleParametersNET.ParameterBounds):
        self._ParameterBoundsNET=ParameterBoundsNET

    @property
    def Exists(self):  # Whether the parameter has bounds 
        return self._ParameterBoundsNET.Exists
    
    @property
    def Max(self):  # The parameter maximum value, if any 
        return self._ParameterBoundsNET.Max
    
    @property
    def Min(self):  # The parameter minimum value, if any 
        return self._ParameterBoundsNET.Min

# ! DONE
class ParameterCategory(CommonCollections.NamedConstantCollection):  # The base type for categories containing parameters 
    _ParameterCategoryNET=None
    def __init__(self,ParameterCategoryNET):
        self._ParameterCategoryNET=ParameterCategoryNET
        CommonCollections.NamedConstantCollection.__init__(self,ParameterCategoryNET,Parameter)
    
    @property
    def All(self):  # Contains all the parameters in this category and its child categories 
        return ParametersAllCollection(self._ParameterCategoryNET.All)
    
    @property
    def Categories(self):  # Gets the subcategories of this category. 
        return CommonCollections.NamedConstantCollection(self._ParameterCategoryNET.Categories,ParameterCategory)
    
    @property
    def Name(self):  # The name of the category 
        return self._ParameterCategoryNET.Name

# ! DONE
class ParameterContext(Enum):  # Represents the context of a parameter (system, axis, or task) 
    System=AerotechEnsembleParametersNET.ParameterContext.System  # A system parameter 
    Axis=AerotechEnsembleParametersNET.ParameterContext.Axis  # An axis parameter 
    Task=AerotechEnsembleParametersNET.ParameterContext.Task # A task parameter  

# ! DONE
class ParameterFile(BaseParameters):  # Root parameter category that handles parameters from a file 
    _ParameterFileNET=None
    @multimethod
    def __init__(self,ParameterFileNET:AerotechEnsembleParametersNET.ParameterFile=AerotechEnsembleParametersNET.ParameterFile):
        self._ParameterFileNET=ParameterFileNET
        BaseParameters.__init__(self,self._ParameterFileNET)
    
    @multimethod
    def __init__(self,path:str):  # Loads parameters from a file 
        self._ParameterFileNET=AerotechEnsembleParametersNET.ParameterFile(path)
        BaseParameters.__init__(self,self._ParameterFileNET)
    
    @multimethod
    def __init__(self,path:str, failIfNotFound:bool):  # Loads parameters from a file 
        self._ParameterFileNET=AerotechEnsembleParametersNET.ParameterFile(path,failIfNotFound)
        BaseParameters.__init__(self,self._ParameterFileNET)
    
    @multimethod
    def __init__(self,path:str, parameters:BaseParameters):  # Creates a new parameter file 
        self._ParameterFileNET=AerotechEnsembleParametersNET.ParameterFile(path,parameters._BaseParametersNET)
        BaseParameters.__init__(self,self._ParameterFileNET)
    
    @property
    def Axes(self):  # Provides access to parameters on the axes 
        return CommonCollections.NamedMaskableConstantCollection(self._ParameterFileNET.Axes,AxisParameterCategory,Ensemble.AxisMask) 
    
    @property
    def CompatibleVersion(self):  # Specifies the oldest version of software with which the parameter files are compatible.
        # TODO Question: Which Version?
        return Version(self._ParameterFileNET.CompatibleVersion)
    @property
    def DataVersion(self):  # The version of the library that last modified data in the parameter file
        # TODO Question: Which Version?
        return Version(self._ParameterFileNET.DataVersion)
    @property
    def FileInfo(self):  # The FileInfo of the parameter file
        # TODO Question: Which FileInfo?
        return FileInfo(self._ParameterFileNET.FileInfo)
    
    # FileInfoChanged  Is raised when FileInfo changes 
 
    @multimethod
    def Import(self,parameterCategory:ParameterCategory):  # Imports parameter data into this file 
        self._ParameterFileNET.Save(parameterCategory._ParameterCategoryNET)
 
    @multimethod
    def Import(self,parameters:BaseParameters):  # Imports parameter data into this file
        self._ParameterFileNET.Save(parameters._BaseParametersNET)

    @multimethod
    def Save(self,fileName:str):  # Saves parameters to a file 
        self._ParameterFileNET.Save(fileName)
 
    @multimethod
    def Save(self):  # Saves this parameter file 
        self._ParameterFileNET.Save()
 
    @property
    def UserDataSections(self):  # Provides access to the user-customizable tag in the configuration file 
        return NamedXmlSections(self._ParameterFileNET.UserDataSections)

# ! DONE
class ParameterRetrievalErrorEventArgs(EnsembleStatus.ErrorEventArgs):  # Provides data for parameter retrieval errors 
    _ParameterRetrievalErrorEventArgsNET=None
    def __init__(self,ParameterRetrievalErrorEventArgsNET):
        self._ParameterRetrievalErrorEventArgsNET=ParameterRetrievalErrorEventArgsNET
        EnsembleStatus.ErrorEventArgs.__init__(self,ParameterRetrievalErrorEventArgsNET)
        
    @property
    def Continue(self):  # Whether to continue the parameter retrieval  
        return self._ParameterRetrievalErrorEventArgsNET.Continue
        
    @property
    def Parameter(self):  # The name of parameter whose retrieval failed  
        return self._ParameterRetrievalErrorEventArgsNET.Parameter
    
# ! DONE
class ParametersAllCollection(CommonCollections.NamedConstantCollection):  # Represents a category that contains parameters in a non-nested fashion 
    _ParametersAllCollectionNET=None
    def __init__(self,ParametersAllCollectionNET):
        self._ParametersAllCollectionNET=ParametersAllCollectionNET
        CommonCollections.NamedConstantCollection.__init__(self,ParametersAllCollectionNET,Parameter)

# ! DONE
class PiezoDefaultServoState(Enum):  # Represents the piezo default servo state.
    Off=AerotechEnsembleParametersNET.PiezoDefaultServoState.Off  # Servo Off
    On=AerotechEnsembleParametersNET.PiezoDefaultServoState.Off  # Servo On 

# ! DONE
class PositionFeedbackChannel(Enum):  # Represents the position feedback channel type
    Default=AerotechEnsembleParametersNET.PositionFeedbackChannel.Default  # Default
    Channel0=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel0  # Channel 0
    Channel1=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel1  # Channel 1
    Channel2=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel2  # Channel 2
    Channel3=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel3  # Channel 3
    Channel4=AerotechEnsembleParametersNET.PositionFeedbackChannel.Channel4  # Channel 4 

# ! DONE
class PositionFeedbackType(Enum):  # Represents the position feedback type
    LocalEncoderCounter=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Local Encoder Counter
    EncoderMultiplier=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Encoder Multiplier
    AnalogInput=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Analog Input
    EnDatAbsoluteEncoder=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # EnDat Absolute Encoder
    HallEffectSwitches=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Hall-Effect Switches
    Resolver=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Resolver
    ResoluteAbsoluteEncoder=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Resolute Absolute Encoder
    CapacitanceSensor=AerotechEnsembleParametersNET.PositionFeedbackType.LocalEncoderCounter  # Capacitance Sensor 
extend_enum(PositionFeedbackType,'None',getattr(AerotechEnsembleParametersNET.PositionFeedbackType,'None'))

# ! DONE
class PrimitiveType(Enum):  # Represents a primitive type in AeroBasic 
    Integer=AerotechEnsembleParametersNET.PrimitiveType.Integer  # 32-bit integer 
    Double=AerotechEnsembleParametersNET.PrimitiveType.Double  # 64-bit floating point, ANSI/IEEE Standard 754-1985 
    Single=AerotechEnsembleParametersNET.PrimitiveType.Single  # 32-bit floating point, ANSI/IEEE Standard 754-1985 
    Long=AerotechEnsembleParametersNET.PrimitiveType.Long  # 64-bit integer 
    String=AerotechEnsembleParametersNET.PrimitiveType.String  # ASCII null-terminated string 
    
# ! DONE
class SystemCalibrationParameterCategory(ParameterCategory):  # Contains the Calibration Parameters
    _SystemCalibrationParameterCategoryNET=None
    def __init__(self,SystemCalibrationParameterCategoryNET=AerotechEnsembleParametersNET.SystemCalibrationParameterCategory):
        self._SystemCalibrationParameterCategoryNET=SystemCalibrationParameterCategoryNET
        ParameterCategory.__init__(self,SystemCalibrationParameterCategoryNET)
        
    @property
    def CalibrationFile1D(self): # Allows access to the CalibrationFile1D Parameter
        return TypedParameter(self._SystemCalibrationParameterCategoryNET.CalibrationFile1D,str)

    @property
    def CalibrationFile2D(self): # Allows access to the CalibrationFile2D Parameter 
        return TypedParameter(self._SystemCalibrationParameterCategoryNET.CommandFaultCharacter,str)
        
# ! DONE   
class SystemCommunicationAsciiParameterCategory(ParameterCategory):  # Contains the ASCII Parameters
    _SystemCommunicationAsciiParameterCategoryNET=None
    def __init__(self,SystemCommunicationAsciiParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationAsciiParameterCategory):
        self._SystemCommunicationAsciiParameterCategoryNET=SystemCommunicationAsciiParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationAsciiParameterCategoryNET)
        
    @property
    def CommandFaultCharacter(self): # Allows access to the CommandFaultCharacter Parameter
        return TypedParameter(self._SystemCommunicationAsciiParameterCategoryNET.CommandFaultCharacter,int)
        
    @property
    def CommandInvalidCharacter(self): # Allows access to the CommandInvalidCharacter Parameter
        return TypedParameter(self._SystemCommunicationAsciiParameterCategoryNET.CommandInvalidCharacter,int)
        
    @property
    def CommandSetup(self): # Allows access to the CommandSetup Parameter
        return TypedParameter(self._SystemCommunicationAsciiParameterCategoryNET.CommandSetup,int)
        
    @property
    def CommandSuccessCharacter(self): # Allows access to the CommandSuccessCharacter Parameter
        return TypedParameter(self._SystemCommunicationAsciiParameterCategoryNET.CommandSuccessCharacter,int)
        
    @property
    def CommandTerminatingCharacter(self): # Allows access to the CommandTerminatingCharacter Parameter
        return TypedParameter(self._SystemCommunicationAsciiParameterCategoryNET.CommandTerminatingCharacter,int)
        
    @property
    def CommandTimeout(self): # Allows access to the CommandTimeout Parameter
        return TypedParameter(self._SystemCommunicationAsciiParameterCategoryNET.CommandTimeout,int)
        
    @property
    def CommandTimeoutCharacter(self): # Allows access to the CommandTimeoutCharacter Parameter 
        return TypedParameter(self._SystemCommunicationAsciiParameterCategoryNET.CommandTimeoutCharacter,int)
     
# ! DONE   
class SystemCommunicationEthernetIPParameterCategory(ParameterCategory):  # Contains the Ethernet/IP Parameters
    _SystemCommunicationEthernetIPParameterCategoryNET=None
    def __init__(self,SystemCommunicationEthernetIPParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationEthernetIPParameterCategory):
        self._SystemCommunicationEthernetIPParameterCategoryNET=SystemCommunicationEthernetIPParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationEthernetIPParameterCategoryNET)
        
    @property
    def Class1InputDoubles(self): # Allows access to the Class1InputDoubles Parameter
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1InputDoubles,int)
        
    @property
    def Class1InputDoublesOffset(self): # Allows access to the Class1InputDoublesOffset Parameter
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1InputDoublesOffset,int)
        
    @property
    def Class1InputIntegers(self): # Allows access to the Class1InputIntegers Parameter
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1InputIntegers,int)
        
    @property
    def Class1InputIntegersOffset(self): # Allows access to the Class1InputIntegersOffset Parameter
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1InputIntegersOffset,int)
        
    @property
    def Class1OutputDoubles(self): # Allows access to the Class1OutputDoubles Parameter
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1OutputDoubles,int)
        
    @property
    def Class1OutputDoublesOffset(self): # Allows access to the Class1OutputDoublesOffset Parameter
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1OutputDoublesOffset,int)
        
    @property
    def Class1OutputIntegers(self): # Allows access to the Class1OutputIntegers Parameter
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1OutputIntegers,int)
        
    @property
    def Class1OutputIntegersOffset(self): # Allows access to the Class1OutputIntegersOffset Parameter 
        return TypedParameter(self._SystemCommunicationEthernetIPParameterCategoryNET.Class1OutputIntegersOffset,int)
        
# ! DONE         
class SystemCommunicationEthernetSocketsParameterCategory(ParameterCategory):  # Contains the Ethernet Sockets Parameters
    _SystemCommunicationEthernetSocketsParameterCategoryNET=None
    def __init__(self,SystemCommunicationEthernetSocketsParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationEthernetSocketsParameterCategory):
        self._SystemCommunicationEthernetSocketsParameterCategoryNET=SystemCommunicationEthernetSocketsParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationEthernetSocketsParameterCategoryNET)
        
    @property
    def Socket2Port(self): # Allows access to the Socket2Port Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket2Port,int)
        
    @property
    def Socket2RemoteIPAddress(self): # Allows access to the Socket2RemoteIPAddress Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket2RemoteIPAddress,int)
        
    @property
    def Socket2Setup(self): # Allows access to the Socket2Setup Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket2Setup,int)
        
    @property
    def Socket2Timeout(self): # Allows access to the Socket2Timeout Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket2Timeout,int)
        
    @property
    def Socket2TransmissionSize(self): # Allows access to the Socket2TransmissionSize Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket2TransmissionSize,int)
        
    @property
    def Socket3Port(self): # Allows access to the Socket3Port Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket3Port,int)
        
    @property
    def Socket3RemoteIPAddress(self): # Allows access to the Socket3RemoteIPAddress Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket3RemoteIPAddress,int)
        
    @property
    def Socket3Setup(self): # Allows access to the Socket3Setup Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket3Setup,int)
        
    @property
    def Socket3Timeout(self): # Allows access to the Socket3Timeout Parameter
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket3Timeout,int)
        
    @property
    def Socket3TransmissionSize(self): # Allows access to the Socket3TransmissionSize Parameter 
        return TypedParameter(self._SystemCommunicationEthernetSocketsParameterCategoryNET.Socket3TransmissionSize,int)
        
# ! DONE           
class SystemCommunicationGpibParameterCategory(ParameterCategory):  # Contains the GPIB Parameters
    _SystemCommunicationGpibParameterCategoryNET=None
    def __init__(self,SystemCommunicationGpibParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationGpibParameterCategory):
        self._SystemCommunicationGpibParameterCategoryNET=SystemCommunicationGpibParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationGpibParameterCategoryNET)
        
    @property
    def GpibParallelResponse(self): # Allows access to the GpibParallelResponse Parameter
        return TypedParameter(self._SystemCommunicationGpibParameterCategoryNET.GpibParallelResponse,int)
        
    @property
    def GpibPrimaryAddress(self): # Allows access to the GpibPrimaryAddress Parameter
        return TypedParameter(self._SystemCommunicationGpibParameterCategoryNET.GpibPrimaryAddress,int)
        
    @property
    def GpibTerminatingCharacter(self): # Allows access to the GpibTerminatingCharacter Parameter 
        return TypedParameter(self._SystemCommunicationGpibParameterCategoryNET.GpibTerminatingCharacter,int)
    
# ! DONE    
class SystemCommunicationModbusMasterParameterCategory(ParameterCategory):  # Contains the Modbus Master Parameters
    _SystemCommunicationModbusMasterParameterCategoryNET=None
    def __init__(self,SystemCommunicationModbusMasterParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationModbusMasterParameterCategory):
        self._SystemCommunicationModbusMasterParameterCategoryNET=SystemCommunicationModbusMasterParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationModbusMasterParameterCategoryNET)
        
    @property
    def ModbusMasterFunctions(self): # Allows access to the ModbusMasterFunctions Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterFunctions,int)
        
    @property
    def ModbusMasterInputBits(self): # Allows access to the ModbusMasterInputBits Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterInputBits,int)
        
    @property
    def ModbusMasterInputBitsOffset(self): # Allows access to the ModbusMasterInputBitsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterInputBitsOffset,int)
        
    @property
    def ModbusMasterInputWords(self): # Allows access to the ModbusMasterInputWords Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterInputWords,int)
        
    @property
    def ModbusMasterInputWordsOffset(self): # Allows access to the ModbusMasterInputWordsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterInputWordsOffset,int)
        
    @property
    def ModbusMasterOutputBits(self): # Allows access to the ModbusMasterOutputBits Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterOutputBits,int)
        
    @property
    def ModbusMasterOutputBitsOffset(self): # Allows access to the ModbusMasterOutputBitsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterOutputBitsOffset,int)
        
    @property
    def ModbusMasterOutputBitsSections(self): # Allows access to the ModbusMasterOutputBitsSections Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterOutputBitsSections,int)
        
    @property
    def ModbusMasterOutputWords(self): # Allows access to the ModbusMasterOutputWords Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterOutputWords,int)
        
    @property
    def ModbusMasterOutputWordsOffset(self): # Allows access to the ModbusMasterOutputWordsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterOutputWordsOffset,int)
        
    @property
    def ModbusMasterOutputWordsSections(self): # Allows access to the ModbusMasterOutputWordsSections Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterOutputWordsSections,int)
        
    @property
    def ModbusMasterRWReadOffset(self): # Allows access to the ModbusMasterRWReadOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterRWReadOffset,int)
        
    @property
    def ModbusMasterRWWriteOffset(self): # Allows access to the ModbusMasterRWWriteOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterRWWriteOffset,int)
        
    @property
    def ModbusMasterSetup(self): # Allows access to the ModbusMasterSetup Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterSetup,int)
        
    @property
    def ModbusMasterSlaveID(self): # Allows access to the ModbusMasterSlaveID Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterSlaveID,int)
        
    @property
    def ModbusMasterSlaveIPAddress(self): # Allows access to the ModbusMasterSlaveIPAddress Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterSlaveIPAddress,int)
        
    @property
    def ModbusMasterSlavePort(self): # Allows access to the ModbusMasterSlavePort Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterSlavePort,int)
        
    @property
    def ModbusMasterSlaveType(self): # Allows access to the ModbusMasterSlaveType Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterSlaveType,int)
        
    @property
    def ModbusMasterStatusBitsOffset(self): # Allows access to the ModbusMasterStatusBitsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterStatusBitsOffset,int)
        
    @property
    def ModbusMasterStatusWordsOffset(self): # Allows access to the ModbusMasterStatusWordsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterStatusWordsOffset,int)
        
    @property
    def ModbusMasterVirtualInputs(self): # Allows access to the ModbusMasterVirtualInputs Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterVirtualInputs,int)
        
    @property
    def ModbusMasterVirtualInputsOffset(self): # Allows access to the ModbusMasterVirtualInputsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterVirtualInputsOffset,int)
        
    @property
    def ModbusMasterVirtualOutputs(self): # Allows access to the ModbusMasterVirtualOutputs Parameter
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterVirtualOutputs,int)
        
    @property
    def ModbusMasterVirtualOutputsOffset(self): # Allows access to the ModbusMasterVirtualOutputsOffset Parameter 
        return TypedParameter(self._SystemCommunicationModbusMasterParameterCategoryNET.ModbusMasterVirtualOutputsOffset,int)
        
# ! DONE    
class SystemCommunicationModbusSlaveParameterCategory(ParameterCategory):  # Contains the Modbus Slave Parameters
    _SystemCommunicationModbusSlaveParameterCategoryNET=None
    def __init__(self,SystemCommunicationModbusSlaveParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationModbusSlaveParameterCategory):
        self._SystemCommunicationModbusSlaveParameterCategoryNET=SystemCommunicationModbusSlaveParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationModbusSlaveParameterCategoryNET)
        
    @property
    def ModbusSlaveInputBits(self): # Allows access to the ModbusSlaveInputBits Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveInputBits,int)
        
    @property
    def ModbusSlaveInputBitsOffset(self): # Allows access to the ModbusSlaveInputBitsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveInputBitsOffset,int)
        
    @property
    def ModbusSlaveInputWords(self): # Allows access to the ModbusSlaveInputWords Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveInputWords,int)
        
    @property
    def ModbusSlaveInputWordsOffset(self): # Allows access to the ModbusSlaveInputWordsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveInputWordsOffset,int)
        
    @property
    def ModbusSlaveOutputBits(self): # Allows access to the ModbusSlaveOutputBits Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveOutputBits,int)
        
    @property
    def ModbusSlaveOutputBitsOffset(self): # Allows access to the ModbusSlaveOutputBitsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveOutputBitsOffset,int)
        
    @property
    def ModbusSlaveOutputWords(self): # Allows access to the ModbusSlaveOutputWords Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveOutputWords,int)
        
    @property
    def ModbusSlaveOutputWordsOffset(self): # Allows access to the ModbusSlaveOutputWordsOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveOutputWordsOffset,int)
        
    @property
    def ModbusSlaveRWReadOffset(self): # Allows access to the ModbusSlaveRWReadOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveRWReadOffset,int)
        
    @property
    def ModbusSlaveRWWriteOffset(self): # Allows access to the ModbusSlaveRWWriteOffset Parameter
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveRWWriteOffset,int)
        
    @property
    def ModbusSlaveUnitID(self): # Allows access to the ModbusSlaveUnitID Parameter 
        return TypedParameter(self._SystemCommunicationModbusSlaveParameterCategoryNET.ModbusSlaveUnitID,int)
     
# ! DONE
class SystemCommunicationParameterCategory(ParameterCategory):  # Contains the Communication Parameters
    _SystemCommunicationParameterCategoryNET=None
    def __init__(self,SystemCommunicationParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationParameterCategory):
        self._SystemCommunicationParameterCategoryNET=SystemCommunicationParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationParameterCategoryNET)
        
    @property
    def Ascii(self): # Contains the ASCII Parameters
        return SystemCommunicationAsciiParameterCategory(self._SystemCommunicationParameterCategoryNET.Ascii)
        
    @property
    def EthernetIP(self): # Contains the Ethernet/IP Parameters
        return SystemCommunicationEthernetIPParameterCategory(self._SystemCommunicationParameterCategoryNET.EthernetIP)
        
    @property
    def EthernetSockets(self): # Contains the Ethernet Sockets Parameters
        return SystemCommunicationEthernetSocketsParameterCategory(self._SystemCommunicationParameterCategoryNET.EthernetSockets)
        
    @property
    def Gpib(self): # Contains the GPIB Parameters
        return SystemCommunicationGpibParameterCategory(self._SystemCommunicationParameterCategoryNET.Gpib)
        
    @property
    def ModbusMaster(self): # Contains the Modbus Master Parameters
        return SystemCommunicationModbusMasterParameterCategory(self._SystemCommunicationParameterCategoryNET.ModbusMaster)
        
    @property
    def ModbusSlave(self): # Contains the Modbus Slave Parameters
        return SystemCommunicationModbusSlaveParameterCategory(self._SystemCommunicationParameterCategoryNET.ModbusSlave)
        
    @property
    def RS232(self): # Contains the RS-232 Parameters
        return SystemCommunicationRS232ParameterCategory(self._SystemCommunicationParameterCategoryNET.RS232)
        
    @property
    def WebServer(self): # Contains the Web Server Parameters 
        return SystemCommunicationWebServerParameterCategory(self._SystemCommunicationParameterCategoryNET.WebServer)

# ! DONE
class SystemCommunicationRS232ParameterCategory(ParameterCategory):  # Contains the RS-232 Parameters
    _SystemCommunicationRS232ParameterCategoryNET=None
    def __init__(self,SystemCommunicationRS232ParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationRS232ParameterCategory):
        self._SystemCommunicationRS232ParameterCategoryNET=SystemCommunicationRS232ParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationRS232ParameterCategoryNET)
        
    @property
    def SerialPort0BaudRate(self): # Allows access to the SerialPort0BaudRate Parameter
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort0BaudRate,int)
    
    @property
    def SerialPort0Setup(self): # Allows access to the SerialPort0Setup Parameter
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort0Setup,int)
    
    @property
    def SerialPort0XoffCharacter(self): # Allows access to the SerialPort0XoffCharacter Parameter
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort0XoffCharacter,int)
    
    @property
    def SerialPort0XonCharacter(self): # Allows access to the SerialPort0XonCharacter Parameter
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort0XonCharacter,int)
    
    @property
    def SerialPort1BaudRate(self): # Allows access to the SerialPort1BaudRate Parameter
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort1BaudRate,int)
    
    @property
    def SerialPort1Setup(self): # Allows access to the SerialPort1Setup Parameter
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort1Setup,int)
    
    @property
    def SerialPort1XoffCharacter(self): # Allows access to the SerialPort1XoffCharacter Parameter
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort1XoffCharacter,int)
    
    @property
    def SerialPort1XonCharacter(self): # Allows access to the SerialPort1XonCharacter Parameter 
        return TypedParameter(self._SystemCommunicationRS232ParameterCategoryNET.SerialPort1XonCharacter,int)
    
# ! DONE
class SystemCommunicationWebServerParameterCategory(ParameterCategory):  # Contains the Web Server Parameters
    _SystemCommunicationWebServerParameterCategoryNET=None
    def __init__(self,SystemCommunicationWebServerParameterCategoryNET=AerotechEnsembleParametersNET.SystemCommunicationWebServerParameterCategory):
        self._SystemCommunicationWebServerParameterCategoryNET=SystemCommunicationWebServerParameterCategoryNET
        ParameterCategory.__init__(self,SystemCommunicationWebServerParameterCategoryNET)
        
    @property
    def WebServerPort(self): # Allows access to the WebServerPort Parameter
        return TypedParameter(self._SystemCommunicationWebServerParameterCategoryNET.WebServerPort,int)
        
    @property
    def WebServerSetup(self): # Allows access to the WebServerSetup Parameter
        return TypedParameter(self._SystemCommunicationWebServerParameterCategoryNET.WebServerSetup,int)

# ! DONE
class SystemJoystickParameterCategory(ParameterCategory):  # Contains the Joystick Parameters
    _SystemJoystickParameterCategoryNET=None
    def __init__(self,SystemJoystickParameterCategoryNET=AerotechEnsembleParametersNET.SystemJoystickParameterCategory):
        self._SystemJoystickParameterCategoryNET=SystemJoystickParameterCategoryNET
        ParameterCategory.__init__(self,SystemJoystickParameterCategoryNET)
        
    @property
    def JoystickInput0Deadband(self): # Allows access to the JoystickInput0Deadband Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput0Deadband,float)
    
    @property
    def JoystickInput0MaxVoltage(self): # Allows access to the JoystickInput0MaxVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput0MaxVoltage,float)
    
    @property
    def JoystickInput0MinVoltage(self): # Allows access to the JoystickInput0MinVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.DJoystickInput0MinVoltage,float)
    
    @property
    def JoystickInput1Deadband(self): # Allows access to the JoystickInput1Deadband Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput1Deadband,float)
    
    @property
    def JoystickInput1MaxVoltage(self): # Allows access to the JoystickInput1MaxVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput1MaxVoltage,float)
    
    @property
    def JoystickInput1MinVoltage(self): # Allows access to the JoystickInput1MinVoltage Parameter
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickInput1MinVoltage,float)
    
    @property
    def JoystickSetup(self): # Allows access to the JoystickSetup Parameter 
        return TypedParameter(self._SystemJoystickParameterCategoryNET.JoystickSetup,int)

# ! DONE
class SystemMemoryAllocationParameterCategory(ParameterCategory):  # Contains the Memory Allocation Parameters
    _SystemMemoryAllocationParameterCategoryNET=None
    def __init__(self,SystemMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.SystemMemoryAllocationParameterCategory):
        self._SystemMemoryAllocationParameterCategoryNET=SystemMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,SystemMemoryAllocationParameterCategoryNET)
        
    @property
    def DataCollectionPoints(self): # Allows access to the DataCollectionPoints Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.DataCollectionPoints,int)
    
    @property
    def GlobalDoubles(self): # Allows access to the GlobalDoubles Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.GlobalDoubles,int)
    
    @property
    def GlobalIntegers(self): # Allows access to the GlobalIntegers Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.GlobalIntegers,int)
    
    @property
    def GlobalStrings(self): # Allows access to the GlobalStrings Parameter
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.GlobalStrings,int)

    @property
    def PrintBufferSize(self): # Allows access to the PrintBufferSize Parameter 
        return TypedParameter(self._SystemMemoryAllocationParameterCategoryNET.PrintBufferSize,int)

# ! DONE
class SystemParameterCategory(ParameterCategory):  # Contains the System Parameters
    _SystemParameterCategoryNET=None
    def __init__(self,SystemParameterCategoryNET=AerotechEnsembleParametersNET.SystemParameterCategory):
        self._SystemParameterCategoryNET=SystemParameterCategoryNET
        ParameterCategory.__init__(self,SystemParameterCategoryNET)
        
    @property
    def Calibration(self): # Contains the Calibration Parameters
        return SystemCalibrationParameterCategory(self._SystemParameterCategoryNET.Calibration)

    @property
    def Communication(self): # Contains the Communication Parameters
        return SystemCommunicationParameterCategory(self._SystemParameterCategoryNET.Communication) 

    @property
    def DisplayAxes(self): # Allows access to the DisplayAxes Parameter
        return TypedParameter(self._SystemParameterCategoryNET.DisplayAxes,int)

    @property
    def ExternalSyncFrequency(self): # Allows access to the ExternalSyncFrequency Parameter
        return TypedParameter(self._SystemParameterCategoryNET.ExternalSyncFrequency,int)

    @property
    def FaultAckMoveOutOfLimit(self): # Allows access to the FaultAckMoveOutOfLimit Parameter
        return TypedParameter(self._SystemParameterCategoryNET.FaultAckMoveOutOfLimit,int)

    @property
    def Joystick(self): # Contains the Joystick Parameters
        return SystemJoystickParameterCategory(self._SystemParameterCategoryNET.Joystick)

    @property
    def MemoryAllocation(self): # Contains the Memory Allocation Parameters
        return SystemMemoryAllocationParameterCategory(self._SystemParameterCategoryNET.MemoryAllocation)

    @property
    def RequiredAxes(self): # Allows access to the RequiredAxes Parameter
        return TypedParameter(self._SystemParameterCategoryNET.RequiredAxes,int)

    @property
    def SoftwareExternalFaultInput(self): # Allows access to the SoftwareExternalFaultInput Parameter
        return TypedParameter(self._SystemParameterCategoryNET.SoftwareExternalFaultInput,int)

    @property
    def TaskExecutionSetup(self): # Allows access to the TaskExecutionSetup Parameter
        return TypedParameter(self._SystemParameterCategoryNET.TaskExecutionSetup,int)

    @property
    def User(self): # Contains the User Parameters 
        return SystemUserParameterCategory(self._SystemParameterCategoryNET.User)

# ! DONE
class SystemUserParameterCategory(ParameterCategory):  # Contains the User Parameters
    _SystemUserParameterCategoryNET=None
    def __init__(self,SystemUserParameterCategoryNET=AerotechEnsembleParametersNET.SystemUserParameterCategory):
        self._SystemUserParameterCategoryNET=SystemUserParameterCategoryNET
        ParameterCategory.__init__(self,SystemUserParameterCategoryNET)
        
    @property
    def UserDouble0(self): # Allows access to the UserDouble0 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserDouble0,float)
    
    @property
    def UserDouble1(self): # Allows access to the UserDouble1 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserDouble1,float)
    
    @property
    def UserInteger0(self): # Allows access to the UserInteger0 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserInteger0,int)
    
    @property
    def UserInteger1(self): # Allows access to the UserInteger1 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserInteger1,int)
    
    @property
    def UserString0(self): # Allows access to the UserString0 Parameter
        return TypedParameter(self._SystemUserParameterCategoryNET.UserString0,str)
    
    @property
    def UserString1(self): # Allows access to the UserString1 Parameter 
        return TypedParameter(self._SystemUserParameterCategoryNET.UserString1,str)
    
# ! DONE
class TaskMemoryAllocationParameterCategory(ParameterCategory):  # Contains the Memory Allocation Parameters
    _TaskMemoryAllocationParameterCategoryNET=None
    def __init__(self,TaskMemoryAllocationParameterCategoryNET=AerotechEnsembleParametersNET.TaskMemoryAllocationParameterCategory):
        self._TaskMemoryAllocationParameterCategoryNET=TaskMemoryAllocationParameterCategoryNET
        ParameterCategory.__init__(self,TaskMemoryAllocationParameterCategoryNET)
          
    @property
    def CodeSize(self): # Allows access to the CodeSize Parameter
        return TypedParameter(self._TaskMemoryAllocationParameterCategoryNET.CodeSize,int)
    
    @property
    def DataSize(self): # Allows access to the DataSize Parameter
        return TypedParameter(self._TaskMemoryAllocationParameterCategoryNET.DataSize,int)
    
    @property
    def StackSize(self): # Allows access to the StackSize Parameter
        return TypedParameter(self._TaskMemoryAllocationParameterCategoryNET.StackSize,int)

# ! DONE
class TaskMotionParameterCategory(ParameterCategory):  # Contains the Motion Parameters
    _TaskMotionParameterCategoryNET=None
    def __init__(self,TaskMotionParameterCategoryNET=AerotechEnsembleParametersNET.TaskMotionParameterCategory):
        self._TaskMotionParameterCategoryNET=TaskMotionParameterCategoryNET
        ParameterCategory.__init__(self,TaskMotionParameterCategoryNET)
        
    @property
    def DefaultCoordinatedRampDistance(self): # Allows access to the DefaultCoordinatedRampDistance Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampDistance,float)
    
    @property
    def DefaultCoordinatedRampMode(self): # Allows access to the DefaultCoordinatedRampMode Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampMode,int)
    
    @property
    def DefaultCoordinatedRampRate(self): # Allows access to the DefaultCoordinatedRampRate Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampRate,float)
    
    @property
    def DefaultCoordinatedRampTime(self): # Allows access to the DefaultCoordinatedRampTime Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedRampTime,float)
    
    @property
    def DefaultCoordinatedSpeed(self): # Allows access to the DefaultCoordinatedSpeed Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultCoordinatedSpeed,float)
    
    @property
    def DefaultDependentCoordinatedRampRate(self): # Allows access to the DefaultDependentCoordinatedRampRate Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultDependentCoordinatedRampRate,float)
    
    @property
    def DefaultDependentCoordinatedSpeed(self): # Allows access to the DefaultDependentCoordinatedSpeed Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultDependentCoordinatedSpeed,float)
    
    @property
    def DefaultSCurve(self): # Allows access to the DefaultSCurve Parameter
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultSCurve,float)
    
    @property
    def DefaultWaitMode(self): # Allows access to the DefaultWaitMode Parameter 
        return TypedParameter(self._TaskMotionParameterCategoryNET.DefaultWaitMode,int)

# ! DONE
class TaskParameterCategory(ParameterCategory):  # Contains the Task Parameters
    _TaskParameterCategoryNET=None
    def __init__(self,TaskParameterCategoryNET=AerotechEnsembleParametersNET.TaskParameterCategory):
        self._TaskParameterCategoryNET=TaskParameterCategoryNET
        ParameterCategory.__init__(self,TaskParameterCategoryNET)
        
    @property
    def AutoRunProgram(self): # Allows access to the AutoRunProgram Parameter
        return TypedParameter(self._TaskParameterCategoryNET.AutoRunProgram,str)
    
    @property
    def MemoryAllocation(self): # Contains the Memory Allocation Parameters
        return TaskMemoryAllocationParameterCategory(self._TaskParameterCategoryNET.MemoryAllocation)
    
    @property
    def Motion(self): # Contains the Motion Parameters
        return TaskMotionParameterCategory(self._TaskParameterCategoryNET.Motion)
    
    @property
    def TaskErrorAbortAxes(self): # Allows access to the TaskErrorAbortAxes Parameter
        return TypedParameter(self._TaskParameterCategoryNET.TaskErrorAbortAxes,int)
    
    @property
    def TaskId(self): # The task for which this category is for
        return Ensemble.TaskId[self._TaskParameterCategoryNET.TaskId.ToString()]
    
    @property
    def TaskStopAbortAxes(self): # Allows access to the TaskStopAbortAxes Parameter
        return TypedParameter(self._TaskParameterCategoryNET.TaskStopAbortAxes,int)
    
    @property
    def TaskTerminationAxes(self): # Allows access to the TaskTerminationAxes Parameter
        return TypedParameter(self._TaskParameterCategoryNET.TaskTerminationAxes,int)

# ! DONE
class TypedParameter(Parameter):  # Represents a typed parameter 
    _TypedParameterNET=None
    _pyClass=None
    def __init__(self,TypedParameterNET,pyClass):
        self._TypedParameterNET=TypedParameterNET
        self._pyClass=pyClass
        Parameter.__init__(self,self._TypedParameterNET)
        
    @property
    def Bounds(self):  # Specifies the parameter bounds
        return TypedParameterBounds(self._TypedParameterNET.Bounds,self._pyClass)
    
    @property
    def Default(self):  # The parameter's default value 
        return self._pyClass(self._TypedParameterNET.Default)
 
    def getBounds(self):  # The method that does the work to get the bounds (Overrides Parameter.getBounds()()()().)
        return ParameterBounds(self._TypedParameterNET.getBounds())
    
    @property
    def Value(self):  # The parameter value 
        return self._pyClass(self._TypedParameterNET.Value)
   
# ! DONE
class TypedParameterBounds(ParameterBounds):  # Represents bounds of a typed parameter 
    _TypedParameterBoundsNET=None
    _pyClass=None
    def __init__(self,TypedParameterBoundsNET,pyClass):
        self._TypedParameterBoundsNET=TypedParameterBoundsNET
        self._pyClass=pyClass
        ParameterBounds.__init__(self,self._TypedParameterBoundsNET)
        
    @property
    def Max(self):  # Parameter maximum value 
        return self._pyClass(self._TypedParameterBoundsNET.Max)
    
    @property
    def Min(self):  # Parameter minimum value  
        return self._pyClass(self._TypedParameterBoundsNET.Min)
        
# ! DONE
class VelocityFeedbackChannel(Enum):  # Represents the velocity feedback channel type
    Default=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Default  # Default
    Channel0=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel0  #   Channel 0
    Channel1=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel1  #   Channel 1
    Channel2=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel2  #   Channel 2
    Channel3=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel3  #   Channel 3
    Channel4=AerotechEnsembleParametersNET.VelocityFeedbackChannel.Channel4  #   Channel 4 

# ! DONE
class VelocityFeedbackType(Enum):  # Represents the velocity feedback type 
    LocalEncoderCounter=AerotechEnsembleParametersNET.VelocityFeedbackType.LocalEncoderCounter # Encoder Counter
    EncoderMultiplier=AerotechEnsembleParametersNET.VelocityFeedbackType.EncoderMultiplier  # Encoder Multiplier
    AnalogInput=AerotechEnsembleParametersNET.VelocityFeedbackType.AnalogInput  # Analog Input
    Resolver=AerotechEnsembleParametersNET.VelocityFeedbackType.Resolver # Resolver 
extend_enum(VelocityFeedbackType,'None',getattr(AerotechEnsembleParametersNET.VelocityFeedbackType,'None'))
