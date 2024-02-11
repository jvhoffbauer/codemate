import json

import black
from langchain.vectorstores import Chroma

from codemate.api import schemas
from codemate.embedding.code_splitter import (
    get_node_text_with_indent,
    get_parser,
    iter_nodes,
)
from codemate.embedding.unixcoder import UnixcoderEmbeddings

MAX_EXAMPLE_LENGTH = 1000

# Load vector database
unixcoder_vectordb = Chroma(
    persist_directory="embeddings/unixcoder",
    embedding_function=UnixcoderEmbeddings(),
)

# Load repo urls
repo_urls = json.load(open("data/_meta/repo_urls.json"))


def retrieve(text: str, cursor_line: int, cursor_column: int) -> schemas.Suggestion:
    """
    Retrieve relevant examples for the current cursor location in the file.

    Args:
        text (str): text of the current open file
        cursor_line (int): location of the cursor
        cursor_column (int): location of the cursor

    Returns:
        schemas.Suggestion: relevant exampels for the current cursor location in the file
    """
    # Get query string
    query = get_query(text, cursor_line, cursor_column)

    # In case we're not in a function definition, return dummy data
    if query is None:
        return schemas.Suggestion(examples=[])

    # Run query
    results = unixcoder_vectordb.similarity_search(query, k=3)

    # Get codes
    codes = [r.page_content[:MAX_EXAMPLE_LENGTH] for r in results]

    # Get github urls from metadata
    urls = [r.metadata["filename"] for r in results]
    # Parse filenames back into repository urls
    urls = [f.replace("data/processed/", "").split("/")[0] for f in urls]
    urls = [f.replace("-master", "").replace("-main", "") for f in urls]
    urls = [f"{repo_urls[f]}" for f in urls]

    # Create suggestion from requry results
    suggestions = schemas.Suggestion(
        examples=[schemas.Example(text=code, source=url, stars=100) for code, url in zip(codes, urls)]
    )
    return suggestions


def get_query(text, cursor_line, cursor_column):
    """
    Convert a cursor location in a file to a query string by getting the
    function definition that contains the cursor location.

    Args:
        text
        cursor_line
        cursor_column

    Returns:
        function definition as string or None if no function definition is found
    """
    text = black.format_str(text, mode=black.Mode())

    tree = get_parser().parse(bytes(text, "utf8"))
    nodes = list(iter_nodes(tree))

    # Get the first node that contains the cursor and is a function definition
    for node, depth, _ in nodes:
        start_column = node.start_point[1]
        end_column = node.end_point[1]
        start_line = node.start_point[0]
        end_line = node.end_point[0]
        if start_column <= cursor_column <= end_column and start_line <= cursor_line <= end_line:
            if node.type in ["function_definition", "decorated_definition"]:
                return get_node_text_with_indent(node, depth)
