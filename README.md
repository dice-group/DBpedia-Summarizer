# Towards Abstractive Summarization of DBpedia Abstracts Using Language Models


## Overview

Dataset and code for paper "Towards Abstractive Summarization of DBpedia Abstracts Using Language Models".


We propose an abstractive summarization approach using pre-trained language models to generate short, concise and comprehensive summaries for DBpedia abstracts. We evaluate the efficiency of state-of-the-art language models **BART** and **T5** in generating abstractive summaries of DBpedia abstracts in six languages (English, German, French, Italian, Spanish and Dutch). 


## Dependencies:

```
bert-score 0.3.12
ipykernel 6.17.1
ipython 8.6.0
nltk 3.7
notebook 6.5.2
pandas 1.5.1
spacy 3.4.3
torch 1.13.0
transformers 4.25.1
```


## Installation

```
pip install -r requirements.txt
```


## Data preparation

1. Download DBpedia abstract file (.ttl) in required language [source](http://downloads.dbpedia.org/2015-04/ext/nlp/abstracts/) and put in in the [full_abstracts](/full_abstracts/) folder.
2. Download DBpedia shorteabstract file (.ttl) in required language [source](https://databus.dbpedia.org/dbpedia/text/short-abstracts/) and unzip it in the [short_abstracts](/short_abstracts/) folder.
3. Run the [data_creation notebook](/data_creation.ipynb). Final dataframes should be located in [data](/data/) folder.


## Pretrained models

1. Data for generating summaries located in [data](/data/) folder in .csv files.
2. Notebook [baselines.ipynb](/baselines.ipynb) contains code for running pretrained models (T5, BART and BART-CNN).
3. Generated summaries storing in the dataframe files in separate columns ([example](/data/t5sum_nl_1000.csv), [example](/data/BARTsum_nl_534.csv)).


## Contact

If you have any further questions/feedback, please contact corresponding authors at [fedor.vitiugin@upf.edu](mailto:fedor.vitiugin@upf.edu) and [hamada.zahera@uni-paderborn.de](mailto:hamada.zahera@uni-paderborn.de).