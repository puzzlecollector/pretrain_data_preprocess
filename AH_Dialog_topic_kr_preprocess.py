meta_path = "/nas/AH_Dialog_topic_kr/020.주제별 텍스트 일상 대화 데이터/01.데이터/1.Training/라벨링데이터/" 

import numpy as np
import pandas as pd
import json
import os
from tqdm.auto import tqdm
import csv

directories = os.listdir(".")

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")

full_list = []

for directory in tqdm(directories):
	if ".json" in directory:
		try: 
			with open(directory, "r") as f: 
				data = json.load(f) 
				arr = data["info"] 
				for i in range(len(arr)): 
					text = arr[i]["annotations"]["text"] 
					cur_dict = {}
					cur_dict["text"] = text 
					cur_dict["meta"] = meta_path + str(directory) 
					full_list.append(cur_dict)  
		except Exception as e: 
			print(e) 

print(full_list[-5:]) 


filename = "AH_Dialog_topic_kr_batch1.jsonl" 
dict_to_jsonl(full_list, filename) 
print("done!") 
