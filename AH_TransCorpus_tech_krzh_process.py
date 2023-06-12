import numpy as np 
import pandas as pd
import json 
import os 
from tqdm import tqdm 

files = os.listdir(".") 

full_lines = [] 

for curfile in tqdm(files, position=0, leave=True, desc="itearting over files"): 
	if ".csv" in curfile: 
		df = pd.read_csv(curfile) 
		texts = df["한국어"].values 
		for text in texts: 
			cur_dict = {} 
			cur_dict["text"] = text 
			cur_dict["meta"] = "/nas/AH_TransCorpus_tech_krzh/한국어-중국어 번역 말뭉치(기술과학)/Training/" + str(curfile) 
			full_lines.append(cur_dict) 

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")

filename = "AH_TransCorpus_tech_krzh_batch1.jsonl" 

dict_to_jsonl(full_lines, filename) 

print(full_lines[-5:]) 
print("done!") 
