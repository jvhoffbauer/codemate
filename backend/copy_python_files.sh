rsync -a --prune-empty-dirs --include '*/' --include '*.py' --exclude '*' data/raw/ data/processed
cd data/processed
black .
