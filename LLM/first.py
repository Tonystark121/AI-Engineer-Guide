from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
llm = OpenAI(model = 'gpt-5.6-luna')
results = llm.invoke("Most of the AI companies are in loss for example anthropic: 40 billion dollars, openAI around: 20 billion dollars. then how these companies are running and being profitable?")

print(results)