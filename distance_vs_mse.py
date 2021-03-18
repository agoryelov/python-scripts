import h5py
import numpy as np

import matplotlib.pyplot as plt
from numpy.core.defchararray import index
plt.style.use('seaborn-whitegrid')

muon_path = '/home/agoryelov/muon.npz'
electron_path = '/home/agoryelov/electron.npz'
data_path = "/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_emg_E0to1000MeV_digihits.h5"

indices_path = {
  "distance": "/home/agoryelov/young/WatChMaL/outputs/2021-03-10/02-26-52/outputs/indices.npy",
  "mse": "/home/agoryelov/young/WatChMaL/outputs/2021-03-10/02-28-28/outputs/indices.npy"
}

preds_path = {
  "distance": "/home/agoryelov/young/WatChMaL/outputs/2021-03-10/02-26-52/outputs/predictions.npy",
  "mse": "/home/agoryelov/young/WatChMaL/outputs/2021-03-10/02-28-28/outputs/predictions.npy"
}

idxs_dis = np.load(indices_path["distance"])
idxs_mse = np.load(indices_path["mse"])

preds_dis = np.load(preds_path["distance"])
preds_mse = np.load(preds_path["mse"])

elec_test = np.load(electron_path)['test_idxs']
muon_test = np.load(muon_path)['test_idxs']

data = h5py.File(data_path, 'r')
position_data = data["positions"]

def compare(actual, predicted):
  return (predicted - actual) / actual

dis_compare = [compare(position_data[elec_test[idxs_dis[index]]][0][0], preds_dis[index][0]) for index in range(len(idxs_dis))]
mse_compare = [compare(position_data[elec_test[idxs_mse[index]]][0][0], preds_mse[index][0]) for index in range(len(idxs_mse))]

plt.hist(dis_compare, bins=64, histtype='step', range=(-1, 1), label="Distance between")
plt.hist(mse_compare, bins=64, histtype='step', range=(-1, 1), label="Mean square error")
plt.xlabel(f"(predicted - actual) / actual")
plt.ylabel(f"# of events")
plt.legend()
plt.savefig('./distance_vs_mse.png')
