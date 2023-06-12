import pandas as pd 
import numpy as np 
import os 
import json 
from tqdm import tqdm 

files = os.listdir(".") 

full = [] 

for curfile in tqdm(files): 
	if ".csv" in curfile: 
		df = pd.read_csv(curfile) 
		texts = df["한국어"].values  
		for text in texts: 
			cur_dict = {} 
			cur_dict["text"] = text 
			cur_dict["meta"] = "/nas/AH_TransCorpus_social_krzh/한국어-중국어 번역 말뭉치(사회과학)/Training/" + str(curfile) 
			full.append(cur_dict) 
def dict_to_jsonl(data, filename): 
    with open(filename, "w") as f: 
        for entry in data:
            json.dump(entry, f, ensure_ascii=False) 
            f.write("\n") 


dict_to_jsonl(full, "AH_TransCorpus_social_krzh_batch1.jsonl") 
print(full[-3:]) 
print("done!") 
