import os 
import numpy as np 
import pandas as pd 
import json 
from tqdm.auto import tqdm 
import re 

full_list = [] 

def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f: 
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 

def extract_text_from_dict(data): 
	texts = [] 
	for key, value in data.items():
		if key in ["info", "acusr", "dedat", "disposalform"]:
			continue 
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


files = os.listdir("TL_2.약관/01.유리") 
d1 = [] 
for idx, curfile in enumerate(files):
	cur_dict = {} 
	with open("TL_2.약관/01.유리/" + str(curfile), "r") as f: 
		data = json.load(f) 
		cur_text = "" 
		for i in range(len(data["clauseArticle"])): 
			cur_text += data["clauseArticle"][i] 
		for i in range(len(data["comProvision"])): 
			cur_text += data["comProvision"][i] 
	cur_dict["text"] = cur_text
	cur_dict["meta"] = "/nas/AH_Classify_law_doc_kr/019.법률, 규정 (판결서, 약관 등) 텍스트 분석 데이터/01.데이터/1.Training/라벨링데이터/1.Training/라벨링데이터/TL_2.약관/01.유리/" + str(curfile)
	d1.append(cur_dict) 


files = os.listdir("TL_2.약관/02.불리") 
d2 = [] 
for idx, curfile in enumerate(files):
	cur_dict = {} 
	with open("TL_2.약관/02.불리/" + str(curfile), "r") as f:
		data = json.load(f) 
		cur_text = "" 
		for i in range(len(data["clauseArticle"])):
			cur_text += data["clauseArticle"][i] 
		for i in range(len(data["illdcssBasiss"])):
			cur_text += data["illdcssBasiss"][i] 
		for i in range(len(data["relateLaword"])): 
			cur_text += data["relateLaword"][i] 
	cur_dict["text"] = cur_text 
	cur_dict["meta"] = "/nas/AH_Classify_law_doc_kr/019.법률, 규정 (판결서, 약관 등) 텍스트 분석 데이터/01.데이터/1.Training/라벨링데이터/1.Training/라벨링데이터/TL_2.약관/02.불리/" + str(curfile)
	d2.append(cur_dict)  



full_list.extend(d1) 
full_list.extend(d2) 

filename = "AH_Classify_law_doc_kr_batch2.jsonl" 
dict_to_jsonl(full_list, filename) 


print(full_list[-5:]) 

print("done!") 
