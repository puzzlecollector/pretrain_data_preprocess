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


files = os.listdir("TL_1.판결문/01.민사/2018") 
d1 = []  
for curfile in tqdm(files, position=0, leave=True, desc="민사"): 
	with open("TL_1.판결문/01.민사/2018/" + str(curfile), "r") as f: 
		data = json.load(f)
		texts = extract_text_from_dict(data)
		joined_texts = ' '.join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_law_doc_kr/019.법률, 규정 (판결서, 약관 등) 텍스트 분석 데이터/01.데이터/1.Training/라벨링데이터/1.Training/라벨링데이터/T_1.판결문/01.민사/2018/" + str(curfile) 
	d1.append(cur_dict) 


files = os.listdir("TL_1.판결문/02.형사/2018") 
d2 = []
for curfile in tqdm(files, position=0, leave=True, desc="형사"): 
	with open("TL_1.판결문/02.형사/2018/" + str(curfile), "r") as f: 
		data = json.load(f) 
		texts = extract_text_from_dict(data) 
		joined_texts = ' '.join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_law_doc_kr/019.법률, 규정 (판결서, 약관 등) 텍스트 분석 데이터/01.데이터/1.Training/라벨링데이터/1.Training/라벨링데이터/T_1.판결문/02.형사/2018/" + str(curfile) 
	d2.append(cur_dict) 


files = os.listdir("TL_1.판결문/03.행정/2018") 
d3 = [] 
for curfile in tqdm(files, position=0, leave=True, desc="행정"): 
	with open("TL_1.판결문/03.행정/2018/" + str(curfile), "r") as f:
		data = json.load(f) 
		texts = extract_text_from_dict(data) 
		joined_texts = ' '.join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_law_doc_kr/019.법률, 규정 (판결서, 약관 등) 텍스트 분석 데이터/01.데이터/1.Training/라벨링데이터/1.Training/라벨링데이터/T_1.판결문/03.행정/2018/" + str(curfile) 
	d3.append(cur_dict)  

full_list.extend(d1) 
full_list.extend(d2) 
full_list.extend(d3) 

filename = "AH_Classify_law_doc_kr_batch1.jsonl" 
dict_to_jsonl(full_list, filename) 
print("done!") 
