import os 
import pandas as pd 
import numpy as np 
import json 
import csv 
from tqdm.auto import tqdm
def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f:
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 

def extract_text_from_dict(data):
	texts = [] 
	for key, value in data.items(): 
		if isinstance(value, str): 
			texts.append(value) 
		elif isinstance(value, list): 
			for element in value: 
				if isinstance(element, str): 
					texts.append(element) 
				elif isinstance(element, dict): 
					nested_texts = extract_text_from_dict(element) 
					texts.extend(nested_texts) 
		elif isinstance(value, dict): 
			nested_texts = extract_text_from_dict(value) 
			texts.extend(nested_texts) 
	return texts 


full_list = [] 


files = os.listdir('.')  

for curfile in tqdm(files, position=0, leave=True): 
	if '.json' in curfile: 
		with open(curfile, "r") as f: 
			data = json.load(f)
			for i in range(len(data["data"])): 
				texts = extract_text_from_dict(data["data"][i]) 
				joined_texts = ' '.join(texts) 
				cur_dict = {} 
				cur_dict["text"] = joined_texts 
				cur_dict["meta"] = "/nas/AH_Corpus_expert_kr/전문분야 말뭉치/Training/" + str(curfile) 
				full_list.append(cur_dict) 

filename = "AH_Corpus_expert_kr_batch1.jsonl" 
dict_to_jsonl(full_list, filename) 

print("done!") 
