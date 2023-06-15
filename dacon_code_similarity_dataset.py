import os
import numpy as np
import pandas as pd
import json
from tqdm import tqdm

test_df = pd.read_csv("code_data/test.csv")
codes = np.concatenate([test_df["code1"].values, test_df["code2"].values])
full_data = []
for code in codes:
    cur_dict = {}
    cur_dict["text"] = code
    cur_dict["meta"] = "dacon_code_similarity"
    full_data.append(cur_dict)

print(full_data[-3:])

def dict_to_jsonl(data, filename):
	with open(filename, "w") as f:
		for entry in data:
			json.dump(entry, f, ensure_ascii=False)
			f.write("\n")
dict_to_jsonl(full_data, "dacon_code_similarity_batch1.jsonl")
print("done!")
