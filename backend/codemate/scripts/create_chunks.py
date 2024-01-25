import argparse
import json
import os
from os.path import join

import pandas as pd
from codemate.code2text.llm_code_description import (
    MAX_ALLOWED_CHUNK_SIZE_FOR_DESCRIPTION,
    explain_code,
    get_pipeline,
)
from codemate.embedding.code_splitter import PythonCodeSplitter
from langchain.docstore.document import Document
from tqdm import tqdm


def create_chunks():
    """
    Create the chunks from the processed python files.

    Returns:
        List[Document]: Lanchain documents for each chunk
    """
    # Load the files
    all_files = []
    for root, dirs, files in os.walk("data/processed/", topdown=True):
        files = [
            os.path.join(root, f)
            for f in files
            if f.endswith(".py") or f.endswith(".md")
        ]
        all_files += files

    # Print number of files
    print(f"Has {len(all_files)} files, e.g.: {all_files[0]}")

    # Read the files and create documents
    texts = []
    for file in all_files:
        with open(file) as f:
            try:
                file_content = f.read()
                if file_content:
                    texts.append(
                        Document(page_content=file_content, metadata={"filename": file})
                    )
            except Exception as e:
                print(f"Error reading file {file}: {e}")

    # Print number of documents
    print(f"Has {len(texts)} documents, e.g. {str(texts[0])[:50]}")

    # Split the documents using custom code splitter (technically one could add other splitters here)
    splitters = [
        PythonCodeSplitter(
            enabled_node_types=["function_definition", "decorated_definition"],
            apply_black=True,
            skip_syntax_errors=True,
        )
    ]
    chunks = [splitter.split_documents(texts) for splitter in tqdm(splitters)]

    # Print the number of chunks per splitter
    print("Number of chunks per splitter:", [len(chunk) for chunk in chunks])

    # Flatten the chunks into a single list
    chunks = [chunk for sublist in chunks for chunk in sublist]

    # Remove any duplicates by page_content
    len_before_dedup = len(chunks)
    chunks = list({chunk.page_content: chunk for chunk in chunks}.values())
    print(f"Removed {len_before_dedup - len(chunks)} duplicates")

    # Print the cost of embedding with OpenAI (for reference) and the number of chunks
    approx_tokens = sum([len(t.page_content) for t in chunks])
    print(f"Embedding cost with OpenAI: {round(approx_tokens / 1000 * 0.0001, 2)}$")
    print(f"Number of chunks: {len(chunks)}")

    # Print some examples
    for i in [0, 1000, 5000, 10000, 20000, 30000, 40000]:
        if i >= len(chunks):
            break
        print(chunks[i].page_content)
        print("-" * 80)

    return chunks


def save_chunks(dir_name, chunks):
    """
    Save the chunks to disk.

    Args:
        dir_name
        chunks
    """
    # Create the directory if necessary
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    # Save the chunks
    for i, chunk in enumerate(chunks):
        with open(join(dir_name, f"{i}.py"), "w") as f:
            f.write(chunk.page_content)
        with open(join(dir_name, f"{i}.meta"), "w") as f:
            json.dump(chunk.metadata, f)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--add_text_description", action="store_true", default=False)
    args = parser.parse_args()

    # Get the chunks
    chunks = create_chunks()

    # Print the length quantiles
    chunk_lens = [len(c.page_content) for c in chunks]
    series = pd.Series(chunk_lens)
    print("Length quantiles:")
    print(series.quantile([0.1, 0.25, 0.5, 0.75, 0.9]))

    # Store chunks
    save_chunks("data/chunks", chunks)

    # Embedd with text if necessary
    if args.add_text_description:
        # Keep track of chunks
        chunks_described = []
        # Create the pipeline for text description
        pipe = get_pipeline()
        for i, chunk in enumerate(tqdm(chunks)):
            # Skip long chunks (as they would not fit into VRAM)
            if len(chunk.page_content) > MAX_ALLOWED_CHUNK_SIZE_FOR_DESCRIPTION:
                continue

            # Describe the chunk
            description = explain_code(chunk.page_content, pipe)

            # Create new chunk. Store original code in metadata and description in page_content
            chunk.metadata = {"original_code": chunk.page_content}
            chunk.page_content = description
            chunks_described.append(chunk)

            # Print some examples
            if i % 100 == 0 or i < 100:
                print(chunk.page_content)
                print("-" * 80)

        # Store chunks
        save_chunks("data/chunks_text", chunks_described)


def load_chunks(dir_name):
    """
    Load the chunks from disk.

    Args:
        dir_name
    """

    # Get chunk ids
    ids = os.listdir(dir_name)
    ids = [int(i.split(".")[0]) for i in ids if i.endswith(".py")]
    print(f"Found {len(ids)} chunks in {dir_name}")

    # Load chunks
    chunks = []
    for i in tqdm(ids):
        with open(join(dir_name, f"{i}.py")) as f:
            page_content = f.read()
        with open(join(dir_name, f"{i}.meta")) as f:
            metadata = json.load(f)
        chunks.append(Document(page_content=page_content, metadata=metadata))

    return chunks


if __name__ == "__main__":
    main()
