## Towards Abstractive Summarization of DBpedia Abstracts Using Language Models

---
## Overview

This repository contains the dataset and code for our paper "Abstractive Summarization of DBpedia Abstracts Using Language Models." We propose an approach using pre-trained language models, specifically BART and T5, to generate short and comprehensive summaries for DBpedia abstracts in six languages (English, German, French, Italian, Spanish, and Dutch).

<figure style="text-align: center;">
<img src="dbepdia-summarization.pdf" width="600" height="400">
 <figcaption>The pipeline of DBpedia summarization using language models</figcaption>
</figure>

---
## Dependencies

- bert-score 0.3.12
- ipykernel 6.17.1
- ipython 8.6.0
- nltk 3.7
- notebook 6.5.2
- pandas 1.5.1
- spacy 3.4.3
- torch 1.13.0
- transformers 4.25.1


## Repository Structure:

```
├── data
│   ├── BARTsum_nl_1000.csv
│   ├── BARTsum_nl_534.csv
│   ├── data_en.csv
│   ├── data_fr.csv
│   ├── data_nl.csv
│   ├── sum_en100.csv
│   └── t5sum_nl_1000.csv
├── full_abstracts
│   └── info.md
├── short_abstracts
│   └── info.md
├── baselines.ipynb
├── data_creation.ipynb
├── dbepdia-summarization.pdf
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

To install the dependencies, run:

```
pip install -r requirements.txt
```

## Data Preparation

1. Download the DBpedia abstract file (in .ttl format) for the desired language from [this source](http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/) and place it in the `full_abstracts` folder.
2. Download the DBpedia short abstract file (in .ttl format) for the desired language from [this source](https://databus.dbpedia.org/dbpedia/text/short-abstracts/) and unzip it in the `short_abstracts` folder.
3. Run the `data_creation` notebook. The final dataframes should be located in the `data` folder.

## Pretrained Models

1. The data for generating summaries is located in the `data` folder in .csv files.
2. The `baselines.ipynb` notebook contains the code for running the pretrained models (T5, BART, and BART-CNN).
3. The generated summaries are stored in separate columns in dataframe files (e.g. `t5sum_nl_1000.csv`, `BARTsum_nl_534.csv`).

---
## Contact

For any questions or feedback, please contact the corresponding authors at [fedor.vitiugin@upf.edu](mailto:fedor.vitiugin@upf.edu) and [hamada.zahera@uni-paderborn.de](mailto:hamada.zahera@uni-paderborn.de).
