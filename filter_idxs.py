import h5py
import numpy as np
from numpy import load

idxs_file = load('/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_3M_OD_veto_idxs.npz')
h5_file = h5py.File('/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_emg_E0to1000MeV_digihits.h5','r')

def print_item(name, object):
    print("Dataset: {dname} has size {size}".format(dname=name, size=object.len()))

train_idxs = idxs_file['train_idxs']
val_idxs = idxs_file['val_idxs']
test_idxs = idxs_file['test_idxs']

h5_labels = np.array(h5_file['labels'])


# print(train_idxs)
# print(h5_labels)

train_idxs_muon = np.extract(np.where(h5_labels[train_idxs] == 2, True, False), train_idxs)
val_idxs_muon = np.extract(np.where(h5_labels[val_idxs] == 2, True, False), val_idxs)
test_idxs_muon = np.extract(np.where(h5_labels[test_idxs] == 2, True, False), test_idxs)

# print(len(train_idxs_electron))
# print(len(val_idxs_electron))

# print(train_idxs_electron)
# print(val_idxs_electron)
# print(test_idxs_electron)

# for id in train_idxs_electron:
#     if (h5_labels[id] != 1):
#         print('wrong label here')

np.savez('/home/agoryelov/muon.npz', train_idxs=train_idxs_muon, val_idxs=val_idxs_muon, test_idxs=test_idxs_muon)
# a4 = np.extract(np.where(a1[a2] % 2 == 0, True, False), a2)