import os

import dotenv
import torch
from code_splitter import PythonCodeSplitter
from direct_hf_embedding import DirectHfEmbedding
from langchain.docstore.document import Document
from langchain.vectorstores import Chroma
from tqdm import tqdm

dotenv.load_dotenv("../backend/.env")
print(f"Has GPU: {torch.cuda.is_available()}")


def load_chunks():
    # Load the files
    all_files = []
    for root, dirs, files in os.walk("data/processed/", topdown=True):
        files = [
            os.path.join(root, f)
            for f in files
            if f.endswith(".py") or f.endswith(".md")
        ]
        all_files += files

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

    print(f"Has {len(texts)} documents, e.g. {str(texts[0])[:50]}")

    splitters = [
        PythonCodeSplitter(
            enabled_node_types=["function_definition", "decorated_definition"],
            apply_black=True,
            skip_syntax_errors=True,
        )
    ]
    chunks = [splitter.split_documents(texts) for splitter in tqdm(splitters)]

    print("Lengths:", [len(chunk) for chunk in chunks])

    chunks = [chunk for sublist in chunks for chunk in sublist]

    approx_tokens = sum([len(t.page_content) for t in chunks])
    print(f"Embedding cost with OpenAI: {round(approx_tokens / 1000 * 0.0001, 2)}$")
    print(f"Number of chunks: {len(chunks)}")

    for i in [0, 1000, 5000, 10000, 20000, 30000, 40000]:
        if i >= len(chunks):
            break
        print(chunks[i].page_content)
        print("-" * 80)

    return chunks


def embedd(embedding_function, chunks, persist_directory):
    db = Chroma.from_documents(
        chunks, embedding_function, persist_directory=persist_directory
    )
    return db


def main():
    chunks_code_splitter = load_chunks()

    # # Unixcoder
    # embedd(
    #     embedding_function=UnixcoderEmbeddings(),
    #     persist_directory="embeddings/unixcoder_code_splitter",
    #     chunks=chunks_code_splitter,
    # )

    # # OpenAI
    # embedd(
    #     embedding_function=OpenAIEmbeddings(),
    #     persist_directory="embeddings/openai_code_splitter",
    #     chunks=chunks_code_splitter,
    # )

    # E5 Mistral7B Instruct
    embedd(
        embedding_function=DirectHfEmbedding(
            model_name="intfloat/e5-mistral-7b-instruct",
            model_kwargs={"load_in_8bit": True},
        ),
        persist_directory="embeddings/e5_code_splitter",
        chunks=[c for c in chunks_code_splitter if len(c.page_content) < 4000],
    )

    # chunks = load_chunks()
    #
    # # Unixcoder
    # embedd(
    #     embedding_function=UnixcoderEmbeddings(),
    #     persist_directory="embeddings/unixcoder",
    #     chunks=chunks,
    # )
    #
    # # OpenAI
    # embedd(
    #     embedding_function=OpenAIEmbeddings(),
    #     persist_directory="embeddings/openai",
    #     chunks=chunks,
    # )
    #
    # # Reacc
    # embedd(
    #     embedding_function=HuggingFaceEmbeddings(
    #         model_name="microsoft/reacc-py-retriever",
    #         model_kwargs={"device": "cuda:0"},
    #         encode_kwargs={"show_progress_bar": True},
    #     ),
    #     persist_directory="embeddings/reacc-py-retriever",
    #     chunks=chunks,
    # )
    #
    # # Cocosoda
    # tokenizer_cocosoda = AutoTokenizer.from_pretrained("DeepSoftwareAnalytics/CoCoSoDa")
    # chunks_cocosoda = chunks
    # for c in chunks_cocosoda:
    #     c.page_content = tokenizer_cocosoda.decode(
    #         tokenizer_cocosoda.encode(c.page_content)[:1025][1:-1]
    #     )
    # embedd(
    #     embedding_function=HuggingFaceEmbeddings(
    #         model_name="DeepSoftwareAnalytics/CoCoSoDa",
    #         model_kwargs={"device": "cuda:0"},
    #         encode_kwargs={"show_progress_bar": True},
    #     ),
    #     persist_directory="embeddings/cocosoda",
    #     chunks=chunks_cocosoda,
    # )


if __name__ == "__main__":
    main()
