import os 
import numpy as np 
import pandas as pd 
import json 
from tqdm.auto import tqdm  
import re

full_lists = [] 
 
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


files = os.listdir("TL1")
d1 = []
for curfile in tqdm(files, position=0, leave=True, desc="F1"): 
	with open("TL1/" + str(curfile), "r") as f: 
		data = json.load(f) 
		texts = extract_text_from_dict(data) 
		joined_texts = ' '.join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_patent_enkr/155.산업정보 연계 주요국 특허 영-한 데이터/01.데이터/1.Training/라벨링데이터_0831_add/TL1/" + str(curfile) 
	d1.append(cur_dict) 

files = os.listdir("TL2") 
d2 = [] 
for curfile in tqdm(files, position=0, leave=True, desc="F2"): 
	with open("TL2/" + str(curfile), "r") as f:
		data = json.load(f) 
		texts = extract_text_from_dict(data) 
		joined_texts = " ".join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_patent_enkr/155.산업정보 연계 주요국 특허 영-한 데이터/01.데이터/1.Training/라벨링데이터_0831_add/TL2/" + str(curfile)  
	d2.append(cur_dict) 

files = os.listdir("TL3") 
d3 = [] 
for curfile in tqdm(files, position=0, leave=True, desc="F3"): 
	with open("TL3/" + str(curfile), "r") as f:
		data = json.load(f) 
		texts = extract_text_from_dict(data) 
		joined_texts = " ".join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_patent_enkr/155.산업정보 연계 주요국 특허 영-한 데이터/01.데이터/1.Training/라벨링데이터_0831_add/TL3/" + str(curfile) 
	d3.append(cur_dict) 

files = os.listdir("TL4") 
d4 = [] 
for curfile in tqdm(files, position=0, leave=True, desc="F4"): 
	with open("TL4/" + str(curfile), "r") as f:
		data = json.load(f) 
		texts = extract_text_from_dict(data) 
		joined_texts = " ".join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_patent_enkr/155.산업정보 연계 주요국 특허 영-한 데이터/01.데이터/1.Training/라벨링데이터_0831_add/TL4/" + str(curfile) 
	d4.append(cur_dict) 

files = os.listdir("TL5") 
d5 = [] 
for curfile in tqdm(files, position=0, leave=True, desc="F5"): 
	with open("TL5/" + str(curfile), "r") as f: 
		data = json.load(f) 
		texts = extract_text_from_dict(data) 
		joined_texts = " ".join(texts) 
	cur_dict = {} 
	cur_dict["text"] = joined_texts 
	cur_dict["meta"] = "/nas/AH_Classify_patent_enkr/155.산업정보 연계 주요국 특허 영-한 데이터/01.데이터/1.Training/라벨링데이터_0831_add/TL5/" + str(curfile) 
	d5.append(cur_dict) 

full_lists.extend(d1) 
full_lists.extend(d2) 
full_lists.extend(d3) 
full_lists.extend(d4) 
full_lists.extend(d5) 

filename = "AH_Classify_patent_enkr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename) 

print(full_lists[-5:]) 

print("done!") 
