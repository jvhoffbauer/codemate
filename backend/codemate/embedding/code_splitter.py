import logging
from typing import List

import black
from langchain.text_splitter import TextSplitter
from tree_sitter import Language, Parser

logger = logging.getLogger(__name__)

TAB_WIDTH = 4


class SyntaxError(ValueError):
    def __init__(self, message):
        super().__init__(message)


class PythonCodeSplitter(TextSplitter):
    """
    Custom text splitter that splits Python code into chunks. It works
    only with (mostly) syntactically correct Python code. Every code file
    will generate chunks for

     - every function
     - every method in a class
     - every indent block longer than x lines

    according to what is enabled in the configuration.
    Optionally, applies black formatting to the code before splitting.
    """

    def __init__(
        self,
        enabled_node_types=None,
        min_block_lines=10,
        apply_black=True,
        skip_syntax_errors=False,
    ):
        """Create the PythonCodeSplitter.

        Args:
            enabled_node_types (str, optional): The names of the node types we are returning when splitting. Defaults to ["function_definition", "class_definition", "block"]
            min_block_lines (int, optional): Minimum size for code blocks to be returned. Defaults to 10.
            apply_black (bool, optional): Whether black formatting should be applied to code before chunking. Defaults to True.
            skip_syntax_errors (bool, optional): Whether we skip code with syntax errors. Defaults to False.
        """
        super().__init__()

        # Handle default values. We need to do this because we can't use mutable default arguments.
        if enabled_node_types is None:
            enabled_node_types = [
                "function_definition",
                "class_definition",
                "block",
            ]

        # Store parameters
        self.enabled_node_types = enabled_node_types
        self.min_block_lines = min_block_lines
        self.apply_black = apply_black
        self.skip_syntax_errors = skip_syntax_errors

    def split_text(self, text: str) -> List[str]:
        """
        Split the text into chunks.
        """
        # Apply black if necessary
        if self.apply_black:
            text = black.format_str(text, mode=black.Mode())

        # Parse the code and get nodes
        tree = get_parser().parse(bytes(text, "utf8"))
        nodes = list(iter_nodes(tree))

        # Check for syntax errors
        # if any(node.type == "ERROR" for node, _, _ in nodes):
        #     raise SyntaxError(f"Syntax error in code at {node}: {node.text}")
        if any(node.type == "ERROR" for node, _, _ in nodes):
            logger.warning(f"Syntax error in code at '{text[:100]}'...")
            if self.skip_syntax_errors:
                return []

        # Get the chunks
        chunks = []
        for node, depth, _ in nodes:
            node_text = lambda: get_node_text_with_indent(node, depth)
            if node.type in self.enabled_node_types:
                # Add the node text to the chunks
                if node.type != "block":
                    chunks.append(node_text())
                elif node.type == "block" and len(node.text.decode().split("\n")) > self.min_block_lines:
                    chunks.append(node_text())

        # Remove duplicates
        chunks = list(dict.fromkeys(chunks))

        return chunks


def get_parser():
    """Create a treesitter parser for Python. We need to build the language first, but the result will be cached. once executed once."""
    Language.build_library(
        "../tree-sitter-languages/build/my-languages.so",
        ["../tree-sitter-languages/tree-sitter-python"],
    )

    parser = Parser()
    PY_LANGUAGE = Language("../tree-sitter-languages/build/my-languages.so", "python")
    parser.set_language(PY_LANGUAGE)
    return parser


def iter_nodes(tree):
    """
    Yield every node in the tree. Yields tuples of (node, parents) where parents is a list of parent nodes that the node has.
    """
    cursor = tree.walk()
    parents = []
    while True:
        node = cursor.node
        depth = cursor.depth
        yield node, depth, parents

        # Try going down first, then right, then up+right again unless we're at the root
        if cursor.goto_first_child():
            parents.append(node)
            continue
        if cursor.goto_next_sibling():
            continue
        else:
            while cursor.goto_parent():
                parents.pop()
                if cursor.goto_next_sibling():
                    break
            if cursor.node == tree.root_node:
                break


def get_node_text_with_indent(node, depth):
    """Convert the node with given depth to a string with the correct indentation."""
    text = node.text.decode()
    preceding_whitespaces = node.start_point[1]
    result = " " * preceding_whitespaces + text
    return result


def main():
    code = """
def foo(): 
    if bar: baz()
def foo2():
    if bar:
        baz()
    elif x: y()
    else:
        baz2()
class X:
    def __init__(self):
        self.i = 1
    """

    # parser = get_parser()
    # tree = parser.parse(
    #     bytes(
    #         code,
    #         "utf8",
    #     )
    # )
    #
    # print("---------------------------------")
    # for node, depth, parents in iter_nodes(tree):
    #     print(
    #         f"{'    ' * depth} depth={depth} type={node.type} parents={[p.type for p in parents]} text='{node.text}'"
    #     )
    # print("---------------------------------")

    splitter = PythonCodeSplitter(min_block_lines=1)
    chunks = splitter.split_text(code)
    for chunk in chunks:
        print(chunk)
        print("--")


if __name__ == "__main__":
    main()
