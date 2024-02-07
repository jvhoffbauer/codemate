import argparse
import os

import dotenv
import pandas as pd
from codemate.code2text import llm_code_description
from codemate.embedding.code_splitter import PythonCodeSplitter
from codemate.embedding.unixcoder import UnixcoderEmbeddings
from codemate.scripts.create_embeddings import get_embedding_function
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

dotenv.load_dotenv("../backend/.env")


# We store our test data in this directory
TEST_DATA_DIR = "data/test_data"
# Longer samples are hard to read for annotators
MAX_TEST_RESULT_LEN = 2000
# Evaluate with top 3 results as this is what we use in the frontend
TOP_K = 3


def get_vector_dbs(embedding_names):
    """Get the vector dbs for the given embedding names.

    Args:
        embedding_names (List[str]): list of embedding names

    Returns:
        Dict[str, Chroma]: dict of embedding name to vector db
    """

    embedding_funcs = {name: get_embedding_function(name) for name in embedding_names}
    vector_dbs = {
        name: Chroma(
            persist_directory=f"embeddings/{name}",
            embedding_function=embedding_funcs[name],
        )
        for name in embedding_names
    }
    return vector_dbs


def format_code(code):
    # Add line breaks
    code = code.replace("\n", "<br>")
    # Make code block
    code = f'<pre><code style="background-color: #333">{code.replace("img", "-img")}</code></pre>'
    # Make leftbound
    code = f'<div style="text-align: left; width: 600px; word-wrap: break-word; white-space: normal; overflow: hidden; background-color: #333">{code}</div>'
    return code


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--embedding_names", type=str, required=True)
    args = parser.parse_args()

    # Get the vector dbs and explain usage if there is an error
    try:
        embedding_names = args.embedding_names.split(",")
        vector_dbs = get_vector_dbs(embedding_names)
    except ValueError as e:
        print(
            f"Could not get vector dbs. You gave {args.embedding_names} but it should be a comma separated list of embedding names. E.g. openai,unixcoder"
        )
        raise e

    # Get the pipeline for the code description
    pipe = llm_code_description.get_pipeline()

    # Process each test snippet and retrieve the top k snippets for each model
    rows = []
    for filename in os.listdir(TEST_DATA_DIR):
        # Load the test snippet
        with open(os.path.join(TEST_DATA_DIR, filename)) as f:
            test_snippet = f.read()

        # Split the snippet using our code splitter to get relevant input
        # Heuristic: use the longest part of the snippet
        splitter = PythonCodeSplitter(
            enabled_node_types=["function_definition", "decorated_definition"]
        )
        parts = splitter.split_text(test_snippet)
        longest_part = max(parts, key=lambda x: len(x))

        # Get the text description of the code
        text_description = llm_code_description.explain_code(longest_part, pipe)

        # Retrieve the top k snippets for each model
        retrieved_snippets = {}
        for name, vector_db in vector_dbs.items():
            # Check if we should search in the text embeddings
            textmode = "text" in name

            # Get the query
            query = longest_part if not textmode else text_description

            # Search for the query in the vector db
            result = vector_db.similarity_search(query, k=TOP_K)
            result_str = [
                r.page_content[:MAX_TEST_RESULT_LEN]
                if not textmode
                else r.metadata["original_code"]
                for r in result
            ]
            retrieved_snippets[name] = result_str

            # Print the results
            if textmode:
                print(f"Processed {filename} with {name}")
                print(f"{name} uses text mode")
                print(f"Query: \n{query}\n====>\n{result[0].page_content}")
                print("------")
                print(f"Result: \n{longest_part}\n====>\n{result_str[0]}")
                print("-----------------------------------")

        print(f"Done processing {filename} with {vector_dbs.keys()}")

        # Create the result rows
        for name, snippets in retrieved_snippets.items():
            for i, snippet in enumerate(snippets):
                row = {
                    "filename": filename,
                    "model_name": name,
                    "index": i,
                    "query_description": text_description,
                    "query": longest_part,
                    "found_snippet": snippet,
                }
                rows.append(row)

    # Create dataframe from the results
    df = pd.DataFrame(rows)

    # Print some stats about the results
    print(df.columns)
    print(df.head(1))
    print(f"#rows = {df.shape[0]}")

    # Save results as readable html
    html = df.to_html(
        escape=False,
        formatters={
            "query": format_code,
            "query_description": format_code,
            "found_snippet": format_code,
        },
        index=False,
    )
    with open("out/comparison.html", "w") as f:
        f.write(html)

    # Save excel for labelling
    df.sample(frac=1, random_state=42).sort_values(by=["filename"]).to_excel(
        "out/comparison_labelling.xlsx", index=False
    )


if __name__ == "__main__":
    main()
