import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def train_model(data_file, model_file):
    df = pd.read_csv(data_file)
    X = df["sequence"]
    y = pd.get_dummies(df["function"])

    tokenizer = Tokenizer(char_level=True)
    tokenizer.fit_on_texts(X)
    X = tokenizer.texts_to_sequences(X)
    X = pad_sequences(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = Sequential()
    model.add(Embedding(len(tokenizer.word_index) + 1, 128, input_length=X.shape[1]))
    model.add(LSTM(64))
    model.add(Dense(y.shape[1], activation="softmax"))

    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
    model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, batch_size=32)

    model.save(model_file)

train_model("data/processed_known_proteins.csv", "models/trained_model.h5")
