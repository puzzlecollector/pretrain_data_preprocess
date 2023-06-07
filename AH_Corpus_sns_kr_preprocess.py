import os 
import numpy as np
import pandas as pd 
import json 
from tqdm.auto import tqdm 
import re 

def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f: 
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n") 

files = os.listdir(".") 


full_lists = [] 

for curfile in tqdm(files):
	try:
		with open(curfile, "r") as f: 
			data = json.load(f) 
			arr = data["data"][0]["body"]
			text = "" 
			for i in range(len(arr)): 
				text += arr[i]["utterance"] 
		cur_dict = {} 
		cur_dict["text"] = text 
		cur_dict["meta"] = "/nas/AH_Corpus_sns_kr/한국어 SNS/Training/[라벨]한국어SNS_train/" + str(curfile) 
		full_lists.append(cur_dict)  
	except Exception as e: 
		print(e) 
		continue 


filename = "AH_Corpus_sns_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename) 

print("done!") 
