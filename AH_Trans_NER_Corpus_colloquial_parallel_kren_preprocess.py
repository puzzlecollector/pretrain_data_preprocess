import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm import tqdm


full_lines = [] 

with open("일상생활및구어체_영한_train_set.json", "r") as f:
	data = json.load(f) 
	arr = data["data"] 
	for i in tqdm(range(len(arr)), position=0, leave=True):
		cur_dict = {} 
		cur_dict["text"] = arr[i]["ko"] 
		cur_dict["meta"] = "/nas/AH_Trans_NER_Corpus_colloquial_parallel_kren/025.일상생활 및 구어체 한-영 병렬 말뭉치 데이터/01.데이터/1.Training/라벨링데이터/일상생활및구어체_영한_train_set.json"
		full_lines.append(cur_dict) 

with open("일상생활및구어체_한영_train_set.json", "r") as f: 
	data = json.load(f)
	arr = data["data"] 
	for i in tqdm(range(len(arr)), position=0, leave=True): 
		cur_dict = {} 
		cur_dict["text"] = arr[i]["ko"] 
		cur_dict["meta"] = "/nas/AH_Trans_NER_Corpus_colloquial_parallel_kren/025.일상생활 및 구어체 한-영 병렬 말뭉치 데이터/01.데이터/1.Training/라벨링데이터/일상생활및구어체_영한_train_set.json"
		full_lines.append(cur_dict) 

def dict_to_jsonl(data, filename): 
    with open(filename, "w") as f: 
        for entry in data:
            json.dump(entry, f, ensure_ascii=False) 
            f.write("\n") 

dict_to_jsonl(full_lines, "AH_Trans_NER_Corpus_colloquial_parallel_kren.jsonl") 

print(full_lines[-5:]) 

print("done!") 
