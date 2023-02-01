import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
from enum import Enum


DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Configuration as AerotechEnsembleConfigurationNET
except:
    raise RuntimeError

# * Checked
class BinaryCalibrationActionStatus(Enum):  # Specifies the status of a binary calibration file action.
    TableAdded=AerotechEnsembleConfigurationNET.BinaryCalibrationActionStatus.TableAdded  # The calibration table was added.
    TableRemoved=AerotechEnsembleConfigurationNET.BinaryCalibrationActionStatus.TableRemoved  # The calibration table was removed.
    TableNotAdded=AerotechEnsembleConfigurationNET.BinaryCalibrationActionStatus.TableNotAdded  # The calibration table was not added. 

# * Checked
class BinaryCalibrationActionTableType(Enum):  # Specifies the type of calibration table associated with a calibration file action. 
    Calibration1D=AerotechEnsembleConfigurationNET.BinaryCalibrationActionTableType.Calibration1D  # 1D calibration table.
    Calibration2D=AerotechEnsembleConfigurationNET.BinaryCalibrationActionTableType.Calibration2D  # 2D calibration table. 

    
