import MDAnalysis as mda
from my_lib import Analysis

uni = mda.Universe("top.pdb", "sim.dcd")

first_frame = 0
last_frame = len(uni.trajectory)-1
middle_frame = int(last_frame/2)
contact_map = Analysis(uni)
contact_map.set_frame(middle_frame)
contact_map.genrate_contact_map()