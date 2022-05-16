import numpy as np
NUMTYP=(int,float)
                # s     m     kg    A     K   
SCALAR=np.array([ 0  ,  0  ,  0  ,  0  ,  0  ])
class SIUNITX:
    def __init__(self,scl,unt=SCALAR):
        if isinstance(scl,NUMTYP): self.scl=scl
        else: raise ValueError("Invalid initializer")
        if isinstance(unt,np.ndarray):
            self.siu=unt.copy()
        elif isinstance(unt,SIUNITX):
            self.siu=unt.siu.copy()
            self.scl*=unt.scl
        else: raise ValueError("Invalid initializer")
    def __add__(self,other):
        if isinstance(other,NUMTYP):
            if not np.array_equal(SCALAR,self.siu):
                raise ValueError("Dimension mismatch")
            return SIUNITX(self.scl+other,self.siu)
        elif isinstance(other,SIUNITX):
            if not np.array_equal(other.siu,self.siu):
                raise ValueError("Dimension mismatch")
            return SIUNITX(self.scl+other.scl,self.siu)
        else: raise ValueError("Invalid + operation")
    def __radd__(self,other):
        return self.__add__(other)
    def __sub__(self,other):
        if isinstance(other,NUMTYP):
            if not np.array_equal(SCALAR,self.siu):
                raise ValueError("Dimension mismatch")
            return SIUNITX(self.scl-other,self.siu)
        elif isinstance(other,SIUNITX):
            if not np.array_equal(other.siu,self.siu):
                raise ValueError("Dimension mismatch")
            return SIUNITX(self.scl-other.scl,self.siu)
        else: raise ValueError("Invalid - operation")
    def __rsub__(self,other):
        if isinstance(other,NUMTYP):
            if not np.array_equal(SCALAR,self.siu):
                raise ValueError("Dimension mismatch")
            return SIUNITX(other-self.scl,self.siu)
        elif isinstance(other,SIUNITX):
            if not np.array_equal(other.siu,self.siu):
                raise ValueError("Dimension mismatch")
            return SIUNITX(other.scl-self.scl,self.siu)
        else: raise ValueError("Invalid - operation")
    def __mul__(self,other):
        if isinstance(other,NUMTYP):
            return SIUNITX(other*self.scl,self.siu)
        elif isinstance(other,SIUNITX):
            return SIUNITX(other.scl*self.scl,self.siu+other.siu)
        else: raise ValueError("Invalid * operation")
    def __rmul__(self,other):
        return self.__mul__(other)
    def __truediv__(self,other):
        if isinstance(other,NUMTYP):
            return SIUNITX(self.scl/other,self.siu)
        elif isinstance(other,SIUNITX):
            return SIUNITX(self.scl/other.scl,self.siu-other.siu)
        else: raise ValueError("Invalid / operation")
    def __rtruediv__(self,other):
        if isinstance(other,NUMTYP):
            return SIUNITX(other/self.scl,-self.siu)
        elif isinstance(other,SIUNITX):
            return SIUNITX(other.scl/self.scl,other.siu/self.siu)
        else: raise ValueError("Invalid / operation")
    def __pow__(self,other):
        return SIUNITX(self.scl**other,self.siu*other)
    def __str__(self):
        stro="%e"%(self.scl)
        if self.siu[0]!=0: stro+=" s^"+str(self.siu[0])
        if self.siu[1]!=0: stro+=" m^"+str(self.siu[1])
        if self.siu[2]!=0: stro+=" kg^"+str(self.siu[2])
        if self.siu[3]!=0: stro+=" A^"+str(self.siu[3])
        if self.siu[4]!=0: stro+=" K^"+str(self.siu[4])
        return stro
    def __repr__(self):
        return self.__str__()
                                                                        # s     m     kg    A     K   
Second                 =  SIUNITX(1                           ,np.array([ 1  ,  0  ,  0  ,  0  ,  0  ]))
Metre                  =  SIUNITX(1                           ,np.array([ 0  ,  1  ,  0  ,  0  ,  0  ]))
Kilogram               =  SIUNITX(1                           ,np.array([ 0  ,  0  ,  1  ,  0  ,  0  ]))
Ampere                 =  SIUNITX(1                           ,np.array([ 0  ,  0  ,  0  ,  1  ,  0  ]))
Kelvin                 =  SIUNITX(1                           ,np.array([ 0  ,  0  ,  0  ,  0  ,  1  ]))
AvogadroConstant       =  SIUNITX(6.02214076e23               ,np.array([ 0  ,  0  ,  0  ,  0  ,  0  ]))
Joule                  =  SIUNITX(1                           ,np.array([-2  ,  2  ,  1  ,  0  ,  0  ]))
Electronvolt           =  SIUNITX(1.602176634e-19             ,np.array([-2  ,  2  ,  1  ,  0  ,  0  ]))
Hartree                =  SIUNITX(4.3597447222071e-18         ,np.array([-2  ,  2  ,  1  ,  0  ,  0  ]))
Kilocalories           =  SIUNITX(4184                        ,np.array([-2  ,  2  ,  1  ,  0  ,  0  ]))
KilocaloriesPerMole    =  SIUNITX(4184/6.02214076e23          ,np.array([-2  ,  2  ,  1  ,  0  ,  0  ]))
Angstrom               =  SIUNITX(1e-10                       ,np.array([ 0  ,  1  ,  0  ,  0  ,  0  ]))
Femtosecond            =  SIUNITX(1e-15                       ,np.array([ 1  ,  0  ,  0  ,  0  ,  0  ]))
Dalton                 =  SIUNITX(1.66053906660e-27           ,np.array([ 0  ,  0  ,  1  ,  0  ,  0  ]))
MassOfElectron         =  SIUNITX(9.1093837015e-31            ,np.array([ 0  ,  0  ,  1  ,  0  ,  0  ]))
BoltmannConstant       =  SIUNITX(1.380649e-23                ,np.array([-2  ,  2  ,  1  ,  0  , -1  ]))
SpeedOfLight           =  SIUNITX(299792458                   ,np.array([-1  ,  1  ,  0  ,  0  ,  0  ]))
ElectricConstant       =  SIUNITX(8.8541878128e-12            ,np.array([ 4  , -3  , -1  ,  2  ,  0  ]))
ElementaryCharge       =  SIUNITX(1.602176634e-19             ,np.array([ 1  ,  0  ,  0  ,  1  ,  0  ]))
PlanckConstant         =  SIUNITX(6.62607015e-34              ,np.array([-1  ,  2  ,  1  ,  0  ,  0  ]))
ReducedPlanckConstant  =  SIUNITX(6.62607015e-34/(2*np.pi)    ,np.array([-1  ,  2  ,  1  ,  0  ,  0  ]))
BohrMagneton           =  SIUNITX(9.2740100783e-24            ,np.array([ 0  ,  2  ,  0  ,  1  ,  0  ]))
Tesla                  =  SIUNITX(1                           ,np.array([-2  ,  0  ,  1  , -1  ,  0  ]))
BohrRadius             =  SIUNITX(5.29177210903e-11           ,np.array([ 0  ,  1  ,  0  ,  0  ,  0  ]))
FineStructureConstant  =  SIUNITX(0.0072973525                ,np.array([ 0  ,  0  ,  0  ,  0  ,  0  ]))
KilogramPerCubicmetre  =  SIUNITX(1                           ,np.array([ 0  , -3  ,  1  ,  0  ,  0  ]))
