from codemate import schemas
from codemate.dummy_data import suggestions as dummy_suggestions

# vectorstore = FAISS.from_texts(
#    ["import numpy as np", "import pandas as pd", "import torch"], embedding=OpenAIEmbeddings()
# )
# retriever = vectorstore.as_retriever()
#
# pinecone_api_key = os.environ.get("PINECONE_API_KEY", None)
# assert pinecone_api_key is not None, "Needs PINECONE_API_KEY"
#
# pinecone.init(api_key=pinecone_api_key, environment="gcp-starter")
# # index = pinecone.Index('codemate')
#
# embeddings = OpenAIEmbeddings()
# docsearch = Pinecone.from_existing_index("codemate", embeddings)
#
# def run_retriever(context):
#     # result = retriever.invoke(context)
#     # result = result[0].page_content
#     result = docsearch.similarity_search(context)
#     result = result[0].page_content
#     return result


def retrieve(text, cursor_line, cursor_column) -> schemas.Suggestion:
    return dummy_suggestions
