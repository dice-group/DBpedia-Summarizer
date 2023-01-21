import torch
import argparse

if torch.cuda.is_available():
    dev = torch.device("cuda:1") 
    print("Running on the GPU")
else:
    dev = torch.device("cpu")
    print("Running on the CPU")


# load CNN-trained BART model and tokenizer
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import glob

sum_model = AutoModelForSeq2SeqLM.from_pretrained("t5-large")
tokenizer = AutoTokenizer.from_pretrained("t5-large")
sum_model.to(dev)


def abstractive_summarization(fname):
    with open(fname, 'r') as infile:

        for line in infile:

            triple=line.split('> "')
            tokens=triple[1].split('\"@')

            inputs = tokenizer("summarize: " + tokens[0], return_tensors="pt", max_length=512, truncation=True) # input abstract text
            inputs.to(dev)
            outputs = sum_model.generate(inputs["input_ids"], max_length=100, min_length=40, length_penalty=4.0, num_beams=4, early_stopping=True) # generating summary        
            summary=tokenizer.decode(outputs[0])[6:-4]


            new_file= fname.split('/')[-1]
            with open("abstractive-summaries-de/"+new_file, "a") as outfile:            
                outfile.write(triple[0]+'> \"'+summary+'\"@'+tokens[1])

                outfile.close()
                

def main():
    parser = argparse.ArgumentParser()         
    parser.add_argument("--path",  help="please specifiy the path of DBpedia split")
    
    args= parser.parse_args()    
        
    abstractive_summarization(args.path)
    


if __name__ == '__main__':
    main()