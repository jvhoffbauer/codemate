import os

import dotenv
import nomic
import numpy as np
import pandas as pd
from codemate.embedding.code_splitter import PythonCodeSplitter
from codemate.embedding.unixcoder import UnixcoderEmbeddings
from langchain.vectorstores import Chroma
from nomic import atlas

dotenv.load_dotenv("../backend/.env")

nomic.login(os.environ["NOMIC_TOKEN"])


def main():
    vector_db = Chroma(
        persist_directory="embeddings/unixcoder",
        embedding_function=UnixcoderEmbeddings(),
    )

    content = vector_db.get(include=["documents", "embeddings"])

    content["documents"][0], content["embeddings"][0].__len__()

    atlas.map_data(
        identifier="unixcoder",
        data=[{"text": text} for text in content["documents"]],
        embeddings=np.array(content["embeddings"]),
    )


if __name__ == "__main__":
    main()
