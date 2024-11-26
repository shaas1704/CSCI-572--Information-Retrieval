import re
import os
from collections import defaultdict
from functools import reduce

PATTERN = re.compile(r'[^\w\s]')

KEY_BIGRAMS = {
    "computer science", "information retrieval", "power politics",
    "los angeles", "bruce willis"
}

def clean_text(data):
    data = PATTERN.sub(' ', data)
    data = re.sub(r'\d+', ' ', data)
    return data.lower().strip()

def collect_files(path):
    paths = []
    for name in os.listdir(path):
        if name.endswith(".txt"):
            paths.append(os.path.join(path, name))
    return paths

def parse_file(filepath):
    results = defaultdict(lambda: defaultdict(int))

    with open(filepath, 'r') as f:
        for entry in f:
            split_entry = entry.strip().split('\t', 1)
            if len(split_entry) < 2:
                continue
            doc, text = split_entry[0].strip(), split_entry[1].strip()

            tokens = clean_text(text).split()

            for j in range(len(tokens) - 1):
                pair = f"{tokens[j]} {tokens[j + 1]}"
                if pair in KEY_BIGRAMS:
                    results[f"bigram:{pair}"][doc] += 1

    return results

def merge_results(dict1, dict2):
    for k, docs in dict2.items():
        if k in dict1:
            for doc, val in docs.items():
                dict1[k][doc] += val
        else:
            dict1[k] = docs
    return dict1

def write_output(data):
    with open("selected_bigram_index.txt", "w") as out_file:
        for key, docs in data.items():
            doc_str = ' '.join([f"{doc}:{count}" for doc, count in docs.items()])
            if key.startswith("bigram:"):
                out_file.write(f"{key[7:]}\t{doc_str}\n")

if __name__ == "__main__":
    data_path = 'devdata'

    files = collect_files(data_path)

    mapped_data = map(parse_file, files)

    final_data = reduce(merge_results, mapped_data)

    write_output(final_data)
