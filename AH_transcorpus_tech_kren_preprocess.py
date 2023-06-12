import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm import tqdm 


df = pd.read_csv("1113_tech_train_set_1195228.csv") 

texts = df["ko"].values 

full = [] 

for text in tqdm(texts): 
	cur_dict = {}
	cur_dict["text"] = text 
	cur_dict["meta"] = "/nas/AH_TransCorpus_tech_kren/한국어-영어 번역 말뭉치(기술과학)/Training/1113_tech_train_set_1195228.csv" 
	full.append(cur_dict) 

def dict_to_jsonl(data, filename): 
    with open(filename, "w") as f: 
        for entry in data:
            json.dump(entry, f, ensure_ascii=False) 
            f.write("\n") 

dict_to_jsonl(full, "AH_TransCorpus_tech_kren_batch1.jsonl") 
print("done!") 

print(full[-5:]) 
