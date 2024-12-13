# Monopoly AI v1.2.1

Monopoly AI is an interactive application designed to work with an Local Retrieval-Augmented Generation (RAG) model. It features a graphical user interface (GUI) for user interaction and Ollama to process and query data.

## Features
* Ollama Local LLM: Utilize a Local LLM to interpolate data and generate responses.

* GUI Interface: User interface built with CustomTkinter to demonstrate how the Local RAG model works.

* Data Management: Scripts for embedding generation, database population, and querying.

## Requirements
The project dependencies are listed in requirements.txt and include:

* pypdf
* langchain
* chromadb (for vector storage)
* pytest
* boto3
* langchain_ollama
* langchain_chroma
* customtkinter
* pillow
* pywinstyles

## Installation 
* Clone the repository or extract the ZIP archive.
Install the required Python packages using:
bash


``` bash
pip install -r requirements.txt
```

## Usage
Launching the GUI: Run the main GUI script:
```Python
python gui.py
```
Embedding Generation: Use ```get_embeddings.py``` to generate embeddings for your data.

Populating the Database: Run ```populate_database.py``` to populate the local database with embeddings or other data.

Querying Data: Use ```query_data.py``` to retrieve data using the RAG model.

## Configuration
Theme: Modify theme.json to customize the look and feel of the application.

Assets: Update the images in the images/ folder for custom branding or visuals.

## License

[MIT](https://choosealicense.com/licenses/mit/)