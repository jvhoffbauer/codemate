# Stop on error
set -e

python3 -m codemate.scripts.create_embeddings --embedding_name=unixcoder --drop
python3 -m codemate.scripts.create_embeddings --embedding_name=unixcoder-poj104 --drop
python3 -m codemate.scripts.create_embeddings --embedding_name=openai --drop
python3 -m codemate.scripts.create_embeddings --embedding_name=reacc --drop

python3 -m codemate.scripts.create_embeddings --embedding_name=openai_text --drop
python3 -m codemate.scripts.create_embeddings --embedding_name=e5_text --drop
