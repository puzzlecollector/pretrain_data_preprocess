import numpy as np 
import pandas as pd 
import os 
import json 
from tqdm.auto import tqdm 
import re 


def remove_word_from_paragraph(word, paragraph): 
    pattern = r"\b" + re.escape(word) + r"\b" 
    updated = re.sub(pattern, "", paragraph) 
    return updated 


remove = "#@문장구분#"


full_lists = [] 

d1 = [] 
files = os.listdir("글짓기") 
for f in tqdm(files, position=0, leave=True, desc="글짓기"):
    dirname = "글짓기/" + str(f)
    cur_text = "" 
    with open(dirname, "r") as f: 
        data = json.load(f) 
        for i in range(len(data["paragraph"])):
            cur_text += data["paragraph"][i]["paragraph_txt"] + "\n\n\n" 
    cur_text = cur_text.replace(remove, "")  
    cur_dict = {"text":cur_text, "meta":"/nas/AH_Classify_Correct_essay_kr/024.에세이 글 평가 데이터/01.데이터/1.Training/라벨링데이터/글짓기/" + str(dirname)} 
    d1.append(cur_dict) 


d2 = [] 
files = os.listdir("대안제시") 
for f in tqdm(files, position=0, leave=True, desc="대안제시"):
    dirname = "대안제시/" + str(f)  
    cur_text = "" 
    with open(dirname, "r") as f: 
        data = json.load(f) 
        for i in range(len(data["paragraph"])):
            cur_text += data["paragraph"][i]["paragraph_txt"] + "\n\n\n" 
    cur_text = cur_text.replace(remove, "") 
    cur_dict = {"text":cur_text, "meta":"/nas/AH_Classify_Correct_essay_kr/024.에세이 글 평가 데이터/01.데이터/1.Training/라벨링데이터/대안제시/" + str(dirname)} 
    d2.append(cur_dict) 


d3 = [] 
files = os.listdir("설명글") 
for f in tqdm(files, position=0, leave=True, desc="설명글"): 
    dirname = "설명글/" + str(f) 
    cur_text = "" 
    with open(dirname, "r") as f: 
        data = json.load(f) 
        for i in range(len(data["paragraph"])): 
            cur_text += data["paragraph"][i]["paragraph_txt"] + "\n\n\n" 
    cur_text = cur_text.replace(remove, "")  
    cur_dict = {"text":cur_text, "meta":"/nas/AH_Classify_Correct_essay_kr/024.에세이 글 평가 데이터/01.데이터/1.Training/라벨링데이터/설명글/" + str(dirname)} 
    d3.append(cur_dict) 


d4 = [] 
files = os.listdir("주장") 
for f in tqdm(files, position=0, leave=True, desc="주장"): 
    dirname = "주장/" + str(f) 
    cur_text = "" 
    with open(dirname, "r") as f:  
        data = json.load(f) 
        for i in range(len(data["paragraph"])):
            cur_text += data["paragraph"][i]["paragraph_txt"] + "\n\n\n" 
    cur_text = cur_text.replace(remove, "")   
    cur_dict = {"text":cur_text, "meta":"/nas/AH_Classify_Correct_essay_kr/024.에세이 글 평가 데이터/01.데이터/1.Training/라벨링데이터/주장/" + str(dirname)} 
    d4.append(cur_dict) 

d5 = [] 
files = os.listdir("찬성반대") 
for f in tqdm(files, position=0, leave=True, desc="찬성반대"): 
    dirname = "찬성반대/" + str(f) 
    cur_text = "" 
    with open(dirname, "r") as f:
        data = json.load(f) 
        for i in range(len(data["paragraph"])):
            cur_text += data["paragraph"][i]["paragraph_txt"] + "\n\n\n"  
    cur_text = cur_text.replace(remove, "")  
    cur_dict = {"text":cur_text, "meta":"/nas/AH_Classify_Correct_essay_kr/024.에세이 글 평가 데이터/01.데이터/1.Training/라벨링데이터/찬성반대/" + str(dirname)} 
    d5.append(cur_dict) 


def dict_to_jsonl(data, filename): 
    with open(filename, "w") as f: 
        for entry in data:
            json.dump(entry, f, ensure_ascii=False) 
            f.write("\n") 

full_lists.extend(d1) 
full_lists.extend(d2) 
full_lists.extend(d3) 
full_lists.extend(d4) 
full_lists.extend(d5) 

filename = "AH_Classify_Correct_essay_kr_batch1.jsonl" 
dict_to_jsonl(full_lists, filename) 

print("done!") 

