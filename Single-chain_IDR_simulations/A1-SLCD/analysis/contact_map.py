import MDAnalysis as mda
from my_lib import Analysis

uni = mda.Universe("top.pdb", "sim.dcd")


last_frame = len(uni.trajectory)-1
contact_map = Analysis(uni)
#contact_map.set_frame(last_frame)
contact_map.genrate_contact_map()