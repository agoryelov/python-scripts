import h5py
import numpy as np
from numpy import load

filename = "/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_emg_E0to1000MeV_digihits.h5"
filename_out = "/home/agoryelov/python-scripts/data_chunk.h5"
# filename = "/home/esuom/Downloads/IWCDmPMT_4pi_fulltank_test_graphnet.h5"
# filename_out = "/home/esuom/Downloads/out.h5"

h5_file = h5py.File(filename,'r')
idxs_file = load('/home/agoryelov/electron.npz')

val_idxs = idxs_file['val_idxs']
angles = h5_file['angles']

angle_min = angles[val_idxs[0]][1]
angle_max = angles[val_idxs[0]][1]

electron_polar = []
electron_azimuth = []

for id in val_idxs:
    electron_polar = np.append(electron_polar, angles[id][0])
    electron_azimuth = np.append(electron_azimuth, angles[id][1])

polar_std = np.std(electron_polar)

print("Calculating polar std...")
p_std = np.std(electron_polar)
print("...")
print(str(p_std))

print("Calculating azimuth std...")
a_std = np.std(electron_azimuth)
print("...")
print(str(a_std))

print("Polar std: {std}.".format(std=p_std))
print("Azimuth std: {std}.".format(std=a_std))

# for id in val_idxs:
#     if angles[id][1] > angle_max:
#         angle_max = angles[id][1]
#     if angles[id][1] < angle_min:
#         angle_min = angles[id][1]

def print_item(name, object):
    print("Dataset: {dname} has size {size}".format(dname=name, size=object.len()))

h5_file.visititems(print_item)

h5_file.close()