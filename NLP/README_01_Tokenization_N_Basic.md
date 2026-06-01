# Tokenization and Basic Terminologies

## 1. What is Tokenization?

### Simple Explanation
Tokenization is the process of breaking a sentence or text into smaller parts called **tokens**.

A token can be:

- A word
- A part of a word
- A punctuation mark
- A number
- A special symbol

### Interview Answer
Tokenization is the first step in Natural Language Processing and Large Language Models. It converts raw text into smaller units called tokens, so the machine can understand and process the text. Since computers do not directly understand human language, tokenization helps convert text into a format that can be handled by models.

### Example
```text
Input: I love programming.
Tokens: ["I", "love", "programming", "."]
```

---

## 2. Why is Tokenization Required?

### Simple Explanation
Computers cannot understand full sentences directly. They need text to be divided into smaller pieces.

### Interview Answer
Tokenization is required because machine learning models and language models work with numbers, not raw text. Tokenization breaks text into smaller meaningful units. After tokenization, these tokens are converted into numeric IDs, which are then processed by the model.

### Example
```text
Text: ChatGPT is useful
Tokens: ["Chat", "G", "PT", "is", "useful"]
Token IDs: [1234, 567, 890, 45, 6789]
```

---

## 3. What is a Token?

### Simple Explanation
A token is a small unit of text.

### Interview Answer
A token is the smallest piece of text that a model processes. It can be a complete word, part of a word, punctuation, or special character. In LLMs, the input and output are measured in tokens.

### Example
```text
Sentence: I am learning AI.
Tokens: I | am | learning | AI | .
```

---

## 4. Token vs Word

### Simple Explanation
A word and a token are not always the same.

### Interview Answer
A word is a natural language unit used by humans. A token is a model-level unit created after tokenization. Sometimes one word can become one token, but long or uncommon words can be split into multiple tokens.

### Example
```text
Word: unbelievable
Tokens: ["un", "believable"]
```

So, one word can become multiple tokens.

---

## 5. Types of Tokenization

## 5.1 Word Tokenization

### Simple Explanation
Text is split word by word.

### Interview Answer
Word tokenization splits a sentence into individual words. It is simple and easy to understand, but it may not handle unknown words very well.

### Example
```text
Input: I like machine learning
Output: ["I", "like", "machine", "learning"]
```

---

## 5.2 Character Tokenization

### Simple Explanation
Text is split character by character.

### Interview Answer
Character tokenization breaks text into individual characters. It avoids unknown word problems, but it creates longer sequences, which can make processing slower.

### Example
```text
Input: AI
Output: ["A", "I"]
```

---

## 5.3 Subword Tokenization

### Simple Explanation
Text is split into meaningful word parts.

### Interview Answer
Subword tokenization breaks words into smaller parts. It is commonly used in modern language models because it can handle known and unknown words efficiently. Common words may remain as one token, while rare words are split into smaller tokens.

### Example
```text
Input: playing
Output: ["play", "ing"]
```

---

## 6. Common Tokenization Algorithms

## 6.1 Byte Pair Encoding (BPE)

### Simple Explanation
BPE learns common word parts and uses them as tokens.

### Interview Answer
Byte Pair Encoding is a tokenization technique that starts with small units and repeatedly merges the most frequent pairs. It is useful because it can represent common words as single tokens and rare words as combinations of smaller tokens.

### Example
```text
lower + est = lowest
```

---

## 6.2 WordPiece

### Simple Explanation
WordPiece splits words into common subword units.

### Interview Answer
WordPiece is a subword tokenization algorithm used in models like BERT. It tries to split words into pieces that are useful for understanding language. It helps reduce the unknown word problem.

### Example
```text
Input: unhappy
Output: ["un", "##happy"]
```

Here `##` means the token is a continuation of the previous word.

---

## 6.3 SentencePiece

### Simple Explanation
SentencePiece tokenizes text without needing pre-splitting by spaces.

### Interview Answer
SentencePiece is a tokenizer that treats the input text as a raw stream. It does not depend only on spaces, so it works well for many languages, including languages where words are not separated by spaces.

