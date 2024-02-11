## Ingest the data

This repo already comes with downloaded data and created embeddings so that you can start running the extension right away. However, you can also download the data yourself or ingest your own files to get even more relevant examples. 

All code in this section runs within the backend folder, i.e. run 

```
cd backend
```

### Download Github Repositories

Get an access token for the Github API as explained [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-fine-grained-personal-access-token). Then, set your Github API key via 

``` 
export GITHUB_API_KEY="YOUR_API_KEY"
```

Open the notebook [load_repos](backend/codemate/scripts/load_repos.ipynb) and run all cells. This will download the top repos for FastAPI and store them within the project under `backend/data/raw`. 

To filter any unrelated files and format the code files, run 

```
sh ./copy_python_files.sh
```

Create a mapping from repo names to their URLs (done in hindsight to enable repo links in the URL)

```
python3 -m codemate.scripts.store_repo_urls
```

Finally, you can finde the downloaded code files under `backend/data/processed`. 

### Chunk the code and create text representations

The existing code needs to be chunked using 

``` 
python3 -m codemate.scripts.create_chunks
```

To also convert the code to text explanations (which we can embedd), run the following code. This requires a GPU with 32GB VRAM and takes 8 hours or more. 

``` 
python3 -m codemate.scripts.create_chunks --add_text_description
```

### Create the vectorstores

To create the unixcoder embeddings which are required to run the extension, run the following script. You can replace unixcoder with any other embedding to create this one specifically. 

``` 
python3 -m codemate.scripts.create_embeddings --embedding_name=unixcoder --drop
```

To create all embeddings that are used during development of the app, run 

```
cd backend
sh ./create_embeddings.sh
```

The embeddings will be stored in `backend/embeddings`

### Visualize the embeddings

Visualize the embeddings using Nomic Atlas. Make sure to login to their service as outlined [here](https://docs.nomic.ai/atlas/introduction/quick-start) and set the `NOMIC_TOKEN` environment variable accordingly. 

```
python3 -m codemate.scripts.nomic_atlas_upload
```