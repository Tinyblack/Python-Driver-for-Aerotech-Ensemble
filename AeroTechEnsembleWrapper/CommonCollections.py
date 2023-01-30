from collections.abc import Sequence,MutableSequence

# A constant collection of objects that have a name associated with them 
class NamedConstantCollection(Sequence): 
    def __init__(self,TObject,pyClass):
        # TObject is .NET instance, pyClass is the type decorator for python wrapper
        self.TObject=TObject
        self.pyClass=pyClass
        super().__init__()

    def __getitem__(self, TName):
        return self.pyClass(self.TObject[TName])
    
    def __len__(self):
        return self.TObject.Count
        
    @property
    def Capacity(self):
        return self.TObject.Capacity
    
    @property
    def Count(self):
        return self.TObject.Count
    
# A collection of objects that have a name associated with them
class NamedCollection(MutableSequence,NamedConstantCollection): 
    def __init__(self,TObject,pyClass):
        super(NamedConstantCollection,self).__init__(TObject,pyClass)

    def __delitem__(self,TName):
        del self.TObject[TName]
        
    def __setitem__(self,TName,TObject):
        self.TObject[TName]=TObject
        
    def insert(self,TName,TObject):
        pass
    
    def Add(self,TObject):  # Adds an object to the collection 
        self.TObject.Add(TObject)

    def Clear(self):  # Clears the collection from objects 
        self.TObject.Clear()
        
    def Remove(self,TName):
        self.TObject.Remove(TName)

                                        
class NamedMaskedConstantCollection(NamedConstantCollection):
    def __init__(self,TObject,pyClass,pyMask):
        self.pyMask=pyMask
        super(NamedConstantCollection,self).__init__(TObject,pyClass)
                                        
    @property
    def Mask(self):  # The mask of the collection 
        return self.pyMask[self.TObject.Mask.ToString()]
    
    def Remask(self,TMask):   # Produces a new collection with some additional objects masked 
        self.TObject.Remask(TMask) 
        
        
class NamedMaskableConstantCollection(NamedMaskedConstantCollection):
    def __init__(self,TObject,pyClass,pyMask):
        self.pyMask=pyMask
        super(NamedMaskedConstantCollection,self).__init__(TObject,pyClass)
                                        
    @property
    def Mask(self):  # The mask of the collection 
        return self.pyMask[self.TObject.Mask.ToString()]
    
    @Mask.setter
    def Mask(self,TMask):
        self.TObject.Mask=TMask
    
    def Remask(self,TMask):   # Produces a new collection with some additional objects masked 
        self.TObject.Remask(TMask) 

