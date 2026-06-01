# Word2Vec

## What is Word2Vec?

Word2Vec is a technique used to convert words into numerical vectors (embeddings) while preserving their meaning and relationships.

Unlike Bag of Words or TF-IDF, Word2Vec understands that similar words should have similar representations.

For example:

```text
King   ≈ Queen
Car    ≈ Vehicle
Dog    ≈ Puppy
```

Words with similar meanings are placed close to each other in vector space.

---

## Why Do We Need Word2Vec?

Traditional techniques such as Bag of Words and TF-IDF have several limitations:

- They create sparse vectors.
- They cannot understand word meanings.
- They cannot identify relationships between words.

For example:

```text
King
Queen
Pizza
```

In Bag of Words, all three words are treated as completely different and unrelated.

However, humans know that:

```text
King and Queen are related.
King and Pizza are not related.
```

Word2Vec learns these relationships automatically.

---

## Core Idea Behind Word2Vec

### Golden Rule

> Words that appear in similar contexts tend to have similar meanings.

Consider the following sentences:

```text
The cat drinks milk.
The dog drinks milk.
```

Since "cat" and "dog" appear in similar contexts, Word2Vec learns that they are semantically related.

Similarly:

```text
The king rules the kingdom.
The queen rules the kingdom.
```

Word2Vec learns that:

```text
King ≈ Queen
```

---

# CBOW (Continuous Bag of Words)

## Intuition

CBOW predicts a missing word using the surrounding words (context).

Example:

```text
I love ____ learning
```

Context Words:

```text
I
love
learning
```

Predicted Word:

```text
machine
```

### Simple Memory Trick

```text
Context → Predict Word
```

or

```text
CBOW = Context → Word
```

---

## Why CBOW Works

If the model repeatedly sees:

```text
I love machine learning
Machine learning is awesome
```

it learns that the word "machine" often appears between "love" and "learning".

Over time it learns meaningful word representations.

---

## Advantages of CBOW

- Faster training
- Works well on smaller datasets
- Less computationally expensive

---

# Skip-Gram

## Intuition

Skip-Gram does the opposite of CBOW.

Instead of predicting the target word from context, it predicts the surrounding context words from a target word.

Example:

```text
I love machine learning
```

Input Word:

```text
machine
```

Predicted Context:

```text
love
learning
```

### Simple Memory Trick

```text
Word → Predict Context
```

or

```text
Skip-Gram = Word → Context
```

---

## Why Skip-Gram Works

If the word:

```text
king
```

frequently appears near:

```text
queen
kingdom
royal
prince
```

the model learns meaningful relationships between these words.

---

## Advantages of Skip-Gram

- Better embeddings
- Handles rare words well
- Captures semantic relationships more effectively

---

# CBOW vs Skip-Gram

| Feature | CBOW | Skip-Gram |
|----------|--------|------------|
| Input | Context Words | Target Word |
| Output | Target Word | Context Words |
| Speed | Faster | Slower |
| Rare Words | Average | Better |
| Dataset Size | Small to Medium | Medium to Large |

---

# Average Word2Vec

Machine Learning models need a fixed-size vector for an entire sentence or document.

But Word2Vec generates vectors only for individual words.

Example:

Sentence:

```text
I love AI
```

Word Vectors:

```text
I     → [1,2]
love  → [3,4]
AI    → [5,6]
```

Average Vector:

```text
[(1+3+5)/3 , (2+4+6)/3]

= [3,4]
```

This single vector now represents the entire sentence.

---

# Advantages of Word2Vec

### 1. Captures Semantic Meaning

```text
King ≈ Queen
Car ≈ Vehicle
```

### 2. Dense Vectors

Produces compact vectors instead of huge sparse vectors.

### 3. Better Performance

Improves:

- Text Classification
- Sentiment Analysis
- Recommendation Systems
- Search Engines

### 4. Learns Relationships

Example:

```text
King - Man + Woman ≈ Queen
```

---

# Limitations of Word2Vec

### 1. Same Word, Same Vector

Word2Vec generates one vector per word.

Example:

```text
bank
```

Financial bank and river bank receive the same vector.

### 2. No Context Awareness

Cannot understand different meanings of the same word based on the sentence.

### 3. Requires Large Training Data

Better embeddings require more text data.

---

# Interview Questions

### What is Word2Vec?

Word2Vec is a neural-network-based technique that converts words into dense numerical vectors by learning from surrounding words.

### What is CBOW?

CBOW predicts a target word using surrounding context words.

### What is Skip-Gram?

Skip-Gram predicts surrounding context words using a target word.

### Which is better, CBOW or Skip-Gram?

- CBOW is faster.
- Skip-Gram produces better embeddings and handles rare words more effectively.

---

# One-Line Summary

```text
Bag of Words counts words.
Word2Vec understands word meanings.
```