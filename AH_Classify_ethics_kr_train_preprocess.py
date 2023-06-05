import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm.auto import tqdm 
import re 

def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 


file1 = os.listdir("talksets-train-1")[0] 
file2 = os.listdir("talksets-train-2")[0] 
file3 = os.listdir("talksets-train-3")[0] 
file4 = os.listdir("talksets-train-4")[0] 
file5 = os.listdir("talksets-train-5")[0] 


full_list = [] 


d1 = [] 
with open("talksets-train-1/" + str(file1), "r") as f: 
	data = json.load(f)
	for j in tqdm(range(len(data)), desc="file1"): 
		cur_text = "" 
		for i in range(len(data[j]["sentences"])): 
			cur_text += data[j]["sentences"][i]["text"] 
		cur_dict = {} 
		cur_dict["text"] = cur_text 
		cur_dict["meta"] = "/nas/AH_Classify_ethics_kr/147.텍스트 윤리검증 데이터/01.데이터/1.Training/라벨링데이터/aihub/talksets-train-1/" + str(file1) 
		d1.append(cur_dict) 


d2 = [] 
with open("talksets-train-2/" + str(file2), "r") as f: 
	data = json.load(f) 
	for j in tqdm(range(len(data)), desc="file2"):
		cur_text = "" 
		for i in range(len(data[j]["sentences"])):
			cur_text += data[j]["sentences"][i]["text"] 
		cur_dict = {} 
		cur_dict["text"] = cur_text 
		cur_dict["meta"] = "/nas/AH_Classify_ethics_kr/147.텍스트 윤리검증 데이터/01.데이터/1.Training/라벨링데이터/aihub/talksets-train-2/" + str(file2) 
		d2.append(cur_dict) 


d3 = [] 
with open("talksets-train-3/" + str(file3), "r") as f:
	data = json.load(f) 
	for j in tqdm(range(len(data)), desc="file3"):
		cur_text = "" 
		for i in range(len(data[j]["sentences"])):
			cur_text += data[j]["sentences"][i]["text"]
		cur_dict = {} 
		cur_dict["text"] = cur_text
		cur_dict["meta"] = "/nas/AH_Classify_ethics_kr/147.텍스트 윤리검증 데이터/01.데이터/1.Training/라벨링데이터/aihub/talksets-train-3/" + str(file3) 
		d3.append(cur_dict) 

d4 = [] 
with open("talksets-train-4/" + str(file4), "r") as f:
	data = json.load(f) 
	for j in tqdm(range(len(data)), desc="file4"): 
		cur_text = "" 
		for i in range(len(data[j]["sentences"])):
			cur_text += data[j]["sentences"][i]["text"] 
		cur_dict = {} 
		cur_dict["text"] = cur_text 
		cur_dict["meta"] = "/nas/AH_Classify_ethics_kr/147.텍스트 윤리검증 데이터/01.데이터/1.Training/라벨링데이터/aihub/talksets-train-4/" + str(file4) 
		d4.append(cur_dict) 

d5 = [] 
with open("talksets-train-5/" + str(file5), "r") as f:
	data = json.load(f)
	for j in tqdm(range(len(data)), desc="file5"):
		cur_text = "" 
		for i in range(len(data[j]["sentences"])): 
			cur_text += data[j]["sentences"][i]["text"] 
		cur_dict = {} 
		cur_dict["text"] = cur_text 
		cur_dict["meta"] = "/nas/AH_Classify_ethics_kr/147.텍스트 윤리검증 데이터/01.데이터/1.Training/라벨링데이터/aihub/talksets-train-5/" + str(file5) 
		d5.append(cur_dict) 

full_list.extend(d1) 
full_list.extend(d2) 
full_list.extend(d3) 
full_list.extend(d4) 
full_list.extend(d5) 

filename = "AH_Classify_ethics_kr_batch1.jsonl" 
dict_to_jsonl(full_list, filename) 
print("done!") 
