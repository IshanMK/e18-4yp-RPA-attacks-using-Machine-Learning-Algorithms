import sys
sys.path.append('/mnt/f/e18-4yp-RPA-attacks-using-Machine-Learning-Algorithms/code/AISY_Framework') # change this path accordingly

import aisy_sca
from app import *
from custom.custom_models.neural_networks import *

dataset_dict = {
    "filename": "ds1_190.h5",
    "key": "000102030405060708090A0B0C0D0EF0",
    "first_sample": 0,
    "number_of_samples": 190,
    "number_of_profiling_traces": 200000,
    "number_of_attack_traces": 90000
}

aisy = aisy_sca.Aisy()
aisy.set_resources_root_folder(resources_root_folder)
aisy.set_database_root_folder(databases_root_folder)
aisy.set_datasets_root_folder(datasets_root_folder)
aisy.set_database_name("constant_key.sqlite")
aisy.set_dataset(dataset_dict)
aisy.set_aes_leakage_model(leakage_model="ID", byte=4, round=1, 
                           target_state="Sbox", direction="Encryption", cipher="AES128")

aisy.set_batch_size(1000)
aisy.set_epochs(15)
aisy.set_neural_network(custom_cnn)
aisy.run(key_rank_attack_traces=25000)
