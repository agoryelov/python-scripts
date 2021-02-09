import h5py

filename = "/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_emg_E0to1000MeV_digihits.h5"
# filename = "/home/esuom/Downloads/IWCDmPMT_4pi_fulltank_test_graphnet.h5"

h5_file = h5py.File(filename,'r')

print(list(h5_file.keys()))

h5_file.close()