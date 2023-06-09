import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm.auto import tqdm 

directories = ["기술과학", "기타", "사회과학", "예술"]

full_lines, full_lines_summary = [], []  

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 

for directory in directories: 
	files = os.listdir(directory) 
	for curfile in tqdm(files): 
		with open(os.path.join(directory, curfile), "r") as f: 
			data = json.load(f) 
			cur_dict = {} 
			cur_dict["text"] = data["passage"] 
			cur_dict["meta"] = "/nas/AH_Summ_book_kr/도서자료 요약/Training/" + str(directory) + "/" + str(curfile) 
			full_lines.append(cur_dict) 
			
			cur_dict2 = {} 
			cur_dict2["text"] = data["summary"] 
			cur_dict2["meta"] = "/nas/AH_Summ_book_kr/도서자료 요약/Training/" + str(directory) + "/" + str(curfile) 
			full_lines_summary.append(cur_dict2) 
	

filename1 = "AH_Summ_book_kr_batch1.jsonl" 
filename2 = "AH_Summ_book_kr_batch2.jsonl" 

dict_to_jsonl(full_lines, filename1) 
dict_to_jsonl(full_lines_summary, filename2) 
print("done!") 
