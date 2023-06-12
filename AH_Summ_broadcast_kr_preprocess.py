import numpy as np 
import pandas as pd 
import json 
from tqdm import tqdm 
import os 
import glob 


def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f: 
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 


def find_and_read_json(root_folder): 
	json_files = glob.glob(root_folder + "/**/*.json", recursive=True) 
	json_data = [] 
	for json_file in json_files:
		with open(json_file, "r") as f: 
			data = json.load(f) 
		if data is not None: 
			json_data.append(data["Meta"]["passage"]) 
	return json_data 

directories = ["c_event", "culture", "enter", "fm_drama", "fs_drama", "history"]

full_lists = [] 

for directory in tqdm(directories): 
	json_data = find_and_read_json(directory) 
	for data in json_data: 
		cur_dict = {} 
		cur_dict["text"] = data  
		cur_dict["meta"] = "/nas/AH_Summ_broadcast_kr/023.방송 콘텐츠 대본 요약 데이터/01.데이터/1.Training/라벨링데이터/" + str(directory) 
		full_lists.append(cur_dict) 

filename = "AH_Summ_broadcast_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename) 

print("done!") 
