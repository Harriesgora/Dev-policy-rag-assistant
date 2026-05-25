# Imports Path from Python's pathlib module

# Path helps us work with folders and files more easily
from pathlib import Path

def load_documents(): 
    documents_folder = Path("documents")
    loaded_documents = []

    # Loops through every .txt file inside the documents folder
    for file_path in documents_folder.glob("*.*"):
        document_text = file_path.read_text()
        
        # We add the document's name and its text to the loaded_documents list as a dictionary
        loaded_documents.append({
            "document_name": file_path.name,
            "text": document_text
        })

        return loaded_documents
    
    # function that is responsible for splitting documents into smaller chunks
def chunk_documents(documents):
        chunks = []

        for document in documents:
            text = document["text"]
            document_name = document["document_name"]

            # We split the text into sections into smaller sections based on double newlines (\n\n)
            text_sections = text.split("\n\n") 

            for index, section in enumerate(text_sections):
                clean_section = section.strip()

                # We only add the section to the chunks list if it's not empty after stripping whitespace
                if clean_section:

                    chunks.append ({
                        "document_name": document_name,
                        "chunk_id": index + 1,
                        "chunk_text": clean_section
                    })

        return chunks
