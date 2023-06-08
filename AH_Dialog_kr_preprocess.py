import os 
import numpy as np 
import json 
import pandas as pd 
from tqdm.auto import tqdm 

files = os.listdir(".") 
files2 = os.listdir("J 민원")

files3 = [] 
for curfile in files2: 
	files3.append("J 민원/" + curfile) 


all_files = files + files3 

full_lines = [] 

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 



for curfile in tqdm(all_files): 
	if ".xlsx" in curfile:
		try: 
			df = pd.read_excel(curfile, engine="openpyxl") 
			texts = df["SENTENCE"] 
			for text in texts: 
				cur_dict = {} 
				cur_dict["text"] = text 
				cur_dict["meta"] = "/nas/AH_Dialog_kr/한국어 대화/" + curfile
				full_lines.append(cur_dict)   
		except Exception as e: 
			print(e) 
			questions = df["question"] 
			answers = df["answer"] 
			for q, a in zip(questions, answers): 
				text = str(q) + "\n" + str(a) 
				cur_dict = {} 
				cur_dict["text"] = text 
				cur_dict["meta"] = "/nas/AH_Dialog_kr/한국어 대화/" + curfile 
				full_lines.append(cur_dict) 

filename = "AH_Dialog_kr_batch1.jsonl" 
dict_to_jsonl(full_lines, filename) 

print(full_lines[-5:]) 
print("done!") 
