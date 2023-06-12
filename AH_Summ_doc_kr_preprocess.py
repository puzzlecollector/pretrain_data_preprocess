import numpy as np 
import pandas as pd
import json 
import pandas as pd
from tqdm.auto import tqdm 

def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f:
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 

with open("train_original.json", "r") as f: 
	data = json.load(f) 

arr = data["documents"] 

full_lists = [] 

for i in tqdm(range(len(arr)), position=0, leave=True): 
	cur_data = arr[i] 
	cur_dict = {} 
	cur_dict["text"] = arr[i]["abstractive"] 
	cur_dict["meta"] = "/nas/AH_Summ_doc_kr/문서요약 텍스트/Training/train_original.json"   
	full_lists.append(cur_dict)  

	arr_text = arr[i]["text"] 
	for j in range(len(arr_text)):
		for k in range(len(arr_text[j])): 
			stuff = arr_text[j][k]["sentence"] 	
			cur_dict2 = {}  
			cur_dict2["text"] = stuff 
			cur_dict2["meta"] = "/nas/AH_Summ_doc_kr/문서요약 텍스트/Training/train_original.json" 
			full_lists.append(cur_dict2) 
	
filename = "AH_Summ_doc_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename) 

print("done!") 

print(full_lists[-10:])
