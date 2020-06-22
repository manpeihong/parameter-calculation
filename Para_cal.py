import numpy as np

class CalParameters: 
    def __init__(self, T=300, x=0.2): 
        self.list_of_paras = ["ELECTRON_AFFINITY", "STATIC_PERMITIVITY", "ELECTRON_MOBILITY", 
                              "HOLE_MOBILITY", "ELECTRON_AUGER_COEFFICIENT", "HOLE_AUGER_COEFFICIENT", 
                              "RAD_RECOMB_CONST", "ELECTRON_DOS_MASS", "HOLE_DOS_MASS",
                              "CONDUCTION_BAND_EFFECTIVE_DENSITY_OF_STATES", 
                              "VALENCE_BAND_EFFECTIVE_DENSITY_OF_STATES"]
        # NAME IN SIMWINDOWS (NAME IN PADRE)
        # ELECTRON_AFFINITY (AFFINITY)
        self.ELECTRON_AFFINITY =4.23-0.813*((-0.302+1.93*x-0.81*x*x+0.832*x*x*x+5.35e-4*T*(1-2*x))-0.083)
        # STATIC_PERMITIVITY (PERMITTI)
        self.STATIC_PERMITIVITY=20.5-15.5*x+5.7*x*x
        # ELECTRON_MOBILITY (MUN)
        self.ELECTRON_MOBILITY =(9.0e8*(0.2/x)**7.5)/(T**(2*(0.2/x)**0.6))
        # HOLE_MOBILITY (MUP)
        self.HOLE_MOBILITY=(9.0e8*(0.2/x)**7.5)/(T**(2*(0.2/x)**0.6))/(-0.6+6.333*((2.0/(-0.302+1.93*x-0.81*x*x+0.832*x*x*x+5.35e-4*T*(1-2*x)))+(1.0/((-0.302+1.93*x-0.81*x*x+0.832*x*x*x+5.35e-4*T*(1-2*x))+1.0))))/0.5
        # ELECTRON_AUGER_COEFFICIENT (AUGN)
        self.ELECTRON_AUGER_COEFFICIENT=3.33e-25-(x-.2)*2.83e-24
        # HOLE_AUGER_COEFFICIENT (AUGP)
        self.HOLE_AUGER_COEFFICIENT=3.33e-26-(x-.2)*2.83e-25
        # RAD_RECOMB_CONST (B0dir)
        self.RAD_RECOMB_CONST=1.07587e-10
        # ELECTRON_DOS_MASS
        self.ELECTRON_DOS_MASS=1.0/(-0.6+6.333*((2.0/(-0.302+1.93*x-0.81*x*x+0.832*x*x*x+5.35e-4*40.*(1-2*x)))+(1.0/((-0.302+1.93*x-0.81*x*x+0.832*x*x*x+5.35e-4*40.*(1-2*x))+1.0))))
        # self.ELECTRON_DOS_MASS = 0.01249
        # HOLE_DOS_MASS
        self.HOLE_DOS_MASS=0.55
        # self.HOLE_DOS_MASS=0.5
        # CONDUCTION_BAND_EFFECTIVE_DENSITY_OF_STATES
        me = 9.11e-31 # (Kg)
        k = 1.380649e-23 # (J/K)
        h = 6.62607004e-34 # (J.s)
        # h = 4.135667696e-15 # (eV.s)
        self.CONDUCTION_BAND_EFFECTIVE_DENSITY_OF_STATES = (2*np.pi*self.ELECTRON_DOS_MASS*me*k*T/h/h)**1.5 * 2 / 1000000
        # VALENCE_BAND_EFFECTIVE_DENSITY_OF_STATES
        self.VALENCE_BAND_EFFECTIVE_DENSITY_OF_STATES = (2*np.pi*self.HOLE_DOS_MASS*me*k*T/h/h)**1.5 * 2 / 1000000
        
    def printall(self): 
        for para in self.list_of_paras: 
            print("{}: {}".format(para, getattr(self, "{}".format(para))))



def main():
    CalParameters(T=300, x=0.21).printall()


if __name__ == '__main__':
    main()

