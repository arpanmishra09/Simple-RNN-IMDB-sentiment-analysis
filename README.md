# Simple RNN for IMDB Sentiment Analysis (Learning Project)

This repository is created **purely for learning and experimentation** to understand how:
- Word embeddings work
- Recurrent Neural Networks (SimpleRNN) process text
- Sentiment analysis is performed on the IMDB dataset

**Note**: This is not a production-ready model. The goal is conceptual clarity, not state-of-the-art accuracy.

---

##  Project Overview

The project demonstrates:
- Building word embeddings from scratch using `one_hot` + `Embedding`
- Training a **Simple RNN** for binary sentiment classification
- Understanding model limitations like overfitting and negation handling
- Deploying a simple NLP model using **Streamlit**
- Version control and deployment using **GitHub**

---

- Dataset: **IMDB movie reviews**
- Task: **Binary sentiment classification (Positive / Negative)**

---

## Repository Structure
├── main.py # Streamlit app for model inference
├── requirements.txt # Project dependencies
├── embedded.ipynb # Exploring word embeddings using keras one_hot
├── simplernn.ipynb # Training & experimenting with SimpleRNN
├── .h5 #the trained model
└── README.md


---

## Notebooks Included

### `embedded.ipynb`
- Demonstrates:
  - `keras.preprocessing.text.one_hot`
  - Padding sequences
  - Embedding layer behavior
- Useful for understanding **how words are converted to vectors**
- IMDB dataset embeddings are already provided by Keras, so this notebook helps learn embeddings independently

### `simplernn.ipynb`
- Step-by-step training of a SimpleRNN on IMDB data
- Early stopping, overfitting observation
- Testing model behavior on custom sentences
- Highlights limitations of SimpleRNN for sentiment tasks

---

## Streamlit App

The project includes a simple **Streamlit UI** to:
- Input custom movie reviews
- Get sentiment prediction scores
- Observe real-world behavior of a SimpleRNN model

---

## Learning Outcomes

- Difference between **one-hot encoding vs embeddings**
- Why embeddings are necessary for NLP
- Why SimpleRNN struggles with:
  - Negation
  - Long-term dependencies
- Importance of LSTM/GRU for real NLP tasks
- End-to-end ML workflow (train → test → deploy)

---

## Disclaimer

This project is meant for:
- Beginners starting with NLP & Deep Learning
- Conceptual understanding
- Hands-on experimentation

For real-world applications, prefer:
- LSTM / GRU
- Bidirectional RNNs
- Transformer-based models

---

## Acknowledgements

- TensorFlow / Keras
- IMDB Dataset
- Streamlit
- Krish Naik!

Happy learning!
