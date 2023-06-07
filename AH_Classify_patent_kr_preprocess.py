import os 
import numpy as np 
import pandas as pd 
import json 
from tqdm.auto import tqdm 
import re 

directories = ["A_농업_임업및어업_01_03", "B_광업_05_08", "C_제조업_10_34", "D_전기_가스_증기및공기조절공급업_35", "E_수도_하수및폐기물처리_원료재생업_36_39", "F_건설업_41_42", "J_정보통신업_58_63"]

def find_json_files(directory): 
	json_files = [] 
	for root, dirs, files in os.walk(directory): 
		for file in files: 
			if file.endswith("json"): 
				json_files.append(os.path.join(root, file)) 
	return json_files 


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


full_lists = [] 
for directory_path in tqdm(directories, position=0, leave=True, desc="find all json files and extract texts"):
	json_files = find_json_files(directory_path) 
	for curfile in json_files:
		with open(curfile, "r") as f: 
			data = json.load(f) 
			texts = extract_text_from_dict(data) 
			joined_texts = " ".join(texts) 
		cur_dict = {} 
		cur_dict["text"] = joined_texts 
		cur_dict["meta"] = "/nas/AH_Classify_patent_kr/032.특허 분야 자동분류 데이터/01.데이터/1.Training/라벨링데이터/" + curfile 
		full_lists.append(cur_dict) 


filename = "AH_Classify_patent_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename)  
print("done!") 
