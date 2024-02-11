# CodeMate 🚀

CodeMate is a VSCode extension that helps you find helpful examples while you code using AI

<p align="center">
    <img src="./demo_screenshot.png" width="90%" style="margin-left: auto; margin-right: auto" /> 
</p>

## 💽 Setup

### Prerequisites

To run this app locally, you need

-   Python 3.11 or above
-   An OpenAI API key (get it here [here](https://platform.openai.com/api-keys) or reach out to me if you're testing)
-   VSCode installed locally

### Python Backend

Create virtualenv and install requirements

```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Extension (Frontend)

Install dependencies

```
cd extension
npm install
npm compile
```

## 📚 Ingest Data 

This repo already comes with downloaded data and created embeddings so that you can start running the extension right away. However, you can also download the data yourself or ingest your own files to get even more relevant examples. To do that, refer to the [instructions](./INGEST_DATA.md). 

## ▶️ Start the app 

First, you need to start the Python backend and then the TypeScript VSCode extension.

### Python Backend 

Start the backend

```
export OPENAI_API_KEY="YOUR_API_KEY"
python3 -m codemate.api.main
```

### Extension (Frontend)

Open the extension's code in VSCode

```
cd extension
code .
```

And launch the application by pressing `F5` or by using the run button (config "Run Extension") ![Run Button](./run_button.png)

## 📋 Test embeddings

A fundamental part of the project was testing the embeddings. To reproduce these results, you can run 

```
cd backend 
python3 -m codemate.scripts.evaluate_embeddings --embedding_names=unixcoder
```

where the embedding name can be any of the possible embedding names that we created embeddings for. 

The test queries are stored in `backend/data/test_data`. 

The script will store an HTML file containing the different code chunks that were retrieved for each test query in `backend/out`. It will also store an Excel file that can be used to manually evaluate the results in randomized order and anonymized. 

## ❗ Known Issues

* Repository URLs are an afterthought. They were re-generated after the code was downloaded. However, as there are multiple repos with the same name (from different authors), an exact mapping is hard to re-create. This leads to the links of examples being broken sometimes. 