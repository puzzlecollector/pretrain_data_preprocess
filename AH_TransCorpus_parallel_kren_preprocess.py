import numpy as np 
import pandas as pd 
import os 
import json
from tqdm import tqdm 

files = os.listdir(".") 

full_lines = [] 

for curfile in tqdm(files):
	if ".xlsx" in curfile:
		try: 
			df = pd.read_excel(curfile, engine="openpyxl") 
			sentences = df["원문"].values 
			for sentence in sentences:
				cur_dict = {} 
				cur_dict["text"] = sentence 
				cur_dict["meta"] = "/nas/AH_TransCorpus_parallel_kren/한국어-영어 번역(병렬) 말뭉치/" + str(curfile) 
				full_lines.append(cur_dict) 
		except Exception as e: 
			print(e) 


def dict_to_jsonl(data, filename): 
    with open(filename, "w") as f: 
        for entry in data:
            json.dump(entry, f, ensure_ascii=False) 
            f.write("\n") 


filename = "AH_TransCorpus_parallel_kren_batch1.jsonl" 
dict_to_jsonl(full_lines, filename) 
print(full_lines[-5:]) 
print("done!") 
