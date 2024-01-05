import html
import os

import dotenv
import pandas as pd
from code_splitter import PythonCodeSplitter
from langchain.embeddings.huggingface import HuggingFaceEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from tqdm import tqdm
from unixcoder import UnixcoderEmbeddings

dotenv.load_dotenv("../backend/.env")


TOP_K = 3


def main():
    vector_dbs = {
        "unixcoder": Chroma(
            persist_directory="embeddings/unixcoder",
            embedding_function=UnixcoderEmbeddings(),
        ),
        "openai": Chroma(
            persist_directory="embeddings/openai",
            embedding_function=OpenAIEmbeddings(),
        ),
        # "e5_code": Chroma(
        #     persist_directory="embeddings/e5",
        #     embedding_function=HuggingFaceEmbeddings(
        #         model_name="intfloat/e5-mistral-7b-instruct",
        #         model_kwargs={"device": "cuda:0"},
        #     ),
        # ),
        "reacc": Chroma(
            persist_directory="embeddings/reacc-py-retriever",
            embedding_function=HuggingFaceEmbeddings(
                model_name="microsoft/reacc-py-retriever",
                model_kwargs={"device": "cuda:0"},
            ),
        ),
        # "cocosoda": Chroma(
        #     persist_directory="embeddings/cocosoda",
        #     embedding_function=HuggingFaceEmbeddings(
        #         model_name="DeepSoftwareAnalytics/CoCoSoDa",
        #         model_kwargs={"device": "cuda:0"},
        #     ),
        # ),
    }

    rows = []
    for filename in os.listdir("test_data"):
        with open(os.path.join("test_data", filename)) as f:
            test_snippet = f.read()

        splitter = PythonCodeSplitter(
            enabled_node_types=["function_definition", "decorated_definition"]
        )
        parts = splitter.split_text(test_snippet)
        longest_part = max(parts, key=lambda x: len(x))

        retrieved_snippets = {}
        for name, vector_db in vector_dbs.items():
            result = vector_db.similarity_search(longest_part, k=TOP_K)
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
                    "query": longest_part,
                    "found_snippet": snippet,
                }
                rows.append(row)

    df = pd.DataFrame(rows)
    print(df.columns)
    print(df.head(1))
    print(f"#rows = {df.shape[0]}")
    # Save html
    html = df.to_html(
        escape=False,
        formatters={"query": format_code, "found_snippet": format_code},
        index=False,
    )
    with open("out/comparison.html", "w") as f:
        f.write(html)
    # Save excel for labelling
    df.sample(frac=1, random_state=42).sort_values(by=["filename"]).to_excel(
        "out/comparison_labelling.xlsx", index=False
    )


def format_code(code):
    # Add line breaks
    code = code.replace("\n", "<br>")
    # Make code block
    code = f'<pre><code style="background-color: #333">{code.replace("img", "-img")}</code></pre>'
    # Make leftbound
    code = f'<div style="text-align: left; width: 600px; word-wrap: break-word; white-space: normal; overflow: hidden; background-color: #333">{code}</div>'
    return code


if __name__ == "__main__":
    main()
