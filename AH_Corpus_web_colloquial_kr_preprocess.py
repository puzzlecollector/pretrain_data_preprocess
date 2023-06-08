import os 
import numpy as np 
import pandas as pd
import json 
from tqdm.auto import tqdm 
import re 

directories = ["건강_의학", "게임", "과학", "동물", "방송", "뷰티", "엔터테인먼트",  "연애_결혼", "유머",  "음식",  "인터넷방송", "일상",  "취미"] 


def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f: 
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 


full_list = [] 



for directory in tqdm(directories):
	files = os.listdir(directory) 
	for idx in range(len(files)): 
		try: 
			with open(os.path.join(directory, files[idx]), "r") as f: 
				data = json.load(f) 
				for i in range(len(data["intj"])): 
					texts = data["intj"][i]["content"] 
					cur_dict = {} 
					for j in range(len(texts)):
						cur_dict["text"] = texts[j]["sentence"] 
						cur_dict["meta"] = "/nas/AH_Corpus_web_colloquial_kr/031.온라인 구어체 말뭉치 데이터/01.데이터/1.Training_220728_add/라벨링데이터/" + str(directory) + "/" + str(files[idx]) 
						full_list.append(cur_dict)  
		except Exception as e: 
			print(e) 
		

filename = "AH_Corpus_web_coloquial_kr_batch1.jsonl" 
dict_to_jsonl(full_list, filename) 
print("done!") 
