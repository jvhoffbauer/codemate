import pinecone
from langchain.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os


# vectorstore = FAISS.from_texts(
#    ["import numpy as np", "import pandas as pd", "import torch"], embedding=OpenAIEmbeddings()
# )
# retriever = vectorstore.as_retriever()

pinecone_api_key = os.environ.get("PINECONE_API_KEY", None)
assert pinecone_api_key is not None, "Needs PINECONE_API_KEY"

pinecone.init(      
	api_key=pinecone_api_key,      
	environment='gcp-starter'      
)      
# index = pinecone.Index('codemate')

embeddings = OpenAIEmbeddings()
docsearch = Pinecone.from_existing_index("codemate", embeddings)


def run_retriever(context):
    # result = retriever.invoke(context)
    # result = result[0].page_content
    result = docsearch.similarity_search(context)
    result = result[0].page_content
    return result


def main():
    print(run_retriever("np.zeros(10)"))
    print(run_retriever("pd.DataFrame()"))


if __name__ == "__main__":
    main()
