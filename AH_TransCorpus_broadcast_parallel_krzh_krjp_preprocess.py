import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm import tqdm 

files = os.listdir(".") 

full_lines = [] 

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")


for idx, curfile in tqdm(enumerate(files), desc="iterating over files"): 
	if curfile[-4:] == "json":
		with open(curfile, "r") as f: 
			data = json.load(f) 
			arr = data["data"]
			for i in range(len(arr)): 
				cur_dict = {} 
				cur_dict["text"] = arr[i]["ko"] 
				cur_dict["meta"] = "/nas/AH_TransCorpus_broadcast_parallel_krzh_krjp/157.방송 콘텐츠 한-중, 한-일 번역 병렬 말뭉치 데이터/01.데이터/1.Training/라벨링데이터/" + str(curfile) 
				full_lines.append(cur_dict)  

print(full_lines[-10:])

filename = "AH_TransCorpus_broadcaast_parallel_krzh_krjp_batch1.jsonl"

dict_to_jsonl(full_lines, filename) 

print("done!") 
