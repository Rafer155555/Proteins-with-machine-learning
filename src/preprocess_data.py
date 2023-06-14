import pandas as pd
from Bio import SeqIO

def preprocess_data(input_file, output_file):
    sequences = []
    functions = []

    for record in SeqIO.parse(input_file, "fasta"):
        sequences.append(str(record.seq))
        functions.append(record.description.split("|")[-1])

    df = pd.DataFrame({"sequence": sequences, "function": functions})
    df.to_csv(output_file, index=False)

preprocess_data("data/known_proteins.fasta", "data/processed_known_proteins.csv")
