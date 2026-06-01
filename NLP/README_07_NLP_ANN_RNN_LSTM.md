# NLP, ANN, RNN, LSTM and GRU

## Big Picture

Text
↓
Tokens
↓
Numbers
↓
Embeddings
↓
RNN
↓
LSTM
↓
GRU
↓
Transformers
↓
LLMs

---

# NLP in Deep Learning

## What is NLP?

Natural Language Processing (NLP) is the field of AI that helps computers understand human language.

Examples:

- Reviews
- Emails
- Chat messages
- Documents
- Questions

### Why is NLP needed?

Humans understand:

```text
The movie is amazing
```

Computers understand:

```text
[12, 45, 89]
```

Therefore text must be converted into numbers before training a model.

### Important Terms

| Term | Meaning |
|--------|----------|
| Corpus | Collection of documents |
| Document | One text record |
| Token | Smallest unit of text |
| Vocabulary | All known tokens |
| Embedding | Dense vector representing a word |

### Interview Question

**What is NLP?**

NLP is a field of AI that enables computers to understand, process, and generate human language.

---

# ANN vs RNN

## ANN

ANN works best when every row is independent.

Examples:

- House Price Prediction
- Customer Churn
- Loan Approval

```text
Input
 ↓
Hidden Layer
 ↓
Output
```

### Limitation

ANN has no memory.

---

## RNN

RNN is designed for sequence data.

Examples:

- Text
- Speech
- Time Series

```text
Word1 → Word2 → Word3 → Word4
           ↑
        Memory
```

### Why RNN?

Meaning depends on previous words.

```text
The food is good
```

```text
The food is not good
```

The word "not" changes everything.

RNN remembers previous information.

### Interview Question

**Why is RNN better than ANN for NLP?**

RNN maintains a hidden state that stores previous context, allowing it to process sequences effectively.

---

# RNN Forward Propagation

## Intuition

Imagine reading:

```text
I love this movie
```

You do not read all words at once.

You read:

```text
I
↓
love
↓
this
↓
movie
```

RNN does the same.

At every step:

```text
Current Word
+
Previous Memory
=
New Memory
```

This memory is called the Hidden State.

### Memory Trick

```text
RNN = Reading + Remembering
```

### Interview Question

**What is Hidden State?**

Hidden State is the memory of the RNN that stores information from previous time steps.

---

# Backpropagation Through Time (BPTT)

## Intuition

Suppose the model predicts:

```text
Positive = 0.3
```

Actual:

```text
Positive = 1
```

The model made a mistake.

The error is sent backward to update weights.

For RNN, the error must travel through every time step.

This is called:

```text
Backpropagation Through Time (BPTT)
```

### Interview Question

**What is BPTT?**

BPTT is the training process used in RNNs where gradients are propagated backward through all previous time steps.

---

# Problems with Simple RNN

## Short-Term Memory Problem

Sentence:

```text
I grew up in India.

...

I speak Hindi.
```

Simple RNN may forget:

```text
India
```

before reaching:

```text
Hindi
```

---

## Vanishing Gradient

Gradients become:

```text
0.8
↓
0.08
↓
0.008
↓
0
```

Learning stops.

---

## Exploding Gradient

Gradients become:

```text
0.5
↓
5
↓
50
↓
500
```

Training becomes unstable.

### Interview Question

**Why was LSTM introduced?**

LSTM was introduced to solve the long-term memory problem and vanishing gradient problem of Simple RNN.

...