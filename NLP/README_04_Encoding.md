# One-Hot Encoding

## What is One-Hot Encoding?

One-Hot Encoding is a technique used to convert categorical text data into numerical vectors that Machine Learning algorithms can understand.

Each unique word in the vocabulary is represented by a binary vector where:

- `1` indicates the presence of the word.
- `0` indicates the absence of the word.

---

## Example

### Documents

```text
D1: The food is good
D2: The food is bad
```

### Vocabulary

```text
[food, good, bad]
```

### One-Hot Vectors

| Word | Vector |
|--------|---------|
| food | [1, 0, 0] |
| good | [0, 1, 0] |
| bad | [0, 0, 1] |

---

## Sentence Representation

### D1: "The food is good"

```text
food → [1,0,0]
good → [0,1,0]
```

Combined representation:

```text
[1,1,0]
```

### D2: "The food is bad"

```text
food → [1,0,0]
bad  → [0,0,1]
```

Combined representation:

```text
[1,0,1]
```

---

## Python Example

```python
from sklearn.preprocessing import OneHotEncoder
import numpy as np

data = np.array([
    ['food'],
    ['good'],
    ['bad']
])

encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(data)

print(encoded)
```

Output:

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

## Advantages

- Easy to implement.
- Works well for small vocabularies.
- Converts categorical data into numerical format.

---

## Disadvantages

### High Dimensionality

If vocabulary contains 10,000 words:

```text
food → [1,0,0,0,0,...]
```

Vector length becomes 10,000.

### Sparse Vectors

Most values are 0.

Example:

```text
[0,0,0,0,1,0,0,0,0]
```

### No Semantic Meaning

One-Hot Encoding cannot capture relationships between words.

Example:

```text
King  → [1,0,0]
Queen → [0,1,0]
```

The model cannot understand that "King" and "Queen" are related.

---

## One-Hot Encoding vs Word Embeddings

| Feature | One-Hot Encoding | Word2Vec / Embeddings |
|-----------|-----------------|----------------------|
| Sparse | Yes | No |
| High Dimensions | Yes | No |
| Semantic Meaning | No | Yes |
| Memory Efficient | No | Yes |
| Used in Modern LLMs | No | Yes |

---

## Interview Questions

### What is One-Hot Encoding?

A technique that converts categorical text data into binary vectors where only one position contains 1 and all others contain 0.

### What is the main drawback of One-Hot Encoding?

It creates high-dimensional sparse vectors and cannot capture semantic relationships between words.

### Why are embeddings preferred over One-Hot Encoding?

Embeddings are dense, memory-efficient, and capture semantic meaning between words.

# Bag of Words (BoW)

## Intuition

Bag of Words (BoW) is a text vectorization technique that converts text into numerical vectors by counting the occurrence of words in a document.

The idea is simple:

1. Create a vocabulary of all unique words.
2. Count how many times each word appears in a document.
3. Represent the document as a vector of word counts.

Machine Learning models cannot understand text directly, so BoW converts text into numbers.

---

## Example Dataset

| Document | Text |
|-----------|------|
| D1 | The food is good |
| D2 | The food is bad |
| D3 | Pizza is amazing |
| D4 | Burger is bad |

---

## Step 1: Create Vocabulary

Extract all unique words:

```text
food, good, bad, pizza, amazing, burger
```

Assign an index to each word:

| Word | Index |
|--------|--------|
| food | 0 |
| good | 1 |
| bad | 2 |
| pizza | 3 |
| amazing | 4 |
| burger | 5 |

---

## Step 2: Convert Documents to Vectors

### Document 1

Input:

```text
The food is good
```

Vector:

| food | good | bad | pizza | amazing | burger |
|--------|--------|--------|--------|--------|--------|
| 1 | 1 | 0 | 0 | 0 | 0 |

```text
[1, 1, 0, 0, 0, 0]
```

### Document 2

Input:

```text
The food is bad
```

Vector:

```text
[1, 0, 1, 0, 0, 0]
```

### Document 3

Input:

```text
Pizza is amazing
```

Vector:

```text
[0, 0, 0, 1, 1, 0]
```

---

## Why Is It Called "Bag" of Words?

BoW treats a document as a bag containing words.

It ignores:

- Word order
- Grammar
- Sentence structure

Example:

```text
The food is good
```

and

```text
Good food is the
```

produce the same vector because BoW only counts words.

---

## Real-Life Analogy

Imagine a shopping bag containing:

```text
Apple
Apple
Milk
Bread
```

Instead of storing the order, we simply count:

```text
Apple = 2
Milk = 1
Bread = 1
```

Bag of Words follows the same idea for text documents.

---

## Advantages

- Simple and easy to understand
- Easy to implement
- Works well for basic text classification tasks
- Fast to train

---

## Disadvantages

### 1. Loses Context

```text
I love pizza
```

and

```text
Pizza love I
```

have the same representation.

### 2. High Dimensionality

Large vocabularies create very large vectors.

Example:

```text
10,000 unique words
→ vector size = 10,000
```

### 3. No Semantic Understanding

BoW treats similar words as completely different.

Example:

```text
good
excellent
```

Although both have similar meanings, BoW considers them unrelated.

---

## Python Example

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "The food is good",
    "The food is bad",
    "Pizza is amazing"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

### Output

```text
['amazing' 'bad' 'food' 'good' 'is' 'pizza' 'the']

[[0 0 1 1 1 0 1]
 [0 1 1 0 1 0 1]
 [1 0 0 0 1 1 0]]
```

---

## Interview Questions

### What is Bag of Words?

Bag of Words is a text vectorization technique that converts text into numerical vectors by counting the occurrence of words while ignoring grammar and word order.

### Why is it called Bag of Words?

Because it treats a document as a collection (bag) of words and only considers word frequency.

### What are the limitations of BoW?

- Ignores word order
- Cannot capture semantic meaning
- Produces sparse high-dimensional vectors

---

## Evolution of Text Representation

```text
One-Hot Encoding
        ↓
Bag of Words
        ↓
TF-IDF
        ↓
Word2Vec
        ↓
Embeddings
        ↓
Transformers / LLMs
```

Modern LLMs use dense embeddings instead of Bag of Words because embeddings capture semantic meaning and contextual relationships between words.


## Advantages of Bag of Words (BoW)

### 1. Simple and Easy to Understand

BoW is one of the simplest text vectorization techniques.

Example:

```text
"The food is good"
→ [1, 1, 0, 0]
```

### 2. Easy to Implement

Can be implemented using Scikit-Learn's `CountVectorizer` in just a few lines of code.

```python
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
```

### 3. Fast Training

Since BoW only counts word frequencies, training is computationally efficient.

### 4. Works Well for Small Datasets

BoW often provides good results for:

- Sentiment Analysis
- Spam Detection
- Document Classification
- Topic Classification

### 5. Interpretable

Each feature directly corresponds to a word in the vocabulary, making the model easy to explain.

---

## Disadvantages of Bag of Words (BoW)

### 1. Ignores Word Order

BoW treats documents as a collection of words and ignores sequence.

Example:

```text
"I love pizza"
```

and

```text
"Pizza love I"
```

produce the same representation.

---

### 2. No Semantic Understanding

BoW cannot understand word meanings or relationships.

Example:

```text
good
excellent
amazing
```

Although similar in meaning, BoW treats them as completely different words.

---

### 3. High Dimensionality

Vocabulary size determines vector size.

Example:

```text
Vocabulary Size = 50,000
```

Every document becomes a vector of length 50,000.

---

### 4. Sparse Vectors

Most values in the vector are zeros.

Example:

```text
[0,0,0,0,1,0,0,0,0,0]
```

This increases memory usage.

---

### 5. Cannot Handle Context

BoW cannot distinguish between:

```text
"The movie is good"
```

and

```text
"The movie is not good"
```

because it lacks contextual understanding.

---

### 6. Vocabulary Explosion

As the dataset grows, new words continuously increase the vocabulary size.

Example:

```text
10,000 documents
→ 100,000+ unique words
```

This makes the feature space very large.

---

## Interview Summary

### Advantages

- Simple and easy to implement
- Fast training
- Interpretable features
- Works well on small datasets

### Disadvantages

- Ignores word order
- No semantic meaning
- High-dimensional sparse vectors
- Cannot capture context
- Large vocabulary size

---

## Why Modern LLMs Don't Use BoW

```text
Bag of Words
    ↓
TF-IDF
    ↓
Word2Vec
    ↓
Embeddings
    ↓
Transformers / LLMs
```

