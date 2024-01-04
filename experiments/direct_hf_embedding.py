import torch
import torch.nn as nn
from langchain_core.embeddings import Embeddings
from tqdm import tqdm
from transformers import RobertaConfig, RobertaModel, RobertaTokenizer, pipeline


class DirectHfEmbedding(Embeddings):
    """Interface for embedding models."""

    def __init__(self, model_name, model_kwargs):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.pipe = pipeline(
            "feature-extraction", model=model_name, device=self.device, **model_kwargs
        )

    def embed_documents(self, texts):
        """Embed texts"""
        print(f"Embedding documents: {len(texts)}")
        embeddings = []
        for text in tqdm(texts):
            embedding = self.embed_query(text)
            embeddings.append(embedding)

        return embeddings

    def embed_query(self, text: str):
        """Embed single text."""
        embedding = self.pipe(text)
        embedding = embedding[0][-1]
        return embedding


def main():
    model = DirectHfEmbedding(
        "intfloat/e5-mistral-7b-instruct", model_kwargs={"load_in_8bit": True}
    )
    print(model.embed_query("def foo(): return 1"))


if __name__ == "__main__":
    main()
