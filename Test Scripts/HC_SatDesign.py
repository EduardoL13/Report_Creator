# Libraries
import numpy as np
import englib.profile as ge
import sympy as smp
from pathlib import Path



# Assignment 5: Sizing  communications satellite

# CLASES Y FUNCIONES -----------------------------------------
# Estas funciones se definen aquí para resolver preguntas de las tareas, pero la idea es extraer de acá la info que puedea
# ser releveante para los design modules. Hay funciones que puede que no se empleen en el desarrollo de la tarea.
class material():
    def __init__(self,E,sigmaUlt):
        self.E = E
        self.UltimateStress = sigmaUlt
    

class satLaunchDesign():
    
    def setMaterial(self,material):
        self.Material = material # Recibe de input un objeto de clase material
        
    # def setSectionalGeometry(self,geometry):
    #     self.SectionalGeometry = geometry # Recibe de input un objeto de clase profile (importado del módulo de englib)
    
    def setDiameter(self,diameter):
        self.Diameter = diameter
    
    def setOverallDimensions(self,height):
        self.Height = height
        
    def setMass(self,mass):
        self.Mass = mass
    
    def setIntertia(self,thk):
        self.Inertia = np.pi*1/8*self.Diameter**3*thk
    
    def setSectionalArea(self,thk):
        self.AreaSection = np.pi*self.Diameter*thk
    
    # def setGs(gLoad):
    #     self.Load = gLoad # Load expressed as acceleration in gs
        
    def calcWallThkForCriticNatFreq(self,criticFreq,loadCase = "axial"):
        # Calculates wall thickness for a thin walled round tube
        if loadCase == "axial":
            thkWall = 4*np.pi*criticFreq**2*self.Height*self.Mass * 1/(self.Material.E*self.Diameter)
            return thkWall
        if loadCase == "lateral":
            thkWall = 32*np.pi*criticFreq**2*(self.Height)**3*self.Mass * 1/(3*self.Material.E*self.Diameter**3)
            return thkWall
        
    def calcEulerLoading(self):
        eulerF = np.pi**(2)*self.Material.E*self.Inertia * 1/(4*self.Height**2)
        return eulerF
    





# Axial direction constraints and BC

freqNatAxial = 27 #[Hz] Frecuencia natural al despegue (sentido axial)
accelAxial = 6.5 #[g's] Aceleraciones en gs al despegue (sentido axial)

# Lateral direction constraints and BC

freqNatLat = 10 #[Hz] Frecuencia natural al despegue (sentido axial)
accelLat = 2 #[g's] Aceleraciones en gs al despegue (sentido axial)

g = 9.81 #[m/s**2]
sf = 2 #Safety Factor

# Assumptions: 
# - The satellite can de modelled as a point mass on top of a thin walled cylinder with mass and dimensions:

massSatellite = 6000 #[kg]
heightSatellite = 4#[m]
diameterSatellite = 2 #[m]

# Material properties

E = 72 #[GPa] Módulo de Young del material
stressUlt = 483 #[MPa] Esfuerzo último del material

E = E * 10**9 #[Pa]
stressUlt = stressUlt * 10**6 #[Pa]





# Questions
# Set Problem conditions

materialSat = material(E,stressUlt)

launchSat = satLaunchDesign()
launchSat.setMaterial(materialSat)
launchSat.setDiameter(diameterSatellite)
launchSat.setMass(massSatellite)
launchSat.setOverallDimensions(heightSatellite)



# Case: Axial Launch critical natural frequency
# 1. Calculate minimum thickness (cylinder) for the axial launch scenario

thkForCriticFreq = launchSat.calcWallThkForCriticNatFreq(freqNatAxial) #[m]

# Point 1. Answer
print("Thk For critical frequencies for axial case at launch [mm] = ",thkForCriticFreq*10**3)

# Case: Lateral Launch critical nautural frequency
# 1. Calculate minimum thickness (cylinder) for the axial launch scenario

thkForCriticFreqLat = launchSat.calcWallThkForCriticNatFreq(freqNatLat, loadCase = "lateral") #[m]

# Point 2. Answer
print("Thk For critical frequencies for lateral case at launch [mm] = ",thkForCriticFreqLat*10**3)



# Cálculo mediante sympy para confirmar------------------------------------

# t,tl = smp.symbols('t tl', real=True, positive=True)

# exp_axial = 1/(2*np.pi)*(E*np.pi*diameterSatellite*t/(heightSatellite*massSatellite))**(1/2) - freqNatAxial

# thkForCriticFreqSmp = smp.solve(exp_axial,t)[0]

# print("Thk For critical frequencies for axial case at launch (Sympy solution) [mm] = ",thkForCriticFreqSmp*10**3)

# exp_lat =  1/(2*np.pi)*(3*E*np.pi*diameterSatellite**(3)/8*tl/(heightSatellite**3*massSatellite))**(1/2) - freqNatLat

# thkForCriticFreqLatSmp = smp.solve(exp_lat,tl)[0]

# print("Thk For critical frequencies for lateral case at launch (Sympy solution) [mm] = ",thkForCriticFreqLatSmp*10**3)

#----------------------------------------------------------------------------

# Point 3. Answer
thk = max([thkForCriticFreq,thkForCriticFreqLat]) #[mm] greater thickness among the optional thicknesses

# Case: Buckling caused by axial dynamic forces
axialGs = 6.5 # Axial acceleration normalized by g acceleration
loadAxial = launchSat.Mass*axialGs*g # [N] Axial loading

launchSat.setIntertia(thk) # Set Satellite inertia with the chosen critical thickness for naural frequencies
loadEuler = launchSat.calcEulerLoading() #[N]

boolResult = loadEuler>loadAxial
boolResult = str(boolResult)

# Point 4 Answer
print("It is " + boolResult + " that the chosen wall thickness withstand the buckling conditions")


# Check Stress calculation

latGs = 2
loadLateral = launchSat.Mass*latGs*g
launchSat.setSectionalArea(thk)


stressAxial = loadAxial/launchSat.AreaSection #[pa]
stressLat = loadLateral*launchSat.Height*launchSat.Diameter/2 * 1/launchSat.Inertia #[pa]

stressSum = stressAxial + stressLat #[pa]

stressAllowable = launchSat.Material.UltimateStress *1/sf

boolStressResult = stressAllowable > stressSum
boolStressResult = str(boolStressResult)

# Point 5 answer
print("It is " + boolStressResult + " that the current material strength can withstand the stress conditions")


# --------------CREATE CALCULATIONS REPORT--------------------

# r al inicio es para raw string


tex_file = Path("C:\\Users\\ELC\\Documents\\ModulesEL\\repDoc\\TestsScripts\\report2Test.tex")


# Strings of variables
stringVarMassSatellite = f"{massSatellite}"
stringVarHeightSatellite = f"{launchSat.Height}"
stringVarDiameterSatellite = f"{launchSat.Diameter}"
stringVarMaterialESatellite = f"{launchSat.Material.E *1/(10**9)}"
stringVarMaterialStressUltSatellite = f"{launchSat.Material.UltimateStress * 1/(10**6)}"

# Strings of results
stringThkForCriticFreq = f"{round(thkForCriticFreq * 10**3,2)}"
