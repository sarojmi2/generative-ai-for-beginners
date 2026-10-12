import os
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY") or os.getenv("API_KEY")
base_url = os.getenv("OPENAI_API_BASE")

if not api_key:
    raise RuntimeError("Set OPENAI_API_KEY or API_KEY in your environment.")
if not base_url:
    raise RuntimeError("Set OPENAI_API_BASE in your environment.")

client = OpenAI(api_key=api_key, base_url=base_url)
model = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-3-small")

prompt = "Today we are going to learn about Azure Machine Learning."

response = client.embeddings.create(
    model=model,
    input=prompt,
)
embedding = response.data[0].embedding
print(f"Embedding length: {len(embedding)}")
print(f"Embedding : {(embedding)}")

# Back to text from embeeding from the vector using cosine simolarities
# Keep each original text with the embedding you created for it.
saved_items = [
    {"text": "Today we are going to learn about Azure Machine Learning.", "embedding": embedding},
    # Add other saved text-and-embedding pairs here.
]
# `embedding` is the embedding you want to look up.
query_vector = np.array(embedding)


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
closest = max(
    saved_items,
    key=lambda item: cosine_similarity(query_vector, item["embedding"]),
)

print("Closest saved text:", closest["text"])
