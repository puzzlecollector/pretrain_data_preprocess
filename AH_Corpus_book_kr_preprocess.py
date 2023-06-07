import numpy as np 
import pandas as pd 
import os 
from tqdm import tqdm 
import csv 
import json 

tsv_file_path = "000_DATA.tsv" 


full_lines = [] 

with open(tsv_file_path, "r", encoding="utf-8") as file: 
	reader = csv.reader(file, delimiter="\t") 
	for line_num, line in tqdm(enumerate(reader, start=1)): 
		cur_dict = {} 
		try:
			cur_dict["text"] = line[1] 
			cur_dict["meta"] = "/nas/AH_Corpus_book_kr/029.대규모 구매도서 기반 한국어 말뭉치 데이터/01.데이터/4.Sample/sample/라벨링데이터/000/" + tsv_file_path 
			full_lines.append(cur_dict) 
		except csv.Error as e: 
			print(f"Error occurred on line {line_num}: {str(e)}") 
			continue


def dict_to_jsonl(data, filename): 
	with open(filename, "w") as f: 
		for entry in data:
			json.dump(entry, f, ensure_ascii=False) 
			f.write("\n") 

filename = "AH_Corpus_book_kr_batch1.jsonl"  
dict_to_jsonl(full_lines, filename)
print("done!") 
