# rag-mongo-atlas-poc
Prototype to do Retrieval Augmented Generation with MongoDB Atlas

## steps to embed.
1. Knowledge Source Define your documents or data — e.g., PDFs, text files, website content.
2. Ingestion & Indexing Split documents into chunks.
3. Embed the chunks using an embedding model (e.g., OpenAI Embeddings).
4. Store the embeddings in a vector database (e.g., MongoDB Atlas).

## Steps for the retrieval process when use asks a question.
1. Embed the question.
2. Search the vector database for the most relevant document chunks.
3. Pass the retrieved chunks (as context) along with the user’s query into an LLM (e.g., OpenAI GPT) to generate the final answer.


