#mixing and plotting of rotating and non-rotating supernova models at solar metallicity, to observe their effects
#import all required packages
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import decimal
#import the rotating and non rotating supernova yield data
with open('rot.txt.rtf', "r") as ins:
	array = []
	for line in ins:
		line = line.split()
		array.append(line)
#import the observation data
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

#clean up the imports of the supernova yields to make them easier to access later. As there are a large number of unneeded blank spaces.
for  i in range(0,10):
	array.pop(0)
array.pop(-1)
array[-1].pop(-1)
array[-1].pop(-1)
array[-1].pop(-1)
array[294].pop(0)
array[294].pop(0)
for i in range(0, len(array)):
	array[i].pop(-1)


#Do we want to use a rotating or non-rotating supernova yield?
sn = input("Rot. or Non.? ")
if str(sn) == "rot":
	rt = 0
	sn = "Rot."
else:
	rt = 1
	sn = "Non."

#create a lis tof possible masses of supernova yields to use.
mass = []
for i in range(3, len(array[0])):
	mass.append(array[0][i])
print(mass)

#in the supernova array it gives the mass of the isotopes from the yield, so i can simply use this instead of having to define a value from a seperate data file.
atm = []
for i in range(1 + (294 * rt), 209 + (294 * rt)):
	atm.append(int(array[i][0]))
atm = np.array(atm)

#choose the mass of supernova you want to use, don't have to choose metallicity as they are all solar.
x = input('Mass: ')

#define a list of the atomic masses of each ISOTOPE that are going to be mixed in
atm = [1.007825032, 2.014101778, 3.016029319, 4.002603254, 6.015122795, 7.01600455, 9.0121822, 12, 13.00335484, 14.003074, 15.0001089, 15.99491462, 16.9991317, 17.999161, 18.99840322, 19.99244018, 20.99384668, 21.99138511, 22.98976928, 23.9850417, 24.98583692, 25.98259293, 26.98153863, 27.97692653, 28.9764947, 29.97377017, 30.97376163, 31.97414808, 32.978, 33.978576, 35.9866, 34.96885268, 36.96590259, 35.96754511, 37.9627324, 39.96238312, 38.96370668, 39.96399848, 40.96182576, 39.96259098, 41.95861801, 42.9587666, 43.9554818, 45.9536926, 47.952534, 44.9559119, 45.9526316, 46.9517631, 47.9479463, 48.94787, 49.9447912, 49.9471585, 50.9439595, 49.9460442, 51.9405075, 52.9406494, 53.9388804, 54.9380451, 53.9396105, 55.9349375, 56.935394, 57.9332756, 58.933195, 57.9353429, 59.9307864, 60.931056, 61.9283451, 63.927966, 62.9295975, 64.9277895, 63.9291422, 65.9260334, 66.9271273, 67.9248442, 69.9253193, 68.9255736, 70.9247013, 69.9242474, 71.9220758, 72.9234589, 73.9211778,75]
#list of the initial mass fraction value of the abudnance of each element in the sun
esolx = [0.706, 0.21, 1.0000E-08, 1.6600E-10, 5.8000E-09, 3.0670E-03, 1.1140E-03, 9.6160E-03, 4.0500E-07, 1.7540E-03, 3.3400E-05, 6.6030E-04, 5.8100E-05, 7.1080E-04, 8.1600E-06, 4.1800E-04, 3.3850E-06, 9.2830E-05, 3.7390E-06, 6.1980E-05, 3.8900E-08, 2.9090E-06, 3.7790E-07, 1.7800E-05, 1.3300E-05, 1.2740E-03, 3.3600E-06, 7.3370E-05, 8.4000E-07, 2.0870E-06, 6.6700E-08, 2.0200E-07]
#define a list of the atomic masses of the elements in the solar twin to convert to the mass fraction from epsilon
atmsun = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.997, 20.180, 22.990, 24.305, 26.982, 28.085, 30.974, 32.06, 35.45, 39.948, 39.098, 40.078, 44.969, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.38, 69.723, 72.630]


atm = np.array(atm)
#define the inital hydrogen mass fraction as the mass fraction in the sun
hsol = 0.706
#initial = input("Initial: ")
#the scaled metalicity mass fraction of each element based upon the inital metallicity
ensolx = float(initial) * np.array(esolx)

#defines a list for the charge numbers to be appended to
num = []

#m defines a mass fraction list from the supernova
m = []
#set j to be a variable that can be used to add together the different isotope mass fractions of the same elements.
j = 0
#j1 is the final list of abundances after mixing
j1 = []
#k is an interating variable that is used in conjunction with j to add the mass fractions for different isotopes of the same element into the same mass fraction.
k = 0


