import numpy as np
import scipy
from scipy import interpolate

from ct_phantom import ct_phantom
from ct_scan import ct_scan

def ct_calibrate(photons, material, sinogram, scale):

	""" ct_calibrate convert CT detections to linearised attenuation
	sinogram = ct_calibrate(photons, material, sinogram, scale) takes the CT detection sinogram
	in x (angles x samples) and returns a linear attenuation sinogram
	(angles x samples). photons is the source energy distribution, material is the
	material structure containing names, linear attenuation coefficients and
	energies in mev, and scale is the size of each pixel in x, in cm."""

	# Get dimensions and work out detection for just air of twice the side
	# length (has to be the same as in ct_scan.py)
	n = sinogram.shape[1] #columns of sinogram= number of samples (values along each angle)
	a = sinogram.shape[0] #number of angles
	p= ct_phantom(material.name, 2*n, 1, 'Air')
	c= ct_scan(photons, material, p ,scale, 1, mas=10000)

	# perform calibration
	sumI0= sum(c[0]) #c[0] is taking the first angles energy list (for us theres only one but still required)
	print(sumI0) #see if realistic


	#computes calibrated value for each pixel 
	for i in range(a): #number of angles
		for j in range(n):   #number of energies
			sinogram[i][j]= -np.log(sinogram[i][j]/sumI0)

	return sinogram
