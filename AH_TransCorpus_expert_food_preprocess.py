import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm import tqdm

files = os.listdir(".")

full_lines = [] 

for curfile in tqdm(files): 
	if ".json" in curfile:
		with open(curfile, "r") as f: 
			data = json.load(f)
			arr = data["data"] 
			for i in range(len(arr)): 
				cur_dict = {} 
				cur_dict["text"] = arr[i]["ko"] 
				cur_dict["meta"] = "/nas/AH_TransCorpus_expert_food_enkr_zhkr/156.전문분야 영-한, 중-한 번역 말뭉치(식품)/01.데이터/1.Training/라벨링데이터/" + str(curfile) 
				full_lines.append(cur_dict)


def dict_to_jsonl(data, filename): 
    with open(filename, "w") as f: 
        for entry in data:
            json.dump(entry, f, ensure_ascii=False) 
            f.write("\n") 

filenames = "AH_TransCorpus_expert_food_enkr_zhkr_batch1.jsonl" 
dict_to_jsonl(full_lines, filenames) 
print("done!")
