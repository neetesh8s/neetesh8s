import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),  # read from .env
    temperature=0.2,
)

response = llm.invoke("Explain FastAPI in one sentence.")
print(response)