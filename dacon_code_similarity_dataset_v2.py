import os
import numpy as np
import pandas as pd
import json
from tqdm import tqdm
full = []
folders = os.listdir("code_data/code")
for folder in tqdm(folders):
    if "problem" in folder:
        files = os.listdir("code_data/code/" + folder)
        for file in files:
            with open("code_data/code/" + str(folder)  + "/" + str(file), "r") as f:
                file_contents = f.read()
            cur_dict = {}
            cur_dict["text"] = file_contents
            cur_dict["meta"] = "dacon_code_similarity"
            full.append(cur_dict)
def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")
dict_to_jsonl(full, "dacon_code_similarity_batch2.jsonl")
print(full[-3:])
print("done!")
