basta = float(input("Any number: "))

import math

def GradesRoundOff(basta, decimals=0):
    multiplier = 10**decimals
    return math.floor(basta*multiplier + 0.5)/multiplier

Roundedoff = GradesRoundOff(basta)

print(int(Roundedoff))


