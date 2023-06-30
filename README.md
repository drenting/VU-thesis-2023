# VU-thesis-2023

1. Download data from the links below and place in separate folders

    sarcasm:
    https://github.com/EducationalTestingService/sarcasm/tree/master

    sentiment:
    https://github.com/leelaylay/TweetSemEval/tree/master/dataset/train

    emotion:
    #Emotional Tweets
    http://saifmohammad.com/WebPages/SentimentEmotionLabeledData.html

    irony:
    https://github.com/Cyvhee/SemEval2018-Task3/blob/master/datasets/train/SemEval2018-T3-train-taskA.txt

    abuseeval:
    https://github.com/tommasoc80/AbuseEval/tree/master/data/abuseval_labels

    trac:
    https://sites.google.com/view/trac1/shared-task 

    implicithate:
    https://github.com/SALT-NLP/implicit-hate


2. change headers of text columns to 'text', label columns to 'labels'

3. run convert-json.py to convert the jsonl files to tsv files

4. run train-test-split.py to split IHC into train and test

4. run preprocessing.py on all the datasets

5. ready to run the notebooks!