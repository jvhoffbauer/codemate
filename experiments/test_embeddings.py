import dotenv
dotenv.load_dotenv("../backend/.env")

import os
import pandas as pd
from langchain.vectorstores import Chroma
from tqdm import tqdm
from unixcoder import UnixcoderEmbeddings
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings


CONTEXT_LENGTH = 10
TOP_K = 3


def main():

    vector_dbs = {
        "unixcoder": Chroma(persist_directory="embeddings/unixcoder", embedding_function=UnixcoderEmbeddings()),
        #"reacc": Chroma(persist_directory="embeddings/reacc-py-retriever", embedding_function=HuggingFaceEmbeddings(model_name="microsoft/reacc-py-retriever", model_kwargs={'device': 'cuda:0'})),
        "cocosoda": Chroma(persist_directory="embeddings/cocosoda", embedding_function=HuggingFaceEmbeddings(model_name="DeepSoftwareAnalytics/CoCoSoDa", model_kwargs={'device': 'cuda:0'})),
        #"openai": Chroma(persist_directory="./openai_embeddings", embedding_function=OpenAIEmbeddings())
    }

    rows = []
    
    for filename in os.listdir("test_data"):

        with open(os.path.join("test_data", filename)) as f:
            test_snippet = f.read()
            
    
        lines = test_snippet.split("\n")
        cursor_index = [i for i, line in enumerate(lines) if "[CURSOR]" in line][0]
        lines = lines[max(0, cursor_index - CONTEXT_LENGTH):cursor_index + CONTEXT_LENGTH + 1]
        snippet_test_cursor = "\n".join(lines).replace("[CURSOR]", "")

        retrieved_snippets = {}
        for name, vector_db in vector_dbs.items():
            result = vector_db.similarity_search(snippet_test_cursor, k=TOP_K)
            result = [r.page_content[:2000] for r in result]
            retrieved_snippets[name] = result
        print(f"Processed {filename} with {vector_dbs.keys()}")

        # Create the result row 
        row = {}
        row["filename"] = filename
        row["example"] = test_snippet
        for name, snippets in retrieved_snippets.items():
            for i, snippet in enumerate(snippets):
                row[f"{name} #{i}"] = snippet

        rows.append(row)


    df = pd.DataFrame(rows)
    print(df.columns)
    print(df.head(1))
    html = df.to_html(
        escape=False, 
        formatters = {'example': format_code, **{column: format_code for column in df.columns if "#" in column}}, 
        index=False
    )
    with open("out/comparison.html", "w") as f:
        f.write(html)


def format_code(code):
    # Add line breaks
    code = code.replace('\n', '<br>')
    # Make code block
    code = f'<pre><code style="background-color: #333">{code}</code></pre>'
    # Make leftbound 
    code = f'<div style="text-align: left; width: 450px; word-wrap: break-word; white-space: normal; overflow: hidden; background-color: #333">{code}</div>'
    return code


if __name__ == "__main__": 
    main()
