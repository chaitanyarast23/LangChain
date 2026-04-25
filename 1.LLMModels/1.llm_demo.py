from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

lmm=OpenAI(model='gpt-3.5-turbo-instruct')

result=lmm.invoke("What is the captial of Indai")

print(result)