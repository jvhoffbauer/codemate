import argparse
import os
import shutil

import dotenv
import torch
from codemate.embedding.direct_hf_embedding import DirectHfEmbedding
from codemate.embedding.unixcoder import UnixcoderEmbeddings
from codemate.scripts.create_chunks import load_chunks
from langchain.embeddings import HuggingFaceEmbeddings, OpenAIEmbeddings
from langchain.vectorstores import Chroma

dotenv.load_dotenv("../backend/.env")
print(f"Has GPU: {torch.cuda.is_available()}")


def embedd(embedding_name, chunks, chunks_text, drop):
    """Embedd the given chunks with the given embedding function.

    Args:
        embedding_name (str): name of the emebddings
        chunks: List of chunks where page_content is the code
        chunks_text: List of chunks where page_content is the description
        drop: whether to drop the existing embedding

    Returns:
        created vectorstore
    """
    # Get args
    is_text = embedding_name.endswith("_text")
    persist_directory = f"embeddings/{embedding_name}"
    embedding_function = get_embedding_function(embedding_name)

    print(f"Embedding {len(chunks)} chunks with {embedding_name}")
    print(f"  Persisting to {os.path.abspath(persist_directory)}")
    print(f"  Is text: {is_text}")
    print(f"  Embedding function: {embedding_function}")

    # Drop existing embedding if necessary
    if drop and os.path.exists(persist_directory):
        print(f"Dropping existing embedding in {persist_directory}")
        shutil.rmtree(persist_directory)

    # Create the embedding with the given function
    os.makedirs(persist_directory, exist_ok=True)
    db = Chroma.from_documents(
        chunks if not is_text else chunks_text,
        embedding_function,
        persist_directory=persist_directory,
    )
    return db


def get_embedding_function(embedding_name):
    """Return the embedding function for the given name.

    Args:
        embedding_name (str): name of the emebddings

    Raises:
        ValueError: occurs when the embedding name is unknown

    Returns:
        Embedding function to use when embedding the chunks
    """
    # Get embedding function
    if embedding_name == "unixcoder":
        embedding_function = UnixcoderEmbeddings()
    elif embedding_name == "unixcoder-poj104":
        embedding_function = UnixcoderEmbeddings(
            model_name="/workspaces/codemate/unixcoder-poj104-model"
        )
    elif embedding_name in ["openai", "openai_text"]:
        embedding_function = OpenAIEmbeddings()
    elif embedding_name in ["e5", "e5_text"]:
        embedding_function = DirectHfEmbedding(
            model_name="intfloat/e5-mistral-7b-instruct",
            model_kwargs={"load_in_8bit": True},
        )
    elif embedding_name == "reacc":
        embedding_function = HuggingFaceEmbeddings(
            model_name="microsoft/reacc-py-retriever",
            model_kwargs={"device": "cuda:0"},
            encode_kwargs={"show_progress_bar": True},
        )

    # Raise error if embedding name is unknown
    if embedding_function is None:
        raise ValueError(f"Unknown embedding name: {embedding_name}")

    return embedding_function


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--embedding_name", type=str, required=True)
    parser.add_argument("--drop", action="store_true", default=False)
    args = parser.parse_args()

    # Load chunks from disk
    chunks = load_chunks("data/chunks")
    chunks_text = load_chunks("data/chunks_text")

    # Run embedding
    embedd(
        embedding_name=args.embedding_name,
        chunks=chunks,
        chunks_text=chunks_text,
        drop=args.drop,
    )


if __name__ == "__main__":
    main()
