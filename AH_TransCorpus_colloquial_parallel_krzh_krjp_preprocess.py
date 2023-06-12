import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm import tqdm 

directories = ["일한",  "중한",  "한일",  "한중"]

full_lines = [] 

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")


for directory in tqdm(directories, desc="iterating over directories"): 
	cur_dirs = os.listdir(directory) 
	for cur_dir in cur_dirs: 
		files = os.listdir(os.path.join(directory, cur_dir)) 
		for curfile in files: 
			if ".json" in curfile:
				with open(str(directory) + "/" + str(cur_dir) + "/" + curfile, "r") as f: 
					data = json.load(f)
					for i in range(len(data)): 
						cur_dict = {} 
						if directory in ["일한", "중한"]: 
							cur_dict["text"] = data[i]["최종번역문"]
							cur_dict["meta"] = "/nas/AH_TransCorpus_colloquial_parallel_krzh_krjp/027.일상생활 및 구어체 한-중, 한-일 번역 병렬 말뭉치 데이터/01.데이터/1_Training/라벨링데이터/" + str(directory) + "/" + str(cur_dir) + "/" + curfile  
						else:
							cur_dict["text"] = data[i]["원문"] 
							cur_dict["meta"] = "/nas/AH_TransCorpus_colloquial_parallel_krzh_krjp/027.일상생활 및 구어체 한-중, 한-일 번역 병렬 말뭉치 데이터/01.데이터/2_Validation/라벨링데이터/" + str(directory) + "/" + str(cur_dir) + "/" + curfile 
						full_lines.append(cur_dict) 



filename = "AH_TransCorpus_colloquial_parallel_krzh_krjp_batch1.jsonl" 
dict_to_jsonl(full_lines, filename) 

print("done!") 
