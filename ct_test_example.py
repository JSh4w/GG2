
# these are the imports you are likely to need
import numpy as np
from material import *
from source import *
from fake_source import *
from ct_phantom import *
from ct_lib import *
from scan_and_reconstruct import *
from create_dicom import *

# create object instances
material = Material()
source = Source()

# define each end-to-end test here, including comments
# these are just some examples to get you started
# all the output should be saved in a 'results' directory

def test_1():
	# explain what this test is for
	"""Used for experiment 3.3 to test source energy"""
	# work out what the initial conditions should be
	
	y1= ct_detect(source.photon('100kVp, 1mm Al'), material.coeff('Water'),np.arange(0, 10.1, 0.1), 1)
	y2= ct_detect(source.photon('100kVp, 4mm Al'), material.coeff('Water'),np.arange(0, 10.1, 0.1), 1)
	y3= ct_detect(source.photon('80kVp, 2mm Al'), material.coeff('Carbon'),np.arange(0, 10.1, 0.1), 1)
	y4= ct_detect(source.photon('80kVp, 2mm Al'), material.coeff('Adipose'),np.arange(0, 10.1, 0.1), 1)


	plt.plot(np.log(y1), label='100kVp, 1mm Al , Water')
	plt.plot(np.log(y2), label='100kVp, 4mm Al , Water')
	plt.plot(np.log(y3), label='80kVp, 2mm Al , Carbon')
	plt.plot(np.log(y4),label='80kVp, 2mm Al , Adipose')
	plt.legend()
	plt.show()
	# how to check whether these results are actually correct?

def test_2():
	# explain what this test is for

	# work out what the initial conditions should be
	p = ct_phantom(material.name, 256, 7, metal=None)
	s = source.photon('100kVp, 2mm Al')
	y = scan_and_reconstruct(s, material, p, 0.1, 128, alpha=0.01)

	# save some meaningful results
	save_plot(y[128,:], 'results', 'test_2_plot')

	# how to check whether these results are actually correct?
	draw(y, caxis=[-0.1,0.4])

def test_3():
	# explain what this test is for

	# work out what the initial conditions should be
	p = ct_phantom(material.name, 256, 1)
	s = fake_source(source.mev, 0.1, method='ideal')
	y = scan_and_reconstruct(s, material, p, 0.1, 256)

	# save some meaningful results
	f = open('results/test_3_output.txt', mode='w')
	f.write('Mean value is ' + str(np.mean(y[64:192, 64:192])))
	f.close()

	# how to check whether these results are actually correct?


# Run the various tests
print('Test 1')
test_1()
print('Test 2')
test_2()
print('Test 3')
test_3()
