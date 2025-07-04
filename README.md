

https://github.com/user-attachments/assets/cd2648c0-7981-4a7a-a7f8-5ac4a09611a0




﻿# RAG Template

A powerful and easy-to-use Retrieval-Augmented Generation (RAG) template for building knowledge-based AI applications.

## Quick Start

### 1. Import the RAG Class
```python
from class.rag import EmbRag
```

### 2. Initialize the RAG System
Create an instance of the RAG system by providing two essential paths:

```python
# Path to your knowledge base documents
documents_path = "path/to/your/documents"

# Path where RAG system will store its data
faiss_path = "path/to/store/faiss_data"

# Initialize the RAG system
rag = EmbRag(documents_path, faiss_path)
```

### What Happens During Initialization?

When you create a new instance of `EmbRag`, the system automatically:

1. **Document Processing**
   - Scans through all documents in your knowledge base
   - Converts documents to markdown format if not already cached
   - Caches processed documents for faster future access

2. **Text Chunking**
   - Splits documents into smaller, manageable chunks
   - Maintains context through overlapping chunks
   - Optimizes chunk size for effective retrieval

3. **Index Creation**
   - Generates embeddings for all text chunks
   - Creates a FAISS index for efficient similarity search
   - Stores metadata for quick document retrieval

### Example Usage
```python
# Example paths
DOC = "C:/path/to/your/documents"
faiss_path = "C:/path/to/store/faiss_data"

# Create RAG instance
rag = EmbRag(DOC, faiss_path)
```

## Note
Make sure your document paths are accessible and you have sufficient storage space for the FAISS index and cached documents.
