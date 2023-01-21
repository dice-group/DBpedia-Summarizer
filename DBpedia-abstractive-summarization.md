## Generating Abstractive Summaries for DBpedia Abstracts

This guide provides a step-by-step process for generating abstractive summaries for the entire DBpedia abstracts.

### Steps: 

1) Download the DBpedia abstracts from this link ((https://downloads.dbpedia.org/repo/dbpedia/text/long-abstracts/2022.09.01/)). Please note that the version provided in this link is updated until September 2022.

```
e.g.,
wget https://downloads.dbpedia.org/repo/dbpedia/text/long-abstracts/2022.09.01/long-abstracts_lang%3dde.ttl.bz2
```
2) Extract the compressed version of DBpedia abstracts using the command:
  
```
e.g., 
bzip2 -d long-abstracts_lang=de.ttl.bz2
```
3) To process the DBpedia abstracts in parallel, split them into smaller files by lines using the following command:

```
split -l 70000 long-abstracts_lang\=de.ttl batch.
```
This command will generate equally split DBpedia abstracts with the prefix 'batch' and 70000 lines per file.

4) Run batches of DBpedia abstracts in parallel using the following command: 

```
(python3 summarization-cuda1.py --path='splits-de/batch.aj' & python3 summarization-cuda1.py --path='splits-de/batch.ak' & python3 summarization-cuda1.py --path='splits-de/batch.al' & python3 summarization-cuda1.py --path='splits-de/batch.am') ; (python3 summarization-cuda1.py --path='splits-de/batch.an' & python3 summarization-cuda1.py --path='splits-de/batch.ao' & python3 summarization-cuda1.py --path='splits-de/batch.ap' & python3 summarization-cuda1.py --path='splits-de/batch.aq' & python3 summarization-cuda1.py --path='splits-de/batch.ar')
```

This command generates abstractive summaries for each batch of DBpedia using the pre-defined language model (e.g., T5-large or BART-cnn-large) in ```summarization-cuda1.py```. To run different batches in parallel on another CUDA device, change the following line of code in ```summarization-cuda1.py```:

```
dev = torch.device("cuda:1") 
print("Running on the GPU")
```

5) Finally, merge the processed batches into one DBpedia-abstractive-file using the following command:

```
cat batch* >> dbpedia-abstractive-summaries.ttl
```

---

If you have any further questions, please contact [hamada.zahera@uni-paderborn.de](mailto:hamada.zahera@uni-paderborn.de)