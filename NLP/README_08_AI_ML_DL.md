# What is Generative AI? (AI vs ML vs DL vs Generative AI)

One of the most common interview questions is:

> What is the difference between AI, Machine Learning, Deep Learning, and Generative AI?

The easiest way to understand this is to think of them as a hierarchy.

```text
Artificial Intelligence (AI)
        ↓
Machine Learning (ML)
        ↓
Deep Learning (DL)
        ↓
Generative AI (Gen AI)
```

Every Generative AI model is a Deep Learning model.

Every Deep Learning model is a Machine Learning model.

Every Machine Learning model is a part of Artificial Intelligence.

---

# Artificial Intelligence (AI)

## What is AI?

Artificial Intelligence is the broad field of making machines perform tasks that normally require human intelligence.

Examples:

- Playing chess
- Solving puzzles
- Recommendation systems
- Self-driving cars
- Virtual assistants

### Simple Definition

AI is the ability of a machine to mimic human intelligence.

---

## Real-Life Example

Imagine a robot that can:

- Understand commands
- Make decisions
- Solve problems

That robot is using AI.

---

## Examples of AI

- Siri
- Alexa
- Google Assistant
- Self-driving cars
- Chess-playing computers

---

# Machine Learning (ML)

## What is Machine Learning?

Machine Learning is a subset of AI where computers learn patterns from data instead of being explicitly programmed.

### Traditional Programming

```text
Rules + Data
        ↓
     Output
```

Example:

```python
if marks > 40:
    print("Pass")
else:
    print("Fail")
```

Rules are manually written.

---

### Machine Learning

```text
Data + Output
        ↓
      Model
```

The machine learns the rules automatically.

---

## Example

Suppose we have:

| Study Hours | Result |
|------------|---------|
| 2 | Fail |
| 4 | Pass |
| 6 | Pass |

Machine Learning learns:

```text
More study hours
↓
Higher chance of passing
```

without us explicitly writing the rule.

---

## Applications of ML

- Spam Detection
- Fraud Detection
- Recommendation Systems
- Customer Churn Prediction
- House Price Prediction

---

# Deep Learning (DL)

## What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses Neural Networks with multiple layers.

Inspired by the human brain.

---

## Why Deep Learning?

Traditional ML struggles with:

- Images
- Videos
- Audio
- Complex NLP

Deep Learning handles these problems much better.

---

## Neural Network

```text
Input Layer
      ↓
Hidden Layer
      ↓
Hidden Layer
      ↓
Output Layer
```

More hidden layers = Deep Learning.

---

## Example

Image:

```text
🐱
```

Deep Learning can automatically learn:

- Eyes
- Nose
- Face shape

and identify it as a cat.

---

## Applications

- Face Recognition
- Image Classification
- Speech Recognition
- NLP
- Autonomous Vehicles

---

# Generative AI

## What is Generative AI?

Generative AI is a branch of Deep Learning that can create new content.

Instead of only predicting or classifying, it generates.

Examples:

- Text
- Images
- Audio
- Video
- Code

---

## Traditional ML

Input:

```text
Email
```

Output:

```text
Spam or Not Spam
```

This is classification.

---

## Generative AI

Input:

```text
Write an email to my manager.
```

Output:

```text
Entire email generated.
```

This is generation.

---

## Examples

### Text Generation

Prompt:

```text
Write a story about a dragon.
```

Output:

```text
Complete story generated.
```

---

### Image Generation

Prompt:

```text
A tiger riding a motorcycle
```

Output:

```text
Generated image
```

---

### Code Generation

Prompt:

```text
Create a FastAPI endpoint.
```

Output:

```python
@app.get("/users")
def get_users():
    return users
```

---

## Popular Generative AI Models

### Text

- GPT-4
- GPT-5
- Claude
- Gemini
- Llama

### Image

- DALL·E
- Midjourney
- Stable Diffusion

### Video

- Sora
- Veo

---

# Visual Comparison

```text
AI
│
├── Rule-Based Systems
│
└── Machine Learning
      │
      └── Deep Learning
              │
              └── Generative AI
```

---

# AI vs ML vs DL vs Generative AI

| Feature | AI | ML | DL | Generative AI |
|----------|----|----|----|----|
| Goal | Mimic intelligence | Learn from data | Learn complex patterns | Create new content |
| Uses Data? | Optional | Yes | Yes | Yes |
| Learns Automatically? | Sometimes | Yes | Yes | Yes |
| Neural Networks? | Not required | Optional | Required | Required |
| Generates Content? | No | No | Usually No | Yes |
| Example | Chess Engine | Spam Detector | Face Recognition | ChatGPT |

---

# Real-World Analogy

Imagine teaching a child.

### AI

```text
Child can solve problems.
```

---

### ML

```text
Child learns from examples.
```

---

### DL

```text
Child learns very complex patterns.
```

---

### Generative AI

```text
Child can create stories,
draw pictures,
write essays,
and generate code.
```

---

# Where Does ChatGPT Fit?

```text
AI
 ↓
Machine Learning
 ↓
Deep Learning
 ↓
Generative AI
 ↓
Large Language Models (LLMs)
 ↓
ChatGPT
```

ChatGPT is:

- AI ✅
- Machine Learning ✅
- Deep Learning ✅
- Generative AI ✅
- Large Language Model (LLM) ✅

---

# Interview Questions & Answers

### What is Artificial Intelligence?

Artificial Intelligence is the field of creating systems that can perform tasks requiring human intelligence.

---

### What is Machine Learning?

Machine Learning is a subset of AI where systems learn patterns from data without explicit programming.

---

### What is Deep Learning?

Deep Learning is a subset of Machine Learning that uses multi-layer neural networks to learn complex patterns.

---

### What is Generative AI?

Generative AI is a branch of Deep Learning that can generate new content such as text, images, audio, video, and code.

---

### Is ChatGPT AI, ML, or Deep Learning?

ChatGPT is all three:

- AI
- Machine Learning
- Deep Learning

More specifically, it is a Generative AI application built on a Large Language Model.

---

### Difference Between Traditional ML and Generative AI?

Traditional ML predicts or classifies.

Example:

```text
Spam / Not Spam
```

Generative AI creates new content.

Example:

```text
Generate an email.
Generate an image.
Generate code.
```

---

# One-Line Summary

```text
AI = Make machines intelligent

ML = Learn from data

DL = Learn using deep neural networks

Generative AI = Create new content using deep learning
```