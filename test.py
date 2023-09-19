import math

combinedData = "3.09327738688E+009,7.72990113024E+009,2.498936E+000,-5.778590E+000,1.00000000000E+006"

separatedData = combinedData.split(',')

loadedQFactor = float(separatedData[2])

couplingS21 = separatedData[3]  # CALC1:PAR1:MARK1:Y? # -5.778590E+000

power = float(couplingS21) / 20

unloadedQ = loadedQFactor * (1 / (1 - math.pow(10, power)))

print(unloadedQ)

# peakFrequency = self.calculatePeakFq(frequency)