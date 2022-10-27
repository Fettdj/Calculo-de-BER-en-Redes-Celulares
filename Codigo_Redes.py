#Functions 
from math import log
from math import factorial

#Imputs 
A = 2 # Numero de antenas
B = 15*10**3 # Channel bandwidth for 4g

Ptmax = 23 # Maximum transmission power 
TargetBER = 1*10**(-4) #Target BER

No = 4.004*10**(-21) #Noise Power Spectral Density
M = 2 # BPS Modulation order
K = 1 #Propagation Factor 
beta = 4.5 # Propagation exponent 

# Obtaining the Eb/No from the BER expression

BER = 1
EbNo = 0.1

while BER > TargetBER:
  acum = 0 
  u = (EbNo/(A+EbNo))**(1/2)
  for k in range(A):
    acum = acum + (factorial(A-1+k)/(factorial(A-1)*factorial(k))) * ((1+u)/2)**k
  BER = (((1-u)/2)**A)*acum
  EbNo = EbNo + 0.1

#Calculating the Recieved Power
Pr = No * (B+log(M,2)) * EbNo #in Watts 

#Calculating the maximum coverage radies
Pt = 0
r = 0.1
PtMaxW = (10**(Ptmax/10))/1000 #Para transformar de dBm a Watts
while Pt < PtMaxW:
  Pt = (1/K)*Pr*r**beta
  r = r + 0.1
print('The maximum coverage radius is ' + str("{:.2f}".format(r)) + ' meters')