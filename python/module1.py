import math

class Module1:
    def getFuelRequired(self, mass ):
        return math.floor(mass / 3) - 2
    
    def getRecursiveFuel(self, mass):
        return self.recursiveFuel(mass, 0)

    def recursiveFuel(self, mass, fuel):
        tempMass = self.getFuelRequired(mass);

        if (tempMass <= 0):
            return fuel
        
        fuel += tempMass;
        
        return self.recursiveFuel(tempMass, fuel)

