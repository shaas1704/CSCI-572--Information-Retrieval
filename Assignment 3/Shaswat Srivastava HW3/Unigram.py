import re
import os
from collections import defaultdict
from functools import reduce

PATTERN = re.compile(r'[^\w\s]')

def clean_text(data):
    data = PATTERN.sub(' ', data)
    data = re.sub(r'\d+', ' ', data)
    return data.lower().strip()

def find_files(directory):
    paths = []
    for item in os.listdir(directory):
        if item.endswith(".txt"):
            paths.append(os.path.join(directory, item))
    return paths

def process_file(file_path):
    results = defaultdict(lambda: defaultdict(int))

    with open(file_path, 'r') as f:
        for line in f:
            split_line = line.strip().split('\t', 1)
            if len(split_line) < 2:
                continue
            doc_id, content = split_line[0].strip(), split_line[1].strip()

            tokens = clean_text(content).split()

            for token in tokens:
                results[f"unigram:{token}"][doc_id] += 1
    return results

def merge_data(data1, data2):
    for key, docs in data2.items():
        if key in data1:
            for doc_id, count in docs.items():
                data1[key][doc_id] += count
        else:
            data1[key] = docs
    return data1

def output_results(data):
    with open("unigram_index.txt", "w") as output_file:
        for key, docs in data.items():
            doc_str = ' '.join([f"{doc_id}:{count}" for doc_id, count in docs.items()])
            if key.startswith("unigram:"):
                output_file.write(f"{key[8:]}\t{doc_str}\n")

if __name__ == "__main__":
    data_dir = 'fulldata'

    files = find_files(data_dir)

    mapped_data = map(process_file, files)

    combined_data = reduce(merge_data, mapped_data)

    output_results(combined_data)
