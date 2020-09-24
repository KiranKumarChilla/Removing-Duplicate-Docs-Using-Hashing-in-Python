import datetime
import multiprocessing
import os
import hashlib
from os import listdir
from os.path import isfile, join

# main function in this file which calls all other function and process inputs

input_files_path = r'H:\files\input'
input_files = [f for f in listdir(input_files_path) if isfile(join(input_files_path, f))]
input_files = [os.path.join(input_files_path, x) for x in input_files]
inp_dups = {}
unique_inps = {}



# It calculates the hash value for each file ; decrease the block size if input file size is more
def calculate_hash_val(path, blocks=65536):
    file = open(path, 'rb')
    hasher = hashlib.md5()
    data = file.read()
    while len(data) > 0:
        hasher.update(data)
        data = file.read()
    file.close()
    return hasher.hexdigest()


# Identifying unique files
def find_unique_files(dic_unique, dict1):
    for key in dict1.keys():
        if key not in dic_unique:
            dic_unique[key] = dict1[key]



def remove_duplicate_files(all_inps, unique_inps):
    for file_name in all_inps.keys():
        if all_inps[file_name] in unique_inps and file_name!=unique_inps[all_inps[file_name]]:
            os.remove(file_name)
        elif all_inps[file_name] not in unique_inps:
            os.remove(file_name)




if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=4)
    keys_dict = pool.map(calculate_hash_val, input_files)
    print(len(keys_dict), len(input_files))
    inp_dups = dict(zip(keys_dict, input_files))
    all_inps = dict(zip(input_files, keys_dict))
    pool.close()

    datetime1 = datetime.datetime.now()
    find_unique_files(unique_inps, inp_dups)
    remove_duplicate_files(all_inps, unique_inps)
