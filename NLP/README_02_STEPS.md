# NLP Text Classification Pipeline

This project demonstrates a traditional Natural Language Processing (NLP) workflow for sentiment classification using Machine Learning.

## Sample Dataset

| Document | Text | Label |
|-----------|------|---------|
| D1 | The food is good | 1 (Positive) |
| D2 | The food is bad | 0 (Negative) |
| D3 | Pizza is amazing | 1 (Positive) |
| D4 | Burger is bad | 0 (Negative) |

---

# Pipeline Overview

```text
Raw Text
   ↓
Text Preprocessing
   ↓
Text Normalization
   ↓
Text Vectorization
   ↓
Machine Learning Model
   ↓
Prediction
```

---

# Step 1: Text Collection

Collect raw text along with labels.

Example:

```text
"The food is good" → Positive
"The food is bad" → Negative
```

---

# Step 2: Text Preprocessing

Clean and standardize text before feature extraction.

## 2.1 Tokenization

Split sentences into words.

```python
"The food is good"
```

Output:

```python
["The", "food", "is", "good"]
```

## 2.2 Lowercase Conversion

Convert all text to lowercase.

```python
["the", "food", "is", "good"]
```

## 2.3 Regular Expression Cleaning

Remove:

- Special Characters
- Punctuation
- Extra Spaces
- Numbers (optional)

Example:

```python
"food!!!"
```

Output:

```python
"food"
```

---

# Step 3: Text Normalization

## 3.1 Stemming

Convert words to their root stem.

Examples:

```text
running → run
playing → play
studies → studi
```

## 3.2 Lemmatization

Convert words to meaningful dictionary forms.

Examples:

```text
running → run
better → good
studies → study
```

## 3.3 Stopword Removal

Remove frequently occurring words that add little meaning.

Examples:

```text
is, am, are, the, a, an, of
```

---

# Step 4: Convert Text to Numerical Vectors

Machine Learning algorithms cannot understand text directly.

Text must be converted into numerical representations.

## 4.1 One-Hot Encoding

Represents each word as a binary vector.

Example:

```text
food → [1,0,0,0]
good → [0,1,0,0]
```

---

## 4.2 Bag of Words (BoW)

Counts word occurrences.

Vocabulary:

```text
[food, good, bad, pizza]
```

Sentence:

```text
"The food is good"
```

Vector:

```text
[1,1,0,0]
```

---

## 4.3 TF-IDF

Term Frequency - Inverse Document Frequency.

Advantages:

- Reduces importance of common words
- Highlights important words
- Better than simple word counts

---

## 4.4 Word2Vec

Converts words into dense vector representations.

Examples:

```text
King ≈ Queen
Delhi ≈ India
Paris ≈ France
```

Benefits:

- Captures semantic meaning
- Learns word relationships
- Produces dense embeddings

---

# Step 5: Machine Learning Model

Use the generated vectors as input to ML algorithms.

Common Algorithms:

- Logistic Regression
- Naive Bayes
- Decision Tree
- Random Forest
- Support Vector Machine (SVM)
- XGBoost

Example:

```python
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

---

# Complete Workflow

```text
Text
 ↓
Tokenization
 ↓
Lowercase Conversion
 ↓
Regex Cleaning
 ↓
Stemming / Lemmatization
 ↓
Stopword Removal
 ↓
Vectorization
 ↓
(One-Hot / BoW / TF-IDF / Word2Vec)
 ↓
Machine Learning Algorithm
 ↓
Prediction
```

---

# Libraries Used

## NLP Libraries

- NLTK
- spaCy
- Gensim

## Machine Learning Libraries

- Scikit-Learn
- XGBoost

## Data Processing Libraries

- NumPy
- Pandas

---

# Traditional NLP vs Modern LLMs

## Traditional NLP

```text
Text
 ↓
Preprocessing
 ↓
Feature Engineering
 ↓
Machine Learning Model
 ↓
Prediction
```

## Modern LLMs

```text
Text
 ↓
Tokenizer
 ↓
Embeddings
 ↓
Transformer Model
 ↓
Prediction
```

Modern LLMs automatically learn features and embeddings, reducing the need for manual feature engineering techniques such as Bag of Words and TF-IDF.

---

# Learning Outcomes

After completing this project, you will understand:

- Tokenization
- Regular Expressions
- Stemming
- Lemmatization
- Stopword Removal
- One-Hot Encoding
- Bag of Words (BoW)
- TF-IDF
- Word2Vec
- NLP Classification Pipeline
- Traditional NLP vs LLMs
- Feature Engineering for Text Data