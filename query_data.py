# Query vector database and use an Ollama LLM Model to generate a response based on the retreived data.
# Created: 2024-10-29
# By: Jacky Luong

import argparse
import os
import asyncio
from concurrent.futures import ThreadPoolExecutor
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM
from get_embeddings import get_embedding_function

# Path to vector database
CHROMA_PATH = os.path.join(os.path.dirname(__file__), "chroma")

# Prompt template
PROMPT_TEMPLATE = """
Imagine you're a laid-back surfer dude teaching someone how to play Monopoly. 
Use chill language, like "dude","gnarly", "bro", and make everything sound relaxed and fun. 
Explain in simple steps, like you’re chatting with friends at the beach. 
Keep it positive, and use analogies like catching waves or chilling on the sand when it makes sense. 
Make sure you start your sentences differently every sentence or every other sentence.

Answer the question based only on the following context:

{context}

---

Answer the question based on the above context: {question}
"""


# def main():
#     # Create CLI.
#     parser = argparse.ArgumentParser()
#     parser.add_argument("query_text", type=str, help="The query text.")
#     args = parser.parse_args()
#     query_text = args.query_text
#     query_rag(query_text)

# Function query the vector database and feed the data to a LLM model and return a response
#
# Params
# string question
# 
# Returns
# string response
async def query_rag(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=3)

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = OllamaLLM(model="mistral")
    response_text = model.invoke(prompt)

    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"

    response_text = f"{response_text}\n\n{sources}"
    response_text = response_text.replace(r"data\\", "")
    print(formatted_response)
    return response_text


# if __name__ == "__main__":
#     main()