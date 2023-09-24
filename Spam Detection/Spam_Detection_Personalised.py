import io
import json
import pickle
import tensorflow
from tensorflow import keras
from keras.preprocessing.text import Tokenizer
import pandas as pd
import numpy as np
# from keras.preprocessing.sequence import pad_sequences
from keras.utils import pad_sequences
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Embedding, LSTM, Dense, Bidirectional, Attention, BatchNormalization, Dropout
from sklearn.model_selection import train_test_split
import re
from keras.callbacks import EarlyStopping
from sklearn.metrics import precision_score, f1_score, balanced_accuracy_score, roc_auc_score, accuracy_score

early_stopping = EarlyStopping(patience=2, monitor='val_loss', restore_best_weights=True)

action_label = ["Spam", "Ham"]

action_map = {"ham": 0, "spam": 1}

tokenizer = Tokenizer(num_words=10000, oov_token='<OOV>')

data = pd.read_csv('../Spam_SMS_3.csv', encoding='latin1')

data = data[['Label', 'SMS']]

file_name_pattern = r'\b\w+\.\w+\b'
time_pattern = r'\b\d{1,2}:\d{2}\b'
url_pattern = r'\bhttps?://\S+\b'
url_pattern1 = r'\bwww\.\S+\b'
phone_number_pattern = r'\b(?:\+\d{1,3}[- ]?)?\(?\d{1,4}\)?[- ]?\d{1,5}[- ]?\d{1,5}[- ]?\d{1,5}\b'

current = []
for sentence in data['SMS']:
    if sentence is not "nan":
        # print(sentence)
        new_sentence = re.sub(file_name_pattern, '', sentence)
        new_sentence = re.sub(time_pattern, '', new_sentence)
        new_sentence = re.sub(url_pattern, '', new_sentence)
        new_sentence = re.sub(url_pattern1, '', new_sentence)
        new_sentence = re.sub(phone_number_pattern, '', new_sentence)
        current.append(new_sentence)

tokenizer.fit_on_texts(current)
total_words = len(tokenizer.word_index) + 1
# print(total_words)
# print(tokenizer.word_index)
common_words = pd.read_csv("Commonly_used_words.csv", encoding='latin1')
sorted_count = pd.DataFrame()
words = []
counts = []
for word, count in tokenizer.word_counts.items():
    words.append(word)
    counts.append(count)
sorted_count["Word"] = words
sorted_count["Count"] = counts
sorted_count = sorted_count.sort_values(by=["Count"], ascending=False)
print(sorted_count[:40])

pri

for word, count in tokenizer.word_counts.items():
    print(f"{word}: {count}")
# print([x for _, x in tokenizer.word_counts.items()])
pri
input_sequences = tokenizer.texts_to_sequences(data["SMS"])
max_sequence_len = max([len(seq) for seq in input_sequences])
print(max_sequence_len)
# input_sequences = pad_sequences(input_sequences, maxlen=max_sequence_len, padding='post')

output_labels = [action_map[label] for label in data["Label"]]

spam_act = 0
ham_act = 0
for actual in output_labels:
    if actual == 0:
        ham_act += 1
    else:
        spam_act += 1
print(f"Spam: {spam_act}, Ham: {ham_act}")

print(max_sequence_len)

input_sequences = np.array(pad_sequences(input_sequences, maxlen=max_sequence_len, padding='pre'))
output_labels = to_categorical(output_labels, num_classes=len(action_label))

xs = input_sequences
labels = output_labels

x_train, x_test, y_train, y_test = train_test_split(xs, labels, test_size=0.2, random_state=42)

# with open('tokenizerForSpamDetection4.pickle', 'wb') as handle:
#     pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)

model = Sequential()
model.add(Embedding(total_words, 64, input_length=max_sequence_len))
model.add(Bidirectional(LSTM(64, return_sequences=True)))
# model.add(Dropout(0.2))
model.add(Bidirectional(LSTM(32)))
# model.add(Dropout(0.2))
model.add(Dense(len(action_label), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=2, verbose=1, batch_size=128, validation_data=(x_test, y_test), callbacks=early_stopping)

prediction = model.predict(x_test)
prediction = np.argmax(prediction, axis=1)
y_test = np.argmax(y_test, axis=1)
print(prediction[:20])
print(y_test[:20])
# predicted_action_index = np.argmax(prediction)
accuracy = np.mean(prediction == y_test)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision_score(prediction, y_test)}")
print(f"F1 Score: {f1_score(prediction, y_test)}")
print(f"Balanced Accuracy: {balanced_accuracy_score(prediction, y_test)}")
print(f"Auc: {roc_auc_score(prediction, y_test)}")
print(f"Accuracy: {accuracy_score(prediction, y_test)}")

spam_pred = 0
ham_pred = 0
for pred in prediction:
    if pred == 0:
        ham_pred += 1
    else:
        spam_pred += 1

spam_act = 0
ham_act = 0
for actual in y_test:
    if actual == 0:
        ham_act += 1
    else:
        spam_act += 1

print(f"Ham Pred: {ham_pred}, Spam Pred: {spam_pred}, Ham Act: {ham_act}, Spam Act: {spam_act}")

# model.save('SpamDetectionModel.h5')

input1 = "Valentines Day Special! Win over Â£1000 in our quiz and take your partner on the trip of a lifetime! Send GO to 83600 now. CustCare:08718720201"
input1 = tokenizer.texts_to_sequences(input1)
input1 = np.array(pad_sequences(input1, maxlen=max_sequence_len, padding='pre'))
p1 = model.predict(input1)

print(p1)