#find the position value (b) of the mass that we choose
for i in range(0,len(mass)):
	if str(mass[i]) == x:
		b = i

#for all of the elements in the yield append them to a list
for i in range(1 + (294 * rt), 209 + (294 * rt)):
	m.append(float(array[i][b+2]))

#convert the mass in the yield of each element to the mass fraction by dividing by the mass of the total ejecta.
m = np.array(m)
m = m / sum(m)
hsn = m[0]

#Whether you want to see the decayed or non-decayed yields
d = input("Decay?")
if d == 1:
	#this is the part where we differ from suoernova.py. As the yields are taken of the supernova after a few seconds the elements do not decay into what we would observe today so in our yields we have large peaks that are unexplained by our observations.
	#we take the elements that would beta decay (as given in the week 5 section) and we take the ratio of the mass of the isotopes that would decay (to account for the mass loss throught the expulsion of the electron and the energy of the reaction).
	f = [45, 151, 145, 42, 33, 141]
	t = [43, 145, 137, 39, 30, 149]
	ratio = [26981538.63/26999230, 55939839.3/55942132, 55934937.5/55939839.3, 25982592.929/25986891.69, 21991385.114/21994436.4, 59933817.1/59934072]

	#if the element decays (from our above list) add the decayed mass to the daughter element
	for i in range(0,len(f)):
		m[t[i]] = m[t[i]] + ratio[i]*m[f[i]]
		m[f[i]] = 0


m = m / atm
#add different isotope yield mass fractions to the same position in the final abundance list
for i in range(1 + 294 * rt, 209 + 294 * rt):
	if str(array[i-1][0]) == "Charge":
		j = m[k]
	else:
		if array[i][1] == array[i-1][1]:
			j = j + (m[k])
		else:
			j1.append(j)
			j = (m[k])
	k += 1
j1.append(j)


#remove the first two entries as their pertain to hydrogen and helium, whos abundances we dont actually want to look at.
j1.pop(0)
j1.pop(0)


#make a charge number list from li to ge, the elements in the supernova yield list.
for  i in range(3, 33):
	num.append(i) 


#finding the mixing amount fron the abundance in hip and the initial metallcity

#the abundance of iron in hip
fex = xh[14]
#define the abundance of iron in the sun
felogex = np.log10(esolx[25]/atmsun[25]/0.706) + 12
#find the change in abundance of fe from the supernova that needs to be mixed into the sun get the abudance in hip
felogexsn = felogex + float(fex)
#convert the abundance to the mass fraction that needs to be mixed in
fexsn = 10**(felogexsn - 12) * hsol * atmsun[25]
#use the "reverse" of the mix used later in the  code to find the amount needed to mixed in
mix1 = (fexsn - ensolx[25])/((j1[23] * atmsun[25]) - fexsn)

#define a list for the mixed in amounts of the supernova yield into the protostellar gas
xhmixed=[]

#for all elements in the yield of the supernova
for i in range(0, len(j1)):
	#from the mass fraction of each element in the sun convert this to x value of that element.
	logxsun = np.log10(esolx[i + 2]/atmsun[i+2]/0.706) + 12
	#mix in the defined mixing amount into the mass fraction of each element in the sun from the supernova yield mass fraction.
	xnew = (ensolx[i + 2] + (mix1 * j1[i] * atmsun[i + 2]))/(1 + mix1)
	#convert this value to the x value of each element
	logxnew = np.log10(xnew/atmsun[i+2]/0.706) + 12
	#find the difference between the mixed value and the sun value to find the abundance/
	xhnew = logxnew - logxsun
	#append the newly found abundance to a list to be plotted later
	xhmixed.append(xhnew)

#decide what the label should say depending on whether you chose to decay the yields or not
if d == 1:
	plt.plot(num, new, label = 'Adjusted Decays with energy loss' + sn + " SN. Mass: " + x + " M" + r'$_{\odot}$' + " Metallicity: z = " + r'$z_\odot$' + " Mixing: " + str(mix))
else:
	plt.plot(num, new, label = 'Non-adjusted decays' + sn + " SN. Mass: " + x + " M" + r'$_{\odot}$' + " Metallicity: z = " + r'$z_\odot$' + " Mixing: " + str(mix))

#plot the HIP observations
plt.plot(chargeno, xh, label= 'Observation data')

#give some axis labels
plt.xlabel('Charge No.')
plt.ylabel('[X/H] Following Mixing')

#show the legend
plt.legend(loc = 'best')	