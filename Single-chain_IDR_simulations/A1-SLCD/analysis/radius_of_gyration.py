import MDAnalysis as mda
from my_lib import Analysis

uni = mda.Universe("top.pdb", "sim.dcd")

rgyr = Analysis(uni)
rgyr.plot_radius_of_gyration()

# probabilistic distributaion 

#rgyr.probability_rgyr()
