#Scatter plot of abundance vs condensation temperature code
#import all required packages
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import decimal
#supernova yield data
with open('YIELD_CK13.dat.txt', "r") as ins:
	array = []
	for line in ins:
		line = line.split()
		array.append(line)
#observation data
with open('obsdata.txt', "r") as ins:
	array2 = []
	for line in ins:
		line = line.split()
		array2.append(line)
chargeno = []
tcond = []
xh = []
error=[]

#define the positions of the elements that are being plotted from hip based upon their relative positions in the mixing abundance list
q = [6,8,11,12,13,14,16,19,20,21,22,23,24,25,26,27,28,29,30]
q = np.array(q)
q = q-2
print(q)


#define the lists of the charge number, condensation temp, abundance and error values for hip.
for i in range(1, len(array2)):
	chargeno.append(float(array2[i][0]))
	tcond.append(float(array2[i][2]))
	xh.append(float(array2[i][3]))
	error.append(float(array2[i][4]))
xh = np.array(xh)
tcond = np.array(tcond)
chargeno = np.array(chargeno)


#define the elemental names that will be attached to the data points
obslabel = ['C', 'O', 'Na', 'Mg', 'Al', 'Si', 'S', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Sr', 'Y', 'Zr', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Sm']

#plot the negative abundance vs condensation temperature plot to be more in line with the sun - <solar twin> abundance in the peculiarity paper
plt.errorbar(tcond, xh, yerr=error, capsize=4, fmt = 'o', label='HIP Abundance')
for i in range(0, len(obslabel)):
	xy = (tcond[i], xh[i])
	plt.annotate(obslabel[i], xy)


linex=np.array([100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700])
liney=linex*0.000038-0.08
#plot a line at T=1200K the refractory vs volatile line
plt.plot(linex,liney,linestyle='dashed', label='Abundance vs Condensation temperature fitting line', color='C2')
plt.axvline(x=1200, linestyle='dashed', color='#ff7f0e')
plt.annotate('Voltatile',(1000,0.0))
plt.annotate('Refractory',(1250,0.0))

#label axis'
plt.xlabel('Condensation Temperature of Element (K)')
plt.ylabel('[X/H]')
plt.legend(loc = 'best')