import pandas as pd
import re
import sys
from wordsegment import load, segment

load()

def segment_hashtags(s):

    s = ' '.join([' '.join(segment(w.lstrip('#'))) if w.startswith('#') else w for w in s.split()])
    return s

#from https://stackoverflow.com/questions/3809401/what-is-a-good-regular-expression-to-match-a-url
def replace_urls(s):
    r = 'https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,}'
    return re.sub(r, 'URL', s)

def replace_mentions(s):
    r = "@(\w+)"
    return re.sub(r, '@USER', s)

def main(argv=None): #infile, sep, column, outfile
    if argv is None:
        argv = sys.argv

    infile = argv[1]
    column = argv[2]
    outfile = argv[3]

    df = pd.read_csv(infile, sep='\t')
    
    df[column] = df[column].astype(str)
    df[column] = df[column].apply(lambda x: segment_hashtags(x))
    df[column] = df[column].apply(lambda x: replace_mentions(x))
    df[column] = df[column].apply(lambda x: replace_urls(x))
    df.to_csv(outfile, sep='\t', index=False)


in_file = 'irony/train.tsv'
columnname = 'text'
out_file = 'irony/train.tsv'

args = [0, 'unprocessed-data/'+in_file, columnname, 'data/'+out_file]
main(args)

