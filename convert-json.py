import json
import csv

def convert_json(in_file, out_file):
    with open('unprocessed-data/sarcasm/'+in_file, 'r') as json_file:
        json_list = list(json_file)

    data = []
    for json_str in json_list:
        result = json.loads(json_str)
        del result['context']
        data.append(result)

    with open('unprocessed-data/sarcasm/'+out_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['label', 'response'], delimiter='\t') ## context-1, etc
        writer.writeheader()
        writer.writerows(data)

in_file = 'reddit-train.jsonl'
out_file='reddit-train-nocontext.tsv'
convert_json(in_file, out_file)

in_file = 'twitter-train.jsonl'
out_file='twitter-train-nocontext.tsv'
convert_json(in_file, out_file)

