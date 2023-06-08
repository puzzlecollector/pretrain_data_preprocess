import numpy as np 
import pandas as pd 
import json 
import os 
from tqdm.auto import tqdm 
import re 

def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f: 
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 


directories = ["건축허가",  "경제",  "공통",  "교통",  "농업_축산",  "문화_체육_관광", "보건소",  "복지",  "산림",  "상하수도",  "세무",  "안전건설",  "위생",  "자동차",  "정보통신",  "토지",
"행정",  "환경미화"]  

full_lists = [] 


for directory in tqdm(directories): 
	files = os.listdir(directory) 
	for curfile in files: 
		try: 
			with open(os.path.join(directory, curfile), "r") as f: 
				data = json.load(f) 
				arr = data["documents"] 
				for i in range(len(arr)): 
					cur_dict = {} 
					text = arr[i]["Q_refined"]  
					cur_dict["text"] = text 
					cur_dict["meta"] = "/nas/AH_Dialog_Complaint_kr/143.민원 업무 효율, 자동화를 위한 언어 AI 학습데이터/01.데이터/1.Training/라벨링데이터/" + os.path.join(directory, curfile)
					full_lists.append(cur_dict) 
		except Exception as e: 
			print(e)


print(full_lists[-5:]) 

filename = "AH_Dialog_Complaint_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename) 
print("done!") 
