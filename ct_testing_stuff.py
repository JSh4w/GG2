import numpy as np
import math
from ct_detect import ct_detect
from material import *
from source import *
import matplotlib.pyplot as plt 
from source import *
from fake_source import *
from ct_phantom import *
from ct_lib import *
from scan_and_reconstruct import *
from create_dicom import *
from ct_calibrate import *
from ct_scan import *

material = Material()
source = Source()
"""
y= ct_detect(source.photon('100kVp, 2mm Al'), material.coeff('Water'),np.arange(0, 10.1, 0.1), 1)
x=ct_phantom(material.name, 100, 3, metal=None)
draw(x)

z=ct_calibrate(material.name)
print(material.name)"""
X=ct_phantom(material.name, 256, 7, metal=None)
#draw(X)
#y =ct_scan(source.photon('100kVp, 2mm Al'), material, X, 0.1, 256)

#z=ct_calibrate(source.photon('100kVp, 2mm Al'), material,y, 0.1 )
#draw(z)
w=scan_and_reconstruct(source.photon('100kVp, 2mm Al'), material, X, 0.1, 128, alpha=0.01)
draw(w, caxis=[-0.1,0.4])
