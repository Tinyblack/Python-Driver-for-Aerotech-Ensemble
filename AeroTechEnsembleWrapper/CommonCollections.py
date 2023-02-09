from collections.abc import Sequence,MutableSequence

# * Checked
class NamedConstantCollection(Sequence): 
    def __init__(self,TObject,pyClass):
        # TObject is .NET instance, pyClass is the type decorator for python wrapper
        self.TObject=TObject
        self.pyClass=pyClass
        super().__init__()

    def __getitem__(self, TName):
        try:
            return self.pyClass(self.TObject.get_Item(TName))
        except:
            return self.pyClass[self.TObject[TName].ToString()]
    
    def __len__(self):
        return self.TObject.Count
        
    @property
    def Capacity(self):
        return self.TObject.Capacity
    
    @property
    def Count(self):
        return self.TObject.Count
    
# * Checked
class NamedCollection(MutableSequence,NamedConstantCollection): 
    def __init__(self,TObject,pyClass):
        NamedConstantCollection.__init__(self,TObject,pyClass)

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

# * Checked                                     
class NamedMaskedConstantCollection(NamedConstantCollection):
    def __init__(self,TObject,pyClass,pyMask):
        self.pyMask=pyMask
        NamedConstantCollection.__init__(self,TObject,pyClass)
                                        
    @property
    def Mask(self):  # The mask of the collection 
        return self.pyMask[self.TObject.Mask.ToString()]
    
    def Remask(self,TMask):   # Produces a new collection with some additional objects masked 
        self.TObject.Remask(TMask) 
        
# * Checked   
class NamedMaskableConstantCollection(NamedMaskedConstantCollection):
    def __init__(self,TObject,pyClass,pyMask):
        self.pyMask=pyMask
        NamedMaskedConstantCollection.__init__(self,TObject,pyClass)
                                        
    @property
    def Mask(self):  # The mask of the collection 
        return self.pyMask[self.TObject.Mask.ToString()]
    
    @Mask.setter
    def Mask(self,TMask):
        self.TObject.Mask=TMask
    
    def Remask(self,TMask):   # Produces a new collection with some additional objects masked 
        self.TObject.Remask(TMask) 