# NLP in Deep Learning: ANN vs RNN

## Introduction

When we started Machine Learning, most problems involved structured data such as:

- House Price Prediction
- Customer Churn Prediction
- Sales Forecasting
- Loan Approval

For these problems, Artificial Neural Networks (ANNs) work well because the order of features does not matter.

Example:

| House Size | Bedrooms | Price |
|------------|-----------|--------|
| 1200 | 3 | 50 Lakhs |

If we change the order of columns, the meaning remains the same.

This type of data is called **non-sequential data**.

---

## Why ANN is Not Enough for NLP?

Natural Language Processing (NLP) deals with text.

In text data, the order of words is extremely important.

Consider these sentences:

```text
The food is good
```

```text
The food is not good
```

The word **"not"** completely changes the meaning.

However, ANN sees only numbers and does not remember the order in which words appeared.

As a result, ANN struggles to understand context.

---

## Sequential Data

Sequential data is data where order matters.

Examples:

### Text

```text
I love AI
```

```text
AI love I
```

Both contain the same words, but the meanings are different.

---

### Time Series

```text
Jan → Feb → Mar → Apr
```

Previous values affect future values.

---

### Language Translation

```text
English → French
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

All these tasks require understanding sequence and context.

---

# Recurrent Neural Network (RNN)

To solve the problem of sequential data, Recurrent Neural Networks (RNNs) were introduced.

The biggest difference between ANN and RNN is memory.

ANN has no memory.

RNN remembers previous information while processing new information.

---

## Intuition Behind RNN

Imagine reading a sentence:

```text
The food is good
```

You do not read all words simultaneously.

You read:

```text
The
↓
food
↓
is
↓
good
```

At every step, your brain remembers previous words.

RNN tries to mimic this behavior.

---

## Hidden State (Memory)

The memory inside an RNN is called the **Hidden State**.

While processing each word, RNN stores useful information from previous words.

Example:

```text
The → Memory1

food + Memory1 → Memory2

is + Memory2 → Memory3

good + Memory3 → Memory4
```

The final memory helps make predictions.

---

# Forward Propagation in RNN

Forward propagation means moving information from input to output.

Consider:

```text
The food is good
```

RNN processes the sentence one word at a time.

```text
t=1 → The
t=2 → food
t=3 → is
t=4 → good
```

At every timestep:

```text
Current Input
+
Previous Memory
=
New Memory
```

This new memory is passed to the next timestep.

This is how RNN remembers context.

---

# Backpropagation Through Time (BPTT)

Every model makes mistakes during training.

Example:

Actual Output:

```text
Positive = 1
```

Predicted Output:

```text
Positive = 0.4
```

Error:

```text
1 - 0.4 = 0.6
```

The model updates its weights to reduce this error.

In RNN, because the network unfolds through time, the error is propagated backward across all timesteps.

This process is called:

```text
Backpropagation Through Time (BPTT)
```

---

# Problems with Simple RNN

Although RNN introduced memory, it has serious limitations.

---

## Short-Term Memory Problem

Suppose we have:

```text
I grew up in France.

...

I speak fluent French.
```

The word:

```text
France
```

appeared much earlier.

By the time RNN reaches:

```text
French
```

it may forget the earlier information.

---

## Vanishing Gradient Problem

During training, gradients become smaller and smaller.

```text
0.8
↓
0.08
↓
0.008
↓
0.0008
```

Eventually the gradient becomes nearly zero.

Learning stops.

The model cannot learn long-term dependencies.

---

## Exploding Gradient Problem

Sometimes gradients become extremely large.

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

Weights start changing wildly.

---

# Why LSTM Was Introduced

LSTM stands for:

```text
Long Short-Term Memory
```

LSTM was designed specifically to solve the memory problem of Simple RNN.

The goal was:

```text
Remember important information

Forget unimportant information
```

for a long period of time.

---

# Intuition Behind LSTM

Think of LSTM as a smart notebook.

It constantly decides:

```text
What should I remember?
```

```text
What should I forget?
```

```text
What should I share?
```

To make these decisions, LSTM uses gates.

---

# Forget Gate

The Forget Gate decides:

```text
What information should be removed?
```

Example:

```text
My old phone was broken.
I bought a new phone.
```

The model can forget:

```text
old phone
```

and keep:

```text
new phone
```

---

# Input Gate

The Input Gate decides:

```text
What new information should be stored?
```

Example:

```text
I moved to Paris.
```

The model stores:

```text
Paris
```

in memory.

---

# Output Gate

The Output Gate decides:

```text
What information should be passed forward?
```

Only important information is sent to the next timestep.

---

# GRU (Gated Recurrent Unit)

GRU is a simplified version of LSTM.

Researchers noticed that LSTM works very well but contains many parameters.

GRU reduces complexity while maintaining good performance.

---

## Difference Between LSTM and GRU

LSTM uses:

```text
Forget Gate
Input Gate
Output Gate
```

GRU uses:

```text
Update Gate
Reset Gate
```

As a result:

- GRU trains faster
- GRU uses less memory
- GRU has fewer parameters

---

# Bidirectional RNN

Normal RNN reads text only in one direction.

Example:

```text
The movie was not good
```

Reading:

```text
Left → Right
```

sometimes misses future context.

Bidirectional RNN reads:

```text
Left → Right
```

and

```text
Right → Left
```

simultaneously.

This allows the model to understand both past and future context.

---

# Evolution of NLP Models

```text
Bag of Words
      ↓
TF-IDF
      ↓
Word2Vec
      ↓
RNN
      ↓
LSTM
      ↓
GRU
      ↓
Bidirectional RNN
      ↓
Attention
      ↓
Transformers
      ↓
LLMs (GPT, Claude, Gemini)
```

---

# Interview Questions & Answers

### What is Sequential Data?

Sequential data is data where the order of information matters.

Examples include text, speech, and time-series data.

---

### Why is ANN not suitable for NLP?

ANN does not have memory and cannot understand word order or context.

---

### What is RNN?

RNN is a neural network designed for sequential data that maintains memory through hidden states.

---

### What is Hidden State?

Hidden State is the memory of an RNN that stores information from previous timesteps.

---

### What is BPTT?

BPTT (Backpropagation Through Time) is the training algorithm used for RNNs.

---

### What is the biggest limitation of Simple RNN?

Simple RNN suffers from the Vanishing Gradient Problem and struggles to remember long-term information.

---

### Why was LSTM introduced?

LSTM was introduced to solve the long-term memory problem of Simple RNN.

---

### What are the gates in LSTM?

- Forget Gate
- Input Gate
- Output Gate

---

### What is GRU?

GRU is a simplified version of LSTM that uses fewer gates and trains faster.

---

### Why use Bidirectional RNN?

Bidirectional RNN captures both past and future context by reading sequences in both directions.

---

### Which is better: LSTM or GRU?

LSTM usually provides better memory retention, while GRU is faster and computationally lighter.

---

# Quick Revision

```text
ANN
→ No Memory

RNN
→ Has Memory

LSTM
→ Long-Term Memory

GRU
→ Faster LSTM

Bidirectional RNN
→ Reads Both Directions

Transformers
→ Replaced RNN Family

LLMs
→ Built on Transformers
```