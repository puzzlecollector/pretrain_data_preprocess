import pandas as pd 
import os 
import json 
from tqdm.auto import tqdm 
import re 

directories = ["IT_과학", "건강", "경제",  "교육",  "국제",  "라이프스타일",  "문화",  "사건사고",  "사회일발",  "산업",  "스포츠",  "여성복지",  "여행레저",  "연예",  "정치",  "지역",  "취미"]


def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")


full_list = []

for directory in tqdm(directories, desc="iterating over all directories", position=0, leave=True):
	files = os.listdir(directory)
	for idx in tqdm(range(len(files)), desc="iterating over json files", position=0, leave=True):
		try:
			with open(os.path.join(directory, files[idx]), "r") as f:
				data = json.load(f)
				arr = data["named_entity"] 
				for i in range(len(arr)): 
					texts = arr[i]["title"] 
					for j in range(len(texts)): 
						sentence = texts[j]["sentence"] 
						cur_dict = {}
						cur_dict["text"] = sentence 
						cur_dict["meta"] = "/nas/AH_Corpus_web_kr/030.웹데이터 기반 한국어 말뭉치 데이터/01.데이터/1.Training/라벨링데이터" + str(directory) + "/" + str(files[idx])
						full_list.append(cur_dict)
				
		except Exception as e:
			print(e)



print(full_list[-5:]) 

filename = "AH_Corpus_web_kr_batch1.jsonl"
dict_to_jsonl(full_list, filename)
print("done!")
