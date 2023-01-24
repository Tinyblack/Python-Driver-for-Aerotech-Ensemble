import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

from GlobalLogger import GlobalLogger

import time

from AeroTechEnsembleWrapper import AerotechEnsemble


if __name__=='__main__':
    stage=AerotechEnsemble.connect()
    #stage.enableAxis(stage.controllerAxisX)
    #stage.enableAxis(stage.controllerAxisY)
    #stage.enableAxis(stage.controllerAxisZ)
    #stage.enableAxes("X","Y","Z")
    #stage.moveAxesRelative("X","Y","Z",distance=[0.1,0.1,0.1],speed=1,wait=True)
    #stage.moveAxisRelative(stage.controllerAxisX.axisNET,distance=10,speed=0.1,wait=True)
    stage.updateStatus()
    print(stage.controllerAxisX.status.toString())
    a=1