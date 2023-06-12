import numpy as np 
import pandas as pd  
import os 
import json 
from tqdm import tqdm
df = pd.read_csv("1113_social_train_set_1210529.csv") 
texts = df["ko"]  

full_lines = [] 

for text in tqdm(texts): 
	cur_dict = {} 
	cur_dict["text"] = text 
	cur_dict["meta"] = "/nas/AH_TransCorpus_social_kren/한국어-영어 번역 말뭉치(사회과학)/Training/1113_social_train_set_121059.csv" 
	full_lines.append(cur_dict) 

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")

dict_to_jsonl(full_lines, "AH_TransCorpus_social_kren_batch1.jsonl") 
print(full_lines[-5:]) 
print("done!") 
