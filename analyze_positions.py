import h5py
import numpy as np

import matplotlib.pyplot as plt
from numpy.core.defchararray import index
plt.style.use('seaborn-whitegrid')

muon_path = '/home/agoryelov/muon.npz'
electron_path = '/home/agoryelov/electron.npz'
data_path = "/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_emg_E0to1000MeV_digihits.h5"
indices_path = "/home/agoryelov/young/WatChMaL/outputs/2021-03-17/21-24-13/outputs/indices.npy"
predicted_path = [
  "/home/agoryelov/young/WatChMaL/outputs/2021-02-28/20-07-49/outputs/predictions.npy",
  "/home/agoryelov/young/WatChMaL/outputs/2021-03-03/19-58-35/outputs/predictions.npy",
  "/home/agoryelov/young/WatChMaL/outputs/2021-03-10/00-56-37/outputs/predictions.npy",
  "/home/agoryelov/young/WatChMaL/outputs/2021-03-10/01-35-26/outputs/predictions.npy",
  "/home/agoryelov/young/WatChMaL/outputs/2021-03-17/20-52-28/outputs/predictions.npy", # no flips
  "/home/agoryelov/young/WatChMaL/outputs/2021-03-17/21-09-04/outputs/predictions.npy", # horizontal only
  "/home/agoryelov/young/WatChMaL/outputs/2021-03-17/21-24-13/outputs/predictions.npy", # vertical only
]

indices = np.load(indices_path)
print(len(indices))

elec_test = np.load(electron_path)['test_idxs']
muon_test = np.load(muon_path)['test_idxs']
preds_elec = np.load(predicted_path[0])
preds_muon = np.load(predicted_path[1])

preds_posz = np.load(predicted_path[5])

data = h5py.File(data_path, 'r')
energy_data = data["energies"]
position_data = data["positions"]
label_data = data["labels"]

def compare(actual, predicted):
  return (predicted - actual) / actual

print(len(preds_posz))

x = [position_data[elec_test[index]][0][2] for index in range(len(preds_posz))]
y = [preds_posz[index][0] for index in range(len(preds_posz))]

plt.scatter(x, y, color='black', s=3)
plt.savefig('./electron_position_z_scatter.png')
