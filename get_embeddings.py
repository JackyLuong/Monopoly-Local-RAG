# Retrieve embeddings function for the RAG Function
# Created: 2024-10-29
# By: Jacky Luong

from langchain_ollama import OllamaEmbeddings
# from langchain_community.embeddings.bedrock import BedrockEmbeddings

# Function to retrieve embeddings function form Ollama
#
# Returns 
# Embedding embeddings
def get_embedding_function():
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-east-1"
    # )
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings