import pandas as pd
from sklearn.model_selection import train_test_split

df1 = pd.read_csv('implicithate/implicit_hate_v1_stg1_posts.tsv', sep='\t')

train1, test1 = train_test_split(df1, test_size=0.2, stratify=df1['labels'])

train1.to_csv('implicithate/train1.tsv', sep='\t', index=False)
test1.to_csv('implicithate/test1.tsv', sep='\t', index=False)