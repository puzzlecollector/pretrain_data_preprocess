import numpy as np 
import pandas as pd 
import json 
from tqdm import tqdm 
import os 
import glob 

def find_and_read_json(root_folder): 
	json_files = glob.glob(root_folder + "/**/*.json", recursive=True) 
	json_data = [] 
	for json_file in json_files:
		with open(json_file, "r") as f: 
			data = json.load(f) 
		if data is not None: 
			json_data.append(data) 
	return json_data 

directories = ["c_event", "culture", "enter", "fm_drama", "fs_drama", "history"]

all_json_data = [] 

for directory in tqdm(directories): 
	json_data = find_and_read_json(directory) 
	all_json_data.extend(json_data) 

print(all_json_data[:10])  
