# Simple Search Engine Application

This application helps you to search basic stuff .

The current application involves usage of DuckDuckGo integrated with Langchain to enable various LLM models to retrieve information and perform web searches.


```DuckDuckGoSearchRun``` is the built-in tool provided by ```langchain_community.tools```


The project uses modular architecture .


Important concepts of Langchain :

1. Models
2. Prompts
3. Chains
4. Indexes
5. Memory
6. Agents





## Project Setup


Clone the repository
```bash
git clone https://github.com/uchiha-vivek/Search-Tool-Langchain.git
```

Navigate to the directory
```bash
Search-Tool-Langchain
```

Make virtual environment (Here for Windows)
```bash
python -m venv venv
```

Activate the virtual environment
```bash
venv\Scripts\activate
```

Install the dependencies
```bash
pip install -r requirements.txt
```

Run command
```bash
python main.py
```

Your flask server will successfully run on ```localhost:5000```

Now use curl to test the api:
```
curl -X POST http://localhost:5000/news      -H "Content-Type: application/json"      -d '{"query": "Hiking tips to mountains"}'
```




Make sure to make a .env file and place your credentials in it.
For reference i have included a .env-sample file


```bash
AZURE_OPENAI_API_KEY = "<your-azure-openai-apikey>"
AZURE_OPENAI_ENDPOINT = "<your azure openai endpoint>"
AZURE_OPENAI_DEPLOYMENT_NAME = "<your azure deployment name>"
AZURE_OPENAI_API_VERSION = "<your azure openai version>"

```

NOTE : you need to use azure openai api key 
Different LLM have different ways of creating chat instance

For more info visit : [Langchain Docs](https://python.langchain.com/docs/introduction/)


 


