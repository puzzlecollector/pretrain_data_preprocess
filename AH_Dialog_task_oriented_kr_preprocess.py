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
	if ".zip" not in directory: 
		if ".py" not in directory:
			try: 
				json_files = os.listdir(directory) 
				for json_file in json_files: 
					with open(os.path.join(directory, json_file), "r") as f: 
						data = json.load(f)
						arr = data["info"] 
						for i in range(len(arr)): 
							text = arr[i]["annotations"]["text"] 
							cur_dict = {} 
							cur_dict["text"] = text 
							cur_dict["meta"] = "/nas/AH_Dialog_task_oriented_kr/021.용도별 목적대화 데이터/01.데이터/1.Training/라벨링데이터/" + str(os.path.join(directory,json_file)) 
							full_list.append(cur_dict)
			except Exception as e: 
				print(e) 
			


filename = "AH_Dialog_task_oriented_kr_batch1.jsonl" 
dict_to_jsonl(full_list, filename) 

print(full_list[-5:]) 

print("done!") 
