from codemate.api import schemas
from codemate.api.dummy_data import suggestions as dummy_suggestions
import black
from codemate.embedding.code_splitter import get_parser, iter_nodes, get_node_text_with_indent
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from codemate.embedding.unixcoder import UnixcoderEmbeddings


MAX_EXAMPLE_LENGTH = 1000


unixcoder_vectordb = Chroma(
    persist_directory="embeddings/unixcoder",
    embedding_function=UnixcoderEmbeddings(),
)


def retrieve(text, cursor_line, cursor_column) -> schemas.Suggestion:
    query = get_query(text, cursor_line, cursor_column)
    if query is None:
        return schemas.Suggestion(examples=[])
    results = unixcoder_vectordb.similarity_search(query, k=3)
    results = [r.page_content[:MAX_EXAMPLE_LENGTH] for r in results]
    suggestions = schemas.Suggestion(examples=[
        schemas.Example(text=r, source="https://github.com/dummy", stars=100)
        for r in results
    ])
    return suggestions


def get_query(text, cursor_line, cursor_column):
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
                return  get_node_text_with_indent(node, depth)