import numpy as np 
import pandas as pd 
import os
import json 
from tqdm import tqdm 

files = os.listdir(".") 

full_lines = [] 


for curfile in tqdm(files): 
	if ".json" in curfile: 
		try: 
			with open(curfile, "r") as f: 
				data = json.load(f) 
				for i in range(len(data)): 
					cur_dict = {} 
					cur_dict["text"] = data[i]["한국어"] 
					cur_dict["meta"] = "/nas/AH_TransCorpus_expert_kren/전문분야 한영 말뭉치/Training/" + str(curfile) 
					full_lines.append(cur_dict) 
		except Exception as e: 
			print(e) 
filename = "AH_TransCorpus_expert_kren_batch1.jsonl" 


def dict_to_jsonl(data, filename):
    with open(filename, "w") as f:
        for entry in data:
            json.dump(entry, f, ensure_ascii=False)
            f.write("\n")

dict_to_jsonl(full_lines, filename) 

print(full_lines[-5:])
print("done!") 
