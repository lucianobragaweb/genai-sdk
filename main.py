import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_GENAI_API_KEY")

client = genai.Client(api_key=api_key)


res = client.models.generate_content_stream(
    model="gemini-2.5-flash-lite",
    contents="Escreva um poema sobre a vida"
)
for chunk in res:
    print(chunk.text, end="", flush=True)