---

## 7. Vocabulary

### Simple Explanation
Vocabulary is the list of all tokens known by the tokenizer.

### Interview Answer
Vocabulary is the collection of tokens that a tokenizer can recognize. Each token in the vocabulary has a unique numeric ID. During tokenization, text is converted into these token IDs.

### Example
```text
Vocabulary:
"I"       -> 10
"love"    -> 25
"AI"      -> 50
"."       -> 5
```

---

## 8. Token ID

### Simple Explanation
A token ID is a number assigned to each token.

### Interview Answer
After tokenization, each token is mapped to a numeric ID. Models process these token IDs internally. This is required because neural networks work with numbers, not text.

### Example
```text
Text: I love AI
Tokens: ["I", "love", "AI"]
Token IDs: [10, 25, 50]
```

---

## 9. Encoding

### Simple Explanation
Encoding means converting text into token IDs.

### Interview Answer
Encoding is the process of converting raw text into tokens and then mapping those tokens to their numeric IDs. This encoded form is given as input to the model.

### Example
```text
Text: Hello
Token: ["Hello"]
Token ID: [15496]
```

---

## 10. Decoding

### Simple Explanation
Decoding means converting token IDs back into text.

### Interview Answer
Decoding is the reverse process of encoding. The model outputs token IDs, and decoding converts those token IDs back into human-readable text.

### Example
```text
Token IDs: [10, 25, 50]
Text: I love AI
```

---

## 11. Embedding

### Simple Explanation
Embedding is a numeric representation of a token.

### Interview Answer
An embedding is a vector representation of a token. It captures the meaning or context of the token in numeric form. Tokens with similar meanings usually have similar embeddings.

### Example
Words like `king` and `queen` may have embeddings close to each other because they are semantically related.

---

## 12. Context Window

### Simple Explanation
Context window is the maximum number of tokens a model can read at one time.

### Interview Answer
The context window is the limit of tokens that a language model can take as input and output together. If the text is longer than the context window, some part may need to be removed, shortened, or split into chunks.

### Example
If a model has a context window of 8,000 tokens, then input plus output must fit within that limit.

---

## 13. Prompt

### Simple Explanation
A prompt is the input given to a language model.

### Interview Answer
A prompt is the instruction, question, or text given to an LLM to generate a response. The quality of the prompt affects the quality of the output.

### Example
```text
Prompt: Explain tokenization in simple English.
```

---

## 14. Completion

### Simple Explanation
Completion is the response generated by the model.

### Interview Answer
Completion is the output text generated by a language model based on the given prompt. In chat models, completion is usually the assistant's reply.

---

## 15. Prompt Tokens and Completion Tokens

### Simple Explanation
Prompt tokens are input tokens. Completion tokens are output tokens.

### Interview Answer
Prompt tokens are the tokens present in the input provided to the model. Completion tokens are the tokens generated by the model as output. The total token usage is the sum of prompt tokens and completion tokens.

### Example
```text
Prompt: What is AI?
Completion: AI means Artificial Intelligence.
```

```text
Total Tokens = Prompt Tokens + Completion Tokens
```

---

## 16. Special Tokens

### Simple Explanation
Special tokens are tokens used for specific purposes.

### Interview Answer
Special tokens are not normal words. They are used to mark the beginning or end of text, separate sentences, add padding, or represent unknown tokens.

### Common Special Tokens
```text
[CLS]  -> Start of input
[SEP]  -> Separator
[PAD]  -> Padding
[UNK]  -> Unknown token
```

---

## 17. Padding

### Simple Explanation
Padding means adding extra tokens to make all inputs the same length.

### Interview Answer
Padding is used when multiple input sequences have different lengths. Extra padding tokens are added to shorter sequences so that all inputs in a batch have the same length.

### Example
```text
Sentence 1: [I, love, AI]
Sentence 2: [I, love, machine, learning]

After padding:
Sentence 1: [I, love, AI, PAD]
Sentence 2: [I, love, machine, learning]
```

---

## 18. Truncation

