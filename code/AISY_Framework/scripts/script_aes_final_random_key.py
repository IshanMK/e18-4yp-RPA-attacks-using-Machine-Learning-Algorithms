import sys
sys.path.append('/mnt/f/e18-4yp-RPA-attacks-using-Machine-Learning-Algorithms/code/AISY_Framework') # change this path accordingly

import aisy_sca
from app import *
from custom.custom_models.neural_networks import *

dataset_dict = {
    "filename": "random_key_190.h5",
    "key": "000102030405060708090A0B0C0D0EF0",
    "first_sample": 0,
    "number_of_samples": 190,
    "number_of_profiling_traces": 1000000,
    "number_of_attack_traces": 290000
}


aisy = aisy_sca.Aisy()
aisy.set_resources_root_folder(resources_root_folder)
aisy.set_database_root_folder(databases_root_folder)
aisy.set_datasets_root_folder(datasets_root_folder)
aisy.set_database_name("random_key.sqlite")
aisy.set_dataset(dataset_dict)
aisy.set_aes_leakage_model(leakage_model="ID", byte=4, round=1, 
                           target_state="Sbox", direction="Encryption", cipher="AES128")

aisy.set_batch_size(10000)
aisy.set_epochs(10)
aisy.set_neural_network(custom_cnn)
aisy.run(key_rank_attack_traces=25000)
