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

full_lines = [] 

with open("도서_220419_add.json", "r") as f: 
	data = json.load(f) 
	arr = data["data"] 
	for i in tqdm(range(len(arr))):
		text = "" 
		text += arr[i]["title"] + "\n"  
		paragraphs = arr[i]["paragraphs"] 
		for j in range(len(paragraphs)): 
			text += paragraphs[j]["context"] 
		cur_dict = {} 
		cur_dict["text"] = text 
		cur_dict["meta"] = "/nas/AH_MRC_book_kr/도서자료 기계독해/Training/도서_220419_add/도서_220419_add.json"
		full_lines.append(cur_dict) 
	


print(full_lines[-2:]) 
filename = "AH_MRC_book_batch1.jsonl" 
dict_to_jsonl(full_lines, filename) 
print("done!")  