### Simple Explanation
Truncation means cutting extra tokens when input is too long.

### Interview Answer
Truncation is used when the input text is longer than the maximum allowed token limit. Extra tokens are removed so the input can fit into the model's context window.

---

## 19. Attention Mask

### Simple Explanation
Attention mask tells the model which tokens are real and which are padding.

### Interview Answer
An attention mask is used to help the model ignore padding tokens. It usually contains `1` for real tokens and `0` for padding tokens.

### Example
```text
Tokens:         [I, love, AI, PAD]
Attention Mask: [1, 1, 1, 0]
```

---

## 20. Out-of-Vocabulary Words

### Simple Explanation
Out-of-vocabulary words are words not present in the tokenizer vocabulary.

### Interview Answer
Out-of-vocabulary words are words that the tokenizer does not directly recognize. Modern subword tokenizers reduce this issue by splitting unknown words into smaller known parts.

### Example
```text
Unknown word: ChatGPTization
Subword tokens: ["Chat", "GPT", "ization"]
```

---

## 21. Stemming

### Simple Explanation
Stemming reduces a word to its root form, but the result may not always be a real word.

### Interview Answer
Stemming is a text preprocessing technique used to reduce words to their base or root form. It is faster but less accurate because the output may not always be a proper dictionary word.

### Example
```text
playing -> play
studies -> studi
```

---

## 22. Lemmatization

### Simple Explanation
Lemmatization converts a word to its correct dictionary form.

### Interview Answer
Lemmatization reduces words to their base form using grammar and vocabulary knowledge. It is more accurate than stemming but usually slower.

### Example
```text
better -> good
running -> run
```

---

## 23. Stop Words

### Simple Explanation
Stop words are common words like `is`, `the`, `a`, and `an`.

### Interview Answer
Stop words are very common words that may not add much meaning in some NLP tasks. In traditional NLP, they are often removed. But in LLMs, stop words are usually kept because they help preserve full meaning and sentence structure.

### Example
```text
Original: This is a good book
After removing stop words: good book
```

---

## 24. Corpus

### Simple Explanation
A corpus is a large collection of text.

### Interview Answer
A corpus is a dataset of text used for training or analyzing language models. It can contain books, articles, websites, documents, or conversations.

---

## 25. Dataset

### Simple Explanation
A dataset is organized data used for training or testing a model.

### Interview Answer
A dataset is a structured collection of data used to train, validate, or test machine learning models. In NLP, the dataset usually contains text and sometimes labels.

---

## 26. Training Data

### Simple Explanation
Training data is the data used to teach a model.

### Interview Answer
Training data is used by the model to learn language patterns, relationships, and behavior. The quality of training data directly affects the quality of the model.

---

## 27. Inference

### Simple Explanation
Inference means using a trained model to generate output.

### Interview Answer
Inference is the process where a trained model takes input and produces output. For example, when we ask a chatbot a question and it replies, that is inference.

---

## 28. Large Language Model or LLM

### Simple Explanation
An LLM is an AI model trained on a large amount of text.

### Interview Answer
A Large Language Model is a deep learning model trained on huge text data to understand and generate human-like language. It can answer questions, summarize text, write code, translate, and perform many language-related tasks.

---

## 29. NLP

### Simple Explanation
NLP means Natural Language Processing.

### Interview Answer
Natural Language Processing is a field of AI that helps computers understand, process, and generate human language. Tokenization, sentiment analysis, translation, summarization, and chatbot development are common NLP tasks.

---

## 30. Transformer

### Simple Explanation
Transformer is a model architecture used in many modern LLMs.

### Interview Answer
A Transformer is a deep learning architecture that uses attention mechanisms to understand relationships between words or tokens. It is widely used in modern language models because it handles long text and context better than older models.

---

## 31. Attention

### Simple Explanation
Attention helps the model focus on important tokens.

### Interview Answer
Attention is a mechanism that allows the model to decide which tokens are important while processing text. It helps the model understand context and relationships between words.

### Example
```text
Sentence: The bank is near the river.
```

Here the word `river` helps the model understand that `bank` means river bank, not a financial bank.

