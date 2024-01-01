import os

import dotenv
import pandas as pd
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from tqdm import tqdm
from unixcoder import UnixcoderEmbeddings

dotenv.load_dotenv("../backend/.env")


CONTEXT_LENGTH = 10
TOP_K = 3


def main():
    vector_dbs = {
        "unixcoder_code_splitter": Chroma(
            persist_directory="embeddings/unixcoder_code_splitter",
            embedding_function=UnixcoderEmbeddings(),
        ),
        "unixcoder": Chroma(
            persist_directory="embeddings/unixcoder",
            embedding_function=UnixcoderEmbeddings(),
        ),
        # "reacc": Chroma(persist_directory="embeddings/reacc-py-retriever", embedding_function=HuggingFaceEmbeddings(model_name="microsoft/reacc-py-retriever", model_kwargs={'device': 'cuda:0'})),
        # "cocosoda": Chroma(persist_directory="embeddings/cocosoda", embedding_function=HuggingFaceEmbeddings(model_name="DeepSoftwareAnalytics/CoCoSoDa", model_kwargs={'device': 'cuda:0'})),
        # "openai_code_splitter": Chroma(
        #     persist_directory="embeddings/openai_code_splitter",
        #     embedding_function=OpenAIEmbeddings(),
        # ),
        # "openai": Chroma(
        #     persist_directory="embeddings/openai", embedding_function=OpenAIEmbeddings()
        # ),
    }

    rows = []

    for filename in os.listdir("test_data"):
        with open(os.path.join("test_data", filename)) as f:
            test_snippet = f.read()

        lines = test_snippet.split("\n")
        cursor_index = [i for i, line in enumerate(lines) if "[CURSOR]" in line][0]
        lines = lines[
            max(0, cursor_index - CONTEXT_LENGTH) : cursor_index + CONTEXT_LENGTH + 1
        ]
        snippet_test_cursor = "\n".join(lines).replace("[CURSOR]", "")

        retrieved_snippets = {}
        for name, vector_db in vector_dbs.items():
            result = vector_db.similarity_search(snippet_test_cursor, k=TOP_K)
            result = [r.page_content[:2000] for r in result]
            retrieved_snippets[name] = result
        print(f"Processed {filename} with {vector_dbs.keys()}")

        # Create the result rows
        for name, snippets in retrieved_snippets.items():
            for i, snippet in enumerate(snippets):
                row = {
                    "filename": filename,
                    "model_name": name,
                    "index": i,
                    "query": test_snippet,
                    "found_snippet": snippet,
                }
                rows.append(row)

    df = pd.DataFrame(rows)
    print(df.columns)
    print(df.head(1))
    html = df.to_html(
        escape=False,
        formatters={"query": format_code, "found_snippet": format_code},
        index=False,
    )
    with open("out/comparison.html", "w") as f:
        f.write(html)


def format_code(code):
    # Add line breaks
    code = code.replace("\n", "<br>")
    # Make code block
    code = f'<pre><code style="background-color: #333">{code}</code></pre>'
    # Make leftbound
    code = f'<div style="text-align: left; width: 600px; word-wrap: break-word; white-space: normal; overflow: hidden; background-color: #333">{code}</div>'
    return code


if __name__ == "__main__":
    main()
