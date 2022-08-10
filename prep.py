import os
import sys

from dvc.api import params_show

# Split data into train and test
lang = sys.argv[1]
params = params_show(stages=f"prep@{lang}")["country_models"][lang]
raw_path = f"raw/{lang.split('_')[0]}"
with open(raw_path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# Train split
train_path = f"train/{lang}"
os.makedirs("train", exist_ok=True)
train_lines = int(len(lines) * params["split"])
with open(train_path, "w", encoding="utf-8") as f:
    for line in lines[:train_lines]:
        f.write(line)
        f.write("\n")

# Test split
test_path = f"test/{lang}"
os.makedirs("test", exist_ok=True)
with open(test_path, "w", encoding="utf-8") as f:
    for line in lines[train_lines:]:
        f.write(line)
        f.write("\n")