Modern LLMs use embeddings instead of BoW because embeddings capture semantic meaning, context, and relationships between words.

# N-Grams

## What are N-Grams?

N-Grams are contiguous sequences of **N words** from a given text.

Instead of considering single words only (Bag of Words), N-Grams preserve some word order and context by considering groups of words together.

---

## Why Do We Need N-Grams?

Bag of Words ignores word order.

Example:

```text
I love this movie
```

and

```text
This movie love I
```

produce similar representations.

N-Grams help capture local context and word relationships.

---

## Types of N-Grams

### 1. Unigram (N = 1)

Single words.

Sentence:

```text
I love NLP
```

Output:

```text
[I, love, NLP]
```

---

### 2. Bigram (N = 2)

Groups of 2 consecutive words.

Sentence:

```text
I love NLP
```

Output:

```text
[I love, love NLP]
```

---

### 3. Trigram (N = 3)

Groups of 3 consecutive words.

Sentence:

```text
I love NLP
```

Output:

```text
[I love NLP]
```

---

### 4. Four-Gram (N = 4)

Groups of 4 consecutive words.

Sentence:

```text
I love learning NLP
```

Output:

```text
[I love learning NLP]
```

---

## Example

Sentence:

```text
The food is very good
```

### Unigrams

```text
The
food
is
very
good
```

### Bigrams

```text
The food
food is
is very
very good
```

### Trigrams

```text
The food is
food is very
is very good
```

---

## Why N-Grams Are Useful

Consider:

```text
The movie is good
```

and

```text
The movie is not good
```

### Bag of Words

```text
movie, good, not
```

The context of "not good" may be lost.

### Bigrams

```text
movie is
is good

movie is
is not
not good
```

Now the model can learn that:

```text
not good
```

indicates negative sentiment.

---

## Python Example

```python
from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "The food is good",
    "The food is bad"
]

vectorizer = CountVectorizer(ngram_range=(2,2))

X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
```

Output:

```text
['food is' 'is bad' 'is good' 'the food']
```

---

## Advantages of N-Grams

### 1. Captures Word Order

Unlike Bag of Words, N-Grams preserve local sequence information.

Example:

```text
not good
very good
```

are treated differently.

### 2. Better Context Understanding

Captures phrases instead of individual words.

### 3. Improves Text Classification

Often improves:

- Sentiment Analysis
- Spam Detection
- Text Classification

---

## Disadvantages of N-Grams

### 1. Vocabulary Size Grows Rapidly

Example:

```text
1000 words
```

can generate thousands of bigrams and trigrams.

### 2. Sparse Feature Vectors

Most N-Grams appear rarely.

### 3. Increased Memory Usage

Large vocabularies require more storage.

### 4. Limited Context

Bigrams only look at two words.

Example:

```text
The food is not very good
```

The complete meaning may still be missed.

---

## Interview Questions

### What is an N-Gram?

An N-Gram is a sequence of N consecutive words extracted from a text.

### What is a Bigram?

A Bigram is a sequence of two consecutive words.

Example:

```text
I love NLP
```

Output:

```text
I love
love NLP
```

### Why are N-Grams better than Bag of Words?

N-Grams preserve word order and capture local context, while Bag of Words ignores word sequence.

---

## Evolution of Text Representation

```text
One-Hot Encoding
        ↓
Bag of Words
        ↓
N-Grams
        ↓
TF-IDF
        ↓
Word2Vec
        ↓
Embeddings
        ↓
Transformers / LLMs
```

N-Grams were an important improvement over Bag of Words because they introduced context awareness, but modern LLMs use embeddings and transformers to capture much richer semantic and contextual information.



# TF-IDF (Term Frequency - Inverse Document Frequency)

## Intuition

Bag of Words treats all words equally.

Consider the documents:

```text
D1: The food is good
D2: The food is bad
D3: The food is amazing
```

Using Bag of Words:

| Word | Count |
|--------|--------|
| the | 3 |
| food | 3 |
| good | 1 |
| bad | 1 |
| amazing | 1 |

Notice that:

```text
the
food
```

appear in every document.

These words are common and do not help distinguish documents.

TF-IDF reduces the importance of common words and increases the importance of rare but meaningful words.

---

# Why Do We Need TF-IDF?

Bag of Words only counts frequency.

Example:

