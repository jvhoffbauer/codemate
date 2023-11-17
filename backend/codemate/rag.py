from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


vectorstore = FAISS.from_texts(
    ["import numpy as np", "import pandas as pd", "import torch"], embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()



def run_retriever(context):
    result = retriever.invoke(context)
    result = result[0].page_content
    return result


def main():
    print(run_retriever("np.zeros(10)"))
    print(run_retriever("pd.DataFrame()"))


if __name__ == "__main__":
    main()
