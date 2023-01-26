from collections.abc import Sequence

class INamedCollection(Sequence):
    def __init__(self,INamed):
        self.INamed=INamed
        super().__init__()

    def __getitem__(self, i):
        return self.INamed[i]
    
    def __len__(self):
        return len(self.INamed)

class INamedConstantCollection(Sequence):
    def __init__(self,INamedConstant,IClass):
        # INamedConstant is .NET instance, IClass is the type decorator for python wrapper
        self.INamedConstant=INamedConstant
        self.IClass=IClass
        super().__init__()

    def __getitem__(self, i):
        return self.IClass(self.INamedConstant[i])
    
    def __len__(self):
        return len(self.INamedConstant)

class INamedMaskableConstantCollection(Sequence):
    def __init__(self,INamedMaskableConstant):
        self.INamedMaskableConstant=INamedMaskableConstant
        super().__init__()

    def __getitem__(self, i):
        return self.INamedMaskableConstant[i]
    
    def __len__(self):
        return len(self.INamedMaskableConstant)

class INamedMaskedConstantCollection(Sequence):
    def __init__(self,INamedMaskedConstant):
        self.INamedMaskedConstant=INamedMaskedConstant
        super().__init__()

    def __getitem__(self, i):
        return self.INamedMaskedConstant[i]
    
    def __len__(self):
        return len(self.INamedMaskedConstant)