import os
import pathlib
import sys
import glob

sys.path.insert(0, os.path.abspath('.'))
sys.path.extend(glob.glob(f'{pathlib.Path(__file__).parents[0].resolve()}/*/**/', recursive=True))

import clr

from multimethod import multimethod

from collections.abc import Sequence

import EnsembleTasks
import Ensemble
import Common

DEFAULT_DLL_PATH:str=os.path.join(os.path.join(os.path.dirname(__file__),'Aerotech_DotNet_dll'),'')
DEFAULT_DLL_NAME:str='Aerotech.Ensemble'
if DEFAULT_DLL_PATH.upper() not in [path.upper() for path in sys.path]:
    sys.path.extend(DEFAULT_DLL_PATH)
try:
    clr.AddReference(DEFAULT_DLL_NAME)
    import Aerotech.Ensemble.Tasks.Debug as AerotechEnsembleTasksDebugNET
except:
    raise RuntimeError

class Variable():
    _VariableNET=None
    def __init__(self,VariableNET=AerotechEnsembleTasksDebugNET.Variable):
        self._VariableNET=VariableNET
    
    @property
    def Address(self):
        return self._VariableNET.Address
    
    @property
    def controller(self):
        return Ensemble.Controller(self._VariableNET.controller)
    
    @property
    def Name(self):
        return self._VariableNET.Name
    
    @property
    def Scope(self):
        return EnsembleTasks.VariableScope[self._VariableNET.Scope.ToString()]
    
    @property
    def task(self):
        return EnsembleTasks.Task(self._VariableNET.task)
    
    @property
    def Type(self):
        return EnsembleTasks.VariableType[self._VariableNET.Type.ToString()]
    
    @property
    def Value(self):
        # TODO Solve what Object and value represents here
        pass
     
class ArrayVariable(Variable,Sequence):
    _ArrayVariableNET=None
    def __init__(self,ArrayVariableNET=AerotechEnsembleTasksDebugNET.ArrayVariable):
        self._ArrayVariableNET=ArrayVariableNET
        super(Variable,self).__init__(self._ArrayVariableNET)

    def __getitem__(self, i):
        return self._ArrayVariableNET[i]
    
    def __len__(self):
        return len(self._ArrayVariableNET)
    
    @property
    def Address(self):
        return self._ArrayVariableNET.Address
    
    @property
    def Count(self):
        return self._ArrayVariableNET.Count
    
    @property
    def ElementType(self):
        return self._ArrayVariableNET.ElementType
    
    @property
    def Type(self):
        return EnsembleTasks.VariableType[self._ArrayVariableNET.Type.ToString()]
    
    @property
    def Value(self):
        # TODO Solve what Object and value represents here
        pass
    
class BreakpointsManager():
    _BreakpointsManagerNET=None
    def __init__(self,BreakpointsManagerNET=AerotechEnsembleTasksDebugNET.BreakpointsManager):
        self._BreakpointsManagerNET=BreakpointsManagerNET
    
    def Add(self,location:Common.FilePoint):
        self._BreakpointsManagerNET.Add(location._FilePointNET)
        
    def Remove(self,location:Common.FilePoint):
        self._BreakpointsManagerNET.Remove(location._FilePointNET)
        
    def RemoveAll(self):
        self._BreakpointsManagerNET.RemoveAll()
 
class CurrentContext(Sequence):
    _CurrentContextNET=None
    
    def __init__(self,CurrentContextNET=AerotechEnsembleTasksDebugNET.CurrentContext):
        self._CurrentContextNET=CurrentContextNET
        
    def __getitem__(self, i):
        return self._CurrentContextNET[i]
    
    def __len__(self):
        return len(self._CurrentContextNET)
        
    @property
    def Arguments(self):
        return Variable(self._CurrentContextNET.Arguments)
    
    @property
    def Function(self):
        return self._CurrentContextNET.Function
    
    @property
    def Globals(self):
        return Variable(self._CurrentContextNET.Globals)
    
    @property
    def InFunction(self):
        return self._CurrentContextNET.InFunction
    
    @property
    def Locals(self):
        return Variable(self._CurrentContextNET.Locals)
    
    @property
    def Location(self):
        return Common.FilePoint(self._CurrentContextNET.Location)

class ProgramDebug():
    _ProgramDebugNET=None
    
    def __init__(self,ProgramDebugNET=AerotechEnsembleTasksDebugNET.ProgramDebug):
        self._ProgramDebugNET=ProgramDebugNET
        
    @property
    def Breakpoints(self):
        return BreakpointsManager(self._ProgramDebugNET.BreakPoints)
 
    def CounterToPosition(self,counter:int):
        return Common.FilePoint(self._ProgramDebugNET.CounterToPosition(counter))

    @property
    def FileNames(self):
        return self._ProgramDebugNET.FileNames
    
    @multimethod
    def LoadContext(self):
        return CurrentContext(self._ProgramDebugNET.LoadContext())

    @multimethod
    def LoadContext(self,position:Common.FilePoint):
        return CurrentContext(self._ProgramDebugNET.LoadContext(position._FilePointNET))

    @multimethod
    def LoadContext(self,programCounter:int):
        return CurrentContext(self._ProgramDebugNET.LoadContext(programCounter))

    def LoadSymbols(self, path:str):
        self._ProgramDebugNET.LoadSymbols(path)

    @property
    def Location(self):
        return Common.FilePoint(self._ProgramDebugNET.ProgramDebug.Location)
    
    def Pause(self):
        self._ProgramDebugNET.ProgramDebug.Pause
    
    def StepInto(self):
        self._ProgramDebugNET.ProgramDebug.StepInto
        
    def StepOut(self):
        self._ProgramDebugNET.ProgramDebug.StepOut
    
    def StepOver(self):
        self._ProgramDebugNET.ProgramDebug.StepOver
        
    @property
    def SymbolsFile(self):
        return self._ProgramDebugNET.ProgramDebug.SymbolsFile

    @property
    def SymbolsLoaded(self):
        return self._ProgramDebugNET.ProgramDebug.SymbolsLoaded

class SimpleVariable(Variable):
    _SimpleVariableNET=None
    def __init__(self,SimpleVariableNET=AerotechEnsembleTasksDebugNET.SimpleVariable):
        self._SimpleVariableNET=SimpleVariableNET
        super(Variable,self).__init__(self._SimpleVariableNET)

    @property
    def Type(self):
        return EnsembleTasks.VariableType[self._SimpleVariableNET.Type.ToString()]
    
    @property
    def Value(self):
        # TODO Solve what Object and value represents here
        pass
        
class StructVariable(Variable,Sequence):
    _StructVariableNET=None
    def __init__(self,StructVariableNET=AerotechEnsembleTasksDebugNET.StructVariable):
        self._StructVariableNET=StructVariableNET
        super(Variable,self).__init__(self._StructVariableNET)

    def __getitem__(self, i):
        return self._StructVariableNET[i]
    
    def __len__(self):
        return len(self._StructVariableNET)
    
    @property
    def Address(self):
        return self._StructVariableNET.Address
    
    @property
    def Fields(self):
        return self._StructVariableNET.Fields
    
    @property
    def NumberOfFields(self):
        return self._StructVariableNET.NumberOfFields
    
    @property
    def Type(self):
        return EnsembleTasks.VariableType[self._StructVariableNET.Type.ToString()]
    
    @property
    def Value(self):
        # TODO Solve what Object and value represents here
        pass
        
if __name__=='__main__':
    a=1
