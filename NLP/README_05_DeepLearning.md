# NLP in Deep Learning & ANN vs RNN

## Introduction to NLP in Deep Learning

Traditional Machine Learning algorithms work well on structured/tabular data. However, Natural Language Processing (NLP) deals with text data where the order of words is extremely important.

Examples:

```text
The food is good
```

```text
The food is not good
```

Both sentences contain similar words, but their meanings are completely different.

To understand such sequential information, Deep Learning architectures like RNN, LSTM, GRU, and Transformers were introduced. :contentReference[oaicite:0]{index=0}

---

# Types of Neural Networks

## 1. ANN (Artificial Neural Network)

Best suited for:

- House Price Prediction
- Customer Churn Prediction
- Loan Approval
- Sales Prediction
- Tabular Data

Example:

```text
House Size
No. of Rooms
Location
```

The order of features does not matter.

---

## 2. CNN (Convolutional Neural Network)

Best suited for:

- Image Classification
- Object Detection
- Face Recognition
- Medical Imaging

---

## 3. RNN Family

Used for Sequential Data:

- NLP
- Time Series Forecasting
- Chatbots
- Language Translation
- Text Generation

Types:

```text
Simple RNN
LSTM
GRU
Bidirectional RNN
Encoder-Decoder
Attention
Transformers
```

---

# Why ANN Fails for NLP?

Consider:

```text
The food is good
```

```text
The food is bad
```

```text
The food is not good
```

After preprocessing:

```text
Text → Vectors
```

ANN only sees numerical values.

It cannot effectively understand:

```text
not good
```

because ANN processes all inputs together and has no memory of previous words.

---

# Sequential Data

Sequential data means:

```text
Order of information matters.
```

Examples:

### NLP

```text
I love AI
```

```text
AI love I
```

Same words, different meanings.

---

### Time Series

```text
Jan → Feb → Mar → Apr
```

Previous values influence future values.

---

### Language Translation

```text
English → French
Hindi → English
```

---

### Chatbots

```text
Question → Answer
```

---

### Text Generation

```text
Input Sentence → Complete Sentence
```

---

# ANN vs RNN

## ANN Architecture

```text
Input
  ↓
Hidden Layer
  ↓
Output
```

Characteristics:

- No memory
- Inputs processed together
- Cannot understand sequence
- Best for tabular data

---

## RNN Architecture

```text
Word1 → Word2 → Word3 → Word4
          ↑
       Memory
```

Characteristics:

- Has memory
- Processes one word at a time
- Understands sequence
- Suitable for NLP and Time Series

---

# Intuition Behind RNN

Suppose the sentence is:

```text
The food is good
```

RNN processes:

```text
t=1 → The
t=2 → food
t=3 → is
t=4 → good
```

At each step:

```text
Current Word
+
Previous Memory
=
New Memory
```

This memory is called the Hidden State.

---

# Hidden State

Hidden State stores information from previous words.

Example:

```text
The food is good
```

When processing:

```text
good
```

the model remembers:

```text
The food is
```

This helps understand context.

---

# Why RNN Was Revolutionary

Before RNN:

```text
BoW
TF-IDF
ANN
```

could not effectively understand word order.

RNN introduced:

```text
Memory
+
Context
+
Sequence Awareness
```

making NLP tasks much more effective.

---

# Evolution of NLP Models

```text
Bag of Words
      ↓
TF-IDF
      ↓
Word2Vec
      ↓
ANN
      ↓
Simple RNN
      ↓
LSTM
      ↓
GRU
      ↓
Bidirectional RNN
      ↓
Encoder-Decoder
      ↓
Attention
      ↓
Transformers
      ↓
LLMs (GPT, Claude, Gemini)
```

---

# ANN vs RNN Comparison

| Feature | ANN | RNN |
|----------|------|------|
| Data Type | Tabular | Sequential |
| Memory | No | Yes |
| Understand Sequence | No | Yes |
| NLP Tasks | Poor | Good |
| Time Series | Poor | Good |
| Language Translation | No | Yes |
| Chatbots | No | Yes |
| Text Generation | No | Yes |

---

# Key Takeaways

- NLP data is sequential.
- Word order affects meaning.
- ANN cannot remember previous inputs.
- RNN introduces memory using hidden states.
- RNN processes words one by one.
- RNN became the foundation for LSTM, GRU, and Transformers.

---

# Interview Questions & Answers

## Q1. What is Sequential Data?

Sequential data is data where the order of information matters.

Examples:

- Text
- Speech
- Time Series
- Stock Prices

---

## Q2. Why is NLP considered Sequential Data?

Because changing the order of words changes the meaning of a sentence.

Example:

```text
I love AI
```

```text
AI love I
```

---

## Q3. Why is ANN not suitable for NLP?

ANN processes all inputs independently and lacks memory, so it cannot capture context and word order.

---

## Q4. What is RNN?

RNN (Recurrent Neural Network) is a neural network designed for sequential data that maintains memory through hidden states.

---

## Q5. What is the main advantage of RNN over ANN?

RNN remembers previous inputs and understands sequence information.

---

## Q6. What is a Hidden State in RNN?

Hidden State is the memory of the network that stores information from previous time steps.

---

## Q7. Give real-world applications of RNN.

- Chatbots
- Language Translation
- Sentiment Analysis
- Text Generation
- Speech Recognition
- Time Series Forecasting

---

## Q8. Why was RNN introduced?

RNN was introduced to handle sequential data and maintain context information that ANN could not capture.

---

## Q9. What is the biggest limitation of Simple RNN?

Simple RNN struggles to remember information over long sequences due to the Vanishing Gradient Problem.

---

## Q10. What came after RNN?

```text
RNN
 ↓
LSTM
 ↓
GRU
 ↓
Transformers
 ↓
LLMs
```

LSTM and GRU were introduced to solve RNN's long-term memory problem.

---

# One-Line Interview Summary

### ANN

```text
ANN processes inputs independently and has no memory.
```

### RNN

```text
RNN processes sequential data and remembers previous information using hidden states.
```

### Difference

```text
ANN sees inputs.
RNN remembers inputs.
```