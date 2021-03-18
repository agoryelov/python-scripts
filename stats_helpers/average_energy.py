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
energies = h5_file['positions']

electron_energies = []

for id in val_idxs:
    electron_energies = np.append(electron_energies, energies[id][0][0] + energies[id][0][1] + energies[id][0][2])
print("Calculating statistics...")
print("...")

print("Energies std: {std}.".format(std=np.std(electron_energies)))
print("Energies mean: {mean}.".format(mean=np.mean(electron_energies)))
print("Energies mean: {median}.".format(median=np.median(electron_energies)))
print("Energies min: {min}.".format(min=np.min(electron_energies)))
print("Energies max: {max}.".format(max=np.max(electron_energies)))

h5_file.close()
idxs_file.close()