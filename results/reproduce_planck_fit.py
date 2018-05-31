import numpy as np
import matplotlib.pyplot as plt


theoretical_fit = np.loadtxt('exercise_1__scalCls.dat')
#experiment = np.genfromtxt('TT_data_2017feb.dat', skip_header=4, dtype = None)
#name_experiment = np.genfromtxt('TT_data_2017feb.dat', skip_header=4, dtype = None, usecols = (0))
data_ACT = np.genfromtxt('TT_data_ACT.dat', skip_header=4, usecols = (1,2,3,4))
data_Planck = np.genfromtxt('TT_data_Planck.dat', skip_header=4, usecols = (1,2,3,4))
data_SPT = np.genfromtxt('TT_data_SPT.dat', skip_header=4, usecols = (1,2,3,4))

#data_actpol = data_experiment[np.where(name_experiment = 'ACTpol')]
#print 'name_experiment\n', name_experiment
#print 'data_actpol\n', data_actpol

plt.errorbar(data_ACT[:,0], data_ACT[:,1], 
						 yerr = np.array([data_ACT[:,2], data_ACT[:,3]]),
						 fmt = '.', label = 'ACT')
plt.errorbar(data_Planck[:,0], data_Planck[:,1], 
						 yerr = np.array([data_Planck[:,2], data_Planck[:,3]]),
						 fmt = '.', label = 'Planck15')
plt.errorbar(data_SPT[:,0], data_SPT[:,1], 
						 yerr = np.array([data_SPT[:,2], data_SPT[:,3]]),
						 fmt = '.', label = 'SPT')
	
#plt.errorbar(data_experiment[:,1], data_experiment[:,2], yerr = np.array([data_experiment[:,3], data_experiment[:,4]]),
#						 fmt = '.')

plt.plot(theoretical_fit[:,0], theoretical_fit[:,1], label = 'Fit')
plt.xscale('log')
plt.xlim(1)
plt.xlabel('$\mathcal{l}$')
plt.ylabel('$[l(l+1)]^2 C_l / 2 \pi$ [$\mu K^2$]')
plt.legend()
plt.show()
