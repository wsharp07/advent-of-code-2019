from module1 import Module1
from module2 import Module2

m1 = Module1()
m2 = Module2()

filename = "../input/input1.txt"
totalFuel = 0

with open(filename) as f:
    content = f.readlines()

for line in content:
    totalFuel += m1.getRecursiveFuel(int(line))



#print(m1.getFuelRequired(21))
print(totalFuel)