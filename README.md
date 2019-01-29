# Taller CCD

In this workshop, you will learn two key parts of the open data science pipeline: collecting data and analysing. Specifically you will learn how to collect text from websites, transform the text into data, and then how build a recommendation engine based in this data.

## Installation instructions

Open your Terminal (Mac) or Command Prompt (Windows) and type the following:

    python3 -m pip install --upgrade pip
    python3 -m pip install jupyter
    python3 -m pip install -U spacy
    python3 -m spacy download en
    python3 -m pip install -U scikit-learn
    python3 -m pip install -U pandas
    python3 -m pip install -U requests
    python3 -m pip install -U retrying
    python3 -m pip install -U beautifulsoup4
    python3 -m pip install -U lxml

## Choose a tutorial

In your Terminal (Mac) or Command Prompt (Windows) navigate to Documents:


Windows:

    cd \Users\[user name]\Documents\taller_centro_cultura_digital

Mac:

    cd /Users/[user name]/Documents/taller_centro_cultura_digital

and run:

    jupyter notebook

and select either 'data_collection_walkthrough.ipynb' or 'data_analysis_walkthrough.ipynb'.
