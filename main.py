import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st


#function to preprocess the user input
def preprocessing_(text):
    word_index=imdb.get_word_index()
    words=text.lower().split()
    encoded_review=[word_index.get(word,2)+3 for word in words]
    padded_review=sequence.pad_sequences([encoded_review],maxlen=1000)
    return padded_review

## prediction function
def senti_pred(review):
    review_processed=preprocessing_(review)
    prediction= model.predict(review_processed)
    sentiment= 'Positive' if prediction[0][0]>0.5 else 'Negative'
    return sentiment,prediction[0][0]

#load model
model=load_model('simple_rnn_imdb.h5')


## streamlit design
st.title('IMDB Movie Review Sentiment Analysis')
st.write('Enter a movie review to classify it as postive or negative')

user_input= st.text_area('Moview Review')

if st.button('Classify'):
    senti,score= senti_pred(user_input)
    st.write(f'Sentiment is {senti} (estimation score={score:.2f})')
else:
    st.write('Please enter the movie review')

