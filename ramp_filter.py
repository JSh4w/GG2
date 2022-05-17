from inspect import BoundArguments
import math
import numpy as np
import numpy.matlib

def ramp_filter(sinogram, scale, alpha=0.001):
	""" Ram-Lak filter with raised-cosine for CT reconstruction

	fs = ramp_filter(sinogram, scale) filters the input in sinogram (angles x samples)
	using a Ram-Lak filter.

	fs = ramp_filter(sinogram, scale, alpha) can be used to modify the Ram-Lak filter by a
	cosine raised to the power given by alpha."""

	# get input dimensions
	a = sinogram.shape[0] #no of rows= different angles
	n = sinogram.shape[1] #no of column= different energies

	#Set up filter to be at least twice as long as input
	m = np.ceil(np.log(2*n-1) / np.log(2))
	m = int(2 ** m)


	# apply filter to all angles
	print('Ramp filtering')
	for i in range(len(sinogram)):
		freq = np.fft.fftfreq(m)
		ft = np.fft.fft(sinogram[i],m)

		wmax = max(freq)

		for j in range(len(ft)):
			ft[j] = abs(freq[j] / 2*np.pi)*(math.cos(freq[j]*np.pi / 2*wmax)**alpha)*ft[j]
		
		chad = np.fft.ifft(ft)
		sinogram[i]=chad[0:n]
	
	return sinogram

