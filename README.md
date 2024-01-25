# CodeMate 🚀

CodeMate is a VSCode extension that helps you find helpful examples while you code using AI

<p align="center">
    <img src="./demo_screenshot.png" width="90%" style="margin-left: auto; margin-right: auto" /> 
</p>

## Setup

First, you need to start the Python backend and then the TypeScript VSCode extension.

### Prerequisites

To run this app locally, you need

-   Python 3.11 or above
-   An OpenAI API key (get it here [here](https://platform.openai.com/api-keys) or reach out to me if you're testing)
-   VSCode installed locally

### Backend

Create virtualenv and install requirements

```
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Start the backend

```
export OPENAI_API_KEY="YOUR_API_KEY"
python3 -m codemate.api.main
```

### Frontend

Install dependencies

```
cd extension
npm i
```

Open the extension's code in VSCode

```
cd extension
code .
```

And launch the application using the run button (config "Run Extension") ![Run Button](./run_button.png)

## How things work

### Embedding your own data

#### Download repositories from github.com

#### Preprocess and format them

#### Embedd them

### RAG explained

### VSCode Extension explained
