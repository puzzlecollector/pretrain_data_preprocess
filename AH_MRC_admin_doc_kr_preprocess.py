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

full_lines = [] 

for curfile in files: 
	if ".json" in curfile: 
		with open(curfile, "r") as f: 
			data = json.load(f) 
			arr = data["data"]  
			for i in range(len(arr)):  
				#text = arr[i]["doc_title"] + "\n" 
				text = "" 
				paragraphs = arr[i]["paragraphs"] 
				for j in range(len(paragraphs)): 
					text += paragraphs[j]["context"] 
				cur_dict = {} 
				cur_dict["text"] = text 
				cur_dict["meta"] = "/nas/AH_MRC_admin_doc_kr/016.행정 문서 대상 기계독해 데이터/01.데이터/1.Training/라벨링데이터/" + str(curfile) 
				full_lines.append(cur_dict) 

filename = "AH_MRC_admin_doc_kr_batch1.jsonl"
dict_to_jsonl(full_lines, filename) 
print("done!") 
