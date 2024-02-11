import os

import dotenv
import nomic
import numpy as np
import pandas as pd
from langchain.vectorstores import Chroma
from nomic import atlas

from codemate.embedding.code_splitter import PythonCodeSplitter
from codemate.embedding.unixcoder import UnixcoderEmbeddings

# Load the environment variables
dotenv.load_dotenv("../backend/.env")

# Login to nomic
nomic.login(os.environ["NOMIC_TOKEN"])


def main():
    # Change the vector db to the one you want to upload
    vector_db = Chroma(
        persist_directory="embeddings/unixcoder",
        embedding_function=UnixcoderEmbeddings(),
    )

    # Get the documents and embeddings from the vector db
    content = vector_db.get(include=["documents", "embeddings"])

    # Upload the data to the atlas
    atlas.map_data(
        identifier="unixcoder",
        data=[{"text": text} for text in content["documents"]],
        embeddings=np.array(content["embeddings"]),
    )


if __name__ == "__main__":
    main()
