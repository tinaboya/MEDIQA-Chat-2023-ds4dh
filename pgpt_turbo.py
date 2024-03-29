import json
import openai
import random
import pandas as pd
import math
import numpy as np
import csv
import re
import joblib
import argparse

from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, confusion_matrix, f1_score, accuracy_score
from sklearn.linear_model import SGDClassifier

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

parser = argparse.ArgumentParser(description='Submission code for run1')

parser.add_argument('-f', '--file', type=str, metavar='', help='File to process')
args = parser.parse_args()

if args.file:
    print('Processing file:', args.file)
else:
    print('No file provided')

df_taska_train = pd.read_csv('./data/TaskA-TrainingSet.csv', header=0)
df_taska_test = pd.read_csv(args.file, header=0)  # this input should be write as an args

X_test = [" ".join(i.split()) for i in df_taska_test['dialogue']]
text_clf = joblib.load('./model/classification_model.joblib')

df_taska_test['section_header'] = list(text_clf.predict(X_test))  # preds, list
df_taska_test.to_csv(args.file, index=False)

openai.api_key = ""

outputs = []

for i, row in df_taska_test.iterrows():  # change this to the test set
    train_rows = df_taska_train[df_taska_train["section_header"] == row["section_header"]]
    train_row = train_rows.sample(n=1).iloc[0]

    dict1 = {"role": "user", "content": "summarize \n" + train_row["dialogue"]}
    dict2 = {"role": "assistant", "content": train_row["section_text"]}  # "correct answer \n" + 
    dict3 = {"role": "user", "content": "summarize \n" + row["dialogue"]}

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[dict1, dict2, dict3]
        )

        output = response['choices'][0]['message']['content']
        outputs.append(output)

        continue  # continue the loop if the request succeeds

    except openai.error.RateLimitError as error:
        wait_time = 2 ** i  # Backoff: wait for 2^i seconds before retrying
        print(f"Request failed. Waiting for {wait_time} seconds before retrying...")
        time.sleep(wait_time)

    else:
        # If all retries fail, raise an exception
        raise Exception("Unable to complete the request after multiple retries.")

df_submission = pd.DataFrame({"TestID": df_taska_test['ID'], "SystemOutput1": df_taska_test["section_header"]})
df_submission["SystemOutput2"] = outputs
df_submission.to_csv('./output/taskA_ds4dh_run1.csv', index=False)
