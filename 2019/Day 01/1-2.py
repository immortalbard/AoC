'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
import math

def fuelamt(mass):
    fuel=math.floor((int(mass)/3))-2
    
    return int(fuel)

def truefuel(mass):
    i=0
    fuel=[fuelamt(mass)]
    truefuel=0
    
    while fuel[i]>0:
        if fuelamt(fuel[i])<0:
            break
        else:
            fuel.append(fuelamt(fuel[i]))
        
        i+=1
        
    
    for f in fuel:
        truefuel+=int(f)
    
    return truefuel

masses=[100725,63593,84738,143809,108595,94419,91617,91573,102728,143383,74613,80331,76530,139884,104607,107171,107640,87284,120827,85742,62474,97582,110668,73426,57656,70819,89848,138732,54386,116905,107954,131488,75056,97660,55295,146265,58026,94712,73636,138077,61480,148868,119364,145430,103901,134202,106759,50254,82440,117801,80263,97022,145229,57702,57460,58401,145652,127341,123585,65291,70219,147009,88728,72059,83815,99635,80913,149475,61798,110054,102505,148511,95160,50208,129867,57079,138435,75865,63185,142389,78370,108077,106438,86267,100785,101165,68501,146079,122420,121429,62608,115338,90667,131391,50260,85343,76411,94432,130126,80915]

testmasses=[1969,100756]

fuels=[]
totalfuel=0

for m in masses:
    fuels.append(truefuel(m))
    totalfuel+=truefuel(m)
    
print(totalfuel)