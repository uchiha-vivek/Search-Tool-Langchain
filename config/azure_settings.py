# config.py
import os
from dotenv import load_dotenv

load_dotenv()

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_OPENAI_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")



# <-----------------Checking the flow ---------------------->
# if __name__=="__main__":
#     print(f'Azure openai key : {AZURE_OPENAI_API_KEY}')
#     print(f'Azure openai endpoint : {AZURE_OPENAI_ENDPOINT}')
#     print(f'Azure openai deployment name :{AZURE_OPENAI_DEPLOYMENT_NAME}')
#     print(f'Azure opena version : f{AZURE_OPENAI_API_VERSION} ')