---

## 32. Temperature

### Simple Explanation
Temperature controls how creative or random the model output is.

### Interview Answer
Temperature is a setting used during text generation. A low temperature gives more focused and predictable answers. A high temperature gives more creative and varied answers.

### Example
```text
Low temperature: More accurate and stable answer
High temperature: More creative and different answer
```

---

## 33. Top-k Sampling

### Simple Explanation
Top-k means the model chooses the next token from the top k most likely tokens.

### Interview Answer
Top-k sampling limits the model's next-token choice to the top k most probable tokens. It helps control randomness and avoids very unlikely outputs.

---

## 34. Top-p Sampling

### Simple Explanation
Top-p means the model chooses from tokens whose combined probability reaches p.

### Interview Answer
Top-p sampling, also called nucleus sampling, selects tokens from the smallest group of tokens whose total probability reaches a given value. It gives dynamic control over randomness.

---

## 35. Hallucination

### Simple Explanation
Hallucination means the model gives an incorrect answer confidently.

### Interview Answer
Hallucination happens when an AI model generates information that sounds correct but is actually wrong or not supported by facts. This is a common challenge in LLMs, so important answers should be verified from reliable sources.

---

## 36. Chunking

### Simple Explanation
Chunking means splitting a large document into smaller parts.

### Interview Answer
Chunking is used when a document is too large to fit into the model context window. The document is divided into smaller chunks so that each chunk can be processed separately.

---

## 37. RAG - Retrieval-Augmented Generation

### Simple Explanation
RAG means the model retrieves information first and then generates an answer.

### Interview Answer
Retrieval-Augmented Generation is an approach where the system first searches relevant documents and then gives the model that information to generate a more accurate answer. It is useful when the model needs updated or company-specific data.

### Example
```text
User question -> Search documents -> Get relevant content -> Generate answer
```

---

## 38. Vector Database

### Simple Explanation
A vector database stores embeddings.

### Interview Answer
A vector database stores numeric representations of text, images, or other data. It is commonly used in semantic search and RAG systems to find similar content based on meaning, not just exact keywords.

---

## 39. Semantic Search

### Simple Explanation
Semantic search finds results based on meaning.

### Interview Answer
Semantic search uses embeddings to find information based on meaning instead of exact word matching. For example, searching `car` may also return results about `vehicle` because the meanings are related.

---

## 40. Cosine Similarity

### Simple Explanation
Cosine similarity measures how close two vectors are.

### Interview Answer
Cosine similarity is used to compare two embeddings. It checks how similar their direction is. In NLP and RAG, it is commonly used to find documents that are semantically close to a user query.

---

## 41. Fine-Tuning

### Simple Explanation
Fine-tuning means training an existing model on specific data.

### Interview Answer
Fine-tuning is the process of taking a pre-trained model and training it further on a specific dataset. It helps the model perform better for a particular domain or task.

---

## 42. Prompt Engineering

### Simple Explanation
Prompt engineering means writing better instructions for the model.

### Interview Answer
Prompt engineering is the technique of designing clear and effective prompts to get better output from an AI model. It includes giving context, examples, constraints, and expected output format.

---

## 43. System Prompt

### Simple Explanation
A system prompt gives high-level instructions to the model.

### Interview Answer
A system prompt defines the behavior, role, and rules for the model. It helps control how the model should respond.

---

## 44. User Prompt

### Simple Explanation
A user prompt is the question or instruction given by the user.

### Interview Answer
A user prompt is the actual input provided by the user during conversation. The model reads this prompt and generates a response according to the instruction.

---

## 45. Few-Shot Prompting

### Simple Explanation
Few-shot prompting means giving examples inside the prompt.

### Interview Answer
Few-shot prompting is a technique where we provide a few examples to the model before asking it to perform a task. It helps the model understand the expected pattern and output style.

---

## 46. Zero-Shot Prompting

### Simple Explanation
Zero-shot prompting means asking the model directly without examples.

### Interview Answer
Zero-shot prompting is when we ask the model to perform a task without giving examples. The model uses its existing knowledge and instruction understanding to generate the answer.

