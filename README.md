# MEDIQA-Chat-2023-ds4dh

The following commands help you to get quick-started:

```
./install.sh
./activate.sh
decode_taskA_run1.sh ./data/taskA_testset.csv
decode_taskA_run2.sh ./data/taskA_testset.csv
```

- The input is in the *.csv format of the original test files
- The output files are in the output folder
- The output files are named taskA_ds4dh_run1.csv and taskA_ds4dh_run2.csv
- openai.api_key = "", please add and use your key

## Please Cite

If you find this work useful, please consider citing the following paper:

```bibtex
@inproceedings{zhang-etal-2023-ds4dh,
    title = "{DS}4{DH} at {MEDIQA}-Chat 2023: Leveraging {SVM} and {GPT}-3 Prompt Engineering for Medical Dialogue Classification and Summarization",
    author = "Zhang, Boya  and
      Mishra, Rahul  and
      Teodoro, Douglas",
    booktitle = "Proceedings of the 5th Clinical Natural Language Processing Workshop",
    month = jul,
    year = "2023",
    address = "Toronto, Canada",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2023.clinicalnlp-1.57",
    doi = "10.18653/v1/2023.clinicalnlp-1.57",
    pages = "536--545",
    abstract = "This paper presents the results of the Data Science for Digital Health (DS4DH) group in the MEDIQA-Chat Tasks at ACL-ClinicalNLP 2023. Our study combines the power of a classical machine learning method, Support Vector Machine, for classifying medical dialogues, along with the implementation of one-shot prompts using GPT-3.5. We employ dialogues and summaries from the same category as prompts to generate summaries for novel dialogues. Our findings exceed the average benchmark score, offering a robust reference for assessing performance in this field.",
}
