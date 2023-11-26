from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import string
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
import os
import random
import json
import pickle

app = Flask(__name__)

# Muat model yang telah dilatih
loaded_model = tf.keras.models.load_model("Chatbot.h5")

# Muat LabelEncoder yang telah dilatih
with open('label_encoder.pkl', 'rb') as le_file:
    le = pickle.load(le_file)

# Muat informasi tokenisasi
intents = json.loads(open('intents.json').read())

# Anggap 'le' tersedia secara global
responses = {intent['tag']: intent['responses'] for intent in intents.get('intents', [])}
tags = []
inputs = []

# Ekstrak pola dan tag dari file intents.json
for intent in intents.get('intents', []):
    for lines in intent.get('patterns', []):
        inputs.append(lines)
        tags.append(intent['tag'])

# Buat DataFrame dari pola dan tag
data = pd.DataFrame({"inputs": inputs, "tags": tags})

# Praproses data input
data["inputs"] = data["inputs"].apply(lambda wrd: [''.join([ltr.lower() for ltr in wrd if ltr not in string.punctuation])])
data["inputs"] = data["inputs"].apply(lambda wrd: ''.join(wrd))

# Tokenisasi dengan menggunakan Tokenizer dari Keras
tokenizer = Tokenizer(num_words=2000)
tokenizer.fit_on_texts(data["inputs"])

# Muat model yang telah dilatih
model = load_model("Chatbot.h5")

# Tentukan bentuk input yang dibutuhkan oleh model
input_shape = model.layers[0].input_shape[1]

# Fungsi untuk praproses input pengguna
def preprocess_input(text):
    if not text:
        return None  # Or handle it accordingly
    text = [''.join([ltr.lower() for ltr in text if ltr not in string.punctuation])]
    seq = tokenizer.texts_to_sequences(text)
    padded = pad_sequences(seq, maxlen=input_shape)
    return padded

# Definisi endpoint untuk prediksi
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_input = data.get('input')

    if not user_input:
        return jsonify({'error': 'Invalid input'})

    # Praproses input pengguna
    processed_input = preprocess_input(user_input)

    if processed_input is None:
        return jsonify({'error': 'Failed to preprocess input'})

    # Lakukan prediksi menggunakan model yang telah dilatih
    prediction = loaded_model.predict(processed_input)

    if prediction.size == 0:
         return jsonify({'error': 'Failed to make predictions'})

    # Konversi prediksi menjadi label menggunakan LabelEncoder yang telah dilatih
    predicted_label = np.argmax(prediction)

    # Sekarang  dapat menggunakan 'prediction' dan 'predicted_label'
    # gunakan inverse_transform secara langsung
    predicted_tag = le.inverse_transform([predicted_label])[0]

    # Siapkan respons berupa tag dan respons acak
    response = {
        'tag': predicted_tag,
        'response': random.choice(responses.get(predicted_tag, []))
    }

    return jsonify(response)

# Jalankan aplikasi jika script ini dijalankan langsung
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

