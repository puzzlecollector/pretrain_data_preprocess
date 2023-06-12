import numpy as np 
import pandas as pd 
import json 
import os 
from tqdm import tqdm

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")


files = os.listdir(".")

full_lists = [] 

for curfile in tqdm(files, desc="iterating over files"): 
	if curfile[-4:] == "json": 
		with open(curfile, "r") as f: 
			data = json.load(f) 
			arr = data["data"] 
			for i in range(len(arr)):
				try: 
					summaries = arr[i]["summary_entire"] 
					for j in range(len(summaries)): 
						cur_dict = {} 
						cur_dict["text"] = summaries[j]["orginal_text"] 
						cur_dict["meta"] = "/nas/AH_Summ_paper_kr/논문자료 요약/Training/" + str(curfile) 
						cur_dict2 = {} 
						cur_dict2["text"] = summaries[j]["summary_text"] 
						cur_dict2["meta"] = "/nas/AH_Summ_paper_kr/논문자료 요약/Training/" + str(curfile) 
						full_lists.append(cur_dict) 
						full_lists.append(cur_dict2) 
				except Exception as e: 
					print(e)
					 

print(full_lists[20]) 
filename = "AH_Summ_paper_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename)
print("done!") 
