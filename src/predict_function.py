import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def predict_function(input_file, model_file, output_file):
    df = pd.read_csv(input_file)
    X = df["sequence"]

    tokenizer = Tokenizer(char_level=True)
    tokenizer.fit_on_texts(X)
    X = tokenizer.texts_to_sequences(X)
    X = pad_sequences(X)

    model = load_model(model_file)
    predictions = model.predict(X)

    df["predicted_function"] = predictions.argmax(axis=1)
    df.to_csv(output_file, index=False)

predict_function("data/unknown_proteins.fasta", "models/trained_model.h5", "results/predictions.csv")
