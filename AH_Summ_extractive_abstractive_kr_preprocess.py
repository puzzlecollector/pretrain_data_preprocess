import numpy as np 
import pandas as pd
import json 
import os 
import glob 
from tqdm.auto import tqdm 
import re 
import csv 

def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f:
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 


directories = ["01.news_r", "02.briefing", "03.his_cul", "04.paper", "05.minute", "06.edit",  "07.public",  "08.speech",  "09.literature",  "10.narration"] 

def find_and_read_json(root_folder): 
	json_files = glob.glob(root_folder + "/**/*.json", recursive=True) 
	json_data = [] 
	for json_file in json_files: 
		with open(json_file, "r") as f: 
			data = json.load(f) 
		if data is not None: 
			json_data.append(data) 
	return json_data 


full_lists = [] 

for directory in tqdm(directories, desc="iterating over directories"): 
	json_data = find_and_read_json(directory) 
	for i in range(len(json_data)): 
		text = json_data[i]["Meta(Acqusition)"]["doc_name"] + "\n"
		text += json_data[i]["Meta(Refine)"]["passage"] 
		cur_dict = {} 
		cur_dict["text"] = text 
		cur_dict["meta"] = "/nas/AH_Summ_extractive_abstractive_kr/022.요약문 및 레포트 생성 데이터/01.데이터/1.Training/라벨링데이터/" + str(directory) 
		full_lists.append(cur_dict) 
	
filename = "AH_Summ_extractive_abstractive_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename)
print("done!") 
