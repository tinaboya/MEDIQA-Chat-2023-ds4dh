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

for _, row in df_taska_test.iterrows():
    prompt_text = row["dialogue"]

    response = openai.Completion.create(
        engine="curie:ft-personal-2023-03-09-09-42-13",  # Specify the GPT model to use
        prompt=prompt_text,
        max_tokens=int(pow(2, math.ceil(math.log2(len(prompt_text.split()) / 2.5)))),
        # Limit the output length to 1024 tokens
        n=1,  # Generate only one completion
        stop=None,  # Don't stop generation at any sequence
    )

    output_text = response.choices[0].text
    outputs.append(output_text)

df_submission = pd.DataFrame({"TestID": data['ID'], "SystemOutput1": data["section_header"]})
df_submission["SystemOutput2"] = outputs
df_submission.to_csv('./output/taskA_ds4dh_run2.csv', index=False)
