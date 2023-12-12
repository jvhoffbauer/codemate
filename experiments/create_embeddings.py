import os
import torch
import dotenv
from tqdm import tqdm
from unixcoder import UnixcoderEmbeddings
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter, Language
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from transformers import AutoTokenizer


dotenv.load_dotenv("../backend/.env")
print(f"Has GPU: {torch.cuda.is_available()}")


def load_chunks():
    # Load the files 
    all_files = []
    for root, dirs, files in os.walk("data/processed/", topdown=True):
        files = [os.path.join(root, f) for f in files if f.endswith('.py') or f.endswith('.md')]
        all_files += files

    print(f'Has {len(all_files)} files, e.g.: {all_files[0]}')

    # Read the files and create documents
    texts = []
    for file in all_files: 
        with open(file) as f:
            try:  
                file_content = f.read()
                if file_content:
                    texts.append(Document(page_content=file_content, metadata={"filename": file}))
            except Exception as e:
                print(f"Error reading file {file}: {e}")

    print(f"Has {len(texts)} documents, e.g. {str(texts[0])[:50]}")

    splitters = [
        CharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=100, 
            separator="\n", 
            is_separator_regex=False,
        ),
        CharacterTextSplitter(
            chunk_size=500, 
            chunk_overlap=100, 
            separator="\n\n", 
            is_separator_regex=False,
        ),
        RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON, chunk_size=200, chunk_overlap=50
        ),
        RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON, chunk_size=400, chunk_overlap=100
        )
    ]
    chunks = [splitter.split_documents(texts) for splitter in tqdm(splitters)]

    print("Lengths:", [len(chunk) for chunk in chunks])

    chunks = [chunk for sublist in chunks for chunk in sublist]

    #approx_tokens = sum([len(t.page_content) for t in chunks])

    #print(f"Embedding cost with OpenAI: {round(approx_tokens / 1000 * 0.0001, 2)}$")
    print(f"Number of chunks: {len(chunks)}")

    for i in [0, 10000, 20000, 30000, 40000]: 
        print(chunks[i].page_content)
    print('-' * 80)

    return chunks


def embedd(embedding_function, chunks, persist_directory):
    db = Chroma.from_documents(chunks, embedding_function, persist_directory=persist_directory)
    return db


def main():
    chunks = load_chunks()

    # db_unix = embedd(
    #     embedding_function=UnixcoderEmbeddings(), 
    #     persist_directory="embeddings/unixcoder",
    #     chunks=chunks
    # )
    
    # db_openai = embedd(
    #   embedding_function=OpenAIEmbeddings(), 
    #   persist_directory="embeddings/openai",
    #   chunks=chunks
    # )

    # db_reacc = embedd(
    #     embedding_function=HuggingFaceEmbeddings(
    #         model_name="microsoft/reacc-py-retriever", 
    #         model_kwargs={'device': 'cuda:0'}, 
    #         encode_kwargs={"show_progress_bar": True}
    #     ), 
    #     persist_directory="embeddings/reacc-py-retriever",
    #     chunks=chunks
    # )

    tokenizer_cocosoda = AutoTokenizer.from_pretrained("DeepSoftwareAnalytics/CoCoSoDa")
    chunks_cocosoda = chunks
    for c in chunks_cocosoda:
        c.page_content = tokenizer_cocosoda.decode(tokenizer_cocosoda.encode(c.page_content)[:1025][1:-1])
    db_cocosoda = embedd(
        embedding_function=HuggingFaceEmbeddings(
            model_name="DeepSoftwareAnalytics/CoCoSoDa", 
            model_kwargs={'device': 'cuda:0'},
            encode_kwargs={"show_progress_bar": True}
        ), 
        persist_directory="embeddings/cocosoda", 
        chunks=chunks_cocosoda
    )

if __name__ == "__main__":
    main()