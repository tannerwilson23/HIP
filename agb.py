#mixing and gce offset code for the AGB (and supernova) mixing

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

#import observation data of HIP
with open('obsdata.txt', "r") as ins:
	array2 = []
	for line in ins:
		line = line.split()
		array2.append(line)

#define and append the charge number, condensation temperature, abundance and error from the observation data of hip to their own lists.
chargeno = []
tcond = []
xh = []
error = []
for i in range(1, len(array2)):
	chargeno.append(float(array2[i][0]))
	tcond.append(float(array2[i][2]))
	xh.append(float(array2[i][3]))
	error.append(float(array2[i][4]))
xh = np.array(xh)
tcond = np.array(tcond)
chargeno = np.array(chargeno)

#create a list for the possible supernova metallicities
metallicity = []
for i in range(0+6*sn,6+6*sn):
	metallicity.append(float(array[87*i][1]))

with open('agb.txt', "r") as ins:
	arrayagb = []
	for line in ins:
		line = line.split()
		arrayagb.append(line)

#we are only choosing sn=1, we could initally chose between agb and sn in the past from YIELD_CK13. The AGB yields YIELD_CK13 do not give us as many elements to work with or as many masses as agb.txt
sn = 1

#a remnant of when we would choose the AGB at the begining of the the running of the script. Now we have a predefined value of the mass of C13 mixing region (which is still an experimental variable), the mass of the AGB and the metallicity (however this is fixed to the one value Amanda gave to me which seems to best fit the data)
magb =[]
metalagb=0.0070
mixagb=[]

for i in arrayagb:
    if i[1] == 'Initial':
        magb.append(i[4])
        mixagb.append(i[13])

#define a list for the charge numbers of the elements that can be used later
num=[]

#define a list of the atomic masses of each ISOTOPE that are going to be mixed in
atm = [1.007825032, 2.014101778, 3.016029319, 4.002603254, 6.015122795, 7.01600455, 9.0121822, 12, 13.00335484, 14.003074, 15.0001089, 15.99491462, 16.9991317, 17.999161, 18.99840322, 19.99244018, 20.99384668, 21.99138511, 22.98976928, 23.9850417, 24.98583692, 25.98259293, 26.98153863, 27.97692653, 28.9764947, 29.97377017, 30.97376163, 31.97414808, 32.978, 33.978576, 35.9866, 34.96885268, 36.96590259, 35.96754511, 37.9627324, 39.96238312, 38.96370668, 39.96399848, 40.96182576, 39.96259098, 41.95861801, 42.9587666, 43.9554818, 45.9536926, 47.952534, 44.9559119, 45.9526316, 46.9517631, 47.9479463, 48.94787, 49.9447912, 49.9471585, 50.9439595, 49.9460442, 51.9405075, 52.9406494, 53.9388804, 54.9380451, 53.9396105, 55.9349375, 56.935394, 57.9332756, 58.933195, 57.9353429, 59.9307864, 60.931056, 61.9283451, 63.927966, 62.9295975, 64.9277895, 63.9291422, 65.9260334, 66.9271273, 67.9248442, 69.9253193, 68.9255736, 70.9247013, 69.9242474, 71.9220758, 72.9234589, 73.9211778,75]
#list of the initial mass fraction value of the abudnance of each element in the sun
esolx = [0.706, 0.21, 1.0000E-08, 1.6600E-10, 5.8000E-09, 3.0670E-03, 1.1140E-03, 9.6160E-03, 4.0500E-07, 1.7540E-03, 3.3400E-05, 6.6030E-04, 5.8100E-05, 7.1080E-04, 8.1600E-06, 4.1800E-04, 3.3850E-06, 9.2830E-05, 3.7390E-06, 6.1980E-05, 3.8900E-08, 2.9090E-06, 3.7790E-07, 1.7800E-05, 1.3300E-05, 1.2740E-03, 3.3600E-06, 7.3370E-05, 8.4000E-07, 2.0870E-06, 6.6700E-08, 2.0200E-07]
#define a list of the atomic masses of the elements in the solar twin to convert to the mass fraction from epsilon
atmsun = [1.008, 4.0026, 6.94, 9.0122, 10.81, 12.011, 14.007, 15.999, 18.997, 20.180, 22.990, 24.305, 26.982, 28.085, 30.974, 32.06, 35.45, 39.948, 39.098, 40.078, 44.969, 47.867, 50.942, 51.996, 54.938, 55.845, 58.933, 58.693, 63.546, 65.38, 69.723, 72.630]