```text
The food is good
The food is bad
The food is amazing
```

Words like:

```text
the
is
food
```

appear everywhere.

These words provide little information.

Words like:

```text
good
bad
amazing
```

are much more useful for classification.

TF-IDF automatically identifies important words.

---

# TF-IDF = TF × IDF

```text
TF-IDF = Term Frequency × Inverse Document Frequency
```

---

# Step 1: Term Frequency (TF)

Measures how frequently a word appears in a document.

Formula:

TF = (Number of times term appears in document)
     ------------------------------------------------
     (Total number of words in document)

---

## Example

Document:

```text
The food is good
```

Word:

```text
food
```

Count:

```text
food = 1
Total words = 4
```

TF:

```text
TF(food) = 1 / 4 = 0.25
```

---

# Step 2: Inverse Document Frequency (IDF)

Measures how rare a word is across all documents.

Formula:

```text
IDF = log(
        Total Documents
        -------------------------
        Number of Documents containing the word
      )
```

---

## Example

Dataset:

```text
D1: The food is good
D2: The food is bad
D3: Pizza is amazing
```

### Word = food

Appears in:

```text
D1
D2
```

Documents containing "food" = 2

Total documents = 3

```text
IDF(food) = log(3 / 2)
```

Small value because "food" is common.

---

### Word = amazing

Appears only in:

```text
D3
```

Documents containing "amazing" = 1

```text
IDF(amazing) = log(3 / 1)
```

Large value because "amazing" is rare.

---

# Final TF-IDF Score

```text
TF-IDF = TF × IDF
```

### Common Words

```text
food
the
is
```

High TF but Low IDF

Result:

```text
Low TF-IDF Score
```

---

### Rare Important Words

```text
good
bad
amazing
```

Moderate TF but High IDF

Result:

```text
High TF-IDF Score
```

---

# Real-Life Analogy

Imagine a classroom.

Every student uses:

```text
pen
book
```

These words are common and not useful for identifying a student.

One student frequently mentions:

```text
astronomy
```

This word is rare and highly informative.

TF-IDF gives more importance to:

```text
astronomy
```

and less importance to:

```text
pen
book
```

---

# TF-IDF vs Bag of Words

| Feature | Bag of Words | TF-IDF |
|----------|-------------|---------|
| Uses Frequency | Yes | Yes |
| Considers Importance | No | Yes |
| Reduces Common Words | No | Yes |
| Better Accuracy | Moderate | Better |
| Captures Semantics | No | No |

---

# Python Example

```python
from sklearn.feature_extraction.text import TfidfVectorizer

corpus = [
    "The food is good",
    "The food is bad",
    "Pizza is amazing"
]

vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names_out())
print(X.toarray())
```

---

# Advantages of TF-IDF

### 1. Reduces Importance of Common Words

Words like:

```text
the
is
are
```

receive lower scores.

### 2. Highlights Important Words

Rare and meaningful words receive higher scores.

### 3. Better Than Bag of Words

Usually provides better performance for:

- Text Classification
- Spam Detection
- Sentiment Analysis
- Information Retrieval

### 4. Easy to Implement

Available directly in Scikit-Learn.

---

# Disadvantages of TF-IDF

### 1. No Semantic Understanding

```text
good
excellent
great
```

are treated as different words.

### 2. Ignores Word Order

```text
I love pizza
```

and

```text
Pizza love I
```

are treated similarly.

### 3. Sparse Vectors

Creates large sparse matrices for large vocabularies.

### 4. Cannot Capture Context

TF-IDF cannot understand sentence meaning.

Example:

```text
The movie is good
```

vs

```text
The movie is not good
```

---

# Interview Answer

### What is TF-IDF?

TF-IDF (Term Frequency-Inverse Document Frequency) is a text vectorization technique that assigns higher weights to important words and lower weights to common words across documents.

### Why is TF-IDF better than Bag of Words?

TF-IDF reduces the importance of frequently occurring words and highlights rare, informative words, resulting in better feature representation.

---

# Evolution of Text Representation

```text
One-Hot Encoding
        ↓
Bag of Words
        ↓
N-Grams
        ↓
TF-IDF
        ↓
Word2Vec
        ↓
Embeddings
        ↓
Transformers / LLMs
```

TF-IDF was a major improvement over Bag of Words because it considers both word frequency and word importance across the entire corpus.