---

## 47. One-Shot Prompting

### Simple Explanation
One-shot prompting means giving one example before asking the question.

### Interview Answer
One-shot prompting provides one sample input and output to guide the model. It helps improve consistency compared to zero-shot prompting.

---

## 48. Token Limit

### Simple Explanation
Token limit is the maximum number of tokens allowed.

### Interview Answer
Token limit defines how much text a model can process or generate. It includes both input tokens and output tokens. If the token limit is crossed, the text may be truncated or rejected.

---

## 49. Cost and Tokens

### Simple Explanation
LLM usage is often calculated based on tokens.

### Interview Answer
Many LLM APIs calculate cost based on the number of input and output tokens. More tokens mean more processing and higher cost. That is why prompt optimization is important.

---

## 50. Tokenization in Real Projects

### Interview Answer
In real projects, tokenization is important when working with chatbots, search systems, summarization, document processing, and RAG applications. We need to understand token limits, chunking, embeddings, and cost because large text cannot always be sent directly to the model.

### Example Use Case
```text
Large PDF document
        ↓
Split into chunks
        ↓
Tokenize chunks
        ↓
Create embeddings
        ↓
Store in vector database
        ↓
Retrieve relevant chunks
        ↓
Generate answer using LLM
```

---

# Common Interview Questions and Answers

## Q1. What is tokenization?

Tokenization is the process of breaking text into smaller units called tokens. These tokens are then converted into numbers so that a machine learning model can process them.

---

## Q2. Why do LLMs use tokens instead of words?

LLMs use tokens because tokens are more flexible than words. A token can represent a word, part of a word, punctuation, or symbol. This helps the model handle different languages and unknown words better.

---

## Q3. Can one word have multiple tokens?

Yes, one word can have multiple tokens. Common words may become one token, but rare or long words can be split into subword tokens.

---

## Q4. What is the difference between encoding and decoding?

Encoding converts text into token IDs. Decoding converts token IDs back into readable text.

---

## Q5. What is vocabulary in tokenization?

Vocabulary is the list of all tokens known by the tokenizer. Each token has a unique ID.

---

## Q6. What is subword tokenization?

Subword tokenization splits words into smaller meaningful parts. It is useful for handling unknown or rare words.

---

## Q7. What is context window?

The context window is the maximum number of tokens a model can process at one time. It includes both input and output tokens.

---

## Q8. What is an embedding?

An embedding is a numeric vector representation of a token or text. It helps the model understand meaning and similarity.

---

## Q9. What is attention mask?

An attention mask tells the model which tokens are actual input and which tokens are padding. Usually `1` means real token and `0` means padding token.

---

## Q10. What is the difference between stemming and lemmatization?

Stemming cuts a word to its root form and may produce an invalid word. Lemmatization converts a word to its correct dictionary form and is more accurate.

---

# Quick Revision Table

| Term | Simple Meaning |
|---|---|
| Tokenization | Breaking text into tokens |
| Token | Small unit of text |
| Token ID | Numeric value of a token |
| Vocabulary | List of known tokens |
| Encoding | Text to token IDs |
| Decoding | Token IDs to text |
| Embedding | Numeric meaning of text |
| Context Window | Maximum tokens model can handle |
| Prompt | Input given to model |
| Completion | Output generated by model |
| Padding | Adding extra tokens to equalize length |
| Truncation | Cutting extra tokens |
| Attention Mask | Marks real tokens and padding tokens |
| Chunking | Splitting large text into smaller parts |
| RAG | Retrieve data first, then generate answer |
| Vector DB | Stores embeddings |
| Semantic Search | Search based on meaning |
| Hallucination | Confident but wrong output |

---

# Final Interview Summary

Tokenization is a basic but very important concept in NLP and LLMs. It breaks text into tokens, converts them into token IDs, and allows the model to process human language as numbers. In real projects, tokenization affects context limit, cost, performance, chunking, embeddings, and response quality. Understanding tokenization helps us design better chatbot, RAG, search, and document processing systems.