#add to these lists with the data from the sun for higher mass elements that arent used in the supernova case (I did them by hand for the supernova case but found an easier way using another data file for the heavier elements but didnt want to mess up the ordering so i didnt get rid of the lists for the supernova case.)
with open('solarabun.dat', "r") as ins:
	array3 = []
	for line in ins:
		line = line.split()
		array3.append(line)
for i in range(33, len(array3)):
	if i == 36 or i == 54: 
		esolx.append(10**(float(array3[i][2])-12)*0.706*float(array3[i][1]))
		atmsun.append(float(array3[i][1]))
	else:
		esolx.append(10**(float(array3[i][4])-12)*0.706*float(array3[i][1]))
		atmsun.append(float(array3[i][1]))


#define a list of the charge numbers of the elements that is going to be the x axis of the abundance plot.
for  i in range(3, len(atmsun)):
	num.append(i)

#set the initial metallicity of the protostellar cloud, usually set to a range of values and plots are made for each, 0.79 gave the best mixing so it was kept as such.
initials = [0.79]

#run the mixing for each value of the initial metallicity of the protostellar dust
for initial in initials:
	#create a figure for each value of initial metallicity
	plt.figure()

	#jk defines which AGB model to use, 10 was found to give the best fitting so it was defined for all cases so we could ignore it when looking at other variables.
	jk = 10

	#we know that the supernova needs to be high mass and low metallicity so we just set these to be 40 msun and metallicity = 0.001 instead of setting them to be this each time.
	#this choice gives the best fitting for the odd even effect.

	#y = input("Input Metallicity")
	y = '0.001'
	#x = input("Input mass")
	x= '40.'


	#define a list to hold the mass fractions of each of the elements from the yield of the AGB
	xagb=[]

	#append the mass fractions for each element for the yield of the AGB to a single list and where there is gaps (i.e. an element is not created) append a 0 so we dont have gaps we have to account for in our data later.
	for i in range(3 + (83*jk), 81 + (83*jk)):
		if i == (5 + (83*jk)):
			xagb.append(float(0))
			xagb.append(float(0))
			xagb.append(float(0))
		if i == (42 + (83*jk)) or i == (59 + (83*jk)):
			xagb.append(float(0))
		xagb.append(float(arrayagb[i][5]))



	#m defines a mass fraction list from the supernova
	m = []
	#set j to be a variable that can be used to add together the different isotope mass fractions of the same elements.
	j = 0
	#j1 is the final list of abundances after mixing
	j1 = []
	#k is an interating variable that is used in conjunction with j to add the mass fractions for different isotopes of the same element into the same mass fraction.
	k = 0

	#a remnant of when we were able to define different supernova masses and metallicities so that we define the position in the large supernova mass fraction array, b and c define the positions.
	for i in range(0,len(mass)):
		if str(mass[i]) == x:
			b = i
	for i in range(0, len(metallicity)):
		if str(metallicity[i]) == y:
			c = i

	#iterate over all elements possible for the supernova of the specific mass and metallicity.
	for i in range(4 + 87 * (6 * sn) + 87 * c , 86 + 87 * (6 * sn) + 87 * c):
		m.append(float(array[i][b+2]))
	m = np.array(m)
	#convert the masses into mass fractions
	m = m / sum(m)
	#hydrogen mass fraction in supernova yield mass fraction list
	hsn = m[0]
	#doing this definition now just saves a few uses later on.
	m = m/atm
	#add different isotope yield mass fractions to the same position in the final abundance list
	for i in range(4 + 87 * (6 * sn) + 87 * c , 86 + 87 * (6 * sn) + 87 * c):
		if str(array[i-1][0]) == "Mrem":
			j = m[k]
		else:
			if array[i][0] == array[i-1][0]:
				j = j + (m[k])
			else:
				j1.append(j)
				j = (m[k])
		k += 1
	j1.append(j)
	#remove the first two entries as their pertain to hydrogen and helium, whos abundances we dont actually want to look at.
	j1.pop(0)
	j1.pop(0)

	#the scaled metalicity mass fraction of each element based upon the inital metallicity
	ensolx = initial * np.array(esolx)

	#finding the mixing amount fron the abundance of iron in hip and the initial metallcity

	#the abundance of iron in hip
	fex = xh[14]
	#define the abundance of iron in the sun
	felogex = np.log10(esolx[25]/atmsun[25]/0.706) + 12
	#find the change in abundance of fe from the supernova that needs to be mixed into the sun get the abudance in hip
	felogexsn = felogex + float(fex)
	#convert the abundance to the mass fraction that needs to be mixed in
	fexsn = 10**(felogexsn - 12) * 0.706 * atmsun[25]
	#use the "reverse" of the mix used later in the  code to find the amount needed to mixed in
	mix1 = (fexsn - ensolx[25])/((j1[23] * atmsun[25]) - fexsn)


	#finding the mixing amound from the abundnace of barium in hip after the mixing of the supernova yield

	#the abundance of barium in hip
	bax = xh[22]
	#define the abundance of barium in the sun
	balogex = np.log10(esolx[55]/atmsun[55]/0.706) + 12
	#find the change in abundance of ba from the AGB that needs to be mixed into suopernova mixed yield get the abudance in hip
	balogexagb = balogex + float(bax)
	#convert the abundance to the mass fraction that needs to be mixed in
	baxagb = 10**(balogexagb - 12) * 0.706 * atmsun[55]
	# use the "reverse" of the mix used later in the  code to find the amount needed to mixed in
	mix2 = (baxagb - ensolx[55])/(xagb[55] - baxagb)


	#if we only want to mix the AGB into the yield we simply set mix1 (the iron mixing amount) to 0 instead of creating its own code.
	mix1 = 0.0

	#define a list that will hold the abundances of the elements following the mixing into the protostellar gas.
	xhmixed=[]

	#for all of the elements in the list of elements that are in the yield of the AGB
	for i in range(2, len(xagb)):
		#define the logx of the element in the sun
		logxsun = np.log10(esolx[i]/atmsun[i]/0.706) + 12
		#always mix in the amount of AGB determined from the Ba
		xnew = (ensolx[i] + (mix2 * xagb[i]))/(1 + mix2)
		#if the element is in the supernova yield also mix in the amount required to get the iron level of the model up to the level of HIP.
		if i < len(j1):
			xnew2 = (xnew + (mix1 * j1[i] * atmsun[i + 2]))/(1 + mix1)
			logxnew = np.log10(xnew2/atmsun[i]/0.706) + 12
		else:
			logxnew = np.log10(xnew/atmsun[i]/0.706) + 12
		xhnew = logxnew - logxsun
		xhmixed.append(xhnew)

	#define a new list initially exactly the same as xhmixed so that we can see the difference that using the offsets from the gce effects and their errors
	xhmixed2 = 1*xhmixed
	xherr = np.zeros(len(xhmixed2))

	#define the offsets, their associated element and the error in that value from the excel file.
	offsets = [-0.03104, -0.030024, -0.01836, -0.007664, 0.010632, -0.00048, -0.02096, 0.03824, 0.0098, 0.014576, 0.00552, 0.009032, -0.000808, -0.025456, -0.005744, -0.009376, -0.025464, -0.024752, 0.004656, 0.002248, 0.046312]
	offsetcharge = [6, 8, 11, 12, 13, 14, 16, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 38, 39, 56]
	offseterr = [0.03206548, 0.03316638, 0.022393406, 0.011206215, 0.017257608, 0.01200101, 0.031018415, 0.025974801, 0.008515184, 0.026306724, 0.010118201, 0.011533513, 0.0070094, 0.015212495, 0.018047559, 0.014154898, 0.025648512, 0.026891561, 0.037015764, 0.030004954, 0.040270034, 0.037015764, 0.030004954, 0.04027]
	print(len(offseterr))

	#apply the offsets to the mixed in values
	for i in offsetcharge:
		xhmixed2[i-3] = xhmixed[i-3] + offsets[offsetcharge.index(i)]
		xherr[i-3] = xherr[i-3] + offseterr[offsetcharge.index(i)]

	#plot the mixed in abundance
	mix2 = '%.2E' % decimal.Decimal(mix2)
	if mix1 == 0:
		plt.plot(num, xhmixed[:-1], label = "AGB")
	else:
		plt.plot(num, xhmixed[:-1], label = "AGB + Supernova")

	#plot the gce offset on the mixed values and HIPs abundances
	plt.errorbar(num, xhmixed2[:-1], yerr=xherr[:-1], capsize = 4, label = "GCE offset on AGB")
	plt.errorbar(chargeno, xh, yerr=error, capsize = 4, label = "HIP 11915", fmt = "o")

	#label our axes'
	plt.xlabel('Charge No.')
	plt.ylabel('[X/H]')
	plt.legend(loc = 'best')