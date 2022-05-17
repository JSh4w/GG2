import numpy as np
import math

def attenuate(original_energy, coeff, depth):
	"""calculates residual photons for a particular material and depth
	attenuate(original_energy, coeff, depth, mas) takes the original_energy
	(energy, samples) and works out the residual_energy (energy, samples)
	for a particular material with linear attenuation coefficients given
	by coeff (energies), and a set of depths given by depth (samples)

	It is more efficient to calculate this for a range of samples rather then
	one at a time
	"""
	#residual photons require I=I0e^-mu*x
	#Itot = sumE=Io, PI*e^-mu*x
	

	# check original energy is energy x samples
	if type(original_energy) != np.ndarray:
		original_energy = np.array([original_energy]).reshape((1, 1))
	elif original_energy.ndim == 1:
		original_energy = original_energy.reshape((len(original_energy), 1))
	elif original_energy.ndim != 2:
		raise ValueError('input original_energy has more than two dimensions')
	energies = original_energy.shape[0] #=number of row
	samples = original_energy.shape[1] #=number of columns

	# check coeff is vector of energies
	if type(coeff) != np.ndarray:
		coeff = np.array([coeff])
	elif coeff.ndim != 1:
		raise ValueError('input coeffs has more than one dimension')
	if len(coeff) != energies:
		raise ValueError('input coeff has different number of energies to input original_energy')

	# check depth is vector of samples
	if type(depth) != np.ndarray:
		depth = np.array([depth])
	elif depth.ndim != 1:
		raise ValueError('input depth has more than one dimension')
	if len(depth) != samples:
		raise ValueError('input depth has different number of samples to input original_energy')

	# Work out residual energy for each depth and at each energy

	#Alternate code using iterative steps rather than vectors
	"""residual_energy=np.zeros((original_energy.shape[0],original_energy.shape[1]))
	for i in range(len(original_energy)):
		for j in range(len(depth)):
			residual_energy[i][j]=original_energy[i][j] * np.exp(-coeff[i]*depth[j])"""

	#vector method 	
	residual_energy=original_energy*np.exp(np.negative(np.outer(coeff.reshape(1,energies),depth)))

	return residual_energy





