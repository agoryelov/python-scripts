import h5py

filename = "/fast_scratch/WatChMaL/data/IWCD_mPMT_Short_emg_E0to1000MeV_digihits.h5"
filename_out = "/home/agoryelov/python-scripts/data_chunk.h5"
# filename = "/home/esuom/Downloads/IWCDmPMT_4pi_fulltank_test_graphnet.h5"
# filename_out = "/home/esuom/Downloads/out.h5"




h5_file = h5py.File(filename,'r')
out_file = h5py.File(filename_out, 'w')

max_index = 10000

def copy_events(name, object):
    if name != 'hit_charge' and name != 'hit_pmt' and name != 'hit_time':
        out_file.create_dataset(name, data=object[0:max_index])

max_hit_index = h5_file['event_hits_index'][max_index + 1]
print(max_hit_index)

def copy_hits(name, object):
    if name == 'hit_charge' or name == 'hit_pmt' and name == 'hit_time':
        out_file.create_dataset(name, data=object[0:max_hit_index])
    

def print_item(name, object):
    print("Dataset: {dname} has size {size}".format(dname=name, size=object.len()))

h5_file.visititems(copy_events)
h5_file.visititems(copy_hits)
out_file.visititems(print_item)

print(list(h5_file.keys()))
print(list(out_file.keys()))

h5_file.close()
out_file.close()
