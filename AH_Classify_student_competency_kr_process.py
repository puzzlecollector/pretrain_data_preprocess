import os 
import numpy as np 
import pandas as pd 
import json 
from tqdm.auto import tqdm 
import re 
import csv 

directories = ["교과목 핵심개념 데이터", "미션정보 데이터", "수업기록 데이터", "역량 변환표 데이터", "프로그램정보 데이터", "학생정보데이터"]

extensions = [".csv", ".json"]

def find_csv_files(directory):
	csv_files = [] 
	for root, dirs, files in os.walk(directory):
		for curfile in files: 
			if curfile.endswith(".csv"):
				csv_files.append(os.path.join(root, curfile)) 
	return csv_files 

def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f: 
		for entry in data: 
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 

def extract_text_from_dict(data): 
	texts = [] 
	for key, value in data.items(): 
		if isinstance(value, str): 
			texts.append(value) 
		elif isinstance(value, list): 
			for element in value:
				if isinstance(element, str): 
					texts.append(element) 
				elif isinstance(element, dict): 
					nested_texts = extract_text_from_dict(element) 
					texts.extend(nested_texts) 
		elif isinstance(value, dict): 
			nested_texts = extract_text_from_dict(value) 
			texts.extend(nested_texts) 
	return texts 

def extract_text_from_csv(file_path):
	texts = [] 
	with open(file_path, "r", encoding="utf-8") as file:
		csv_reader = csv.reader(file) 
		for row in csv_reader:
			for entry in row: 
				if len(entry) >= 10:
					texts.append(entry) 
	return " ".join(texts) 


full_lists = [] 
for directory_path in tqdm(directories, position=0, leave=True, desc="find all json files and extract texts"):
	csv_files = find_csv_files(directory_path) 	
	for csv_file in csv_files: 
		texts = extract_text_from_csv(csv_file)
		cur_dict = {} 
		cur_dict["text"] = texts 
		cur_dict["meta"] = "/nas/AH_Classify_student_competency_kr/142.학생 청소년 교육활동 역량 데이터/01.데이터/1. Training/라벨링데이터/" + str(csv_file) 
		full_lists.append(cur_dict) 

filename = "AH_Classify_student_competency_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename) 
print("done!") 
