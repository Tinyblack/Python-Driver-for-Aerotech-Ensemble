import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr
clr.AddReference('System')
from System import String, Char, Int32, IntPtr,Text, UInt32,Enum,Decimal,Double
from System.ComponentModel import ProgressChangedEventHandler

from copy import deepcopy
from win32api import GetFileVersionInfo, LOWORD, HIWORD

from GlobalLogger import GlobalLogger

import time

from multimethod import multimethod

from collections.abc import Sequence

import CommonCollections
import EnsembleTasks
import Common

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    from Aerotech.Ensemble import Tasks
    from Aerotech.Ensemble.Tasks import Debug
except:
    raise RuntimeError

##################
class Variable():
    @property
    def Address(self):
        return Debug.Variable.Address
    
    #@property
    #def controller(self):
    #    return Debug.Variable.controller
    
    @property
    def Name(self):
        return Debug.Variable.Name
    
    @property
    def Scope(self):
        return EnsembleTasks.VariableScope
    
    #@property
    #def task(self):
    
    @property
    def Type(self):
        return EnsembleTasks.VariableType
    
    @property
    def Value(self):
        return Debug.Variable.Value

        
class ArrayVariable(Variable):
    def Count(self):
        return Debug.ArrayVariable.Count
    
    def ElementType(self):
        return Debug.ArrayVariable.ElementType
    

class BreakpointsManager():
    def Add(self,location:Common.FilePoint):
        Debug.BreakpointsManager.Add(location)
        
    def Remove(self,location:Common.FilePoint):
        Debug.BreakpointsManager.Remove(location)
        
    def RemoveAll(self):
        Debug.BreakpointsManager.RemoveAll()
 

class CurrentContext():
    @property
    def Arguments(self):
        return Debug.CurrentContext.Arguments
    
    @property
    def Function(self):
        return Debug.CurrentContext.Function
    
    @property
    def Globals(self):
        return Debug.CurrentContext.Globals
    
    @property
    def InFunction(self):
        return Debug.CurrentContext.InFunction
    
    #def Item[([( String])])  Allows to retrieve variables by their name 
    @property
    def Locals(self):
        return Debug.CurrentContext.Locals
    
    @property
    def Location(self):
        return Debug.CurrentContext.Location

        
class ProgramDebug():
    @property
    def Breakpoints(self):
        return BreakpointsManager
 
    def CounterToPosition(self,counter:int):
        return Debug.ProgramDebug.CounterToPosition(counter)

    @property
    def FileNames(self):
        return  Debug.ProgramDebug.FileNames
    
    @multimethod
    def LoadContext(self):
        Debug.ProgramDebug.LoadContext()

    @multimethod
    def LoadContext(self,position:Common.FilePoint):
        Debug.ProgramDebug.LoadContext(position)

    @multimethod
    def LoadContext(self,programCounter:int):
        Debug.ProgramDebug.LoadContext(programCounter)

    def LoadSymbols(self, path:str):
        Debug.ProgramDebug.LoadSymbols(path)

    @property
    def Location(self):
        return Debug.ProgramDebug.Location
    
    def Pause(self):
        Debug.ProgramDebug.Pause
    
    def StepInto(self):
        Debug.ProgramDebug.StepInto
        
    def StepOut(self):
        Debug.ProgramDebug.StepOut
    
    def StepOver(self):
        Debug.ProgramDebug.StepOver
        
    @property
    def SymbolsFile(self):
        return Debug.ProgramDebug.SymbolsFile

    @property
    def SymbolsLoaded(self):
        return Debug.ProgramDebug.SymbolsLoaded

class SimpleVariable(Variable):
    def __init__(self):
        pass
        
class StructVariable(Variable):
    def __init__(self):
        pass
    
if __name__=='__main__':
    a=1
    # Use __init__ as a type convertor.