import pickle
import numpy as np
from keras.utils import pad_sequences
from keras.models import load_model
import re

# Load tokenizer and model
with open('tokenizerForSpamDetection.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

model = load_model('SpamDetectionModel.h5')

action_label = ["Ham", "Spam"]


# Function to preprocess input statement
def preprocess_input(statement):
    statement = statement.lower()
    statement = statement.strip()

    file_name_pattern = r'\b\w+\.\w+\b'
    time_pattern = r'\b\d{1,2}:\d{2}\b'
    url_pattern = r'\bhttps?://\S+\b'
    url_pattern1 = r'\bwww\.\S+\b'
    phone_number_pattern = r'\b(?:\+\d{1,3}[- ]?)?\(?\d{1,4}\)?[- ]?\d{1,5}[- ]?\d{1,5}[- ]?\d{1,5}\b'

    new_sentence = re.sub(file_name_pattern, '', statement)
    new_sentence = re.sub(time_pattern, '', new_sentence)
    new_sentence = re.sub(url_pattern, '', new_sentence)
    new_sentence = re.sub(url_pattern1, '', new_sentence)
    new_sentence = re.sub(phone_number_pattern, '', new_sentence)

    return new_sentence


# Function to predict action based on input statement
def predict_action(statement):
    processed_statement = preprocess_input(statement)
    new_sentence = processed_statement
    token_list = tokenizer.texts_to_sequences([new_sentence])
    input_sequence = np.array(pad_sequences(token_list, maxlen=model.input_shape[1], padding='pre'))
    predicted_probabilities = model.predict(input_sequence)
    predicted_action_index = np.argmax(predicted_probabilities, axis=1)
    predicted_action = action_label[predicted_action_index[0]]
    return predicted_action


# Chatbot interaction loop
while True:
    user_input = input("Message: ")
    if user_input.lower() == 'quit':
        break
    action = predict_action(user_input)
    print("Prediction: ", action)
