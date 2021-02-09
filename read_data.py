import h5py

# filename = "/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_emg_E0to1000MeV_digihits.h5"
filename = "/home/esuom/Downloads/IWCDmPMT_4pi_fulltank_test_graphnet.h5"

def print_size(name, object):
    print("Dataset: {dname} has size {size}".format(dname=name, size=object.len()))


h5_file = h5py.File(filename,'r')

print(list(h5_file.keys()))
h5_file.visititems(print_size)

h5_file.close()