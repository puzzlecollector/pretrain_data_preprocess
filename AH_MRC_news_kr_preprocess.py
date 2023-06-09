import numpy as np 
import pandas as pd
import os 
import json 
from tqdm.auto import tqdm 

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 


files = os.listdir(".") 

full_lines = [] 

for curfile in tqdm(files): 
	if ".json" in curfile:
		try:  
			with open(curfile, "r") as f: 
				data = json.load(f) 
				arr = data["data"] 
				for i in range(len(arr)): 
					text = arr[i]["doc_title"] + "\n"  
					paragraphs = arr[i]["paragraphs"] 
					for j in range(len(paragraphs)):
						text += paragraphs[j]["context"]
					cur_dict = {} 
					cur_dict["text"] = text 
					cur_dict["meta"] = "/nas/AH_MRC_news_kr/017.뉴스 기사 기계독해 데이터/01.데이터/1.Training/라벨링데이터/" + str(curfile) 
					full_lines.append(cur_dict) 
						 
		except Exception as e: 
			print(e) 


filename = "AH_MRC_news_kr_batch1.jsonl"
dict_to_jsonl(full_lines, filename) 
print("done!") 
