import numpy as np
"""
following functions mean this:
p= source energy distribution of photon energies
coeffs= linear attenutation coeffs 
depth= list of all theset of depths given by samples
material.name= list of all materials?
original enerrgy= array of energy levels (columns) at different depths (rows)
photons= energy going out 
"""
"""
The values used in the phantom are arbitrary hence when producing the ct_scan it doesnt reconstruct the colours perfectly
this can be adjusted by converting the phantom valuees to density when required

"""